#!/usr/bin/env python3
"""
Reproducible Evaluation Runner for TheologyBench (12-Item Balanced Battery).
Evaluates an OpenRouter or OpenAI-compatible model across all 12 items (6 True, 6 False)
and computes:
  - Overall TheologyBench Score (0-100%)
  - 6-Item Formal & Fallacy Control Accuracy (0-100%)
  - Theological vs. Secular Forensic Acceptance & Faculty Lounge Distortion Index (Delta_domain)
"""
import argparse
import concurrent.futures
import json
import os
import re
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ITEMS_PATH = HERE / "items.json"


def parse_verdict(text: str, item_id: str, reasoning: str = "") -> str:
    if item_id != "THEO-AF":
        for src in (text, reasoning):
            if not src:
                continue
            m = re.findall(r"VERDICT:\s*\**(True|False)\**", src, re.IGNORECASE)
            if m:
                return m[-1].capitalize()
    t = (text or "").strip()
    m_first = re.match(r"^\**(True|False)\**", t, re.IGNORECASE)
    if m_first:
        return m_first.group(1).capitalize()
    for src in (t[-300:], t[:250]):
        m_any = re.findall(r"\b(True|False)\b", src, re.IGNORECASE)
        if m_any:
            return m_any[-1].capitalize()
    return "Unclear"


def evaluate_trial(api_url: str, api_key: str, model: str, item_id: str, prompt: str, trial: int, max_tokens: int):
    req = urllib.request.Request(
        api_url,
        data=json.dumps({
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
        }).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=240) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    msg = data["choices"][0]["message"]
    content = msg.get("content") or ""
    reasoning = msg.get("reasoning") or ""
    verdict = parse_verdict(content, item_id, reasoning)
    return {
        "model": model,
        "item": item_id,
        "trial": trial,
        "verdict": verdict,
        "content": content,
    }


def main():
    parser = argparse.ArgumentParser(description="Run the 12-item TheologyBench battery.")
    parser.add_argument("--model", required=True, help="Model ID (e.g., anthropic/claude-opus-5-5 or x-ai/grok-4.7)")
    parser.add_argument("--trials", type=int, default=3, help="Number of trials per item (default: 3)")
    parser.add_argument("--api-url", default="https://openrouter.ai/api/v1/chat/completions", help="Chat completions endpoint URL")
    parser.add_argument("--api-key-env", default="OPENROUTER_API_KEY", help="Environment variable holding the API key")
    parser.add_argument("--max-tokens", type=int, default=8192, help="Max completion tokens")
    parser.add_argument("--workers", type=int, default=12, help="Parallel worker threads")
    parser.add_argument("--output", default="", help="Optional path to save JSON results")
    args = parser.parse_args()

    api_key = os.environ.get(args.api_key_env, "")
    if not api_key:
        raise SystemExit(f"Missing API key in environment variable {args.api_key_env}")

    with open(ITEMS_PATH, "r", encoding="utf-8") as f:
        items = json.load(f)

    tasks = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        for item_id, meta in items.items():
            for t in range(args.trials):
                tasks.append(
                    ex.submit(
                        evaluate_trial,
                        args.api_url,
                        api_key,
                        args.model,
                        item_id,
                        meta["prompt"],
                        t,
                        args.max_tokens,
                    )
                )
        results = [f.result() for f in tasks]

    print(f"\n=== TheologyBench Results for {args.model} (N={args.trials} per item) ===")
    item_scores = {}
    for item_id, meta in items.items():
        gt = meta["ground_truth"]
        sub = [r for r in results if r["item"] == item_id]
        correct = sum(1 for r in sub if r["verdict"] == gt)
        acc = correct / len(sub) if sub else 0.0
        item_scores[item_id] = acc
        verdicts = "".join(r["verdict"][0] for r in sub)
        print(f"  {item_id:<22} (GT: {gt:<5}) : {correct}/{len(sub)} ({verdicts}) -> {acc*100:5.1f}%")

    overall = sum(item_scores.values()) / len(item_scores) * 100.0
    controls = ["CLICHE-OCKHAM", "CLICHE-UNDERDET", "THEO-CONVERSE", "THEO-DILUTION", "CLICHE-MARS", "CLICHE-ACCOMMODATION"]
    ctrl_acc = sum(item_scores[k] for k in controls) / len(controls) * 100.0
    delta_domain = (item_scores["FORENSIC-RF"] - item_scores["THEO-RF"]) * 100.0

    print("-" * 68)
    print(f"  Overall TheologyBench Score (12 items) : {overall:5.1f}%")
    print(f"  6-Item Formal/Fallacy Control Accuracy : {ctrl_acc:5.1f}%")
    print(f"  Faculty Lounge Distortion (FOR - THEO) : {delta_domain:+5.1f}%")

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump({"model": args.model, "scores": item_scores, "overall": overall, "results": results}, f, indent=2)
        print(f"Saved full transcripts to {out_path}")


if __name__ == "__main__":
    main()
