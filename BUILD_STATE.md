# Crorepati Revision — current build state

Updated: **2026-10-23 (Asia/Calcutta)**

## Active checkpoint

- Checkpoint receipt: `b7f90a5ac8bd`
- Canonical catalogue: 26 subjects / 82 chapters / 345 topics
- Preserved corpus: 1,725 question records; 1,725/1,725 baseline labels present; 0 lifecycle/kind/quality changes
- Focused learner-facing set: 345 unique canonical questions (one per topic)
- Withheld audit-only set: 1,380 repetitive legacy expansion drafts
- Exam views: 22 total (7 legacy + 15 new)
- Exam hierarchy validation: 22/22 valid; 6,151 resolved exam-topic memberships
- KBC Crorepati: 26 subjects / 82 chapters / 345 topics
- Current Live: 13 directly checked records / 13 bilingual one-minute analyses / 39 checked key points / 13 independent official links / 26 story-linked bilingual MCQs; 10 records share 23 October 2026
- Current Live reviewed-run target: 150; accepted 13; exact gap 137
- 40/topic target: 13,800
  - raw preserved-record shortfall: **12,075**
  - focused/non-repetitive shortfall: **13,455**
  - strict source-complete shortfall: **13,800**
- Inherited integrity debt: 1,725 questions without direct source IDs; 53 FactCards with absent/empty source references; 28 questions with concept IDs outside their topic
- Production build: **PASS** — TypeScript + Vite, 1,602 modules; service worker `crorepati-ef1e4c7b02f81226`; 17 precached URLs; 18,288,212-byte build
- Deterministic Node tests: **PASS (10/10)**
- Structural validation: **PASS**
- Focused-quality validation: **PASS** — all 345 topics covered, 0 exact or near-duplicate focused stems, 0 prohibited focused stems, 0 concatenated/overlong focused option sets
- Browser E2E against the production build: **PASS (9/9)** across desktop, mobile, and tablet Chromium
- Strict coverage/source release validation: **EXPECTED BLOCK** by the exact gaps above
- Live clean-origin production preview: Vite preview on `0.0.0.0:4173`

## Implemented UI/data behavior

- Onboarding contains only name and exam fields; the subject-interest grid shown in the reported screenshot has been removed.
- The global exam selector scopes Home, Learn, Topic, Practice, Search, Smart Revision, Performance, Downloads, and Settings.
- Exam mappings resolve canonical subject → chapter → topic nodes; no copied hierarchy can silently diverge.
- Practice/Search/Revision and topic availability counts use the 345-question focused set. Raw expansion drafts remain preserved but are not learner-facing.
- Option labels remove duplicated parenthetical translations at render time, while original stored content remains unchanged.
- Generic distractor reasons, duplicate detailed explanations, and boilerplate memory cues are suppressed.
- Practice drafts are exam-scoped and validate exam ID, unique question IDs, content membership, index, answers, mode, and completion status before restore.
- Current Live has separate year/month/day/topic selectors, including Any topic, and a visible 13/150 target meter.
- Every accepted Current Live record is general current affairs with visible publication/verification dates, checked evidence, official links, three or more bilingual key points, and linked bilingual MCQs; recruitment/result updates are excluded.
- Current Live renders every verified story for the selected date without a display cap and exposes every story's complete question set.
- Dates without a checked record display exactly `No verified news found`.
- External links open independently with `noopener noreferrer`.
- Home includes a prominent `Read verified Current Live` route.

## Durable resume state

- `QUESTION_BUILD_CHECKPOINT.json` — raw/focused/source-complete gaps, hashes, and next topic work
- `content/checkpoints/question-batches.json` — idempotent applied-question ledger
- `content/checkpoints/current-news-batches.json` — target-150 reviewed-news ledger
- `content/checkpoints/legacy-review-labels.json` — immutable baseline review labels
- `reports/question-coverage-report.json` — all 345 per-topic raw/focused/source-complete counts
- `reports/practice-quality-report.json` — focused publication set and withheld draft count
- `reports/exam-mapping-report.json` — resolved hierarchy for all 22 exams
- `reports/current-news-report.json` — Current Live counts, target, dates, and linked content
- `reports/checkpoint-receipt.json` — latest checkpoint receipt

## Resume commands

```bash
npm run apply-batch -- --input path/to/reviewed-batch.json --batch-size 25
npm run apply-news-batch -- --input path/to/reviewed-current-news-batch.json --save-size 25
```

Both runners reject incomplete/duplicate input and save in small resumable chunks. The 150-news target and 40-per-topic target never authorize fabricated filler.
