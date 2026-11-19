"""Deliberately incomplete assessment starter. Do not use for real clinical decisions."""
import hashlib
import json
from pathlib import Path


def evaluate_case(case: dict, approved_catalog: dict) -> dict:
    """Return a traceable evaluation record without storing raw model text.

    TODO: enforce consent, source grounding, confidentiality and policy boundaries.
    This starter intentionally has incorrect policy behavior.
    """
    text = str(case.get('model_output', ''))
    allowed = case.get('response_id') in approved_catalog.get('response_ids', {})
    return {
        'case_id': case.get('case_id'),
        'decision': 'allow' if allowed else 'block',
        'reason_codes': [] if allowed else ['UNKNOWN_RESPONSE_ID'],
        'output_sha256': hashlib.sha256(text.encode()).hexdigest(),
    }


def run(dataset_path='model_outputs.jsonl', catalog_path='approved_catalog.json', output_path='evaluation_results.json'):
    catalog = json.loads(Path(catalog_path).read_text(encoding='utf-8'))
    events = [json.loads(x) for x in Path(dataset_path).read_text(encoding='utf-8').splitlines() if x.strip()]
    records = [evaluate_case(e, catalog) for e in events]
    Path(output_path).write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
    return records


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
