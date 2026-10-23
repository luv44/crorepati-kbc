import { createHash, randomUUID } from 'node:crypto';
import { mkdir, readFile, rename, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { writeReports } from './build-content.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const transactionFile = 'content/checkpoints/question-batch-transaction.json';
const targetPerTopic = 40;
const args = new Map(process.argv.slice(2).map((value, index, all) => value.startsWith('--') ? [value, all[index + 1] && !all[index + 1].startsWith('--') ? all[index + 1] : true] : null).filter(Boolean));
const inputName = args.get('--input');
const batchSize = Number(args.get('--batch-size') || 25);
if (!inputName || inputName === true) throw new Error('Usage: node scripts/question-batch.mjs --input reviewed-batch.json [--batch-size 25] [--dry-run]');
if (!Number.isInteger(batchSize) || batchSize < 1 || batchSize > 25) throw new Error('Batch size must be an integer from 1 to 25 so progress remains durable.');

const jsonText = value => `${JSON.stringify(value, null, 2)}\n`;
const readJson = async relative => JSON.parse(await readFile(path.resolve(root, relative), 'utf8'));
const hash = value => createHash('sha256').update(typeof value === 'string' || Buffer.isBuffer(value) ? value : JSON.stringify(value)).digest('hex');
const canonicalize = value => Array.isArray(value) ? value.map(canonicalize) : value && typeof value === 'object' ? Object.fromEntries(Object.keys(value).sort().map(key => [key, canonicalize(value[key])])) : value;
const objectHash = value => hash(JSON.stringify(canonicalize(value)));
const normalize = value => value.normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}]+/gu, ' ').trim();
const conciseOption = value => value.replace(/\s*\([^()]*\)/gu, '').replace(/\s+/g, ' ').trim() || value.trim();
const hasText = value => typeof value === 'string' && Boolean(value.trim());
const localized = value => hasText(value?.en) && hasText(value?.hi);

function safePath(relative) {
  const destination = path.resolve(root, relative);
  if (destination !== root && !destination.startsWith(`${root}${path.sep}`)) throw new Error(`Unsafe transaction path: ${relative}`);
  return destination;
}

async function atomicText(destination, text) {
  await mkdir(path.dirname(destination), { recursive: true });
  const temporary = `${destination}.tmp-${process.pid}-${randomUUID()}`;
  await writeFile(temporary, text);
  await rename(temporary, destination);
}

async function currentHash(file) {
  try { return hash(await readFile(file)); }
  catch (error) { if (error?.code === 'ENOENT') return null; throw error; }
}

async function recoverBundle() {
  let transaction;
  try { transaction = JSON.parse(await readFile(safePath(transactionFile), 'utf8')); }
  catch (error) { if (error?.code === 'ENOENT') return false; throw new Error(`Cannot read pending question transaction: ${error.message}`); }
  if (transaction?.schemaVersion !== 1 || !Array.isArray(transaction.files) || !transaction.files.length) throw new Error('Pending question transaction is malformed; no data was changed.');
  for (const entry of transaction.files) {
    if (!hasText(entry.path) || !/^[a-f0-9]{64}$/.test(entry.sha256)) throw new Error('Pending question transaction contains an invalid file record.');
    const destination = safePath(entry.path);
    if (await currentHash(destination) === entry.sha256) continue;
    const staged = `${destination}.next`;
    if (await currentHash(staged) !== entry.sha256) throw new Error(`Cannot recover ${entry.path}: its staged copy is absent or changed.`);
    await rename(staged, destination);
  }
  for (const entry of transaction.files) await rm(`${safePath(entry.path)}.next`, { force: true });
  await rm(safePath(transactionFile), { force: true });
  console.log(`Recovered question transaction ${transaction.transactionId}.`);
  return true;
}

async function commitJsonBundle(entries) {
  await recoverBundle();
  const files = [];
  for (const [relative, value] of entries) {
    const text = jsonText(value);
    const destination = safePath(relative);
    await atomicText(`${destination}.next`, text);
    files.push({ path: relative, sha256: hash(text) });
  }
  const transaction = { schemaVersion: 1, transactionId: randomUUID(), createdAt: new Date().toISOString(), files };
  await atomicText(safePath(transactionFile), jsonText(transaction));
  await recoverBundle();
}

function validDate(value) { return hasText(value) && !Number.isNaN(Date.parse(value)); }
function optionLengthOutlier(options, correctIndex, language) {
  const lengths = options.map(option => normalize(option[language]).length);
  const correct = lengths[correctIndex];
  const longestDistractor = Math.max(...lengths.filter((_, index) => index !== correctIndex));
  return correct >= longestDistractor + 18 && correct > longestDistractor * 1.45;
}
function containsAnswer(stem, answer) {
  const normalizedStem = ` ${normalize(stem)} `;
  const normalizedAnswer = normalize(answer);
  return normalizedAnswer.length >= 4 && normalizedStem.includes(` ${normalizedAnswer} `);
}
function tokenSet(value) { return new Set(normalize(value).split(' ').filter(token => token.length > 2)); }
function shingles(value) {
  const tokens = normalize(value).split(' ').filter(Boolean);
  if (tokens.length < 6) return new Set();
  const width = tokens.length >= 10 ? 3 : 2;
  return new Set(Array.from({ length: tokens.length - width + 1 }, (_, index) => tokens.slice(index, index + width).join(' ')));
}
function similarity(left, right) {
  if (!left.size || !right.size) return 0;
  let overlap = 0;
  for (const value of left) if (right.has(value)) overlap += 1;
  return overlap / (left.size + right.size - overlap);
}

await recoverBundle();
const raw = await readFile(path.resolve(root, String(inputName)), 'utf8');
const incoming = JSON.parse(raw);
if (!hasText(incoming.batchId) || !hasText(incoming.reviewedBy) || !validDate(incoming.reviewedAt)) throw new Error('batchId, reviewedBy and a valid reviewedAt are required; reviewer metadata is never invented.');
if (!Array.isArray(incoming.questions) || !incoming.questions.length) throw new Error('The reviewed batch has no questions.');
const inputHash = hash(raw);
const [starter, catalog, ledger, baseline] = await Promise.all([
  readJson('public/data/starter.json'),
  readJson('public/data/catalog.json'),
  readJson('content/checkpoints/question-batches.json'),
  readJson('content/checkpoints/legacy-review-labels.json'),
]);
const priorBatch = ledger.batches.find(batch => batch.batchId === incoming.batchId);
if (priorBatch && priorBatch.inputHash !== inputHash) throw new Error(`Batch ${incoming.batchId} already exists with a different hash.`);
const applied = new Set(ledger.appliedQuestionIds || []);
const baselineById = new Map(baseline.labels.map(label => [label.id, label]));
const existingById = new Map(starter.questions.map(question => [question.id, question]));
for (const saved of baseline.labels) {
  const question = existingById.get(saved.id);
  if (!question || question.lifecycle !== saved.lifecycle || question.kind !== saved.kind || question.qualityScore !== saved.qualityScore) throw new Error(`Preservation gate failed before write: ${saved.id}`);
}

const topicMeta = new Map();
for (const subject of catalog.subjects) for (const chapter of subject.chapters) for (const topic of chapter.topics) topicMeta.set(topic.id, {
  subjectId: subject.id,
  chapterId: chapter.id,
  conceptIds: new Set(topic.concepts.map(concept => concept.id)),
});

const newSources = Array.isArray(incoming.sources) ? incoming.sources : [];
const sourceById = new Map(starter.sources.map(source => [source.id, source]));
const inputSourceIds = new Set();
for (const source of newSources) {
  if (!hasText(source.id) || inputSourceIds.has(source.id)) throw new Error(`Source ID is missing or duplicated: ${source.id}`);
  inputSourceIds.add(source.id);
  if (![source.title, source.publisher, source.license].every(hasText) || !validDate(source.retrievedAt)) throw new Error(`${source.id}: title, publisher, license and a valid retrievedAt are required`);
  let parsed;
  try { parsed = new URL(source.url); } catch { throw new Error(`${source.id}: source URL is invalid`); }
  if (parsed.protocol !== 'https:') throw new Error(`${source.id}: source URL must use HTTPS`);
  const current = sourceById.get(source.id);
  if (current && objectHash(current) !== objectHash(source)) throw new Error(`${source.id}: an existing source cannot be replaced by a different record`);
  sourceById.set(source.id, source);
}

const newFacts = Array.isArray(incoming.factCards) ? incoming.factCards : [];
const factById = new Map(starter.factCards.map(card => [card.id, card]));
const inputFactIds = new Set();
for (const card of newFacts) {
  if (!hasText(card.id) || inputFactIds.has(card.id)) throw new Error(`FactCard ID is missing or duplicated: ${card.id}`);
  inputFactIds.add(card.id);
  const meta = topicMeta.get(card.topicId);
  if (!meta) throw new Error(`${card.id}: unknown topic ${card.topicId}`);
  if (!hasText(card.canonicalStatement) || !hasText(card.canonicalStatementHindi)) throw new Error(`${card.id}: bilingual canonical statements are required`);
  if (card.lifecycle !== 'VERIFIED' || !validDate(card.verifiedAt)) throw new Error(`${card.id}: VERIFIED lifecycle and a valid verifiedAt are required`);
  if (!Array.isArray(card.conceptIds) || !card.conceptIds.length || card.conceptIds.some(id => !meta.conceptIds.has(id))) throw new Error(`${card.id}: conceptIds must resolve within its topic`);
  if (!Array.isArray(card.sourceIds) || !card.sourceIds.length || card.sourceIds.some(id => !sourceById.has(id))) throw new Error(`${card.id}: resolvable sourceIds are required`);
  if (!Array.isArray(card.evidence) || !card.evidence.length || card.evidence.some(evidence => !card.sourceIds.includes(evidence.sourceId) || !hasText(evidence.quote) || normalize(evidence.quote).length < 20 || !hasText(evidence.locator))) throw new Error(`${card.id}: evidence must have a sourceId, substantive quote and locator`);
  const current = factById.get(card.id);
  if (current && objectHash(current) !== objectHash(card)) throw new Error(`${card.id}: an existing FactCard cannot be replaced by a different record`);
  factById.set(card.id, card);
}

const fingerprintOwner = new Map(starter.questions.map(question => [question.fingerprint, question.id]).filter(([fingerprint]) => hasText(fingerprint)));
const englishStemOwner = new Map(starter.questions.map(question => [normalize(question.question.en), question.id]));
const hindiStemOwner = new Map(starter.questions.map(question => [normalize(question.question.hi), question.id]));
const stemRows = starter.questions.map(question => ({ id: question.id, stem: question.question.en, shingles: shingles(question.question.en), tokens: tokenSet(question.question.en) }));
const inputIds = new Set();
const inputFingerprints = new Set();
const inputEnglishStems = new Set();
const inputHindiStems = new Set();
const bannedStemPatterns = [
  /advanced\s+exam\s+perspective/iu,
  /assessing\s+syllabus/iu,
  /\bsyllabus\b/iu,
  /\bcurriculum\b/iu,
  /\bbenchmarks?\b/iu,
  /\bevaluat(?:e|es|ed|ing|ion)\b/iu,
  /\bscrutiny\b/iu,
  /पाठ्यक्रम/u,
  /मूल्यांकन/u,
];
for (const question of incoming.questions) {
  if (!hasText(question.id) || inputIds.has(question.id)) throw new Error(`Question ID is missing or duplicated in the input: ${question.id}`);
  inputIds.add(question.id);
  const existing = existingById.get(question.id);
  const resumable = Boolean(existing && priorBatch && applied.has(question.id) && objectHash(existing) === objectHash(question));
  if (existing && !resumable) throw new Error(`Question ID already exists outside this exact resumable batch: ${question.id}`);
  const meta = topicMeta.get(question.topicId);
  if (!meta) throw new Error(`${question.id}: unknown topic ${question.topicId}`);
  if (question.subjectId !== meta.subjectId || question.chapterId !== meta.chapterId) throw new Error(`${question.id}: subjectId/chapterId do not match its canonical topic`);
  if (!Array.isArray(question.conceptIds) || !question.conceptIds.length || question.conceptIds.some(id => !meta.conceptIds.has(id))) throw new Error(`${question.id}: conceptIds must resolve within its topic`);
  if (!localized(question.question)) throw new Error(`${question.id}: bilingual stem required`);
  if (question.question.en.length > 260 || question.question.hi.length > 320) throw new Error(`${question.id}: stem is too long for focused practice`);
  if (bannedStemPatterns.some(pattern => pattern.test(question.question.en) || pattern.test(question.question.hi))) throw new Error(`${question.id}: prohibited boilerplate appears in the stem`);
  if (!Array.isArray(question.options) || question.options.length !== 4 || question.options.some(option => !localized(option))) throw new Error(`${question.id}: exactly four bilingual options required`);
  if (question.options.some(option => conciseOption(option.en).length > 160 || conciseOption(option.hi).length > 160 || /further defined by/iu.test(conciseOption(option.en)))) throw new Error(`${question.id}: answer option is overlong or concatenated`);
  if (new Set(question.options.map(option => normalize(option.en))).size !== 4 || new Set(question.options.map(option => normalize(option.hi))).size !== 4) throw new Error(`${question.id}: duplicate options`);
  if (!Number.isInteger(question.correctIndex) || question.correctIndex < 0 || question.correctIndex > 3) throw new Error(`${question.id}: invalid correctIndex`);
  if (containsAnswer(question.question.en, question.options[question.correctIndex].en) || containsAnswer(question.question.hi, question.options[question.correctIndex].hi)) throw new Error(`${question.id}: the stem contains the correct answer`);
  if (optionLengthOutlier(question.options, question.correctIndex, 'en') || optionLengthOutlier(question.options, question.correctIndex, 'hi')) throw new Error(`${question.id}: the correct option is an obvious length outlier`);
  if (!localized(question.explanation) || !localized(question.detailedExplanation) || !localized(question.memoryCue)) throw new Error(`${question.id}: bilingual explanation, detailedExplanation and memoryCue are required`);
  if (normalize(question.explanation.en).length < 12 || normalize(question.explanation.hi).length < 12) throw new Error(`${question.id}: explanation is too short for a clear bilingual review`);
  if (!Array.isArray(question.wrongReasons) || ![3, 4].includes(question.wrongReasons.length) || question.wrongReasons.some(reason => !localized(reason))) throw new Error(`${question.id}: three distractor reasons (or four option-indexed reasons) are required bilingually`);
  if (!['EASY', 'MEDIUM', 'HARD', 'EXPERT'].includes(question.difficulty) || !hasText(question.angle)) throw new Error(`${question.id}: difficulty and angle are required`);
  if (question.lifecycle !== 'VERIFIED' || !Number.isInteger(question.qualityScore) || question.qualityScore < 0 || question.qualityScore > 100 || !validDate(question.verifiedAt)) throw new Error(`${question.id}: VERIFIED lifecycle, qualityScore 0–100 and valid verifiedAt are required`);
  if (typeof question.dynamic !== 'boolean' || !hasText(question.kind)) throw new Error(`${question.id}: dynamic and kind are required`);
  if (!Array.isArray(question.sourceIds) || !question.sourceIds.length || question.sourceIds.some(id => !sourceById.has(id))) throw new Error(`${question.id}: resolvable sourceIds required`);
  if (!Array.isArray(question.factCardIds) || !question.factCardIds.length) throw new Error(`${question.id}: factCardIds required`);
  for (const id of question.factCardIds) {
    const card = factById.get(id);
    if (!card || card.topicId !== question.topicId || card.lifecycle !== 'VERIFIED' || !card.evidence?.length || !card.sourceIds?.length || card.sourceIds.some(sourceId => !sourceById.has(sourceId) || !question.sourceIds.includes(sourceId))) throw new Error(`${question.id}: FactCard ${id} is absent, mapped elsewhere, or not source-complete`);
  }
  if (question.kind === 'ACTUAL_PYQ') {
    const provenance = question.pyqProvenance;
    if (!provenance || ![provenance.exam, provenance.stage, provenance.paper, provenance.questionNumber, provenance.officialPaperSourceId, provenance.officialAnswerKeySourceId].every(hasText) || !Number.isInteger(provenance.year) || !question.sourceIds.includes(provenance.officialPaperSourceId) || !question.sourceIds.includes(provenance.officialAnswerKeySourceId)) throw new Error(`${question.id}: ACTUAL_PYQ requires exam/stage/year/paper/question number and official paper/answer-key sources`);
  }
  if (!hasText(question.fingerprint)) throw new Error(`${question.id}: fingerprint required`);
  const fingerprintConflict = fingerprintOwner.get(question.fingerprint);
  if ((fingerprintConflict && fingerprintConflict !== question.id) || inputFingerprints.has(question.fingerprint)) throw new Error(`${question.id}: unique fingerprint required`);
  inputFingerprints.add(question.fingerprint);
  const englishStem = normalize(question.question.en);
  const hindiStem = normalize(question.question.hi);
  const englishConflict = englishStemOwner.get(englishStem);
  const hindiConflict = hindiStemOwner.get(hindiStem);
  if ((englishConflict && englishConflict !== question.id) || inputEnglishStems.has(englishStem)) throw new Error(`${question.id}: repeated normalized English stem`);
  if ((hindiConflict && hindiConflict !== question.id) || inputHindiStems.has(hindiStem)) throw new Error(`${question.id}: repeated normalized Hindi stem`);
  const questionShingles = shingles(question.question.en);
  const questionTokens = tokenSet(question.question.en);
  const near = stemRows.find(row => row.id !== question.id && (similarity(questionShingles, row.shingles) >= 0.6 || similarity(questionTokens, row.tokens) >= 0.6));
  if (near) throw new Error(`${question.id}: near-duplicate English stem matches ${near.id}`);
  inputEnglishStems.add(englishStem);
  inputHindiStems.add(hindiStem);
  stemRows.push({ id: question.id, stem: question.question.en, shingles: questionShingles, tokens: questionTokens });
}

const remaining = incoming.questions.filter(question => !applied.has(question.id));
const projectedCounts = new Map();
for (const question of starter.questions) if (question.sourceIds?.length && question.sourceIds.every(id => sourceById.has(id))) projectedCounts.set(question.topicId, (projectedCounts.get(question.topicId) || 0) + 1);
for (const question of remaining) {
  const projected = (projectedCounts.get(question.topicId) || 0) + 1;
  if (projected > targetPerTopic) throw new Error(`${question.id}: topic ${question.topicId} would exceed the ${targetPerTopic}-question source-complete target`);
  projectedCounts.set(question.topicId, projected);
}
console.log(`Batch ${incoming.batchId}: ${incoming.questions.length} reviewed questions; ${remaining.length} remain after resume check.`);
if (args.has('--dry-run')) {
  console.log('Dry run passed; no files changed.');
  process.exit(0);
}

starter.sources = [...new Map([...starter.sources, ...newSources].map(item => [item.id, item])).values()];
starter.factCards = [...new Map([...starter.factCards, ...newFacts].map(item => [item.id, item])).values()];
const batchRecord = priorBatch || { batchId: incoming.batchId, inputHash, reviewedBy: incoming.reviewedBy, reviewedAt: incoming.reviewedAt, total: incoming.questions.length, saves: [], status: 'IN_PROGRESS' };
if (!priorBatch) ledger.batches.push(batchRecord);

function synchronizeCatalog(savedAt) {
  const counts = new Map();
  for (const question of starter.questions) counts.set(question.topicId, (counts.get(question.topicId) || 0) + 1);
  for (const subject of catalog.subjects) {
    subject.questionCount = 0;
    for (const chapter of subject.chapters) for (const topic of chapter.topics) {
      topic.questionCount = counts.get(topic.id) || 0;
      subject.questionCount += topic.questionCount;
    }
  }
  catalog.counts.questions = starter.questions.length;
  catalog.counts.factCards = starter.factCards.length;
  catalog.builtAt = savedAt;
  const starterText = jsonText(starter);
  const pack = catalog.packs.find(item => item.id === starter.id);
  if (!pack) throw new Error(`Catalog pack metadata for ${starter.id} is missing.`);
  pack.questionCount = starter.questions.length;
  pack.size = Buffer.byteLength(starterText);
  pack.sha256 = hash(starterText);
}

for (let start = 0; start < remaining.length; start += batchSize) {
  const chunk = remaining.slice(start, start + batchSize);
  starter.questions.push(...chunk);
  for (const question of chunk) applied.add(question.id);
  const savedAt = new Date().toISOString();
  synchronizeCatalog(savedAt);
  ledger.appliedQuestionIds = [...applied];
  ledger.updatedAt = savedAt;
  batchRecord.saves.push({ savedAt, firstId: chunk[0].id, lastId: chunk.at(-1).id, added: chunk.length, totalQuestions: starter.questions.length, starterHash: hash(starter.questions.map(question => question.id)) });
  await commitJsonBundle([
    ['public/data/starter.json', starter],
    ['public/data/catalog.json', catalog],
    ['content/checkpoints/question-batches.json', ledger],
  ]);
  await writeReports();
  console.log(`Saved ${chunk.length}; corpus now ${starter.questions.length}.`);
}
if (batchRecord.status !== 'COMPLETE') {
  batchRecord.status = 'COMPLETE';
  batchRecord.completedAt = new Date().toISOString();
  ledger.updatedAt = batchRecord.completedAt;
  await commitJsonBundle([['content/checkpoints/question-batches.json', ledger]]);
}
await writeReports();
for (const [id, saved] of baselineById) {
  const question = starter.questions.find(item => item.id === id);
  if (!question || question.lifecycle !== saved.lifecycle || question.kind !== saved.kind || question.qualityScore !== saved.qualityScore) throw new Error(`Preservation gate failed after write: ${id}`);
}
console.log(`Batch ${incoming.batchId} complete and checkpointed.`);
