import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { auditContent } from '../scripts/build-content.mjs';

const audit = await auditContent();

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

test('all legacy exam choices remain available and new choices exist', () => {
  const legacy = new Set(audit.examCatalog.exams.filter(exam => exam.legacy).map(exam => exam.id));
  for (const id of ['general-knowledge', 'upsc-cse', 'ssc', 'banking', 'railways', 'state-exams', 'just-curious']) assert.ok(legacy.has(id), id);
  for (const id of ['upsc-nda-na', 'upsc-cds', 'upsc-capf-ac', 'ssc-cgl', 'ssc-chsl', 'ibps-po', 'rrb-ntpc', 'afcat', 'ctet']) assert.ok(audit.examCatalog.exams.some(exam => exam.id === id && !exam.legacy), id);
});

test('Current Live contains directly checked general current affairs with story-linked MCQs', () => {
  assert.match(audit.currentNews.policy, /general current affairs/);
  assert.match(audit.currentNews.policy, /not recruitment or result updates/);
  assert.match(audit.currentNews.policy, /directly checked/);
  assert.match(audit.currentNews.policy, /No verified news found/);
  assert.ok(audit.currentNews.items.length > 0);
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

test('40-per-topic audit reports the exact current gap instead of hiding it', () => {
  assert.equal(audit.coverageReport.targetPerTopic, 40);
  assert.equal(audit.coverageReport.topics, 345);
  assert.equal(audit.coverageReport.targetTotal, 13_800);
  assert.equal(audit.coverageReport.questions, 1_725);
  assert.equal(audit.coverageReport.shortfall, 12_075);
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
  assert.match(runner, /would exceed the.*question target/);
  assert.match(runner, /ACTUAL_PYQ requires/);
});

test('UI contains separate year/month/day controls, complete explanations and safe external links', async () => {
  const [library, practice] = await Promise.all([
    readFile(new URL('../src/Library.tsx', import.meta.url), 'utf8'),
    readFile(new URL('../src/Practice.tsx', import.meta.url), 'utf8'),
  ]);
  assert.match(library, /aria-label="News year"/);
  assert.match(library, /aria-label="News month"/);
  assert.match(library, /aria-label="News day"/);
  assert.match(library, /No verified news found/);
  assert.match(library, /target="_blank" rel="noopener noreferrer"/);
  assert.match(practice, /q\.wrongReasons\.length === q\.options\.length/);
  assert.match(practice, /Skip this one/);
  assert.match(practice, /Next question/);
});
