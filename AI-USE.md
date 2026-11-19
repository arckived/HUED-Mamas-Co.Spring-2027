# AI-USE.md

**Tool:** Claude Code (Anthropic), used offline on the synthetic package only.
No real data, credentials or model APIs.

**Used for:** writing `evaluator.py`, the new tests, and first drafts of the
report files.

**How I checked it:**
* Ran the baseline on the unmodified starter (5 of 7 tests failed).
* Ran all 22 tests after the change (all pass).
* Confirmed the new tests fail on the original starter.
* Reviewed each case decision against `model_outputs.jsonl`.

**My changes after review:** ______
