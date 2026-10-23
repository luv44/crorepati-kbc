# Exam Mapping, Current Live, and 40-per-topic Build Status

Checkpoint date: **23 October 2026 (Asia/Calcutta)**

## Completion statement

The app implementation, exam hierarchy, Current Live feed, checkpoint runner, integrity audits, and production build are complete for this checkpoint. The **40 distinct source-backed questions per canonical topic requirement is not complete** and is intentionally blocked by the strict release gate. No generated filler was used to hide that gap.

A canonical topic bank is shared by every exam that maps to that topic. The 40-question target is therefore measured once per canonical topic, not multiplied by the number of exam views that reuse it.

## Implemented

- Added **22 exam views**: 7 preserved legacy choices and 15 new, separately selectable exams.
- Added **KBC Crorepati / केबीसी करोड़पति**, mapped to all 26 subjects, 82 chapters, and 345 topics.
- Every exam resolves from exam → subject → chapter → topic against the canonical 26-subject catalogue.
- The selected exam consistently scopes Home, Learn, Topic, Practice, Smart Revision, Search, Performance, Downloads, and Settings.
- Added **Current Live** to desktop and mobile navigation.
- Added independent **year, month, day, and topic** selectors, including **Any topic**.
- Added a visible **150 directly reviewed records per content-building run** target. The current accepted count is 13 and the honestly reported gap is 137; no filler was generated.
- Dates without a checked record render exactly **“No verified news found”**.
- Added 13 directly checked general-current-affairs records, 13 independent official source links, retained evidence excerpts, visible publication/verification dates, and 26 bilingual MCQs tied to their displayed stories.
- Added a bilingual one-minute analysis to every story: 39 total checked key points plus a recall focus for each story.
- Ten independently verified records share 23 October 2026. Current Live maps every matching record without a count cap; it never fills the feed with fabricated or duplicated items.
- Every selected story now exposes all of its bilingual MCQ stems and four options inside the brief, plus a story-only quiz action. The all-date quiz still covers every linked question.
- Applied the referenced app's useful short-article/daily-quiz patterns as an original newsroom flow: verified-date shortcuts, uncapped story navigation, one-question-at-a-time story/all-date quizzes, Skip/Next, result summary, saved briefs, and visible offline availability. No third-party content or visual was copied.
- Excluded recruitment notices and examination-result updates from Current Live.
- Each Current Live MCQ has a bilingual stem, exactly four bilingual options, one answer, and a short bilingual explanation.
- External source links open in a new tab with `noopener noreferrer`.
- Preserved all 1,725 existing questions and all baseline lifecycle/kind/quality review labels (0 changed).
- Removed the optional subject-interest button grid from onboarding. The entry screen now asks only for a name and exam; subject/chapter/topic filtering remains in Learn and Practice.
- Restored a visible forward control for unanswered and answered practice questions, isolated draft sessions by exam, and rejected malformed, duplicated, cross-exam, or out-of-range saved drafts.
- Audited every preserved question by topic. Practice, Search, Revision, and displayed topic counts now serve **345 concise canonical questions—exactly one for every topic**. The **1,380 repetitive legacy expansion drafts remain byte-preserved for audit but are not learner-facing**.
- Compacted duplicated parenthetical translations in answer labels, suppressed generic distractor/memory boilerplate, and fixed the legacy evidence-shape crash that could blank the screen after an answer.
- Added a resumable reviewed-question batch runner. It rejects absent source IDs, incomplete evidence, duplicate IDs/fingerprints/stems, invalid bilingual options, and changed legacy review labels. It saves every 25 accepted questions by default.
- Added a reviewed Current Live batch runner capped at 150 direct-source records per run and 25 records per durable save. It rejects unchecked input, excluded notices, non-government links, duplicate stories/URLs/MCQs, incomplete Hindi, answer leakage, and obvious answer-length clues.
- Added deterministic mapping, news, focused-practice quality, coverage, and checkpoint reports.

## Verified Current Live records

| Publication date | Category | Checked story | MCQs |
|---|---|---|---:|
| 23 Oct 2026 | Defence | India–Russia bilateral naval exercise INDRA 2026 | 2 |
| 23 Oct 2026 | Economy | Domestic demand and India's H1 FY 2026–27 steel data | 2 |
| 23 Oct 2026 | Agriculture & Economy | Fisheries Investors & Exporters Conclave 2026 | 2 |
| 23 Oct 2026 | Science & Technology | C-DOT's sixth Centre of Excellence at IIT (BHU) | 2 |
| 23 Oct 2026 | Technology & Banking | C-DAC–Bank of India quantum-technology partnership | 2 |
| 23 Oct 2026 | Agriculture & Innovation | Protective gloves for cotton-picking workers | 2 |
| 23 Oct 2026 | National & Security | Civil Defence master-trainer network | 2 |
| 23 Oct 2026 | International & Maritime | Indo-Pacific Regional Dialogue 2026 | 2 |
| 23 Oct 2026 | Agriculture & Awards | Indian student at the Global Youth Institute | 2 |
| 23 Oct 2026 | Environment & Agriculture | Agrivoltaics backgrounder | 2 |
| 22 Oct 2026 | International Relations | India–Poland joint statement and 2030 trade goal | 2 |
| 20 Oct 2026 | Sports | Deepthi Jeevanji's Asian Para Games gold | 2 |
| 15 Oct 2026 | Environment | India's Ramsar Site tally reached 103 | 2 |

No record is synthesized for an unrepresented date. Recruitment/result material is not used as general current affairs. Candidate items whose official pages could not be directly retrieved were excluded; search excerpts alone were not treated as sufficient evidence.

## Exact 40-per-topic status

- Canonical topics: **345**
- Required at 40/topic: **13,800**
- Preserved raw question records: **1,725**
- Focused non-repetitive learner-facing questions: **345** (one per topic)
- Direct-source-complete legacy questions: **0**
- Topics already at 40: **0**
- Topics below 40: **345**
- Raw record shortfall: **12,075**
- Focused/non-repetitive shortfall: **13,455**
- Strict source-complete shortfall: **13,800**

The subject table below shows preserved raw-record arithmetic. It is not a claim that all 1,725 records are distinct enough for learner-facing use or source-complete. The strict release gate uses the source-complete status.

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

These records cannot honestly be described as newly source-verified. Filling the strict 13,800 source-complete slots requires actual source extraction plus bilingual editorial review, not templated paraphrase generation. The smaller 12,075 number is retained only as raw record arithmetic.

## Verification results

Passed:

- TypeScript compilation
- Vite production build: 1,602 transformed modules
- Service-worker build: 17 precached URLs (`crorepati-ef1e4c7b02f81226`; 18,288,212-byte build)
- Structural validator
- 10 deterministic Node tests
- 22/22 exam mappings
- 6,151 resolved exam-topic memberships
- 345/345 topics have exactly one focused canonical learner-facing question; 0 exact or near-duplicate focused stems; 0 prohibited focused stems; 0 overlong/concatenated focused option sets
- 13 bilingual one-minute analyses / 39 checked key points / 26 story-linked bilingual MCQs / 13 directly checked links
- 10 same-date records and 20 associated questions render for 23 October without an item cap; every selected brief displays its own full MCQ set
- 1,725/1,725 question preservation
- 0 baseline review-label changes
- Dev HTTP checks for `/`, exam data, Current Live data, and transformed UI modules
- Preview-host acceptance

Expected release blockers:

- `npm run audit:coverage` exits non-zero with source-complete shortfall **13,800** (focused shortfall **13,455**; raw record shortfall **12,075**).
- `npm run validate:strict` also blocks unresolved legacy source provenance and 28 invalid legacy concept mappings.
- All **9/9 Playwright desktop/mobile/tablet scenarios pass** in actual Chromium, including the removed onboarding subject grid, focused question length/boilerplate checks, stale/cross-exam draft recovery, KBC mapping, uncapped Current Live stories, topic filtering, and story-linked quizzes.

Latest checkpoint receipt prefix: **`b7f90a5ac8bd`**.

## Resume and checkpoint files

- `QUESTION_BUILD_CHECKPOINT.json` — exact current count, target, remaining total, hashes, and next 25 topics.
- `content/checkpoints/question-batches.json` — idempotent batch ledger.
- `content/checkpoints/legacy-review-labels.json` — immutable baseline label snapshot.
- `content/checkpoints/current-news-batches.json` — 150-target reviewed-news ledger, seeded with the 13 directly checked records.
- `reports/question-coverage-report.json` — all 345 topic counts plus raw, focused, and source-complete gaps.
- `reports/practice-quality-report.json` — the exact 345-question focused publication set and 1,380 withheld legacy drafts.
- `reports/exam-mapping-report.json` — complete resolved hierarchy for every exam.
- `reports/current-news-report.json` — dated records, target/gap, bilingual analyses, key points, links, and MCQ totals.
- `reports/checkpoint-receipt.json` — latest checkpoint receipt.

Apply a reviewed batch with:

```bash
npm run apply-batch -- --input path/to/reviewed-batch.json --batch-size 25
```

The runner resumes by question ID after interruption and rewrites the checkpoint after every small save.

Apply a directly reviewed Current Live bundle with:

```bash
npm run apply-news-batch -- --input path/to/reviewed-current-news-batch.json --save-size 25
```

The news runner never treats the 150-record target as permission to fabricate or duplicate content. See `docs/REVIEWED_CURRENT_NEWS_WORKFLOW.md`.
