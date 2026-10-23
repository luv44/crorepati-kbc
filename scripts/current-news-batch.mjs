import { readFile, rename, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { writeReports } from './build-content.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const feedPath = path.join(root, 'public/data/current-news.json');
const ledgerPath = path.join(root, 'content/checkpoints/current-news-batches.json');
const targetPerRun = 150;
const defaultSaveSize = 25;
const args = process.argv.slice(2);
const arg = name => { const index = args.indexOf(name); return index >= 0 ? args[index + 1] : undefined; };
const inputArg = arg('--input');
const saveSize = Number(arg('--save-size') || defaultSaveSize);

if (!inputArg) throw new Error('Usage: npm run apply-news-batch -- --input <reviewed-current-news-batch.json> [--save-size 25]');
if (!Number.isInteger(saveSize) || saveSize < 1 || saveSize > 25) throw new Error('--save-size must be an integer from 1 to 25 so progress remains durable.');

const inputPath = path.resolve(root, inputArg);
const [feed, bundle] = await Promise.all([
  readFile(feedPath, 'utf8').then(JSON.parse),
  readFile(inputPath, 'utf8').then(JSON.parse),
]);
let ledger;
try { ledger = JSON.parse(await readFile(ledgerPath, 'utf8')); }
catch { ledger = { schemaVersion: 1, targetPerRun, appliedItems: [] }; }

const text = value => typeof value === 'string' && value.trim().length > 0;
const hindi = value => text(value) && /[\u0900-\u097f]/u.test(value);
const localized = value => text(value?.en) && hindi(value?.hi);
const date = value => {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) return false;
  const parsed = new Date(`${value}T00:00:00Z`);
  return !Number.isNaN(parsed.valueOf()) && parsed.toISOString().slice(0, 10) === value;
};
const normalized = value => String(value || '').normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}]+/gu, ' ').trim();
const containsAnswer = (stem, answer) => {
  const normalizedAnswer = normalized(answer);
  return normalizedAnswer.length >= 4 && ` ${normalized(stem)} `.includes(` ${normalizedAnswer} `);
};
const tokenSet = value => new Set(normalized(value).split(' ').filter(token => token.length > 2));
const similarity = (left, right) => {
  if (!left.size || !right.size) return 0;
  const overlap = [...left].filter(token => right.has(token)).length;
  return overlap / (left.size + right.size - overlap);
};
const optionLengthOutlier = (options, correctIndex, language) => {
  const lengths = options.map(option => normalized(option[language]).length);
  const correct = lengths[correctIndex];
  const longestDistractor = Math.max(...lengths.filter((_, index) => index !== correctIndex));
  return correct >= longestDistractor + 18 && correct > longestDistractor * 1.45;
};
const bannedStemPatterns = [/advanced\s+exam\s+perspective/iu, /assessing\s+syllabus/iu, /\bsyllabus\b/iu, /\bcurriculum\b/iu, /\bbenchmarks?\b/iu, /\bevaluat(?:e|es|ed|ing|ion)\b/iu, /\bscrutiny\b/iu, /पाठ्यक्रम/u, /मूल्यांकन/u];
const fail = message => { throw new Error(message); };
const assert = (condition, message) => { if (!condition) fail(message); };
const atomicJson = async (destination, value) => {
  await mkdir(path.dirname(destination), { recursive: true });
  const temporary = `${destination}.tmp`;
  await writeFile(temporary, `${JSON.stringify(value, null, 2)}\n`);
  await rename(temporary, destination);
};

assert(text(bundle?.id), 'batch id is required');
assert(bundle?.review?.directSourcePagesChecked === true, 'batch review.directSourcePagesChecked must be true after opening every source page');
assert(date(bundle?.review?.reviewedAt), 'batch review.reviewedAt must be YYYY-MM-DD');
assert(text(bundle?.review?.reviewer), 'batch review.reviewer is required');
assert(Array.isArray(bundle?.items) && bundle.items.length > 0, 'batch items must be a non-empty array');
assert(bundle.items.length <= targetPerRun, `one reviewed run accepts at most ${targetPerRun} records`);
assert(feed.verifiedRecordTargetPerRun === targetPerRun, `feed target must remain ${targetPerRun}`);

const existingById = new Map(feed.items.map(item => [item.id, item]));
const existingUrls = new Set(feed.items.flatMap(item => item.links.map(link => link.url)));
const existingMcqIds = new Set(feed.items.flatMap(item => item.mcqs.map(question => question.id)));
const existingTitles = new Set(feed.items.flatMap(item => [normalized(item.title.en), normalized(item.title.hi)]));
const existingMcqStems = new Set(feed.items.flatMap(item => item.mcqs.flatMap(question => [normalized(question.question.en), normalized(question.question.hi)])));
const titleRows = feed.items.map(item => ({ id: item.id, tokens: tokenSet(item.title.en) }));
const mcqStemRows = feed.items.flatMap(item => item.mcqs.map(question => ({ id: question.id, tokens: tokenSet(question.question.en) })));
const incomingIds = new Set();
const incomingUrls = new Set();
const incomingTitles = new Set();
const incomingMcqIds = new Set();
const incomingMcqStems = new Set();
const blockedNotice = /\b(recruitment|vacanc(?:y|ies)|admit card|exam(?:ination)? result|answer key)\b/i;

for (const item of bundle.items) {
  assert(text(item.id) && !incomingIds.has(item.id), `missing or duplicate incoming news ID: ${item.id || '(empty)'}`);
  incomingIds.add(item.id);
  if (existingById.has(item.id)) {
    assert(JSON.stringify(existingById.get(item.id)) === JSON.stringify(item), `existing news ${item.id} differs from the reviewed input`);
    continue;
  }
  assert(date(item.publicationDate) && date(item.verifiedAt) && item.publicationDate <= item.verifiedAt, `news ${item.id} has invalid publication/verification dates`);
  assert(localized(item.category), `news ${item.id} needs a bilingual category with Hindi text`);
  assert(localized(item.title), `news ${item.id} needs a bilingual title with Hindi text`);
  assert(localized(item.summary), `news ${item.id} needs a bilingual summary with Hindi text`);
  const noticeText = [item.title.en, item.summary.en, ...(item.analysis?.keyPoints || []).map(point => point.en)].join(' ');
  assert(!blockedNotice.test(noticeText), `news ${item.id} is an excluded recruitment/result notice`);
  const titleKeys = [normalized(item.title.en), normalized(item.title.hi)];
  assert(titleKeys.every(key => key && !existingTitles.has(key) && !incomingTitles.has(key)), `news ${item.id} repeats an existing story title`);
  const titleTokens = tokenSet(item.title.en);
  assert(!titleRows.some(row => similarity(titleTokens, row.tokens) >= 0.6), `news ${item.id} is a near-duplicate of an existing story title`);
  titleKeys.forEach(key => incomingTitles.add(key));
  titleRows.push({ id: item.id, tokens: titleTokens });
  assert(item.analysis?.readTimeMinutes === 1, `news ${item.id} must have a one-minute analysis marker`);
  assert(Array.isArray(item.analysis?.keyPoints) && item.analysis.keyPoints.length >= 3 && item.analysis.keyPoints.every(localized), `news ${item.id} needs at least three bilingual checked points with Hindi text`);
  assert(localized(item.analysis?.whatToRemember), `news ${item.id} needs a bilingual recall focus with Hindi text`);
  assert(text(item.evidenceQuote) && item.evidenceQuote.length > 30 && text(item.evidenceLocator), `news ${item.id} needs retained evidence and a locator`);
  assert(Array.isArray(item.links) && item.links.length > 0, `news ${item.id} needs an independent source link`);
  for (const link of item.links) {
    assert(text(link.label), `news ${item.id} has a source link without a label`);
    let url;
    try { url = new URL(link.url); } catch { fail(`news ${item.id} has an invalid source URL`); }
    assert(url.protocol === 'https:' && !url.username && !url.password && (url.hostname.endsWith('.gov.in') || url.hostname.endsWith('.nic.in')), `news ${item.id} source must be an HTTPS government page`);
    assert(!existingUrls.has(link.url) && !incomingUrls.has(link.url), `news ${item.id} reuses a source URL`);
    incomingUrls.add(link.url);
  }
  assert(Array.isArray(item.mcqs) && item.mcqs.length > 0, `news ${item.id} needs source-linked MCQs`);
  for (const question of item.mcqs) {
    assert(text(question.id) && !existingMcqIds.has(question.id) && !incomingMcqIds.has(question.id), `news ${item.id} has a duplicate MCQ ID`);
    incomingMcqIds.add(question.id);
    assert(localized(question.question), `MCQ ${question.id} needs a bilingual stem with Hindi text`);
    assert(question.question.en.length <= 260 && question.question.hi.length <= 320, `MCQ ${question.id} stem is too long for focused practice`);
    assert(!bannedStemPatterns.some(pattern => pattern.test(question.question.en) || pattern.test(question.question.hi)), `MCQ ${question.id} contains prohibited boilerplate`);
    const stemKeys = [normalized(question.question.en), normalized(question.question.hi)];
    assert(stemKeys.every(key => key && !existingMcqStems.has(key) && !incomingMcqStems.has(key)), `MCQ ${question.id} repeats an existing stem`);
    const questionTokens = tokenSet(question.question.en);
    assert(!mcqStemRows.some(row => similarity(questionTokens, row.tokens) >= 0.6), `MCQ ${question.id} is a near-duplicate of an existing stem`);
    stemKeys.forEach(key => incomingMcqStems.add(key));
    mcqStemRows.push({ id: question.id, tokens: questionTokens });
    assert(Array.isArray(question.options) && question.options.length === 4 && question.options.every(localized), `MCQ ${question.id} needs exactly four bilingual options with Hindi text`);
    assert(question.options.every(option => option.en.length <= 160 && option.hi.length <= 160), `MCQ ${question.id} has an overlong answer option`);
    assert(new Set(question.options.map(option => normalized(option.en))).size === 4 && new Set(question.options.map(option => normalized(option.hi))).size === 4, `MCQ ${question.id} repeats an option`);
    assert(Number.isInteger(question.correctIndex) && question.correctIndex >= 0 && question.correctIndex < 4, `MCQ ${question.id} has an invalid answer index`);
    assert(!containsAnswer(question.question.en, question.options[question.correctIndex].en) && !containsAnswer(question.question.hi, question.options[question.correctIndex].hi), `MCQ ${question.id} reveals its answer in the stem`);
    assert(!optionLengthOutlier(question.options, question.correctIndex, 'en') && !optionLengthOutlier(question.options, question.correctIndex, 'hi'), `MCQ ${question.id} makes the answer an obvious length outlier`);
    assert(localized(question.explanation) && normalized(question.explanation.en).length >= 12 && normalized(question.explanation.hi).length >= 12, `MCQ ${question.id} needs a clear bilingual explanation with Hindi text`);
  }
}

const pending = bundle.items.filter(item => !existingById.has(item.id));
if (!pending.length) {
  console.log(`No new records to apply. All ${bundle.items.length} reviewed IDs are already present.`);
  process.exit(0);
}

const runId = bundle.id || `news-run-${bundle.review.reviewedAt}-${Date.now()}`;
for (let offset = 0; offset < pending.length; offset += saveSize) {
  const chunk = pending.slice(offset, offset + saveSize);
  feed.items.push(...chunk);
  feed.items.sort((a, b) => b.publicationDate.localeCompare(a.publicationDate));
  feed.generatedAt = bundle.review.reviewedAt;
  const [major = '1', minor = '0', patch = '0'] = String(feed.version || '1.0.0').split('.');
  feed.version = `${major}.${minor}.${Number(patch) + 1}`;
  ledger.targetPerRun = targetPerRun;
  ledger.appliedItems.push(...chunk.map(item => ({ id: item.id, runId, reviewedAt: bundle.review.reviewedAt, sourceUrls: item.links.map(link => link.url) })));
  await atomicJson(feedPath, feed);
  await atomicJson(ledgerPath, ledger);
  await writeReports();
  console.log(`Saved ${Math.min(offset + chunk.length, pending.length)}/${pending.length} reviewed records for run ${runId}.`);
}

console.log(`Applied ${pending.length} new verified current-news records. Run target ${targetPerRun}; reviewed-input shortfall ${Math.max(0, targetPerRun - bundle.items.length)}.`);
