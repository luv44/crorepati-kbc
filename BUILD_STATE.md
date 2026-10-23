# Crorepati Revision — current build state

Updated: **2026-10-23 (Asia/Calcutta)**

## Active checkpoint

- Branch baseline: `2e93cc1a981e7515787fe59ee9f33828fd65d636`
- Canonical catalogue: 26 subjects / 82 chapters / 345 topics
- Preserved question corpus: 1,725 questions (5 per topic)
- Baseline review-label preservation: 1,725/1,725 present; 0 lifecycle/kind/quality changes
- Exam views: 21 total (7 legacy + 14 new)
- Exam hierarchy validation: 21/21 valid; 5,806 resolved exam-topic memberships
- Current Live: 3 directly checked general-current-affairs records / 3 official links / 6 story-linked bilingual MCQs
- Target: 40 distinct, source-backed questions per canonical topic = 13,800
- Complete topics: 0/345
- Exact verified shortfall: **12,075**
- Static integrity debt inherited from baseline: 1,725 questions without direct source IDs; 53 FactCards with absent/empty source references; 28 questions with concept IDs outside their topic
- Production build: PASS (TypeScript + Vite, 1,602 modules + generated service worker)
- Deterministic Node tests: PASS (8/8)
- Structural validation: PASS
- Strict coverage/source release validation: BLOCKED by the exact gaps above
- Browser E2E: scenarios authored; not run because this environment lacks the Playwright Chromium executable
- Live development preview: Vite on `0.0.0.0:5173`, preview host allowed

## Implemented UI/data behavior

- Global exam selector scopes Home, Learn, Topic, Practice, Search, Smart Revision, Performance, Downloads, and Settings.
- Exam mappings resolve canonical subject → chapter → topic nodes; no copied hierarchy can silently diverge.
- Current Live has separate year/month/day selectors.
- Every published Current Live record is general current affairs, shows publication and verification dates, checked evidence, and source links; recruitment/result updates are excluded.
- Dates without a checked record display `No verified news found`.
- Current Live MCQs contain bilingual stems, four bilingual options, answer keys, and short bilingual explanations.
- External links open in a new tab with `noopener noreferrer`.
- Practice has a visible forward control before and after answering.

## Durable resume state

- `QUESTION_BUILD_CHECKPOINT.json` — exact totals, hashes, and next 25 topic gaps
- `content/checkpoints/question-batches.json` — idempotent applied-question ledger
- `content/checkpoints/legacy-review-labels.json` — immutable baseline review labels
- `reports/question-coverage-report.json` — all 345 per-topic counts
- `reports/exam-mapping-report.json` — resolved hierarchy for all 21 exams
- `reports/current-news-report.json` — Current Live counts and dates
- `reports/checkpoint-receipt.json` — latest save receipt
- `IMPLEMENTATION_STATUS_2026-10-23.md` — human-readable implementation and remaining-work report

## Resume command

Only reviewed inputs with resolvable sources and evidence can be applied:

```bash
npm run apply-batch -- --input path/to/reviewed-batch.json --batch-size 25
```

The runner rejects missing evidence, non-bilingual records, duplicate IDs/fingerprints/stems, invalid options, and any change to preserved baseline review labels. It saves starter data, catalogue counts, the ledger, and reports after every small chunk.
