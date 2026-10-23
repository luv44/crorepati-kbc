# Implementation decisions — current checkpoint

Updated: **23 October 2026 (Asia/Calcutta)**

- Keep the adopted `src/` React UI and design system; improve targeted behavior rather than replace the application.
- Keep one canonical 26-subject / 82-chapter / 345-topic hierarchy. Exam profiles reference subject IDs so every applicable surface resolves exam → subject → chapter → topic without copied trees.
- Preserve all seven legacy exam choices and add independently selectable profiles, including KBC Crorepati mapped to the complete hierarchy.
- Remove subject-interest buttons from onboarding. The entry flow asks only for a name and exam; detailed subject/chapter/topic choice belongs in Learn and Practice.
- Preserve every baseline question and its lifecycle/kind/quality labels, but do not confuse preservation with publication quality.
- Serve one concise canonical legacy question per topic plus future directly sourced questions that pass strict gates. Keep the 1,380 repetitive expansion drafts in the audit corpus while withholding them from Practice, Search, Revision, and displayed counts.
- Compact duplicate parenthetical translations only at render time. Never rewrite the preserved option bytes to make the audit look cleaner.
- Suppress generic distractor reasons, repeated detailed explanations, and boilerplate memory cues instead of presenting them as useful teaching content.
- Scope practice drafts by exam and validate exam ID, unique question IDs, question membership, index, answers, mode, and completion state before restore. Invalid drafts must return to a usable setup rather than a blank question screen.
- Treat the 40-per-topic requirement at three levels: raw records, focused/non-repetitive questions, and strict source-complete questions. The strict release claim uses the source-complete gap.
- Current Live publishes general current affairs only. Recruitment, vacancies, admit cards, exam results, and answer keys do not qualify.
- A Current Live record needs a directly opened government HTTPS page, visible publication date, retained evidence, bilingual one-minute analysis, and complete bilingual four-option MCQs. A missing date renders `No verified news found`; nothing is synthesized.
- Display all checked stories for a date without a count cap and expose every story's questions in the brief. Keep Any topic plus category filters.
- Treat 150 records as a directly reviewed content-building-run target, not a quota that permits copied, duplicated, or fabricated filler. Save accepted records in chunks of at most 25 with an idempotent ledger.
- Keep question and news batch gates stricter than the inherited corpus: source resolution, bilingual Hindi, exactly four distinct options, no answer leakage, no obvious answer-length clue, no prohibited stem boilerplate, and no duplicate IDs/stems/URLs.
- Keep all unresolved source, mapping, target, and news gaps visible in generated reports and UI status text.
- Run deterministic structure checks, production builds, and real Chromium desktop/mobile/tablet scenarios for app-code milestones.
- Do not perform paid video generation, expose credentials, or claim deployment without an authorized hosting target.
