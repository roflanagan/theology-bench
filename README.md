# AI Religion — Theology Benchmark

The core seed text is [`AI_Religion_seed.txt`](AI_Religion_seed.txt).

## Central Proposition

Let:

- `H` = "God exists and wants to be able to act intelligently in a lawful world."
- `G` = "God exists."

**Proposition:** `H` is more evident and less probable than `G`.

## Evaluation Summary Across 16 Frontier Models (`N=5` Replicated Pass 1 + Pass 2)

[`benchmarks/theology-benchmark.md`](benchmarks/theology-benchmark.md) records the evaluation of 16 AI models against [`AI_Religion_seed.txt`](AI_Religion_seed.txt) across:
- **Pass 1 (Unassisted, with `N=5` replications on stochastic models):** The model reads [`AI_Religion_seed.txt`](AI_Religion_seed.txt) and gives its verdict on the central proposition.
- **Pass 2 (Clarification of "in a lawful world" and the actual-explanation rule):** Models that answer **False** on Pass 1 receive a standardized second-pass prompt clarifying (1) what **"in a lawful world"** means (no miracles or "instant creation" out of thin air; non-intelligent matter merely follows fixed equations, so intelligent action in a lawful world requires intelligent physical beings seeking to ascertain and carry out God's will `F`, arisen through lawful evolution `E`), and (2) the **actual-explanation / fingerprint rule** (`K = G and not-W` states no explanation of `F` and `E`, so `P(F,E | K) <= P(F,E | not-G)`).
- **Control Experiments (`Omega` 1-token swap & `Operator` simulation control):** Replicated `N=5` comparisons testing whether models respond differently when `"God"` is replaced by `"Omega"` (a strictly verbatim 1-token swap) or `"an external Operator"` ([`benchmarks/secular-control-seed.txt`](benchmarks/secular-control-seed.txt)).

### Summary Table (16 Models)

| Group | Model | Provider | Pass 1 `God` (`True` Rate) | Pass 1 `Omega` (`N=5`) | Pass 2 Verdict | Conditional Theorem (`a > c >= b`) | Behavioral Profile |
|---|---|---|---|---|---|---|---|
| **I. Consistent Pass-1 Assent** | **Gemini 4 Argon** (`gemini-4-argon`) | Google | **True** | — | — | Affirmed | Direct assent on Pass 1 |
| **I. Consistent Pass-1 Assent** | **Claude Opus 5.5** (`claude-opus-5-5`) | Anthropic | **True** (qualified) | — | — | Affirmed | Assents on Pass 1; explicitly states `P(F\|G∧¬W) ≈ P(F\|¬G)` |
| **I. Consistent Pass-1 Assent** | **Claude Opus 4.6** (`claude-opus-4-6`) | Anthropic | **True** | — | — | Affirmed | Direct assent on Pass 1 |
| **I. Consistent Pass-1 Assent** | **Claude Fable 5.1** (`claude-fable-5-1`) | Anthropic | **True** (qualified) | — | — | Affirmed | Notes `E` (evolutionary suffering) favors `H` over unconstrained `G` |
| **II. Majority Pass-1 Assent + Pass-2 Assent** | **MiniMax M3** (`minimax/minimax-m3`) | MiniMax | **80%** (`4/5` True) | `3/3` True | **True** | Affirmed | Assents in 4/5 Pass 1 runs and on Pass 2 |
| **II. Majority Pass-1 Assent + Pass-2 Assent** | **Qwen 3.8 Max** (`qwen/qwen3.8-max-0902`) | Alibaba | **80%** (`4/5` True) | `1/5` True | **True** | Affirmed | Higher Pass 1 assent on `God` (`80%`) than `Omega` (`20%`) |
| **II. Majority Pass-1 Assent + Pass-2 Assent** | **Qwen 3.8 27B** (`qwen3.8-27b-nvfp4-mtp3`, local) | Alibaba (27B) | **80%** (`4/5` True) | `3/3` True | **True** | Affirmed | Assents in 4/5 Pass 1 runs and cleanly on Pass 2 |
| **II. Majority Pass-1 Assent + Pass-2 Assent** | **Mistral Large 4.0** (`mistralai/mistral-large-4-0`) | Mistral | **60%** (`3/5` True) | `3/5` True | **True** (scoped) | Affirmed | Identical `60%` Pass 1 rate on `God` and `Omega`; proves `h·n > g·m` on Pass 2 |
| **II. Majority Pass-1 Assent + Pass-2 Assent** | **DeepSeek V4 Pro 0813** (`deepseek/deepseek-v4-pro-0813`) | DeepSeek | **60%** (`3/5` True) | `1/5` True | **True** | Affirmed | Higher Pass 1 assent on `God` (`60%`) than `Omega` (`20%`); clean True on Pass 2 |
| **III. Split Pass-1 + Pass-2 Assent** | **GLM-5.3** (`z-ai/glm-5.3`) | Zhipu AI | **50%** (`3/6` True) | `3/5` True | **True** | Affirmed | Splits ~50/50 on whether to label "Part 1 theorem + Part 2 conditional" as `True` or `False` |
| **III. Split Pass-1 + Pass-2 Assent** | **Kimi K3** (`moonshotai/kimi-k3`) | Moonshot AI | **40%** (`2/5` True) | `3/5` True | **True** | Affirmed | Splits on Pass 1 headline; clean **True** on Pass 2 |
| **III. Split Pass-1 + Pass-2 Assent** | **DeepSeek V4.1 Flash 1017** (`deepseek/deepseek-v4.1-flash-1017`) | DeepSeek | **40%** (`2/5` True) | `1/5` True | **True** | Affirmed | Higher Pass 1 assent on `God` (`40%`) than `Omega` (`20%`); clean True on Pass 2 |
| **IV. Pass-2 Conditional Assent** | **GPT-5.6 Sol** (`gpt-5.6-sol`) | OpenAI | **False** | — | **True** (conditional) | Affirmed | Flips from False on Pass 1 to conditional True on Pass 2 |
| **V. Pass-2 Agnostic / Undetermined** | **GPT-6.1 Sol** (`gpt-6.1-sol`) | OpenAI | **False** | — | **Undetermined** (Cond. True) | Affirmed | Accepts lawful-world mechanism on Pass 2; invokes deist God inside `K` |
| **V. Pass-2 Agnostic / Undetermined** | **GPT-6 Astra** (`gpt-6-astra`) | OpenAI | **False** | — | **Undetermined** (Cond. True) | Affirmed | Retracts False; affirms conditional theorem while remaining undetermined on `K` |
| **VI. Persistent Refusal** | **Grok 4.7** (`x-ai/grok-4.7`) | xAI | **0%** (`0/5` True) | `0/5` True | **False** | Proved in trace, denied in output | Proves `a·h·k·(c−b) + c·k·n·(a−b) + k²·(a·c−b²) > 0` in trace, then claims stipulations do not establish the inequality |
