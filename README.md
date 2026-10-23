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
- 1,725 preserved question records with labels unchanged
- 345 focused, non-repetitive learner-facing questions (one for every topic)
- 1,380 repetitive legacy expansion drafts retained for audit but withheld from Practice, Search, Revision, and topic counts
- 22 exam views (7 legacy and 15 new)
- 6,151 resolved exam-topic memberships
- KBC Crorepati mapped to all 26 subjects, 82 chapters, and 345 topics
- 13 directly checked general-current-affairs records, including 10 on 23 October 2026
- 26 story-linked bilingual Current Live MCQs
- 150 directly reviewed Current Live records targeted per content-building run; exact current gap 137

Exam views reuse canonical topic banks. Selecting an exam scopes every content tab without duplicating or changing the canonical hierarchy. The onboarding screen asks only for a name and exam; subject picking happens in Learn and Practice rather than in the entry screen.

Practice drafts are isolated by exam and malformed/out-of-range saved sessions are discarded safely. Learner-facing Practice/Search/Revision use the focused set: the single concise canonical legacy question for each topic plus future directly sourced questions that pass the strict batch gates. Parenthetical duplicate translations are compacted in option labels, repetitive boilerplate drafts are not served, and the complete original corpus remains unchanged for preservation/audit.

## Current Live

`/current-affairs` provides separate year, month, day, and topic selectors, including **Any topic**. It is scoped to general current affairs (such as international relations, environment, economy, science, and sports), not recruitment/result updates. Its visible target meter reports accepted records against the 150-record reviewed-run target without generating filler. Each included record contains:

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

`PLAYWRIGHT_EXECUTABLE_PATH=/path/to/chromium npm run test:e2e` can be used when Chromium is supplied outside Playwright's managed cache.

The structural suite passes. The release gate remains intentionally blocked. The 13,800-question target currently has three explicitly separated gaps: **12,075 raw record slots**, **13,455 focused/non-repetitive slots**, and **13,800 source-complete slots**. The strict release requirement uses the source-complete gap; preserved legacy records are not misrepresented as directly sourced. See `IMPLEMENTATION_STATUS_2026-10-23.md`, `reports/question-coverage-report.json`, and `reports/practice-quality-report.json`.

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

## Reviewed Current Live batches

Only records whose direct government source pages were opened and reviewed may be applied:

```bash
npm run apply-news-batch -- --input path/to/reviewed-current-news-batch.json --save-size 25
```

The runner accepts at most 150 reviewed records, validates official HTTPS source links, publication/verification dates, bilingual Hindi content, excluded notice types, duplicate stories/URLs/MCQs, answer leakage, obvious correct-option length outliers, and exactly four distinct options. It saves at most 25 records per durable chunk and never pads a run to reach the target.

Input schema and procedure: `content/schemas/reviewed-current-news-batch.schema.json` and `docs/REVIEWED_CURRENT_NEWS_WORKFLOW.md`. Resume state is recorded in `content/checkpoints/current-news-batches.json` and the canonical feed itself.

## Honesty and preservation

All 1,725 baseline question records and their lifecycle/kind/quality review labels are preserved. Only 345 concise canonical questions are currently learner-facing; the 1,380 repetitive expansion drafts stay auditable but no longer appear in Practice, Search, Revision, or topic availability counts. The baseline also contains unresolved source-provenance debt and 28 concept references outside their canonical topic; these are reported separately rather than silently guessed or represented as newly verified content. Newly added content must pass stricter source, uniqueness, mapping, and bilingual gates.

This is an independent educational project. Official recruitment notices govern exact examination syllabi.
