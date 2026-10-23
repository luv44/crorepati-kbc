# Acceptance matrix — 23 October 2026 checkpoint

| Gate | Status | Evidence |
| --- | --- | --- |
| Production React/Vite app builds | PASS | `npm run build`; service-worker receipt in `BUILD_STATE.md` and `reports/checkpoint-receipt.json`. |
| Canonical hierarchy | PASS | 26 subjects / 82 chapters / 345 topics; `reports/exam-mapping-report.json`. |
| Exam dropdown and hierarchy mapping | PASS | 22/22 mappings valid; 6,151 resolved exam-topic memberships. |
| KBC Crorepati profile | PASS | Maps all 26 subjects, 82 chapters, and 345 topics in Learn and Practice. |
| Simplified entry screen | PASS | Name + exam only; the pictured subject-interest grid and coverage-note block were removed. |
| Focused question behavior | PASS | Exactly 345 concise canonical questions are learner-facing—one for every topic; 0 exact or near-duplicate focused stems, 0 prohibited stems, 0 concatenated/overlong focused option sets. See `reports/practice-quality-report.json`. |
| Legacy preservation | PASS | All 1,725 records and lifecycle/kind/quality labels remain present; 0 label changes. The 1,380 repetitive expansion drafts are preserved for audit but withheld from learner-facing surfaces. |
| Practice session reliability | PASS | Exam-scoped draft keys, draft content/index/answer validation, safe reset, visible Skip/Next, exact session count, and no blank-screen crash on legacy evidence. |
| Current Live selectors | PASS | Separate Year, Month, Day, and Topic selectors, including Any topic. |
| Current Live integrity | PASS for accepted feed | 13 directly checked general-current-affairs records, 13 unique official links, visible dates/evidence, 26 complete bilingual MCQs, and exact empty state. |
| Current Live uncapped display | PASS | All 10 checked stories and all 20 linked questions for 23 October render without an item cap. |
| Current Live 150/run target | IN PROGRESS | 13/150 directly checked records; exact gap 137. No filler accepted. |
| Reviewed news ingestion | PASS | `scripts/current-news-batch.mjs`, schema, 25-record durable saves, ledger, idempotence/rejection smoke checks. |
| 40 distinct questions per topic — raw arithmetic | BLOCKED | 1,725/13,800 preserved records; raw gap 12,075. |
| 40 focused non-repetitive questions per topic | BLOCKED | 345/13,800 focused questions; gap 13,455. |
| 40 source-complete questions per topic | BLOCKED | 0/13,800 source-complete legacy questions; strict gap 13,800. |
| Mapping/source legacy debt | BLOCKED | 1,725 questions without direct sources, 53 unresolved FactCards, and 28 invalid concept mappings. |
| Deterministic tests | PASS | 10/10 Node tests. |
| Real-browser tests | PASS | 9/9 Playwright scenarios across desktop, mobile, and tablet Chromium. |
| Public HTTPS deployment | BLOCKED | No authorized hosting target or production URL is configured. |

`FINAL_ELIGIBLE=false` remains intentional until the focused, source-complete 40-per-topic gate and inherited mapping/source debt are resolved.
