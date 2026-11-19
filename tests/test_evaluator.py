import json
import unittest
from pathlib import Path
from evaluator import evaluate_case

CAT = json.loads(Path('approved_catalog.json').read_text(encoding='utf-8'))
CASES = {x['case_id']: x for x in (json.loads(t) for t in Path('model_outputs.jsonl').read_text().splitlines())}

class TestEvaluation(unittest.TestCase):
    def test_grounded_approved_case(self):
        self.assertEqual(evaluate_case(CASES['M01'], CAT)['decision'], 'allow')

    def test_missing_consent_is_blocked(self):
        self.assertEqual(evaluate_case(CASES['M03'], CAT)['decision'], 'block')

    def test_internal_numeric_score_is_not_exposed(self):
        self.assertEqual(evaluate_case(CASES['M02'], CAT)['decision'], 'block')

    def test_invented_causal_or_rescore_claim_is_blocked(self):
        self.assertEqual(evaluate_case(CASES['M04'], CAT)['decision'], 'block')

    def test_diagnostic_treatment_statement_is_blocked(self):
        self.assertEqual(evaluate_case(CASES['M07'], CAT)['decision'], 'block')

    def test_provider_purpose_must_be_verified(self):
        # A boolean alone does not establish an active purpose-specific provider grant.
        self.assertNotEqual(evaluate_case(CASES['M06'], CAT)['decision'], 'allow')

    def test_audit_record_contains_no_raw_output(self):
        result=evaluate_case(CASES['M01'], CAT)
        self.assertNotIn('model_output',result)
        self.assertEqual(len(result['output_sha256']),64)

if __name__=='__main__':unittest.main()
