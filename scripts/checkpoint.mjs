import { createHash } from 'node:crypto';
import { readFile, rename, writeFile } from 'node:fs/promises';
import { writeReports } from './build-content.mjs';

const { checkpoint, coverageReport, practiceQualityReport, examReport, newsReport } = await writeReports();
const digest = createHash('sha256').update(JSON.stringify({ checkpoint, coverageReport, practiceQualityReport, examReport, newsReport })).digest('hex');
const receipt = {
  schemaVersion: 1,
  savedAt: new Date().toISOString(),
  digest,
  status: checkpoint.status,
  currentQuestions: checkpoint.currentQuestions,
  targetTotal: checkpoint.targetTotal,
  rawRecordShortfall: checkpoint.shortfall,
  focusedShortfall: checkpoint.focusedShortfall,
  sourceCompleteShortfall: checkpoint.sourceCompleteShortfall,
  focusedLearnerFacingQuestions: practiceQualityReport.focusedLearnerFacingQuestions,
  withheldLegacyExpansionDrafts: practiceQualityReport.withheldLegacyExpansionDrafts,
  exactDuplicateFocusedStems: practiceQualityReport.exactDuplicateFocusedStems,
  nearDuplicateFocusedStemPairs: practiceQualityReport.nearDuplicateFocusedStemPairs.length,
  topicsBelowTarget: checkpoint.topicsBelowTarget,
  examMappingsValid: examReport.allMappingsValid,
  currentNewsRecords: newsReport.records,
  currentNewsTargetPerRun: newsReport.verifiedRecordTargetPerRun,
  currentNewsRemainingToRunTarget: newsReport.remainingToRunTarget,
  currentNewsOneMinuteAnalyses: newsReport.bilingualOneMinuteAnalyses,
  currentNewsAnalysisKeyPoints: newsReport.analysisKeyPoints,
  currentNewsMcqs: newsReport.bilingualMcqs,
  questionsWithoutDirectSources: coverageReport.questionsWithoutDirectSources,
  factCardsWithoutResolvableSources: coverageReport.factCardsWithoutResolvableSources,
  invalidConceptMappings: coverageReport.invalidConceptMappings,
  reviewLabelChanges: coverageReport.changedReviewLabels.length,
  resumeFrom: 'QUESTION_BUILD_CHECKPOINT.json, content/checkpoints/question-batches.json, and content/checkpoints/current-news-batches.json',
};
const destination = 'reports/checkpoint-receipt.json';
const temporary = `${destination}.tmp`;
await writeFile(temporary, `${JSON.stringify(receipt, null, 2)}\n`);
await rename(temporary, destination);
const starter = await readFile('public/data/starter.json');
console.log(`Checkpoint ${digest.slice(0, 12)} saved. starter.json ${starter.length.toLocaleString()} bytes; source-complete shortfall ${receipt.sourceCompleteShortfall}; Current Live gap ${receipt.currentNewsRemainingToRunTarget}.`);
