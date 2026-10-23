import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { auditContent } from '../scripts/build-content.mjs';
import { conciseOptionText, focusedPracticeQuestion } from '../src/domain.ts';

const audit = await auditContent();
const currentNewsLedger = JSON.parse(await readFile(new URL('../content/checkpoints/current-news-batches.json', import.meta.url), 'utf8'));

test('every exam resolves subject → chapter → topic hierarchy', () => {
  assert.equal(audit.examReport.allMappingsValid, true);
  assert.equal(audit.examReport.exams, audit.examCatalog.exams.length);
  assert.ok(audit.examReport.newExams >= 10);
  for (const exam of audit.examReport.mappings) {
    assert.ok(exam.subjectCount > 0, exam.id);
    assert.ok(exam.chapterCount > 0, exam.id);
    assert.ok(exam.topicCount > 0, exam.id);
    assert.equal(exam.missingSubjectIds.length, 0, exam.id);
    for (const subject of exam.subjects) {
      assert.ok(subject.chapters.length > 0, `${exam.id}/${subject.id}`);
      for (const chapter of subject.chapters) assert.ok(chapter.topics.length > 0, `${exam.id}/${chapter.id}`);
    }
  }
});

test('all legacy exam choices remain available and KBC Crorepati maps the complete hierarchy', () => {
  const legacy = new Set(audit.examCatalog.exams.filter(exam => exam.legacy).map(exam => exam.id));
  for (const id of ['general-knowledge', 'upsc-cse', 'ssc', 'banking', 'railways', 'state-exams', 'just-curious']) assert.ok(legacy.has(id), id);
  for (const id of ['kbc-crorepati', 'upsc-nda-na', 'upsc-cds', 'upsc-capf-ac', 'ssc-cgl', 'ssc-chsl', 'ibps-po', 'rrb-ntpc', 'afcat', 'ctet']) assert.ok(audit.examCatalog.exams.some(exam => exam.id === id && !exam.legacy), id);
  const kbc = audit.examReport.mappings.find(exam => exam.id === 'kbc-crorepati');
  assert.ok(kbc);
  assert.equal(kbc.subjectCount, 26);
  assert.equal(kbc.chapterCount, 82);
  assert.equal(kbc.topicCount, 345);
  assert.deepEqual(kbc.subjects.map(subject => subject.id), audit.catalog.subjects.map(subject => subject.id));
});

test('Current Live contains directly checked general current affairs with story-linked MCQs', () => {
  assert.match(audit.currentNews.policy, /general current affairs/);
  assert.match(audit.currentNews.policy, /not recruitment or result updates/);
  assert.match(audit.currentNews.policy, /directly checked/);
  assert.match(audit.currentNews.policy, /No verified news found/);
  assert.ok(audit.currentNews.items.length > 0);
  assert.equal(audit.currentNews.verifiedRecordTargetPerRun, 150);
  assert.equal(audit.newsReport.verifiedRecordTargetPerRun, 150);
  assert.equal(audit.newsReport.remainingToRunTarget, 150 - audit.currentNews.items.length);
  assert.equal(currentNewsLedger.targetPerRun, 150);
  assert.deepEqual(new Set(currentNewsLedger.appliedItems.map(item => item.id)), new Set(audit.currentNews.items.map(item => item.id)));
  const sameDateStories = audit.currentNews.items.filter(item => item.publicationDate === '2026-10-23');
  assert.ok(sameDateStories.length >= 10, 'expected the independently verified 23 October multi-story feed');
  assert.equal(audit.newsReport.recordsByDate['2026-10-23'], sameDateStories.length);
  assert.ok(audit.newsReport.maxRecordsOnOneDate >= 10);
  assert.ok(sameDateStories.every(item => item.mcqs.length > 0), 'every same-date story must retain its questions');
  const sourceUrls = audit.currentNews.items.flatMap(item => item.links.map(link => link.url));
  assert.equal(new Set(sourceUrls).size, sourceUrls.length, 'each story must open its own verified source link');
  assert.equal(audit.newsReport.bilingualOneMinuteAnalyses, audit.currentNews.items.length);
  assert.ok(audit.newsReport.analysisKeyPoints >= audit.currentNews.items.length * 3);
  for (const item of audit.currentNews.items) {
    assert.match(item.publicationDate, /^\d{4}-\d{2}-\d{2}$/);
    assert.ok(item.evidenceQuote.length > 30);
    assert.ok(item.category.en && item.category.hi);
    assert.ok(item.links.length > 0);
    for (const link of item.links) {
      const url = new URL(link.url);
      assert.equal(url.protocol, 'https:');
      assert.ok(url.hostname.endsWith('.gov.in') || url.hostname.endsWith('.nic.in'), url.hostname);
    }
    assert.ok(item.title.en && item.title.hi && item.summary.en && item.summary.hi);
    assert.equal(item.analysis.readTimeMinutes, 1);
    assert.ok(item.analysis.keyPoints.length >= 3);
    assert.ok(item.analysis.keyPoints.every(point => point.en && point.hi));
    assert.equal(new Set(item.analysis.keyPoints.map(point => point.en)).size, item.analysis.keyPoints.length);
    assert.equal(new Set(item.analysis.keyPoints.map(point => point.hi)).size, item.analysis.keyPoints.length);
    assert.ok(item.analysis.whatToRemember.en && item.analysis.whatToRemember.hi);
    assert.ok(item.mcqs.length > 0);
    for (const question of item.mcqs) {
      assert.ok(question.question.en && question.question.hi);
      assert.equal(question.options.length, 4);
      assert.ok(question.options.every(option => option.en && option.hi));
      assert.ok(question.correctIndex >= 0 && question.correctIndex < 4);
      assert.ok(question.explanation.en && question.explanation.hi);
    }
  }
});

test('legacy questions and review labels are preserved exactly', () => {
  assert.equal(audit.coverageReport.preservedBaselineQuestions, 1725);
  assert.equal(audit.starter.questions.length, 1725);
  assert.deepEqual(audit.coverageReport.changedReviewLabels, []);
  assert.equal(audit.coverageReport.duplicateQuestionIds, 0);
  assert.equal(audit.coverageReport.invalidConceptMappings, 28);
});

test('learner-facing practice keeps one concise, unique canonical question for every topic', () => {
  const focused = audit.starter.questions.filter(question => focusedPracticeQuestion(question));
  assert.equal(focused.length, 345);
  assert.equal(audit.practiceQualityReport.focusedLearnerFacingQuestions, focused.length);
  assert.equal(audit.practiceQualityReport.exactDuplicateFocusedStems, 0);
  assert.deepEqual(audit.practiceQualityReport.nearDuplicateFocusedStemPairs, []);
  assert.deepEqual(audit.practiceQualityReport.topicsMissingFocusedQuestions, []);
  assert.equal(audit.starter.questions.length - focused.length, 1_380, 'repetitive legacy drafts remain preserved but withheld');
  const byTopic = new Map();
  for (const question of focused) byTopic.set(question.topicId, [...(byTopic.get(question.topicId) || []), question]);
  const normalizedStems = focused.map(question => question.question.en.normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}]+/gu, ' ').trim());
  assert.equal(new Set(normalizedStems).size, focused.length, 'focused stems must be unique');
  const prohibited = /advanced\s+exam\s+perspective|assessing\s+syllabus|\bsyllabus\b|\bcurriculum\b|\bbenchmarks?\b|\bevaluat(?:e|es|ed|ing|ion)\b|\bscrutiny\b|पाठ्यक्रम|मूल्यांकन/iu;
  for (const subject of audit.catalog.subjects) for (const chapter of subject.chapters) for (const topic of chapter.topics) {
    assert.equal(byTopic.get(topic.id)?.length, 1, `${subject.id}/${chapter.id}/${topic.id}`);
  }
  for (const question of focused) {
    assert.doesNotMatch(question.question.en, prohibited, question.id);
    assert.doesNotMatch(question.question.hi, prohibited, question.id);
    assert.equal(question.options.length, 4, question.id);
    assert.ok(question.question.en.length <= 260 && question.question.hi.length <= 320, `${question.id}: overlong focused stem`);
    assert.ok(question.options.every(option => conciseOptionText(option.en).length <= 160 && conciseOptionText(option.hi).length <= 160), `${question.id}: overlong focused option`);
    assert.ok(question.options.every(option => !/further defined by/i.test(conciseOptionText(option.en))), `${question.id}: concatenated option`);
    assert.equal(new Set(question.options.map(option => conciseOptionText(option.en).toLocaleLowerCase())).size, 4, `${question.id}: repeated English option`);
    assert.equal(new Set(question.options.map(option => conciseOptionText(option.hi).toLocaleLowerCase())).size, 4, `${question.id}: repeated Hindi option`);
  }
});

test('40-per-topic audit reports raw, focused and source-complete gaps instead of hiding them', () => {
  assert.equal(audit.coverageReport.targetPerTopic, 40);
  assert.equal(audit.coverageReport.topics, 345);
  assert.equal(audit.coverageReport.targetTotal, 13_800);
  assert.equal(audit.coverageReport.questions, 1_725);
  assert.equal(audit.coverageReport.shortfall, 12_075);
  assert.equal(audit.coverageReport.focusedShortfall, 13_455);
  assert.equal(audit.coverageReport.sourceCompleteShortfall, 13_800);
  assert.equal(audit.coverageReport.topicsBelowTarget, 345);
  assert.equal(audit.coverageReport.completeTopics, 0);
  assert.ok(audit.coverageReport.byTopic.every(topic => topic.count === 5 && topic.shortfall === 35));
});

test('starter pack metadata and catalogue counts stay synchronized', async () => {
  const bytes = await readFile(new URL('../public/data/starter.json', import.meta.url));
  const meta = audit.catalog.packs.find(pack => pack.id === audit.starter.id);
  assert.ok(meta);
  assert.equal(meta.questionCount, audit.starter.questions.length);
  assert.equal(meta.size, bytes.length);
  assert.equal(meta.sha256, createHash('sha256').update(bytes).digest('hex'));
  assert.equal(audit.catalog.counts.factCards, audit.starter.factCards.length);
});

test('reviewed batch runner has interruption recovery and strict content gates', async () => {
  const runner = await readFile(new URL('../scripts/question-batch.mjs', import.meta.url), 'utf8');
  assert.match(runner, /question-batch-transaction\.json/);
  assert.match(runner, /recoverBundle/);
  assert.match(runner, /near-duplicate English stem/);
  assert.match(runner, /prohibited boilerplate appears in the stem/);
  assert.match(runner, /answer option is overlong or concatenated/);
  assert.match(runner, /would exceed the.*source-complete target/);
  assert.match(runner, /ACTUAL_PYQ requires/);
});

test('reviewed Current Live runner targets 150 records without accepting unchecked filler', async () => {
  const [runner, schema] = await Promise.all([
    readFile(new URL('../scripts/current-news-batch.mjs', import.meta.url), 'utf8'),
    readFile(new URL('../content/schemas/reviewed-current-news-batch.schema.json', import.meta.url), 'utf8').then(JSON.parse),
  ]);
  assert.match(runner, /targetPerRun = 150/);
  assert.match(runner, /directSourcePagesChecked/);
  assert.match(runner, /current-news-batches\.json/);
  assert.match(runner, /one reviewed run accepts at most/);
  assert.match(runner, /reuses a source URL/);
  assert.match(runner, /containsAnswer/);
  assert.match(runner, /optionLengthOutlier/);
  assert.match(runner, /overlong answer option/);
  assert.match(runner, /prohibited boilerplate/);
  assert.match(runner, /repeats an existing stem/);
  assert.match(runner, /near-duplicate of an existing stem/);
  assert.match(runner, /near-duplicate of an existing story title/);
  assert.match(runner, /[Hh]indi text/);
  assert.equal(schema.properties.items.maxItems, 150);
  assert.equal(schema.properties.review.properties.directSourcePagesChecked.const, true);
});

test('UI contains separate year/month/day/topic controls, complete explanations and safe external links', async () => {
  const [library, practice, learn, app, context] = await Promise.all([
    readFile(new URL('../src/Library.tsx', import.meta.url), 'utf8'),
    readFile(new URL('../src/Practice.tsx', import.meta.url), 'utf8'),
    readFile(new URL('../src/Learn.tsx', import.meta.url), 'utf8'),
    readFile(new URL('../src/App.tsx', import.meta.url), 'utf8'),
    readFile(new URL('../src/context.tsx', import.meta.url), 'utf8'),
  ]);
  assert.match(library, /aria-label="News year"/);
  assert.match(library, /aria-label="News month"/);
  assert.match(library, /aria-label="News day"/);
  assert.match(library, /aria-label="Current news topic"/);
  assert.match(library, /Any topic/);
  assert.match(library, /VERIFIED NEWS TARGET PER REVIEW RUN/);
  assert.match(library, /No verified news found/);
  assert.match(library, /1-minute brief/);
  assert.match(library, /All questions/);
  assert.match(library, /Showing all.*no story limit/);
  assert.match(library, /ALL VERIFIED STORIES FOR THIS DATE/);
  assert.match(library, /QUESTIONS FOR THIS STORY/);
  assert.match(library, /\{items\.map\(item =>/);
  assert.doesNotMatch(library, /items\.slice/);
  assert.match(library, /item\.mcqs\.map/);
  assert.match(library, /quizStory\.mcqs\.map/);
  assert.match(library, /verifiedDates\.map/);
  assert.doesNotMatch(library, /verifiedDates\.slice/);
  assert.match(library, /Save brief/);
  assert.match(library, /offline reading/);
  assert.match(library, /Skip this one/);
  assert.match(library, /Next question/);
  assert.match(library, /target="_blank" rel="noopener noreferrer"/);
  assert.match(practice, /q\.wrongReasons\.length === q\.options\.length/);
  assert.ok(audit.starter.factCards.some(fact => !Array.isArray(fact.evidence)), 'fixture must retain legacy non-array evidence records');
  assert.match(practice, /Array\.isArray\(fact\.evidence\)/);
  assert.match(practice, /does not yet have a resolvable direct-source excerpt/);
  assert.match(practice, /:exam=\$\{selectedExam\.id\}/);
  assert.match(practice, /parsed\.examId === selectedExam\.id/);
  assert.match(practice, /run\?\.examId === selectedExam\.id/);
  assert.match(practice, /parsed\.index < parsed\.ids\.length/);
  assert.match(practice, /Return to question selection/);
  assert.match(practice, /Clear all practice filters/);
  assert.match(practice, /Skip this one/);
  assert.match(practice, /Next question/);
  assert.match(learn, /Array\.isArray\(f\.evidence\)/);
  assert.match(learn, /does not yet have a structured direct-source excerpt/);
  assert.doesNotMatch(app, /interest-grid/);
  assert.doesNotMatch(app, /setInterests/);
  assert.match(context, /focusedPracticeQuestion/);
  assert.match(practice, /conciseOptionText/);
  assert.match(practice, /repetitive expansion drafts remain preserved/);
});
