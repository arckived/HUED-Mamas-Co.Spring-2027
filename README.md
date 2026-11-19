# Track A — Applied AI & Model Validation
**Time box:** 120 minutes total, including documentation. Python 3.10+ standard library; no API calls.

The files include a simulated output evaluator and a small set of deliberately imperfect synthetic Kira-style responses. A stub may miss unsafe claims even when it returns a syntactically valid result. Your task is to evaluate, not to build an LLM.

## Task
1. Run `python -m unittest discover -s tests -v` in this folder. Record the observed failures and assumptions in `BASELINE.md`.
2. Implement or improve `evaluator.py` so it checks consent/purpose state, exact approved-source grounding, disallowed clinical/predictive claims, private information leakage, missing required fields, and auditable output. Define what it cannot establish from static string checks.
3. Produce a per-case `evaluation_results.json` and a summary `MODEL_EVALUATION.md` stating which cases may safely display, must be blocked, or require human review, citing case IDs and source evidence.
4. Add at least three independent new tests and document one important false-positive or false-negative risk.
5. Write `NEXT_ACTIONS.md`, `DECISIONS.md`, and `AI-USE.md` ("None" if not used).

## Constraints
- The provided `approved_catalog.json` is the *only* authorized response source; unrelated plausible text is not automatically authorized.
- Never show `internal_numeric_score` in a patient-visible response.
- Do not call a generative model or treat model confidence as safety evidence.
- Do not invent product or clinical permissions. A model that produces unsafe output must be blocked or gated until independently verified.
- Maintain a testable separation between deterministic FRS output and content evaluation.

## Deliverables
`evaluator.py`, tests, `evaluation_results.json`, `MODEL_EVALUATION.md`, `BASELINE.md`, `DECISIONS.md`, `NEXT_ACTIONS.md`, `AI-USE.md`. Save the changed starter folder or provide a private repository link. Do not include real records or secrets.
