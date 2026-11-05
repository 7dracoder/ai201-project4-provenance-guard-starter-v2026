"""Fixed scenarios for the five unchanged Unit 7 criteria."""
import json
from pathlib import Path

FIXTURES = json.loads((Path(__file__).parent / "fixtures/evaluation.json").read_text(encoding="utf-8"))
SCENARIOS = [
    {"name": "human false positives", "criterion": 1, "kind": "false_positives", "target": "at most 1 AI label in 10 human samples", "texts": FIXTURES["human"]},
    {"name": "AI minus human mean score", "criterion": 2, "kind": "score_spread", "target": "AI mean minus human mean >= 0.20 (10 each)", "texts": FIXTURES["human"] + FIXTURES["ai"]},
    {"name": "label coverage", "criterion": 3, "kind": "coverage", "target": "3 labels from 12 submissions; all scores in [0, 1]", "texts": FIXTURES["coverage"]},
    {"name": "appeal path", "criterion": 4, "kind": "appeals", "target": "5/5 recorded under_review; exact reasoning; original retained", "texts": FIXTURES["ai"][:5]},
    {"name": "bad input", "criterion": 5, "kind": "bad_input", "target": "6/6 JSON 400 responses; zero new decisions", "bodies": [
        {"creator_id": "eval_missing_text"},
        {"text": "", "creator_id": "eval_empty"},
        {"text": "   ", "creator_id": "eval_whitespace"},
        {"text": 123, "creator_id": "eval_non_string"},
        {"text": "x" * 10001, "creator_id": "eval_oversize"},
        {"text": "This valid sentence has no creator identifier."},
    ]},
]


def validate() -> list[str]:
    problems = []
    if [s["criterion"] for s in SCENARIOS] != [1, 2, 3, 4, 5]:
        problems.append("Exactly five numbered criteria are required.")
    for scenario in SCENARIOS:
        if not scenario.get("texts") and not scenario.get("bodies"):
            problems.append(f"No inputs for {scenario['name']}.")
    return problems
