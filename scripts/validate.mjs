import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import { auditContent } from './build-content.mjs';

const strictCoverage = process.argv.includes('--strict-coverage');
const strictSources = process.argv.includes('--strict-sources');
const errors = [];
const gaps = [];
const assert = (condition, message) => { if (!condition) errors.push(message); };
const text = value => typeof value === 'string' && value.trim().length > 0;
const normalized = value => value.normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}]+/gu, ' ').trim();
const validDate = value => /^\d{4}-\d{2}-\d{2}$/.test(value) && !Number.isNaN(Date.parse(`${value}T00:00:00Z`));
const containsAnswer = (stem, answer) => {
  const normalizedAnswer = normalized(answer);
  return normalizedAnswer.length >= 4 && ` ${normalized(stem)} `.includes(` ${normalizedAnswer} `);
};
const optionLengthOutlier = (options, correctIndex, language) => {
  const lengths = options.map(option => normalized(option[language]).length);
  const correct = lengths[correctIndex];
  const longestDistractor = Math.max(...lengths.filter((_, index) => index !== correctIndex));
  return correct >= longestDistractor + 18 && correct > longestDistractor * 1.45;
};

const { catalog, starter, examCatalog, currentNews, baseline, topicMap, examReport, coverageReport } = await auditContent();
const baselineQuestionIds = new Set(baseline.labels.map(label => label.id));
const legacyConceptMappingGaps = [];

assert(catalog.subjects.length > 0, 'catalog has no subjects');
assert(topicMap.size === catalog.counts.topics, `catalog topic count ${catalog.counts.topics} does not match ${topicMap.size}`);
assert(starter.questions.length === catalog.counts.questions, `catalog question count ${catalog.counts.questions} does not match starter ${starter.questions.length}`);
assert(starter.factCards.length === catalog.counts.factCards, `catalog FactCard count ${catalog.counts.factCards} does not match starter ${starter.factCards.length}`);
const starterBytes = await readFile(new URL('../public/data/starter.json', import.meta.url));
const starterMeta = catalog.packs.find(pack => pack.id === starter.id);
assert(Boolean(starterMeta), `catalog pack metadata for ${starter.id} is missing`);
if (starterMeta) {
  assert(starterMeta.questionCount === starter.questions.length, `starter pack questionCount ${starterMeta.questionCount} does not match ${starter.questions.length}`);
  assert(starterMeta.size === starterBytes.length, `starter pack size ${starterMeta.size} does not match ${starterBytes.length}`);
  assert(starterMeta.sha256 === createHash('sha256').update(starterBytes).digest('hex'), 'starter pack SHA-256 does not match its file');
}
assert(new Set(catalog.subjects.map(subject => subject.id)).size === catalog.subjects.length, 'duplicate subject IDs');
assert(examReport.allMappingsValid, 'one or more exam mappings reference missing/empty hierarchy nodes');
assert(new Set(examCatalog.exams.map(exam => exam.id)).size === examCatalog.exams.length, 'duplicate exam IDs');
const requiredLegacy = ['general-knowledge', 'upsc-cse', 'ssc', 'banking', 'railways', 'state-exams', 'just-curious'];
for (const id of requiredLegacy) assert(examCatalog.exams.some(exam => exam.id === id && exam.legacy), `legacy exam mapping missing: ${id}`);
for (const exam of examCatalog.exams) {
  assert(text(exam.name) && text(exam.nameHindi), `exam ${exam.id} lacks bilingual name`);
  assert(exam.subjectIds.length > 0, `exam ${exam.id} has no mapped subjects`);
  assert(new Set(exam.subjectIds).size === exam.subjectIds.length, `exam ${exam.id} repeats subject IDs`);
  if (exam.officialUrl) {
    try { assert(new URL(exam.officialUrl).protocol === 'https:', `exam ${exam.id} official URL is not HTTPS`); }
    catch { errors.push(`exam ${exam.id} official URL is invalid`); }
  }
}

const sourceIds = new Set(starter.sources.map(source => source.id));
const factIds = new Set(starter.factCards.map(card => card.id));
const questionIds = new Set();
const fingerprints = new Set();
const stems = new Map();
const countByTopic = new Map([...topicMap.keys()].map(id => [id, 0]));
for (const question of starter.questions) {
  assert(!questionIds.has(question.id), `duplicate question ID: ${question.id}`);
  questionIds.add(question.id);
  assert(topicMap.has(question.topicId), `question ${question.id} references missing topic ${question.topicId}`);
  const topic = topicMap.get(question.topicId);
  if (topic) {
    assert(question.subjectId === topic.subjectId, `question ${question.id} subjectId does not match its topic`);
    assert(question.chapterId === topic.chapterId, `question ${question.id} chapterId does not match its topic`);
    const conceptsResolve = question.conceptIds?.every(id => topic.concepts.some(concept => concept.id === id));
    if (!conceptsResolve && baselineQuestionIds.has(question.id)) legacyConceptMappingGaps.push(question.id);
    else assert(conceptsResolve, `question ${question.id} references a concept outside its topic`);
  }
  assert(question.factCardIds?.length && question.factCardIds.every(id => factIds.has(id)), `question ${question.id} references a missing FactCard`);
  assert(question.sourceIds?.every(id => sourceIds.has(id)), `question ${question.id} references a missing source`);
  countByTopic.set(question.topicId, (countByTopic.get(question.topicId) || 0) + 1);
  assert(text(question.question?.en) && text(question.question?.hi), `question ${question.id} lacks bilingual stem`);
  assert(Array.isArray(question.options) && question.options.length === 4, `question ${question.id} does not have four options`);
  assert(question.options?.every(option => text(option.en) && text(option.hi)), `question ${question.id} has incomplete bilingual options`);
  assert(Number.isInteger(question.correctIndex) && question.correctIndex >= 0 && question.correctIndex < 4, `question ${question.id} has invalid correctIndex`);
  assert(text(question.explanation?.en) && text(question.explanation?.hi), `question ${question.id} lacks bilingual explanation`);
  assert(text(question.lifecycle) && text(question.kind), `question ${question.id} lacks preserved review labels`);
  if (question.fingerprint) {
    assert(!fingerprints.has(question.fingerprint), `duplicate fingerprint: ${question.fingerprint}`);
    fingerprints.add(question.fingerprint);
  }
  const key = normalized(question.question.en);
  const prior = stems.get(key);
  if (prior && prior !== question.id) gaps.push(`exact normalized English stem repeated: ${prior}, ${question.id}`);
  else stems.set(key, question.id);
}
for (const [topicId, count] of countByTopic) {
  const topic = topicMap.get(topicId);
  assert(topic.questionCount === count, `topic ${topicId} catalog count ${topic.questionCount} does not match ${count}`);
}
for (const subject of catalog.subjects) {
  const expected = subject.chapters.flatMap(chapter => chapter.topics).reduce((total, topic) => total + (countByTopic.get(topic.id) || 0), 0);
  assert(subject.questionCount === expected, `subject ${subject.id} catalog count ${subject.questionCount} does not match ${expected}`);
}
assert(!coverageReport.changedReviewLabels.length, `${coverageReport.changedReviewLabels.length} preserved review labels changed or disappeared`);
if (coverageReport.shortfall) gaps.push(`${coverageReport.shortfall} questions remain to reach 40 per topic across ${coverageReport.topicsBelowTarget} topics`);
if (coverageReport.questionsWithoutDirectSources) gaps.push(`${coverageReport.questionsWithoutDirectSources} preserved legacy questions do not carry resolvable direct source IDs`);
const factSourceGaps = starter.factCards.filter(card => !card.sourceIds?.length || card.sourceIds.some(id => !sourceIds.has(id)));
if (factSourceGaps.length) gaps.push(`${factSourceGaps.length} preserved FactCards reference absent or empty source IDs`);
if (legacyConceptMappingGaps.length) gaps.push(`${legacyConceptMappingGaps.length} preserved questions reference concept IDs outside their topic`);

assert(currentNews.items.length > 0, 'Current Live has no verified records');
assert(/general current affairs/i.test(currentNews.policy) && /not recruitment or result updates/i.test(currentNews.policy), 'Current Live policy does not enforce general-current-affairs scope');
assert(currentNews.policy.includes('No verified news found'), 'Current Live policy does not preserve the exact empty-state text');
const newsIds = new Set();
const mcqIds = new Set();
for (const item of currentNews.items) {
  assert(!newsIds.has(item.id), `duplicate news ID: ${item.id}`);
  newsIds.add(item.id);
  assert(validDate(item.publicationDate), `news ${item.id} has invalid publication date`);
  assert(validDate(item.verifiedAt), `news ${item.id} has invalid verification date`);
  assert(item.publicationDate <= item.verifiedAt, `news ${item.id} was marked verified before publication`);
  assert(text(item.category?.en) && text(item.category?.hi), `news ${item.id} lacks bilingual category`);
  assert(text(item.title?.en) && text(item.title?.hi), `news ${item.id} lacks bilingual title`);
  assert(text(item.summary?.en) && text(item.summary?.hi), `news ${item.id} lacks bilingual summary`);
  assert(item.analysis?.readTimeMinutes === 1, `news ${item.id} is missing its one-minute analysis marker`);
  assert(Array.isArray(item.analysis?.keyPoints) && item.analysis.keyPoints.length >= 3, `news ${item.id} needs at least three analyzed key points`);
  assert(item.analysis?.keyPoints?.every(point => text(point.en) && text(point.hi)), `news ${item.id} has incomplete bilingual key points`);
  assert(new Set(item.analysis?.keyPoints?.map(point => normalized(point.en))).size === item.analysis?.keyPoints?.length, `news ${item.id} repeats English analyzed key points`);
  assert(new Set(item.analysis?.keyPoints?.map(point => normalized(point.hi))).size === item.analysis?.keyPoints?.length, `news ${item.id} repeats Hindi analyzed key points`);
  assert(text(item.analysis?.whatToRemember?.en) && text(item.analysis?.whatToRemember?.hi), `news ${item.id} lacks a bilingual recall focus`);
  assert(text(item.evidenceQuote) && text(item.evidenceLocator), `news ${item.id} lacks checked evidence excerpt`);
  assert(Array.isArray(item.links) && item.links.length > 0, `news ${item.id} has no source link`);
  for (const link of item.links || []) {
    try { assert(new URL(link.url).protocol === 'https:', `news ${item.id} source is not HTTPS`); }
    catch { errors.push(`news ${item.id} source URL is invalid`); }
  }
  assert(Array.isArray(item.mcqs) && item.mcqs.length > 0, `news ${item.id} has no MCQs`);
  for (const question of item.mcqs || []) {
    assert(!mcqIds.has(question.id), `duplicate current-news MCQ ID: ${question.id}`);
    mcqIds.add(question.id);
    assert(text(question.question?.en) && text(question.question?.hi), `current-news MCQ ${question.id} lacks bilingual stem`);
    assert(question.options?.length === 4, `current-news MCQ ${question.id} does not have four options`);
    assert(question.options?.every(option => text(option.en) && text(option.hi)), `current-news MCQ ${question.id} has incomplete options`);
    assert(new Set(question.options?.map(option => normalized(option.en))).size === 4, `current-news MCQ ${question.id} repeats English options`);
    assert(new Set(question.options?.map(option => normalized(option.hi))).size === 4, `current-news MCQ ${question.id} repeats Hindi options`);
    const validAnswer = Number.isInteger(question.correctIndex) && question.correctIndex >= 0 && question.correctIndex < 4;
    assert(validAnswer, `current-news MCQ ${question.id} has invalid answer`);
    if (question.options?.length === 4 && validAnswer) {
      assert(!containsAnswer(question.question.en, question.options[question.correctIndex].en) && !containsAnswer(question.question.hi, question.options[question.correctIndex].hi), `current-news MCQ ${question.id} reveals its answer in the stem`);
      assert(!optionLengthOutlier(question.options, question.correctIndex, 'en') && !optionLengthOutlier(question.options, question.correctIndex, 'hi'), `current-news MCQ ${question.id} has an obvious correct-option length outlier`);
    }
    assert(text(question.explanation?.en) && text(question.explanation?.hi), `current-news MCQ ${question.id} lacks bilingual explanation`);
  }
}

console.log(`Structure: ${catalog.subjects.length} subjects / ${topicMap.size} topics / ${starter.questions.length} preserved questions`);
console.log(`Exam mapping: ${examCatalog.exams.length} exams / ${examReport.mappings.reduce((total, exam) => total + exam.topicCount, 0)} resolved exam-topic memberships`);
console.log(`Current Live: ${currentNews.items.length} records / ${mcqIds.size} bilingual MCQs / ${currentNews.items.reduce((total, item) => total + item.links.length, 0)} source links`);
console.log(`40/topic gate: ${coverageReport.completeTopics}/${topicMap.size} topics complete; exact shortfall ${coverageReport.shortfall}`);
console.log(`Preservation: ${coverageReport.preservedBaselineQuestions} baseline questions; ${coverageReport.changedReviewLabels.length} review-label changes`);
if (gaps.length) {
  console.log('\nVERIFIED GAPS:');
  for (const gap of gaps) console.log(`- ${gap}`);
}
if (strictCoverage && coverageReport.shortfall) errors.push(`strict coverage gate failed: exact shortfall ${coverageReport.shortfall}`);
if (strictSources && (coverageReport.questionsWithoutDirectSources || factSourceGaps.length || legacyConceptMappingGaps.length)) errors.push('strict source/mapping gate failed for preserved static content');
if (errors.length) {
  console.error('\nVALIDATION FAILED:');
  for (const error of errors) console.error(`- ${error}`);
  process.exitCode = 1;
} else {
  console.log('\nVALIDATION PASSED (structural gates).');
}
