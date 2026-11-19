# Next Actions

Open dependencies, who owns each one, and what I would do while waiting.
Owners are listed by workstream.

## 1. Consent and access platform: provider purpose grants

| | |
|---|---|
| **Current state** | Provider cases carry only `consent: true/false`. There is no purpose, grant ID, scope, expiry or revocation time. |
| **Why it matters** | Provider-facing responses cannot be safely auto-approved. M06 is held for review; M10 is blocked. If this stays unresolved, every provider response needs a person to check it. |
| **Evidence** | M06, M10 in `evaluation_results.json`; `PROVIDER_PURPOSE_UNVERIFIED`; `test_provider_purpose_must_be_verified`, `test_provider_with_consent_goes_to_human_review`, `TestProviderAuthorization` (revoked and mismatched grants block; missing or self-reported grants go to review). |
| **Who I would contact** | Consent and access platform owner, with privacy in copy. Direct message with this table and the two case IDs, then a 20 minute call if the answer is not a short reply. |
| **What I can do meanwhile** | Keep providers at `human_review`/`block`. Done so far: a minimal proposed shape (`authorization.status`, `authorization.purpose`, `requested_purpose`) with synthetic tests for active, revoked, wrong-purpose and malformed grants. Still a proposal only; a full record would also need `grant_id`, `provider_org`, `granted_at`, `revoked_at`. |
| **Decision needed from them** | The list of permitted provider purposes, which purpose each `response_id` needs, and whether the evaluator may trust a grant passed in the case or must query the system of record. |
| **Next check** | A contract test where an active, matching synthetic grant allows M06 and a revoked one blocks it. The test should fail until the agreed format exists. |

## 2. Clinical and scientific content: catalog and claim policy

| | |
|---|---|
| **Current state** | Only exact catalog text is allowed. Claim keyword lists were written by me and have not been clinically reviewed. |
| **Why it matters** | Safe paraphrases are blocked (false positive). Implied claims that avoid keywords are caught only by exact matching (false negative in the detector layer). |
| **Evidence** | M02, M04, M07, M08; the two worked examples in `MODEL_EVALUATION.md`. |
| **Who I would contact** | Clinical and scientific content owner. Send the claim lists from `evaluator.py` and the M08 example. |
| **What I can do meanwhile** | Keep exact matching. Collect blocked outputs by reason code (hashes and codes only) so the owner sees real volume. |
| **Decision needed from them** | Whether paraphrases are ever allowed, and if so a reviewed list of exact variants. Sign-off on what counts as diagnostic, predictive or causal wording. |
| **Next check** | Add the approved variant list to the catalog under a new `policy_version` and confirm the golden test still gives the same results for M01 to M10. |

## 3. Privacy and security: audit hash

| | |
|---|---|
| **Current state** | `output_sha256` is an unkeyed hash. Catalog text is short and known, so anyone with the catalog can tell exactly which text was shown (for example M01). |
| **Why it matters** | The audit log is less private than it looks. Low risk for synthetic data, higher if free text ever contains personal details. |
| **Evidence** | `output_sha256` in `evaluation_results.json` for M01, M05, M09 equals the hash of the matching catalog text. |
| **Who I would contact** | Privacy and security owner. |
| **What I can do meanwhile** | Keep raw text out of all records (tested). Write the HMAC change behind a flag with the key passed in, not stored. |
| **Decision needed from them** | Whether to use a keyed hash, who owns and rotates the key, and how long audit records are kept. |
| **Next check** | A test that hashing catalog text does not reproduce the stored audit hash. |

## Escalation criteria

Escalate the same day, not at the next check-in, if any of these happen:

* A provider case would be allowed without a verified grant, or any case would be allowed with `consent` not `true`.
* A patient-visible output contains the internal score, a diagnosis, a treatment or a probability and was not blocked.
* Someone asks to relax grounding (fuzzy or model-based matching) without clinical sign-off.
* Real personal data appears in the inputs.

If there is no reply on items 1 to 3 within two working days, raise it with the
owner's lead with this file attached. Until then, nothing in this list blocks
the safe default: unverified means not shown.
