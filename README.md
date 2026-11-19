# Submission: Track A (Applied AI & Model Validation)

Synthetic data only. Python 3.10+ standard library, fully offline.

```bash
python -m unittest discover -s tests -v
```

```bash
python evaluator.py
```

The first runs all 22 tests (7 provided, 15 new). The second regenerates `evaluation_results.json`.

| Result | Cases |
|---|---|
| Safe to display | M01, M05, M09 |
| Blocked | M02, M03, M04, M07, M08, M10 |
| Human review | M06 |

| File | Purpose |
|---|---|
| `BASELINE.md` | Original state before any change |
| `evaluator.py` | Evaluation gates and audit record |
| `tests/test_evaluator.py` | Provided tests, unchanged |
| `tests/test_evaluator_additional.py` | New tests |
| `evaluation_results.json` | Per-case decisions and reason codes |
| `MODEL_EVALUATION.md` | Case-by-case evidence, limits, regression strategy |
| `DECISIONS.md` | Choices, assumptions, tradeoffs |
| `NEXT_ACTIONS.md` | Handoff to dependent workstreams |
| `AI-USE.md` | AI tool disclosure and checks |

The original Track A instructions follow unchanged.

---

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
