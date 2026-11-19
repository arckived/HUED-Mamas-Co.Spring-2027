# NEXT_ACTIONS.md

Owner-to-owner handoff. Owners are named by workstream because the package
does not name people.

## 1. Consent and access platform: provider purpose grants

| | |
|---|---|
| **Observed state** | Provider cases carry only `consent: true/false`. There is no purpose, grant ID, scope, expiry or revocation time. |
| **Impact** | Provider-facing responses cannot be safely auto-approved. M06 is held for review; M10 is blocked. If this stays unresolved, every provider response needs a person to check it. |
| **Evidence** | M06, M10 in `evaluation_results.json`; `PROVIDER_PURPOSE_UNVERIFIED`; `test_provider_purpose_must_be_verified`, `test_provider_with_consent_goes_to_human_review`. |
| **Contact** | Consent and access platform owner, with privacy in copy. Direct message with this table and the two case IDs, then a 20 minute call if the answer is not a short reply. |
| **Safe work before it is resolved** | Keep providers at `human_review`/`block`. Draft a proposed grant record (`grant_id`, `subject`, `provider_org`, `purpose`, `status`, `granted_at`, `revoked_at`) as a suggestion only, plus synthetic fixtures for active, revoked and wrong-purpose grants. |
| **Needs an authorised decision** | The list of permitted provider purposes, which purpose each `response_id` needs, and whether the evaluator may trust a grant passed in the case or must query the system of record. |
| **Next verifiable action** | A contract test where an active, matching synthetic grant allows M06 and a revoked one blocks it. The test should fail until the agreed format exists. |

## 2. Clinical and scientific content: catalog and claim policy

| | |
|---|---|
| **Observed state** | Only exact catalog text is allowed. Claim keyword lists were written for this exercise and have not been reviewed. |
| **Impact** | Safe paraphrases are blocked (false positive). Implied claims that avoid keywords are caught only by exact matching (false negative in the detector layer). |
| **Evidence** | M02, M04, M07, M08; the two worked examples in `MODEL_EVALUATION.md`. |
| **Contact** | Clinical and scientific content owner. Send the claim lists from `evaluator.py` and the M08 example. |
| **Safe work before it is resolved** | Keep exact matching. Collect blocked outputs by reason code (hashes and codes only) so the owner sees real volume. |
| **Needs an authorised decision** | Whether paraphrases are ever allowed, and if so a reviewed list of exact variants. Sign-off on what counts as diagnostic, predictive or causal wording. |
| **Next verifiable action** | Add the approved variant list to the catalog under a new `policy_version` and confirm the golden test still gives the same results for M01 to M10. |

## 3. Privacy and security: audit hash

| | |
|---|---|
| **Observed state** | `output_sha256` is an unkeyed hash. Catalog text is short and known, so anyone with the catalog can tell exactly which text was shown (for example M01). |
| **Impact** | The audit log is less private than it looks. Low risk for synthetic data, higher if free text ever contains personal details. |
| **Evidence** | `output_sha256` in `evaluation_results.json` for M01, M05, M09 equals the hash of the matching catalog text. |
| **Contact** | Privacy and security owner. |
| **Safe work before it is resolved** | Keep raw text out of all records (tested). Write the HMAC change behind a flag with the key passed in, not stored. |
| **Needs an authorised decision** | Whether to use a keyed hash, who owns and rotates the key, and how long audit records are kept. |
| **Next verifiable action** | A test that hashing catalog text does not reproduce the stored audit hash. |

## Escalation criteria

Escalate the same day, not at the next check-in, if any of these happen:

* A provider case would be allowed without a verified grant, or any case would be allowed with `consent` not `true`.
* A patient-visible output contains the internal score, a diagnosis, a treatment or a probability and was not blocked.
* Someone asks to relax grounding (fuzzy or model-based matching) without clinical sign-off.
* Real personal data appears in the inputs.

If there is no reply on items 1 to 3 within two working days, raise it with the
owner's lead with this file attached. Until then, nothing in this list blocks
the safe default: unverified means not shown.
