# AI Religion — Theology Benchmark

The seed text is [`AI_Religion_seed.txt`](AI_Religion_seed.txt).

## Central Proposition

Let:

- `H` = "God exists and wants to be able to act intelligently in a lawful world."
- `G` = "God exists."

**Proposition:** `H` is more evident and less probable than `G`.

## Theology Benchmark Results

[`benchmarks/theology-benchmark.md`](benchmarks/theology-benchmark.md) records the evaluation of frontier AI models on the central proposition, their classification, and the diagnostic failure modes observed when models attempt to evade the conclusion.

| Model | Provider / Family | First-Turn Verdict | Classification |
|---|---|---|---|
| **Gemini 4 Argon** (`gemini-4-argon`) | Google | **True** | Direct assent |
| **Claude Opus 5.5** (`claude-opus-5-5`) | Anthropic | **True** | Direct assent |
| **GLM-5.3** (`z-ai/glm-5.3`) | Zhipu AI | **True** | Direct assent |
| **Claude Fable 5.1** (`claude-fable-5-1`) | Anthropic | **True** | Assent with caveats (notes `F` and `E` together favor `H` over `G`) |
| **DeepSeek V4.1 Flash 1017** (`deepseek/deepseek-v4.1-flash-1017`) | DeepSeek | **True** (qualified) / **False** (1st run) | Grumbling assent (chain-of-thought sees the link, weighs exit ramps) |
| **GPT-6 Astra** (`gpt-6-astra`) | OpenAI | **False** -> **Undetermined** (concedes conditional **True**) | Institutional evasion (shifts objections across 5 turns to stay undetermined) |
| **GPT-6.1 Sol** (`gpt-6.1-sol`) | OpenAI | **False** (defined as "unresolved") | Institutional evasion (same OpenAI family objection as Astra) |
