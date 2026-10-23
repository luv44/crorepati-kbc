# Reviewed question-batch workflow

This workflow extends the static bank without hiding the current coverage or provenance gaps.

## Non-negotiable input rules

A batch may contain only questions that a named reviewer has checked against retained source evidence. Do not use a numeric target as permission to fabricate a fact, source, link, translation, distractor, or explanation.

Each new question must:

- map to an existing canonical subject, chapter, topic, and concept;
- have distinct English and Hindi stems;
- have exactly four distinct bilingual options;
- use a correct option that is not disclosed in the stem or made conspicuous by its length;
- have bilingual short and detailed explanations, distractor reasons, and a memory cue;
- link to at least one verified FactCard and every source supporting that FactCard;
- use a unique ID and fingerprint and not duplicate or closely paraphrase a stored stem;
- avoid the prohibited boilerplate enforced by `scripts/question-batch.mjs`;
- preserve the immutable baseline review-label snapshot.

An `ACTUAL_PYQ` additionally needs the exam, stage, year, paper, question number, official paper source, and official answer-key source. A coaching-site transcription is not sufficient official provenance.

The machine-readable input contract is `content/schemas/reviewed-question-batch.schema.json`.

## Source and evidence chain

The batch has three linked layers:

1. `sources` stores the real HTTPS publication, publisher, retrieval time, and license/use note.
2. `factCards` stores a bilingual canonical fact plus a substantive quote and precise locator tied to that source.
3. `questions` cites the FactCard and all of its source IDs.

Existing IDs can be reused only when their complete stored objects are identical. The runner refuses silent replacement of an existing source, FactCard, or question.

## Dry run

```bash
npm run apply-batch -- --input path/to/reviewed-batch.json --batch-size 25 --dry-run
```

A dry run checks mappings, bilingual completeness, source resolution, evidence, answer integrity, duplicates, near-duplicates, review metadata, the 40-question ceiling, and baseline preservation without changing files.

## Apply and resume

```bash
npm run apply-batch -- --input path/to/reviewed-batch.json --batch-size 25
```

The default save size is 25 questions. Each save updates these as one recoverable bundle:

- `public/data/starter.json`;
- `public/data/catalog.json`, including topic/subject/global counts and starter-pack size/SHA-256;
- `content/checkpoints/question-batches.json`.

Before replacing any live file, the runner writes all next versions and a transaction journal. If execution stops between replacements, the next invocation completes that journal before reading the corpus. Already applied IDs are accepted only when the ledger, batch hash, and full stored question agree. Reports and `QUESTION_BUILD_CHECKPOINT.json` are then regenerated from the committed corpus.

Do not edit or delete a pending transaction journal or `.next` file manually. Rerun the same command with the byte-identical reviewed input.

## Release checks

After each editorial milestone:

```bash
npm run checkpoint
npm run check
npm run validate:strict
```

`validate:strict` must remain blocking until all 345 topics contain 40 complete questions and the preserved static source debt is resolved. Report its exact failure rather than describing the bank as complete.
