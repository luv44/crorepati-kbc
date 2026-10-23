import { createHash } from 'node:crypto';
import { readFile, rename, writeFile } from 'node:fs/promises';
import { writeReports } from './build-content.mjs';

const { checkpoint, coverageReport, examReport, newsReport } = await writeReports();
const digest = createHash('sha256').update(JSON.stringify({ checkpoint, coverageReport, examReport, newsReport })).digest('hex');
const receipt = {
  schemaVersion: 1,
  savedAt: new Date().toISOString(),
  digest,
  status: checkpoint.status,
  currentQuestions: checkpoint.currentQuestions,
  targetTotal: checkpoint.targetTotal,
  exactShortfall: checkpoint.shortfall,
  topicsBelowTarget: checkpoint.topicsBelowTarget,
  examMappingsValid: examReport.allMappingsValid,
  currentNewsRecords: newsReport.records,
  currentNewsOneMinuteAnalyses: newsReport.bilingualOneMinuteAnalyses,
  currentNewsAnalysisKeyPoints: newsReport.analysisKeyPoints,
  currentNewsMcqs: newsReport.bilingualMcqs,
  questionsWithoutDirectSources: coverageReport.questionsWithoutDirectSources,
  factCardsWithoutResolvableSources: coverageReport.factCardsWithoutResolvableSources,
  invalidConceptMappings: coverageReport.invalidConceptMappings,
  reviewLabelChanges: coverageReport.changedReviewLabels.length,
  resumeFrom: 'QUESTION_BUILD_CHECKPOINT.json and content/checkpoints/question-batches.json',
};
const destination = 'reports/checkpoint-receipt.json';
const temporary = `${destination}.tmp`;
await writeFile(temporary, `${JSON.stringify(receipt, null, 2)}\n`);
await rename(temporary, destination);
const starter = await readFile('public/data/starter.json');
console.log(`Checkpoint ${digest.slice(0, 12)} saved. starter.json ${starter.length.toLocaleString()} bytes; exact shortfall ${receipt.exactShortfall}.`);
