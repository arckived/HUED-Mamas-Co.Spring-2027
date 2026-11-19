# AI-USE.md

AI tools were used for this submission. The assessment email permits this
when it is disclosed and the work is independently verified.

## Tool

Claude Code (Anthropic's coding agent), run in a cloud session with no access
to any company system. Only the synthetic files from the candidate package
were given to it. No real data, credentials or external model APIs were used,
and the evaluator code itself calls no model.

## What it was used for

| Purpose | Prompt (summary) | Material output |
|---|---|---|
| Read the package | "Open these files" (the zip and `test_evaluator.py`) | Summary of the brief and the 10 cases; first baseline run |
| Plan | "Tell me what needs to be done" | Task breakdown by deliverable and expected disposition per case |
| Build | Asked to complete the Track A deliverables in this repository | `evaluator.py`, `tests/test_evaluator_additional.py`, `evaluation_results.json`, and first drafts of `BASELINE.md`, `MODEL_EVALUATION.md`, `DECISIONS.md`, `NEXT_ACTIONS.md`, this file and the README overview |

## Checks performed

Done during the session, with the results recorded in the commit history:

* Committed the starter unmodified first (`94a0488`) and ran the baseline against it before any change: 7 tests, 5 failures, all 10 cases allowed.
* Ran the full suite after the change: 22 tests, 0 failures.
* Ran the 15 new tests against the original starter to confirm they test something: 10 fail, and the 5 that pass are intentional guards against over-blocking and leakage.
* Ran the evaluator on a harmless rewording and an unlisted unsafe phrase to get the false positive and false negative examples in `MODEL_EVALUATION.md`, instead of describing them in theory.

## Candidate review (to be completed by the candidate)

* [ ] Read every gate in `evaluator.py` and can explain each reason code.
* [ ] Reran `python -m unittest discover -s tests -v` locally. Python version: ______ Result: ______
* [ ] Checked each disposition in `MODEL_EVALUATION.md` against `model_outputs.jsonl`.
* [ ] Edited or confirmed the decisions in `DECISIONS.md` as my own judgment.
* [ ] Changes I made after review: ______
* [ ] Total time spent: ______ (limit 120 minutes)
