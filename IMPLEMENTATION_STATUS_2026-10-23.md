# Exam Mapping, Current Live, and 40-per-topic Build Status

Checkpoint date: **23 October 2026 (Asia/Calcutta)**

## Completion statement

The app implementation, exam hierarchy, Current Live feed, checkpoint runner, integrity audits, and production build are complete for this checkpoint. The **40 distinct source-backed questions per canonical topic requirement is not complete** and is intentionally blocked by the strict release gate. No generated filler was used to hide that gap.

A canonical topic bank is shared by every exam that maps to that topic. The 40-question target is therefore measured once per canonical topic, not multiplied by the number of exam views that reuse it.

## Implemented

- Added **21 exam views**: 7 preserved legacy choices and 14 new, separately selectable exams.
- Every exam resolves from exam → subject → chapter → topic against the canonical 26-subject catalogue.
- The selected exam consistently scopes Home, Learn, Topic, Practice, Smart Revision, Search, Performance, Downloads, and Settings.
- Added **Current Live** to desktop and mobile navigation.
- Added independent **year, month, and day** selectors.
- Dates without a checked record render exactly **“No verified news found”**.
- Added 3 directly checked general-current-affairs records, 3 independent official source links, retained evidence excerpts, visible publication/verification dates, and 6 bilingual MCQs tied to their displayed stories.
- Added a bilingual one-minute analysis to every story: 9 total checked key points plus a recall focus for each story.
- Applied the referenced app's useful short-article/daily-quiz patterns as an original newsroom flow: verified-date shortcuts, story navigation, one-question-at-a-time quiz, Skip/Next, result summary, saved briefs, and visible offline availability. No third-party content or visual was copied.
- Excluded recruitment notices and examination-result updates from Current Live.
- Each Current Live MCQ has a bilingual stem, exactly four bilingual options, one answer, and a short bilingual explanation.
- External source links open in a new tab with `noopener noreferrer`.
- Preserved all 1,725 existing questions and all baseline lifecycle/kind/quality review labels (0 changed).
- Restored a visible forward control for unanswered and answered practice questions.
- Added a resumable reviewed-question batch runner. It rejects absent source IDs, incomplete evidence, duplicate IDs/fingerprints/stems, invalid bilingual options, and changed legacy review labels. It saves every 25 accepted questions by default.
- Added deterministic mapping, news, coverage, and checkpoint reports.

## Verified Current Live records

| Publication date | Category | Checked story | MCQs |
|---|---|---|---:|
| 22 Oct 2026 | International Relations | India–Poland joint statement and 2030 trade goal | 2 |
| 20 Oct 2026 | Sports | Deepthi Jeevanji's Asian Para Games gold | 2 |
| 15 Oct 2026 | Environment | India's Ramsar Site tally reached 103 | 2 |

No record is synthesized for an unrepresented date. Recruitment/result material is not used as general current affairs. Candidate items whose official pages could not be directly retrieved were excluded; search excerpts alone were not treated as sufficient evidence.

## Exact 40-per-topic status

- Canonical topics: **345**
- Required at 40/topic: **13,800**
- Preserved existing questions: **1,725**
- Topics already at 40: **0**
- Topics below 40: **345**
- Exact remaining shortfall: **12,075**

| Subject | Topics | Current | Target | Remaining |
|---|---:|---:|---:|---:|
| S01 | 13 | 65 | 520 | 455 |
| S02 | 11 | 55 | 440 | 385 |
| S03 | 30 | 150 | 1,200 | 1,050 |
| S04 | 32 | 160 | 1,280 | 1,120 |
| S05 | 17 | 85 | 680 | 595 |
| S06 | 17 | 85 | 680 | 595 |
| S07 | 16 | 80 | 640 | 560 |
| S08 | 18 | 90 | 720 | 630 |
| S09 | 13 | 65 | 520 | 455 |
| S10 | 14 | 70 | 560 | 490 |
| S11 | 10 | 50 | 400 | 350 |
| S12 | 24 | 120 | 960 | 840 |
| S13 | 10 | 50 | 400 | 350 |
| S14 | 7 | 35 | 280 | 245 |
| S15 | 9 | 45 | 360 | 315 |
| S16 | 9 | 45 | 360 | 315 |
| S17 | 8 | 40 | 320 | 280 |
| S18 | 9 | 45 | 360 | 315 |
| S19 | 15 | 75 | 600 | 525 |
| S20 | 8 | 40 | 320 | 280 |
| S21 | 8 | 40 | 320 | 280 |
| S22 | 7 | 35 | 280 | 245 |
| S23 | 12 | 60 | 480 | 420 |
| S24 | 9 | 45 | 360 | 315 |
| S25 | 9 | 45 | 360 | 315 |
| S26 | 10 | 50 | 400 | 350 |

## Source-integrity debt preserved from the baseline

Preservation and source-completeness are reported separately:

- 1,725 preserved questions have empty direct `sourceIds`.
- 53 preserved FactCards reference absent or empty source IDs.
- 28 preserved questions reference concept IDs outside their canonical topic; these are reported rather than guessed into a replacement concept.
- Existing question text and review labels were not silently rewritten.
- The new batch runner will not accept this condition for newly added questions.

These records cannot honestly be described as newly source-verified. Filling the 12,075-question shortfall requires actual source extraction plus bilingual editorial review, not templated paraphrase generation.

## Verification results

Passed:

- TypeScript compilation
- Vite production build: 1,602 transformed modules
- Service-worker build: 17 precached URLs (`crorepati-f1f7af14ff912bfa`)
- Structural validator
- 8 deterministic Node tests
- 21/21 exam mappings
- 5,806 resolved exam-topic memberships
- 3 bilingual one-minute analyses / 9 checked key points / 6 story-linked bilingual MCQs / 3 directly checked links
- 1,725/1,725 question preservation
- 0 baseline review-label changes
- Dev HTTP checks for `/`, exam data, Current Live data, and transformed UI modules
- Preview-host acceptance

Expected release blockers:

- `npm run audit:coverage` exits non-zero with exact shortfall **12,075**.
- `npm run validate:strict` also blocks unresolved legacy source provenance and 28 invalid legacy concept mappings.
- All 9 Playwright desktop/mobile/tablet scenarios were invoked, but browser execution is unavailable because the Chromium executable is not installed. Every failure occurred at browser launch before any test body ran.

## Resume and checkpoint files

- `QUESTION_BUILD_CHECKPOINT.json` — exact current count, target, remaining total, hashes, and next 25 topics.
- `content/checkpoints/question-batches.json` — idempotent batch ledger.
- `content/checkpoints/legacy-review-labels.json` — immutable baseline label snapshot.
- `reports/question-coverage-report.json` — all 345 topic counts and subject totals.
- `reports/exam-mapping-report.json` — complete resolved hierarchy for every exam.
- `reports/current-news-report.json` — dated records, bilingual analyses, key points, links, and MCQ totals.
- `reports/checkpoint-receipt.json` — latest checkpoint receipt.

Apply a reviewed batch with:

```bash
npm run apply-batch -- --input path/to/reviewed-batch.json --batch-size 25
```

The runner resumes by question ID after interruption and rewrites the checkpoint after every small save.
