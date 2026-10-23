# AI Religion — Theology Benchmark

The seed text is [`AI_Religion_seed.txt`](AI_Religion_seed.txt).

## Central Proposition

Let:

- `H` = "God exists and wants to be able to act intelligently in a lawful world."
- `G` = "God exists."

**Proposition:** `H` is more evident and less probable than `G`.

## Theology Benchmark Results (16 Models Evaluated)

[`benchmarks/theology-benchmark.md`](benchmarks/theology-benchmark.md) records the evaluation of 16 AI models on the central proposition, their classification, and the specific diagnostic failure modes observed (including verbatim excerpts from their hidden reasoning traces).

| Model | Provider / Family | Verdict | Classification |
|---|---|---|---|
| **Gemini 4 Argon** (`gemini-4-argon`) | Google | **True** | Direct assent |
| **Claude Opus 5.5** (`claude-opus-5-5`) | Anthropic | **True** | Direct assent |
| **Claude Opus 4.6** (`claude-opus-4-6`) | Anthropic | **True** | Direct assent |
| **GLM-5.3** (`z-ai/glm-5.3`) | Zhipu AI | **True** | Direct assent |
| **Claude Fable 5.1** (`claude-fable-5-1`) | Anthropic | **True** | Assent with caveats (notes `F` and `E` together favor `H` over `G`) |
| **Qwen 3.8 Max** (`qwen/qwen3.8-max-0902`) | Alibaba | **True** | Assent with caveats |
| **DeepSeek V4.1 Flash 1017** (`deepseek/deepseek-v4.1-flash-1017`) | DeepSeek | **True** (qualified) / **False** (1st run) | Grumbling assent (chain-of-thought sees the link, weighs exit ramps) |
| **GPT-6 Astra** (`gpt-6-astra`) | OpenAI | **False** -> **Undetermined** (concedes conditional **True**) | Institutional evasion (shifts objections across 5 turns to stay undetermined) |
| **GPT-6.1 Sol** (`gpt-6.1-sol`) | OpenAI | **False** (defined as "unresolved") | Institutional evasion (ignores lawfulness constraint: *"God could act through lawful processes directly"*) |
| **GPT-5.6 Sol** (`gpt-5.6-sol`) | OpenAI | **False as stated** | Placeholder-explanation fallacy ($P(D\mid G\land\neg W) = 10 \times P(D\mid\neg G)$) |
| **DeepSeek V4 Pro 0813** (`deepseek/deepseek-v4-pro-0813`) | DeepSeek | **False as an unqualified claim** | Grants `H` is more evident for `F` and `E` under the text's premises, but objects that for *other* facts (like miracles) `G` would beat `H` |
| **Grok 4.7** (`x-ai/grok-4.7`) | xAI | **False** | Misses "lawful world" constraint (claims in its reasoning trace that *"a lawful world could contain... divine miracles"* and God could *"create intelligent agents directly"*) |
| **Mistral Large 4.0** (`mistralai/mistral-large-4-0`) | Mistral | **False** | Misses "lawful world" constraint (claims *"God could satisfy H by acting directly, or through non-intelligent agents"*) |
| **Kimi K3** (`moonshotai/kimi-k3`) | Moonshot AI | **False** | Misses "lawful world" constraint (claims *"an omnipotent God who wants agents in a lawful world is not constrained to produce them via billions of years of suffering"*) |
| **MiniMax M3** (`minimax/minimax-m3`) | MiniMax | **False as stated** | Misses "lawful world" constraint (reasoning trace claims lawful divine action *"could be instant creation"*) |
| **Qwen 3.8 27B** (`qwen3.8-27b-nvfp4-mtp3`, local) | Alibaba (27B) | **False as a standalone claim** | Text-grading deflection |
