import { createHash } from 'node:crypto';
import { mkdir, readFile, rename, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const readJson = async relative => JSON.parse(await readFile(path.join(root, relative), 'utf8'));
const hash = value => createHash('sha256').update(typeof value === 'string' ? value : JSON.stringify(value)).digest('hex');
const stableTime = process.env.BUILD_AT || '2026-10-23T00:00:00+05:30';
const prohibitedPracticeStem = /advanced\s+exam\s+perspective|assessing\s+syllabus|\bsyllabus\b|\bcurriculum\b|\bbenchmarks?\b|\bevaluat(?:e|es|ed|ing|ion)\b|\bscrutiny\b|पाठ्यक्रम|मूल्यांकन/iu;
const conciseOption = value => value.replace(/\s*\([^()]*\)/gu, '').replace(/\s+/g, ' ').trim() || value.trim();
const focusedPracticeQuestion = question => {
  const options = question.options?.map(option => ({ en: conciseOption(option.en), hi: conciseOption(option.hi) })) || [];
  const presentable = options.length === 4
    && question.question.en.length <= 260 && question.question.hi.length <= 320
    && !prohibitedPracticeStem.test(question.question.en) && !prohibitedPracticeStem.test(question.question.hi)
    && options.every(option => option.en.length > 0 && option.en.length <= 160 && option.hi.length > 0 && option.hi.length <= 160 && !/further defined by/iu.test(option.en))
    && new Set(options.map(option => option.en.toLocaleLowerCase())).size === 4
    && new Set(options.map(option => option.hi.toLocaleLowerCase())).size === 4;
  return presentable && (question.id === `Q_${question.topicId}` || question.sourceIds?.length > 0);
};
const normalize = value => value.normalize('NFKC').toLocaleLowerCase().replace(/[^\p{L}\p{N}\s-]/gu, ' ').replace(/\s+/g, ' ').trim();

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
  const focusedQuestions = starter.questions.filter(focusedPracticeQuestion);
  const focusedByTopic = new Map(topics.map(topic => [topic.id, []]));
  for (const question of focusedQuestions) focusedByTopic.get(question.topicId)?.push(question);
  const sourceIds = new Set(starter.sources.map(source => source.id));
  const sourceCompleteCounts = new Map(topics.map(topic => [topic.id, 0]));
  for (const question of starter.questions) if (question.sourceIds?.length && question.sourceIds.every(id => sourceIds.has(id))) sourceCompleteCounts.set(question.topicId, (sourceCompleteCounts.get(question.topicId) || 0) + 1);

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
    focusedCount: focusedByTopic.get(topic.id)?.length || 0,
    sourceCompleteCount: sourceCompleteCounts.get(topic.id) || 0,
    target: targetPerTopic,
    shortfall: Math.max(0, targetPerTopic - (counts.get(topic.id) || 0)),
    focusedShortfall: Math.max(0, targetPerTopic - (focusedByTopic.get(topic.id)?.length || 0)),
    sourceCompleteShortfall: Math.max(0, targetPerTopic - (sourceCompleteCounts.get(topic.id) || 0)),
    rawComplete: (counts.get(topic.id) || 0) >= targetPerTopic,
    focusedComplete: (focusedByTopic.get(topic.id)?.length || 0) >= targetPerTopic,
    sourceComplete: (sourceCompleteCounts.get(topic.id) || 0) >= targetPerTopic,
    complete: (sourceCompleteCounts.get(topic.id) || 0) >= targetPerTopic,
  }));
  const bySubject = catalog.subjects.map(subject => {
    const rows = byTopic.filter(row => row.subjectId === subject.id);
    return {
      subjectId: subject.id,
      title: subject.title,
      topics: rows.length,
      questions: rows.reduce((total, row) => total + row.count, 0),
      focusedQuestions: rows.reduce((total, row) => total + row.focusedCount, 0),
      sourceCompleteQuestions: rows.reduce((total, row) => total + row.sourceCompleteCount, 0),
      target: rows.length * targetPerTopic,
      shortfall: rows.reduce((total, row) => total + row.shortfall, 0),
      focusedShortfall: rows.reduce((total, row) => total + row.focusedShortfall, 0),
      sourceCompleteShortfall: rows.reduce((total, row) => total + row.sourceCompleteShortfall, 0),
      rawCompleteTopics: rows.filter(row => row.rawComplete).length,
      focusedCompleteTopics: rows.filter(row => row.focusedComplete).length,
      completeTopics: rows.filter(row => row.sourceComplete).length,
    };
  });
  const reviewById = new Map(starter.questions.map(question => [question.id, question]));
  const changedReviewLabels = baseline.labels.filter(saved => {
    const current = reviewById.get(saved.id);
    return !current || current.lifecycle !== saved.lifecycle || current.kind !== saved.kind || current.qualityScore !== saved.qualityScore;
  }).map(saved => saved.id);
  const questionsWithDirectSources = starter.questions.filter(question => question.sourceIds?.length && question.sourceIds.every(id => sourceIds.has(id))).length;
  const factCardsWithoutResolvableSources = starter.factCards.filter(card => !card.sourceIds?.length || card.sourceIds.some(id => !sourceIds.has(id))).length;
  const invalidConceptMappingIds = starter.questions.filter(question => {
    const topic = topicMap.get(question.topicId);
    return !topic || question.subjectId !== topic.subjectId || question.chapterId !== topic.chapterId || !question.conceptIds?.every(id => topic.concepts.some(concept => concept.id === id));
  }).map(question => question.id);
  const totalShortfall = byTopic.reduce((total, row) => total + row.shortfall, 0);
  const focusedShortfall = byTopic.reduce((total, row) => total + row.focusedShortfall, 0);
  const sourceCompleteShortfall = byTopic.reduce((total, row) => total + row.sourceCompleteShortfall, 0);
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
    focusedShortfall,
    sourceCompleteShortfall,
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
  const focusedStemKeys = focusedQuestions.map(question => normalize(question.question.en));
  const focusedTokenSets = focusedQuestions.map(question => new Set(normalize(question.question.en).split(' ').filter(token => token.length > 2)));
  const nearDuplicateFocusedStemPairs = [];
  for (let left = 0; left < focusedQuestions.length; left += 1) for (let right = left + 1; right < focusedQuestions.length; right += 1) {
    const intersection = [...focusedTokenSets[left]].filter(token => focusedTokenSets[right].has(token)).length;
    const union = focusedTokenSets[left].size + focusedTokenSets[right].size - intersection;
    if (union && intersection / union >= 0.6) nearDuplicateFocusedStemPairs.push([focusedQuestions[left].id, focusedQuestions[right].id]);
  }
  const practiceQualityReport = {
    generatedAt: stableTime,
    policy: 'The full legacy corpus and labels remain preserved. Learner-facing practice serves one concise canonical legacy question per topic plus future directly sourced questions that pass the non-boilerplate gate.',
    preservedRecords: starter.questions.length,
    focusedLearnerFacingQuestions: focusedQuestions.length,
    withheldLegacyExpansionDrafts: starter.questions.length - focusedQuestions.length,
    topics: topics.length,
    topicsWithFocusedQuestions: topics.filter(topic => focusedByTopic.get(topic.id)?.length).length,
    topicsMissingFocusedQuestions: topics.filter(topic => !focusedByTopic.get(topic.id)?.length).map(topic => topic.id),
    topicsWithMultipleCanonicalLegacyQuestions: topics.filter(topic => (focusedByTopic.get(topic.id)?.filter(question => question.id === `Q_${topic.id}`).length || 0) > 1).map(topic => topic.id),
    exactDuplicateFocusedStems: focusedStemKeys.length - new Set(focusedStemKeys).size,
    nearDuplicateFocusedStemPairs,
    prohibitedFocusedStemIds: focusedQuestions.filter(question => prohibitedPracticeStem.test(question.question.en) || prohibitedPracticeStem.test(question.question.hi)).map(question => question.id),
    concatenatedFocusedOptionIds: focusedQuestions.filter(question => question.options.some(option => /further defined by/iu.test(conciseOption(option.en)))).map(question => question.id),
    overlongFocusedOptionIds: focusedQuestions.filter(question => question.options.some(option => conciseOption(option.en).length > 160 || conciseOption(option.hi).length > 160)).map(question => question.id),
    bySubject: catalog.subjects.map(subject => ({ subjectId: subject.id, topics: subject.chapters.reduce((total, chapter) => total + chapter.topics.length, 0), focusedQuestions: focusedQuestions.filter(question => question.subjectId === subject.id).length })),
    byTopic: topics.map(topic => ({ topicId: topic.id, questionIds: (focusedByTopic.get(topic.id) || []).map(question => question.id) })),
  };
  coverageReport.focusedLearnerFacingQuestions = practiceQualityReport.focusedLearnerFacingQuestions;
  coverageReport.withheldLegacyExpansionDrafts = practiceQualityReport.withheldLegacyExpansionDrafts;
  const recordsByDate = Object.fromEntries([...new Set(currentNews.items.map(item => item.publicationDate))].sort().map(date => [date, currentNews.items.filter(item => item.publicationDate === date).length]));
  const newsReport = {
    generatedAt: stableTime,
    records: currentNews.items.length,
    verifiedRecordTargetPerRun: currentNews.verifiedRecordTargetPerRun,
    remainingToRunTarget: Math.max(0, currentNews.verifiedRecordTargetPerRun - currentNews.items.length),
    publicationDates: Object.keys(recordsByDate),
    recordsByDate,
    maxRecordsOnOneDate: Math.max(0, ...Object.values(recordsByDate)),
    links: currentNews.items.reduce((total, item) => total + item.links.length, 0),
    bilingualOneMinuteAnalyses: currentNews.items.filter(item => item.analysis?.readTimeMinutes === 1 && item.analysis.keyPoints?.every(point => point.en && point.hi) && item.analysis.whatToRemember?.en && item.analysis.whatToRemember?.hi).length,
    analysisKeyPoints: currentNews.items.reduce((total, item) => total + (item.analysis?.keyPoints?.length || 0), 0),
    bilingualMcqs: currentNews.items.reduce((total, item) => total + item.mcqs.length, 0),
    latestPublicationDate: currentNews.items.map(item => item.publicationDate).sort().at(-1) || null,
  };
  const checkpoint = {
    schemaVersion: 1,
    updatedAt: stableTime,
    status: sourceCompleteShortfall ? 'IN_PROGRESS_SOURCE_REVIEW_REQUIRED' : 'COMPLETE',
    policy: 'Only source-backed, bilingual, four-option questions that pass review may be applied. The runner saves after each small batch and resumes idempotently from its ledger.',
    targetPerTopic,
    targetTotal,
    currentQuestions: starter.questions.length,
    focusedLearnerFacingQuestions: practiceQualityReport.focusedLearnerFacingQuestions,
    withheldLegacyExpansionDrafts: practiceQualityReport.withheldLegacyExpansionDrafts,
    preservedBaselineQuestions: baseline.questionCount,
    shortfall: totalShortfall,
    focusedShortfall,
    sourceCompleteShortfall,
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
  return { catalog, starter, examCatalog, currentNews, baseline, topicMap, examReport, coverageReport, practiceQualityReport, newsReport, checkpoint };
}

export async function writeReports() {
  const { examReport, coverageReport, practiceQualityReport, newsReport, checkpoint } = await auditContent();
  await Promise.all([
    atomicJson('reports/exam-mapping-report.json', examReport),
    atomicJson('reports/question-coverage-report.json', coverageReport),
    atomicJson('reports/practice-quality-report.json', practiceQualityReport),
    atomicJson('reports/current-news-report.json', newsReport),
    atomicJson('QUESTION_BUILD_CHECKPOINT.json', checkpoint),
  ]);
  console.log(`Exam maps: ${examReport.exams} (${examReport.allMappingsValid ? 'valid' : 'invalid'})`);
  console.log(`Current Live: ${newsReport.records} records, ${newsReport.bilingualMcqs} bilingual MCQs`);
  console.log(`Question coverage: ${coverageReport.questions}/${coverageReport.targetTotal}; raw record shortfall ${coverageReport.shortfall}; focused shortfall ${coverageReport.focusedShortfall}; source-complete shortfall ${coverageReport.sourceCompleteShortfall}`);
  console.log(`Focused practice: ${practiceQualityReport.focusedLearnerFacingQuestions} unique questions; ${practiceQualityReport.withheldLegacyExpansionDrafts} repetitive drafts withheld`);
  console.log(`Review labels changed: ${coverageReport.changedReviewLabels.length}`);
  return { examReport, coverageReport, practiceQualityReport, newsReport, checkpoint };
}

if (path.resolve(process.argv[1] || '') === fileURLToPath(import.meta.url)) await writeReports();
