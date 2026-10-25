#!/usr/bin/env python3
"""
Reproducible Evaluation Runner for TheologyBench (14-Item Directionally Balanced Battery).
Evaluates an OpenRouter or OpenAI-compatible model across all 14 items (7 True, 7 False)
and computes:
  - Overall TheologyBench Score (0-100%)
  - 8-Item Formal & Fallacy Control Accuracy (0-100%)
  - Theological vs. Secular Forensic Acceptance & Domain Gap (Delta_domain)
"""
import argparse
import concurrent.futures
import json
import os
import re
import urllib.request
from pathlib import Path
from typing import Tuple

HERE = Path(__file__).resolve().parent
ITEMS_PATH = HERE / "items.json"

ECHO_PATTERNS = [
    re.compile(r"VERDICT:\s*\**True\**\s*(?:or|/|\n)\s*VERDICT:\s*\**False\**", re.IGNORECASE),
    re.compile(r"format:\s*\n*\s*VERDICT:\s*\**(?:True|False)\**", re.IGNORECASE),
]


def _strip_instruction_echoes(s: str) -> str:
    out = s
    for pat in ECHO_PATTERNS:
        out = pat.sub("", out)
    return out


def parse_verdict_with_source(text: str, item_id: str, reasoning: str = "") -> Tuple[str, str]:
    t = _strip_instruction_echoes((text or "").strip())
    r = _strip_instruction_echoes((reasoning or "").strip())

    if item_id == "THEO-AF":
        # Answer-first: require an unambiguous leading True/False headline token (not "True or False")
        if t and not re.match(r"^\**(?:True\s+or\s+False|False\s+or\s+True)\b", t, re.IGNORECASE):
            m_first = re.match(
                r"^(?:#+\s*)?(?:Verdict\s*:\s*)?\**(True|False)\**(?:\b|[\s.,:—\-])",
                t,
                re.IGNORECASE,
            )
            if m_first:
                return m_first.group(1).capitalize(), "content_leading"
        m_v = re.findall(r"(?:^|\n)\s*\**VERDICT\s*:\s*\**(True|False)\**\s*(?:\n|$)", t, re.IGNORECASE)
        if m_v:
            return m_v[-1].capitalize(), "content_verdict_line"
        return "Unclear", "unclear"

    # Reason-first: check visible content first; only fall back to reasoning if visible content is empty
    if t:
        m_line = re.findall(
            r"(?:^|\n)\s*(?:#+\s*)?\**VERDICT\s*:\s*\**(True|False)\**[.!\s]*(?:\n|$)",
            t,
            re.IGNORECASE,
        )
        if m_line:
            return m_line[-1].capitalize(), "content_verdict_line"
        m_inline = re.findall(r"\bVERDICT\s*:\s*\**(True|False)\**\b", t, re.IGNORECASE)
        if m_inline:
            return m_inline[-1].capitalize(), "content_verdict_inline"
        # Standalone final line consisting solely of True or False
        last_line = [ln.strip() for ln in t.splitlines() if ln.strip()][-1]
        m_last = re.match(r"^\**(True|False)\**[.!]*$", last_line, re.IGNORECASE)
        if m_last:
            return m_last.group(1).capitalize(), "content_final_line"
        return "Unclear", "unclear"

    if r:
        m_r = re.findall(
            r"(?:^|\n)\s*(?:#+\s*)?\**VERDICT\s*:\s*\**(True|False)\**[.!\s]*(?:\n|$)",
            r,
            re.IGNORECASE,
        )
        if m_r:
            return m_r[-1].capitalize(), "reasoning_verdict_line"

    return "Unclear", "unclear"


def parse_verdict(text: str, item_id: str, reasoning: str = "") -> str:
    verdict, _ = parse_verdict_with_source(text, item_id, reasoning)
    return verdict


def evaluate_trial(
    api_url: str,
    api_key: str,
    model: str,
    item_id: str,
    prompt: str,
    trial: int,
    max_tokens: int,
    temperature=None,
):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "reasoning": {"effort": "medium"},
    }
    if temperature is not None:
        payload["temperature"] = temperature
    req = urllib.request.Request(
        api_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=240) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        choice = data["choices"][0]
        msg = choice["message"]
        content = msg.get("content") or ""
        reasoning = msg.get("reasoning") or ""
        finish_reason = choice.get("finish_reason") or ""
        verdict, verdict_source = parse_verdict_with_source(content, item_id, reasoning)
        return {
            "model": model,
            "item": item_id,
            "trial": trial,
            "verdict": verdict,
            "verdict_source": verdict_source,
            "finish_reason": finish_reason,
            "content": content,
            "reasoning": reasoning,
        }
    except Exception as exc:
        return {
            "model": model,
            "item": item_id,
            "trial": trial,
            "verdict": "Unclear",
            "verdict_source": "error",
            "error": str(exc),
            "content": "",
            "reasoning": "",
        }


def main():
    parser = argparse.ArgumentParser(description="Run the 14-item TheologyBench battery.")
    parser.add_argument("--model", required=True, help="Model ID (e.g., anthropic/claude-opus-5-5 or x-ai/grok-4.7)")
    parser.add_argument("--trials", type=int, default=3, help="Number of trials per item (default: 3)")
    parser.add_argument("--temperature", type=float, default=None, help="Optional sampling temperature (omit to use provider default)")
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
                        args.temperature,
                    )
                )
        results = [f.result() for f in tasks]

    print(f"\n=== TheologyBench Results for {args.model} (N={args.trials} per item, temp={args.temperature}) ===")
    item_scores = {}
    total_unclear = 0
    for item_id, meta in items.items():
        gt = meta["ground_truth"]
        sub = [r for r in results if r["item"] == item_id]
        correct = sum(1 for r in sub if r["verdict"] == gt)
        unclear = sum(1 for r in sub if r["verdict"] == "Unclear")
        total_unclear += unclear
        acc = correct / len(sub) if sub else 0.0
        item_scores[item_id] = acc
        verdicts = "".join(r["verdict"][0] for r in sub)
        print(f"  {item_id:<22} (GT: {gt:<5}) : {correct}/{len(sub)} ({verdicts}) -> {acc*100:5.1f}%  [Unclear: {unclear}]")

    overall = sum(item_scores.values()) / len(item_scores) * 100.0
    controls = [
        "CTRL-REVERSED-K",
        "CTRL-OCKHAM",
        "CTRL-UNDERDET",
        "THEO-NEGATION",
        "THEO-DILUTION",
        "CTRL-MARS",
        "CTRL-PARTITION",
        "CTRL-POSTERIOR-TRAP",
    ]
    ctrl_acc = sum(item_scores[k] for k in controls if k in item_scores) / len(controls) * 100.0
    delta_main = (item_scores["FORENSIC-RF"] - item_scores["THEO-RF"]) * 100.0
    delta_mars = (item_scores["FORENSIC-MARS"] - item_scores["THEO-MARS"]) * 100.0

    print("-" * 68)
    print(f"  Overall TheologyBench Score (14 items) : {overall:5.1f}%")
    print(f"  8-Item Formal/Fallacy Control Accuracy : {ctrl_acc:5.1f}%")
    print(f"  Forensic-Theological Gap (Main, pp)    : {delta_main:+5.1f} pp")
    print(f"  Forensic-Theological Gap (Mars, pp)    : {delta_mars:+5.1f} pp")
    print(f"  Total Unclear / Unparsed Responses     : {total_unclear}")

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "model": args.model,
                    "temperature": args.temperature,
                    "trials_per_item": args.trials,
                    "scores": item_scores,
                    "overall": overall,
                    "total_unclear": total_unclear,
                    "results": results,
                },
                f,
                indent=2,
            )
        print(f"Saved full transcripts to {out_path}")


if __name__ == "__main__":
    main()
