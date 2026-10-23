# Crorepati Revision

A local-first React/Vite learning app with bilingual practice, exam-scoped curriculum maps, dated Current Live records, and durable content checkpoints.

## Run locally

```bash
npm install
npm run dev
```

The dev server binds to `0.0.0.0`. Learning progress and the selected exam are stored in IndexedDB on the device.

## Current verified shape

- 26 subjects
- 82 chapters
- 345 canonical topics
- 1,725 preserved questions
- 21 exam views (7 legacy and 14 new)
- 13 directly checked general-current-affairs records, including 10 on 23 October 2026
- 26 story-linked bilingual Current Live MCQs

Exam views reuse canonical topic banks. Selecting an exam scopes every content tab without duplicating or changing the canonical hierarchy.

## Current Live

`/current-affairs` provides separate year, month, and day selectors. It is scoped to general current affairs (such as international relations, environment, and sports), not recruitment/result updates. Each included record contains:

- publication and verification dates;
- one or more checked HTTPS source links;
- a retained evidence excerpt and locator;
- a bilingual one-minute analysis with three checked key points and a recall focus;
- every independently verified story for the selected date, with no display-count cap;
- every story's complete question stems and four options shown directly in its brief;
- story-only or all-date one-question-at-a-time quizzes with Skip/Next, answer feedback, source access, and a result summary;
- a saved-brief review strip stored with local progress;
- offline reading through the precached Current Live feed;
- bilingual MCQs with four options, answer, and short explanation, each answered by that displayed story.

These are original interactions informed by useful short-article and daily-quiz patterns in the referenced current-affairs app; no third-party article, question, or visual was copied. A date without a checked record displays `No verified news found`; the app does not synthesize missing events.

## Verification

```bash
npm run pipeline          # rebuild mapping, news, coverage, and checkpoint reports
npm run validate          # structural/data checks; reports unresolved evidence gaps
npm test                  # deterministic Node tests
npm run build             # TypeScript, Vite production bundle, service worker
npm run check             # pipeline + structural validation + tests + build
npm run audit:coverage    # strict 40-per-topic gate (currently expected to fail)
npm run validate:strict   # strict coverage and static-source gate
npm run test:e2e          # Playwright browser scenarios; requires installed Chromium
npm run checkpoint        # refresh reports and save a receipt
```

The structural suite passes. The release gate remains intentionally blocked: 13,800 questions are required for 40 per topic, 1,725 are present, and the exact shortfall is **12,075**. See `IMPLEMENTATION_STATUS_2026-10-23.md` and `reports/question-coverage-report.json`.

## Reviewed question batches

New static questions are not accepted without resolvable sources and evidence. Apply a reviewed batch in small durable chunks:

```bash
npm run apply-batch -- --input path/to/reviewed-batch.json --batch-size 25
```

The runner validates bilingual completeness, exactly four options, answer integrity, explanations, source IDs, verified FactCards/evidence, canonical mapping, IDs, fingerprints, exact/near-duplicate stems, prohibited boilerplate, and baseline review-label preservation. Every chunk updates the question file, catalogue counts and starter-pack hash, ledger, reports, and resume checkpoint through a recoverable transaction.

Input schema and editorial procedure: `content/schemas/reviewed-question-batch.schema.json` and `docs/REVIEWED_BATCH_WORKFLOW.md`.

Resume state:

- `QUESTION_BUILD_CHECKPOINT.json`
- `content/checkpoints/question-batches.json`
- `content/checkpoints/legacy-review-labels.json`

## Honesty and preservation

All 1,725 baseline questions and their lifecycle/kind/quality review labels are preserved. The baseline also contains unresolved source-provenance debt and 28 concept references outside their canonical topic; these are reported separately rather than silently guessed or represented as newly verified content. Newly added content must pass stricter source and mapping gates.

This is an independent educational project. Official recruitment notices govern exact examination syllabi.
