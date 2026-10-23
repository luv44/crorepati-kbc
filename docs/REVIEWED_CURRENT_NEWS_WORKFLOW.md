# Reviewed Current Live batch workflow

Updated: **23 October 2026 (Asia/Calcutta)**

Current Live has a target of **150 directly reviewed records per content-building run**. The target is a review goal, never permission to copy, invent, repeat, or pad records. The current checked feed contains **13 records**, so the honestly reported gap to that target is **137**.

## 1. Verify candidates before writing

A reviewer must open every source page directly and confirm all of the following:

- the URL is an independent HTTPS page on a permitted Indian government host (`*.gov.in` or `*.nic.in`);
- the page visibly supports the event, publication date, retained evidence excerpt, and each answer;
- the item is general current affairs, not a recruitment, vacancy, admit-card, examination-result, or answer-key notice;
- the story is not already represented by an existing record or source URL;
- English and Hindi text has been reviewed rather than mechanically padded;
- each MCQ has one bilingual stem, exactly four distinct bilingual options, a valid answer index, and a short bilingual explanation.

If the source page cannot be opened and checked, exclude the candidate. Search snippets are not evidence.

## 2. Prepare a reviewed JSON bundle

Use `content/schemas/reviewed-current-news-batch.schema.json` as the input contract. A bundle contains:

- a unique batch `id`;
- `review.reviewedAt`, `review.reviewer`, and `review.directSourcePagesChecked: true`;
- 1–150 complete Current Live records in `items`.

Each record must include its publication and verification dates, bilingual category/title/summary, one-minute analysis, retained evidence and locator, at least one official source link, and at least one complete bilingual MCQ.

Do not put credentials or API keys in a batch file.

## 3. Apply in durable small saves

```bash
npm run apply-news-batch -- --input path/to/reviewed-current-news-batch.json
```

The default save size is 25 records. It can be reduced, but never raised above 25:

```bash
npm run apply-news-batch -- --input path/to/reviewed-current-news-batch.json --save-size 10
```

The runner validates the full reviewed input before writing anything. It rejects malformed dates, excluded notice titles, non-government links, duplicate record/source/MCQ IDs, repeated options, incomplete bilingual content, invalid answer indexes, and unchecked batches. Each accepted chunk atomically rewrites the feed and ledger, then refreshes generated reports. Re-running the same unchanged IDs is safe and reports that they are already present.

Resume state is recorded in:

- `public/data/current-news.json` — canonical accepted feed;
- `content/checkpoints/current-news-batches.json` — applied-record ledger;
- `reports/current-news-report.json` — exact feed counts, target, and remaining gap.

## 4. Verify after each reviewed bundle

```bash
npm run pipeline
npm run validate
npm test
npm run build
npm run checkpoint
```

Then open Current Live in a real browser and verify:

1. Year, Month, Day, and Topic selectors render.
2. **Any topic** shows every checked story for the selected date without a display cap.
3. A topic selection shows only matching stories and questions.
4. Every source opens independently in a new tab and displays the stated publication date/evidence.
5. Every story exposes all of its linked questions.
6. A date without a record displays exactly `No verified news found`.
7. The target meter reports the true accepted count and remaining gap.

Never claim the 150-record target is complete unless the accepted, directly reviewed records actually reach it.
