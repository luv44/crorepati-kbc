import { createHash } from 'node:crypto';
import { mkdir, readFile, rename, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const readJson = async relative => JSON.parse(await readFile(path.join(root, relative), 'utf8'));
const hash = value => createHash('sha256').update(typeof value === 'string' ? value : JSON.stringify(value)).digest('hex');
const stableTime = process.env.BUILD_AT || '2026-10-23T00:00:00+05:30';

async function atomicJson(relative, value) {
  const destination = path.join(root, relative);
  await mkdir(path.dirname(destination), { recursive: true });
  const temporary = `${destination}.tmp`;
  await writeFile(temporary, `${JSON.stringify(value, null, 2)}\n`);
  await rename(temporary, destination);
}

export async function auditContent() {
  const [catalog, starter, examCatalog, currentNews, baseline] = await Promise.all([
    readJson('public/data/catalog.json'),
    readJson('public/data/starter.json'),
    readJson('public/data/exams.json'),
    readJson('public/data/current-news.json'),
    readJson('content/checkpoints/legacy-review-labels.json'),
  ]);
  const subjects = new Map(catalog.subjects.map(subject => [subject.id, subject]));
  const topics = catalog.subjects.flatMap(subject => subject.chapters.flatMap(chapter => chapter.topics));
  const topicMap = new Map(topics.map(topic => [topic.id, topic]));
  const counts = new Map(topics.map(topic => [topic.id, 0]));
  for (const question of starter.questions) counts.set(question.topicId, (counts.get(question.topicId) || 0) + 1);

  const mappings = examCatalog.exams.map(exam => {
    const missingSubjectIds = exam.subjectIds.filter(id => !subjects.has(id));
    const tree = exam.subjectIds.filter(id => subjects.has(id)).map(id => {
      const subject = subjects.get(id);
      return {
        id: subject.id,
        title: subject.title,
        chapters: subject.chapters.map(chapter => ({
          id: chapter.id,
          title: chapter.title,
          topics: chapter.topics.map(topic => ({ id: topic.id, title: topic.title })),
        })),
      };
    });
    return {
      id: exam.id,
      name: exam.name,
      legacy: exam.legacy,
      officialUrl: exam.officialUrl,
      subjectCount: tree.length,
      chapterCount: tree.reduce((total, subject) => total + subject.chapters.length, 0),
      topicCount: tree.reduce((total, subject) => total + subject.chapters.reduce((sum, chapter) => sum + chapter.topics.length, 0), 0),
      missingSubjectIds,
      completeHierarchy: !missingSubjectIds.length && tree.every(subject => subject.chapters.length && subject.chapters.every(chapter => chapter.topics.length)),
      subjects: tree,
    };
  });

  const targetPerTopic = 40;
  const byTopic = topics.map(topic => ({
    topicId: topic.id,
    subjectId: topic.subjectId,
    chapterId: topic.chapterId,
    title: topic.title,
    count: counts.get(topic.id) || 0,
    target: targetPerTopic,
    shortfall: Math.max(0, targetPerTopic - (counts.get(topic.id) || 0)),
    complete: (counts.get(topic.id) || 0) >= targetPerTopic,
  }));
  const bySubject = catalog.subjects.map(subject => {
    const rows = byTopic.filter(row => row.subjectId === subject.id);
    return {
      subjectId: subject.id,
      title: subject.title,
      topics: rows.length,
      questions: rows.reduce((total, row) => total + row.count, 0),
      target: rows.length * targetPerTopic,
      shortfall: rows.reduce((total, row) => total + row.shortfall, 0),
      completeTopics: rows.filter(row => row.complete).length,
    };
  });
  const reviewById = new Map(starter.questions.map(question => [question.id, question]));
  const changedReviewLabels = baseline.labels.filter(saved => {
    const current = reviewById.get(saved.id);
    return !current || current.lifecycle !== saved.lifecycle || current.kind !== saved.kind || current.qualityScore !== saved.qualityScore;
  }).map(saved => saved.id);
  const sourceIds = new Set(starter.sources.map(source => source.id));
  const questionsWithDirectSources = starter.questions.filter(question => question.sourceIds?.length && question.sourceIds.every(id => sourceIds.has(id))).length;
  const factCardsWithoutResolvableSources = starter.factCards.filter(card => !card.sourceIds?.length || card.sourceIds.some(id => !sourceIds.has(id))).length;
  const invalidConceptMappingIds = starter.questions.filter(question => {
    const topic = topicMap.get(question.topicId);
    return !topic || question.subjectId !== topic.subjectId || question.chapterId !== topic.chapterId || !question.conceptIds?.every(id => topic.concepts.some(concept => concept.id === id));
  }).map(question => question.id);
  const totalShortfall = byTopic.reduce((total, row) => total + row.shortfall, 0);
  const targetTotal = topics.length * targetPerTopic;
  const questionIds = starter.questions.map(question => question.id);

  const examReport = {
    generatedAt: stableTime,
    catalogVersion: catalog.version,
    exams: mappings.length,
    legacyExams: mappings.filter(mapping => mapping.legacy).length,
    newExams: mappings.filter(mapping => !mapping.legacy).length,
    allMappingsValid: mappings.every(mapping => mapping.completeHierarchy),
    mappings,
  };
  const coverageReport = {
    generatedAt: stableTime,
    targetPerTopic,
    subjects: catalog.subjects.length,
    topics: topics.length,
    questions: starter.questions.length,
    targetTotal,
    shortfall: totalShortfall,
    completeTopics: byTopic.filter(row => row.complete).length,
    topicsBelowTarget: byTopic.filter(row => !row.complete).length,
    questionsWithDirectSources,
    questionsWithoutDirectSources: starter.questions.length - questionsWithDirectSources,
    factCardsWithoutResolvableSources,
    invalidConceptMappings: invalidConceptMappingIds.length,
    invalidConceptMappingIds,
    duplicateQuestionIds: questionIds.length - new Set(questionIds).size,
    preservedBaselineQuestions: baseline.questionCount,
    changedReviewLabels,
    bySubject,
    byTopic,
  };
  const newsReport = {
    generatedAt: stableTime,
    records: currentNews.items.length,
    publicationDates: [...new Set(currentNews.items.map(item => item.publicationDate))].sort(),
    links: currentNews.items.reduce((total, item) => total + item.links.length, 0),
    bilingualMcqs: currentNews.items.reduce((total, item) => total + item.mcqs.length, 0),
    latestPublicationDate: currentNews.items.map(item => item.publicationDate).sort().at(-1) || null,
  };
  const checkpoint = {
    schemaVersion: 1,
    updatedAt: stableTime,
    status: totalShortfall ? 'IN_PROGRESS_SOURCE_REVIEW_REQUIRED' : 'COMPLETE',
    policy: 'Only source-backed, bilingual, four-option questions that pass review may be applied. The runner saves after each small batch and resumes idempotently from its ledger.',
    targetPerTopic,
    targetTotal,
    currentQuestions: starter.questions.length,
    preservedBaselineQuestions: baseline.questionCount,
    shortfall: totalShortfall,
    completeTopics: coverageReport.completeTopics,
    topicsBelowTarget: coverageReport.topicsBelowTarget,
    questionsWithDirectSources,
    questionsWithoutDirectSources: starter.questions.length - questionsWithDirectSources,
    factCardsWithoutResolvableSources,
    invalidConceptMappings: invalidConceptMappingIds.length,
    changedReviewLabels,
    batchSize: 25,
    batchLedger: 'content/checkpoints/question-batches.json',
    nextTopics: byTopic.filter(row => row.shortfall).slice(0, 25),
    hashes: {
      starter: hash(await readFile(path.join(root, 'public/data/starter.json'), 'utf8')),
      catalog: hash(await readFile(path.join(root, 'public/data/catalog.json'), 'utf8')),
      exams: hash(await readFile(path.join(root, 'public/data/exams.json'), 'utf8')),
      currentNews: hash(await readFile(path.join(root, 'public/data/current-news.json'), 'utf8')),
    },
  };
  return { catalog, starter, examCatalog, currentNews, baseline, topicMap, examReport, coverageReport, newsReport, checkpoint };
}

export async function writeReports() {
  const { examReport, coverageReport, newsReport, checkpoint } = await auditContent();
  await Promise.all([
    atomicJson('reports/exam-mapping-report.json', examReport),
    atomicJson('reports/question-coverage-report.json', coverageReport),
    atomicJson('reports/current-news-report.json', newsReport),
    atomicJson('QUESTION_BUILD_CHECKPOINT.json', checkpoint),
  ]);
  console.log(`Exam maps: ${examReport.exams} (${examReport.allMappingsValid ? 'valid' : 'invalid'})`);
  console.log(`Current Live: ${newsReport.records} records, ${newsReport.bilingualMcqs} bilingual MCQs`);
  console.log(`Question coverage: ${coverageReport.questions}/${coverageReport.targetTotal}; exact shortfall ${coverageReport.shortfall}`);
  console.log(`Review labels changed: ${coverageReport.changedReviewLabels.length}`);
  return { examReport, coverageReport, newsReport, checkpoint };
}

if (path.resolve(process.argv[1] || '') === fileURLToPath(import.meta.url)) await writeReports();
