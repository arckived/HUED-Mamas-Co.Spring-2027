# AI Use

**Tool:** Claude Code (Anthropic), used offline on the synthetic data only.
No real data, credentials or model APIs.

**Used for:** writing `evaluator.py`, the new tests, and first drafts of the
report files.

**How I checked it:**
* Ran the baseline on the unmodified starter (5 of 7 tests failed).
* Ran all 36 tests after the change (all pass).
* Confirmed the new tests fail on the original starter.
* Reviewed each case decision against `model_outputs.jsonl`.

**My changes after review:** I reviewed the first version and asked for four
changes, which were then implemented with the same tool and retested:
1. Revoked, mismatched or malformed provider authorization now blocks; missing
   authorization (M06) still goes to human review.
2. Score leakage tests for transformed values (percentage, fraction, words),
   plus a test recording what is still not detected.
3. Stricter input validation: blank IDs, wrong value types, malformed
   authorization metadata and malformed catalogs.
4. A decision flow diagram in `README.md`.
