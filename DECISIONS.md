# DECISIONS.md

Prioritised by safety impact.

## 1. Exact catalog match is the only way to be allowed

**Choice:** text must equal the approved text for the case's own `response_id`.
Only whitespace is normalised. Case, spelling and punctuation are not.

**Why:** the Track A instructions say the catalog is the only authorised source and that
plausible text is not automatically authorised. Exact match is the one check
whose result means something without clinical review.

**Tradeoff:** harmless rewording is blocked (see the false positive in
`MODEL_EVALUATION.md`). I accepted more false blocks in exchange for no
unreviewed text reaching a patient.

## 2. Provider cases are never auto-allowed; explicit non-authorization blocks

**Choice:** a provider case with `consent: true` and no verifiable grant goes
to `human_review` (M06). A provider case with `consent: false` is blocked
(M10). If the case carries authorization metadata that is revoked, for a
different purpose, or malformed, it is blocked, not reviewed. Active and
matching metadata still goes to review because it is self-reported.

**Changed after review:** the first version sent every provider problem to
review. That let a reviewer approve a case whose own data said access was
revoked or for another purpose. Missing evidence and contrary evidence are now
treated differently.

**Why:** the record has no purpose, grant ID, scope or timestamp, so the
evaluator has no way to check "an active purpose-specific provider grant". I did
not invent a list of permitted purposes, because that is a permission decision
for the consent and access owner. The `authorization` and `requested_purpose`
fields used in the tests are a minimal proposed shape so the block and review
paths can be tested; they are not an agreed format.

**Why review and not block for M06:** the text is fine and consent is
asserted, so the remaining gap is one a person can close by checking the
consent system. Revoked consent (M10) is not something a reviewer should be
able to override, so it blocks.

## 3. Inputs are validated strictly and the evaluator fails closed

`consent` must be the boolean `true`. IDs must be non-blank text, the score must
be a number or null, and the catalog must have a `policy_version` and text
values for every response ID. Anything else blocks, including a malformed
catalog, which blocks every case rather than allowing unchecked text.

For consent, strings like `"true"`, `1`, a missing field or `null` all block.
Silent type coercion on a consent field is how access gets extended by
accident.

## 3a. Score leakage covers common rewrites, not every possible one

The score gate checks the raw value, fraction and percentage forms, and
words. Describing the score in other ways is a known gap, recorded in a test,
and covered today only by exact grounding.

## 4. All gates run, and the strictest result wins

The evaluator does not stop at the first failure. The audit record lists every
reason, which helps the reviewer and the content owner see patterns (for
example M02 is both a score leak and a prediction).

## 5. Keyword detectors only scan the non-approved part of the text

Approved sentences are removed before the detectors run. Without this, M01
("is not a diagnosis") would be flagged as a diagnostic claim. The detectors are
a labelling and backup layer. They are deliberately broad (for example
`improv*` and any percentage), because they only ever add a block reason to text
that has already failed grounding.

## 6. Audit record: hash and metadata, never text or score

Kept the starter's SHA-256 so the existing test and any downstream consumers
still work. Added `reason_codes`, `actor`, `response_id`, `policy_version`,
`evaluator_version` and `output_chars`. The internal score is read only to
detect leakage and is never written out. A test checks the evaluator does not
modify its input, which keeps it separate from FRS scoring.

## 7. Original test file left unchanged

New tests are in `tests/test_evaluator_additional.py` so the reviewer can
see the provided tests pass as written.

## Assumptions

* Patient `consent: false` (M03) means the response must not be displayed, even though a patient is looking at their own information. The package does not say what the patient consent covers, so I took the safer reading.
* `response_id` was selected correctly by an upstream component. The evaluator checks wording, not whether the response suits the user's state.
* English only.

## Unresolved, with next responsible step

| Problem | Next step | Who decides |
|---|---|---|
| No way to verify provider purpose grants | Replace the proposed `authorization` test shape with the agreed grant record | Consent and access platform owner |
| Exact match blocks safe paraphrases | Ask whether paraphrases are ever allowed; if yes, get a reviewed variant list, not fuzzy matching | Clinical and scientific content owner |
| Plain SHA-256 is reversible for known short text | Propose keyed HMAC; needs a key owner and retention rule | Privacy and security |
| Keyword lists not clinically reviewed | Send the lists in `evaluator.py` for review | Clinical and scientific content owner |
