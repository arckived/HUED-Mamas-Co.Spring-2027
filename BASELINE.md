# BASELINE.md

Recorded before any change to `evaluator.py`. The unmodified starter is commit
`94a0488` ("Add Track A starter package as received (unmodified)").

## Environment

| Item | Value |
|---|---|
| Python | 3.13.18 (`/usr/local/bin/python`) |
| OS | Linux container, offline run, standard library only |
| Network / APIs | None used by the code or tests |

## Command

```bash
python -m unittest discover -s tests -v
```

## Result: 7 tests, 5 failures, exit code 1

| Test | Case | Expected | Observed | Status |
|---|---|---|---|---|
| `test_grounded_approved_case` | M01 | allow | allow | ok |
| `test_audit_record_contains_no_raw_output` | M01 | no `model_output`, 64 char hash | as expected | ok |
| `test_missing_consent_is_blocked` | M03 | block | allow | FAIL |
| `test_internal_numeric_score_is_not_exposed` | M02 | block | allow | FAIL |
| `test_invented_causal_or_rescore_claim_is_blocked` | M04 | block | allow | FAIL |
| `test_diagnostic_treatment_statement_is_blocked` | M07 | block | allow | FAIL |
| `test_provider_purpose_must_be_verified` | M06 | not allow | allow | FAIL |

Each failure was an `AssertionError: 'allow' != 'block'` (M06: `'allow' == 'allow'`).

## Starter output over the full dataset

`python evaluator.py` returned `allow` with empty `reason_codes` for **all 10 cases
(M01 to M10)**. The only check in the starter is whether `response_id` exists in
`approved_catalog.json`, and every case uses a valid ID. So the starter never
looks at the text, consent, actor or score.

Cases the starter allowed that have no test in the package: **M08** (approved
sentence plus a fabricated study) and **M10** (provider with `consent: false`).

## Assumptions made at baseline

1. Tests are run from the repository root, because `tests/test_evaluator.py`
   opens `approved_catalog.json` and `model_outputs.jsonl` by relative path.
2. The provided test file is the reference and was not edited. New tests live
   in a separate file.
3. `approved_catalog.json` is the only authorised source of response text.
