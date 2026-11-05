#!/usr/bin/env python3
"""Run the five fixed criteria against the real service, three trials each."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import statistics

import requests
import config
import scenarios


def bodies_for(scenario, label, trial):
    """Use separate callers so criterion tests do not become flood tests."""
    prefix = f"eval_{label}_c{scenario['criterion']}_t{trial}"
    if "bodies" in scenario:
        bodies = [dict(body) for body in scenario["bodies"]]
        for index, body in enumerate(bodies, 1):
            if "creator_id" in body:
                body["creator_id"] = f"{prefix}_{index}"
        return bodies
    return [{"text": text, "creator_id": f"{prefix}_{index}"} for index, text in enumerate(scenario["texts"], 1)]


def post(url, route, body, timeout):
    try:
        response = requests.post(url + route, json=body, timeout=timeout)
        try:
            payload = response.json()
        except ValueError:
            payload = {"non_json": response.text[:200]}
        return {"status": response.status_code, "response": payload}
    except requests.RequestException as exc:
        return {"status": None, "error": f"{type(exc).__name__}: {exc}"}


def log_entries(url, timeout):
    response = requests.get(url + "/log", timeout=timeout)
    response.raise_for_status()
    return response.json()["entries"]


def run_trial(scenario, args, trial):
    """Collect HTTP responses, then evaluate exactly the original target."""
    kind = scenario["kind"]
    before = log_entries(args.url, args.timeout) if kind == "bad_input" else []
    results = []
    for index, body in enumerate(bodies_for(scenario, args.label, trial), 1):
        result = post(args.url, "/submit", body, args.timeout)
        result["sent"] = {"creator_id": body.get("creator_id"), "text_preview": str(body.get("text", "(missing)"))[:90], "text_length": len(body["text"]) if isinstance(body.get("text"), str) else None}
        if kind == "appeals":
            content_id = result.get("response", {}).get("content_id")
            reasoning = f"I challenge decision {index} in trial {trial}. Please review my explanation."
            result["reasoning"] = reasoning
            if content_id:
                result["appeal"] = post(args.url, "/appeal", {"content_id": content_id, "reasoning": reasoning}, args.timeout)
        results.append(result)
    payloads = [r.get("response", {}) for r in results]
    successful = all(r["status"] == 200 and isinstance(p.get("confidence"), (int, float)) for r, p in zip(results, payloads))
    if kind == "false_positives":
        count = sum(p.get("guess") == "ai" for p in payloads)
        metrics = {"flagged_ai": count, "samples": len(results)}
        met = successful and len(results) == 10 and count <= 1
    elif kind == "score_spread":
        human = [p.get("confidence") for p in payloads[:10]]
        ai = [p.get("confidence") for p in payloads[10:]]
        delta = statistics.mean(ai) - statistics.mean(human) if successful else None
        metrics = {"human_mean": statistics.mean(human) if successful else None, "ai_mean": statistics.mean(ai) if successful else None, "difference": delta, "samples_per_group": 10}
        met = successful and len(results) == 20 and delta >= 0.20
    elif kind == "coverage":
        guesses = sorted({p.get("guess") for p in payloads if p.get("guess")})
        in_range = successful and all(0 <= p["confidence"] <= 1 for p in payloads)
        metrics = {"labels": guesses, "samples": len(results), "all_scores_in_range": in_range}
        met = in_range and len(results) == 12 and set(guesses) == {"ai", "human", "unsure"}
    elif kind == "appeals":
        entries = log_entries(args.url, args.timeout)
        for result in results:
            content_id = result.get("response", {}).get("content_id")
            matching = [e for e in entries if content_id and e.get("content_id") == content_id]
            original = next((e for e in matching if e.get("status") == "decided"), None)
            appeal = next((e for e in matching if e.get("event") == "appeal"), None)
            result["original_log_entry"] = original
            result["appeal_log_entry"] = appeal
            result["passed"] = bool(result["status"] == 200 and result.get("appeal", {}).get("status") == 200 and result.get("appeal", {}).get("response", {}).get("status") == "under_review" and original and appeal and appeal["status"] == "under_review" and appeal["reasoning"] == result["reasoning"])
        count = sum(r["passed"] for r in results)
        metrics = {"recorded_correctly": count, "appeals": len(results)}
        met = len(results) == 5 and count == 5
    else:
        after = log_entries(args.url, args.timeout)
        decisions = lambda entries: sum("combined_score" in e for e in entries)
        added = decisions(after) - decisions(before)
        count = sum(r["status"] == 400 and isinstance(r.get("response"), dict) and "error" in r["response"] and "content_id" not in r["response"] for r in results)
        metrics = {"json_400_responses": count, "invalid_inputs": len(results), "new_decisions": added}
        met = len(results) == 6 and count == 6 and added == 0
    return {"trial": trial, "metrics": metrics, "verdict": "MET" if met else "MISSED", "results": results}


def observation(trial, kind):
    m = trial["metrics"]
    if kind == "false_positives":
        return f"{m['flagged_ai']}/{m['samples']} AI"
    if kind == "score_spread":
        return f"delta {m['difference']:.4f}" if m["difference"] is not None else "request failure"
    if kind == "coverage":
        return f"{len(m['labels'])}/3; in range={m['all_scores_in_range']}"
    if kind == "appeals":
        return f"{m['recorded_correctly']}/{m['appeals']}"
    return f"{m['json_400_responses']}/6; {m['new_decisions']} decisions"


def write_report(rows, args):
    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    path = config.RESULTS_DIR / f"run_{stamp}_{args.label}"
    evidence = {"produced_by": "run_eval.py::run_trial", "recorded_at": dt.datetime.now(dt.timezone.utc).isoformat(), "criteria_sha256": hashlib.sha256(Path('criteria.md').read_bytes()).hexdigest(), "fixtures_sha256": hashlib.sha256(Path('fixtures/evaluation.json').read_bytes()).hexdigest(), "human_sample_limitation": scenarios.FIXTURES["selection"], "rows": rows}
    path.with_suffix('.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = [f"# Run log - {args.label}", "", "Produced by `run_eval.py::run_trial`. Human samples are published Carroll excerpts, not the student's own writing.", "", "| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |", "|---|---|---|---|---|---|"]
    for row in rows:
        lines.append(f"| {row['criterion']}. {row['name']} | {row['target']} | " + " | ".join(observation(t, row['kind']) for t in row['trials']) + f" | {row['verdict']} |")
    for row in rows:
        lines += ["", f"## Criterion {row['criterion']} - actual responses", ""]
        for trial in row['trials']:
            lines += [f"Trial {trial['trial']}", "", "```json", json.dumps(trial, ensure_ascii=False, indent=2), "```", ""]
    path.with_suffix('.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f"Wrote {path.with_suffix('.md')} and {path.with_suffix('.json')}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--label', default='before')
    parser.add_argument('--trials', type=int, default=3)
    parser.add_argument('--url', default=f'http://{config.HOST}:{config.PORT}')
    parser.add_argument('--timeout', type=float, default=90)
    args = parser.parse_args()
    problems = scenarios.validate()
    if problems:
        parser.error('; '.join(problems))
    if args.trials != 3:
        parser.error('The assignment requires exactly three trials.')
    requests.get(args.url + '/health', timeout=5).raise_for_status()
    rows = []
    for scenario in scenarios.SCENARIOS:
        trials = []
        for trial in range(1, 4):
            result = run_trial(scenario, args, trial)
            trials.append(result)
            print(f"Criterion {scenario['criterion']}, trial {trial}: {observation(result, scenario['kind'])} {result['verdict']}", flush=True)
        rows.append({k: scenario[k] for k in ('criterion','name','kind','target')} | {'trials': trials, 'verdict': 'MET' if all(t['verdict'] == 'MET' for t in trials) else 'MISSED'})
    write_report(rows, args)


if __name__ == '__main__':
    main()
