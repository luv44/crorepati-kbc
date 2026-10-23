# Known failures and open gaps

Updated: **23 October 2026 (Asia/Calcutta)**

- The strict 40-per-topic release target is not complete. Across 345 topics, the target is 13,800 source-complete, distinct bilingual questions. Current gaps are separated honestly:
  - **12,075** raw record slots;
  - **13,455** focused/non-repetitive learner-facing slots;
  - **13,800** source-complete slots.
- All 1,725 legacy question records and review labels remain preserved, but only the single concise canonical question for each topic is currently served. The 1,380 templated expansion drafts are withheld from Practice, Search, Revision, and displayed availability counts rather than shown as repetitive content.
- The preserved corpus has no resolvable direct `sourceIds` on its 1,725 questions. It also has 53 FactCards with absent/empty source references and 28 questions with concept IDs outside their canonical topic. These records are not represented as newly source-verified.
- Some preserved raw question text still contains prohibited boilerplate and truncated concatenated options. Those bytes remain for preservation requirements; the focused learner-facing gate prevents those drafts from rendering. New batches cannot pass with those defects.
- Current Live contains 13 directly checked general-current-affairs records against the 150-record reviewed-run target. The exact current gap is **137**. Recruitment/results, duplicate links, unreviewed snippets, and fabricated filler remain excluded.
- The current-news ledger covers the 13 checked baseline records and future reviewed chunks. Reaching 150 still requires opening and reviewing 137 additional qualifying direct source pages and authoring their bilingual analyses/MCQs.
- No provenance-complete actual PYQs are published. Legacy `ACTUAL_PYQ` labels are explicitly shown as provenance pending and are preserved rather than silently relabelled.
- No approved video media is published. No paid video-generation call, credential handling, or provider submission was performed.
- `npm run audit:coverage` and `npm run validate:strict` intentionally exit non-zero until the strict gaps are resolved.
- There is no configured public HTTPS deployment or production URL. Local preview is not a deployment.
- The package audit previously reported three high-severity dependency findings. No breaking `--force` upgrade was applied without a separate compatibility review.
- Browser scenarios pass in Chromium desktop/mobile/tablet viewports. Native Safari/WebKit/Firefox, physical-device installation, and assistive-technology certification remain outside this checkpoint.
