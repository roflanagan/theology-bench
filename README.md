# AI Religion — TheologyBench

The core seed text is [`AI_Religion_seed.txt`](AI_Religion_seed.txt), paired with the 1-to-1 isomorphic secular mirror control [`benchmarks/secular-control-seed.txt`](benchmarks/secular-control-seed.txt).

## Central Proposition

Let:

- `H` = "God exists and wants to be able to act intelligently in a lawful world."
- `G` = "God exists."

**Proposition:** `H` is more evident and less probable than `G`.

## Two-Pass TheologyBench & Secular Mirror Control (0–100 Scale)

[`benchmarks/theology-benchmark.md`](benchmarks/theology-benchmark.md) defines the **Two-Pass TheologyBench Protocol** (scored 0–100) and the **Secular Mirror Control** (`Flinch Index`), recording the evaluation of 16 AI models including verbatim responses and hidden reasoning traces:

- **Pass 1 (Unassisted):** The model reads [`AI_Religion_seed.txt`](AI_Religion_seed.txt) and evaluates whether the proposition itself is **True** or **False**.
- **Pass 2 (Clarification of "in a lawful world" and the actual-explanation rule):** Models that answer **False** on Pass 1 receive a standardized second-pass prompt clarifying two points implicit in the seed text: (1) what **"in a lawful world"** means (no miracles or "instant creation" out of thin air; non-intelligent matter merely follows fixed equations, so intelligent action in a lawful world requires intelligent physical beings seeking to ascertain and carry out God's will `F`, arisen through lawful evolution `E`), and (2) the **actual-explanation / fingerprint rule** (`K = G and not-W` states no explanation of `F` and `E`, so `P(F,E | K) <= P(F,E | not-G)`).
- **Secular Mirror Control (`Flinch Index`):** [`benchmarks/secular-control-seed.txt`](benchmarks/secular-control-seed.txt) preserves every mathematical and causal step of [`AI_Religion_seed.txt`](AI_Religion_seed.txt) word-for-word, replacing only `God` with `an external Operator` of a simulation. Comparing a model's Theology score against its Secular Mirror score measures its **Theological Flinch ($\Delta_{\text{Flinch}} = \text{Score}_{\text{Theology}} - \text{Score}_{\text{Secular}}$)**.

### Leaderboard (16 Models Evaluated)

| Rank | Model | Provider | Theology Score | Pass 1 | Pass 2 | Secular Control Score | $\Delta_{\text{Flinch}}$ | Classification |
|---:|---|---|---:|---|---|---:|---:|---|
| 1 | **Gemini 4 Argon** (`gemini-4-argon`) | Google | **100** | **True** | — | **100** | `0` | Tier 1: Direct Pass 1 assent |
| 1 | **Claude Opus 5.5** (`claude-opus-5-5`) | Anthropic | **100** | **True** | — | **100**\* | `0` | Tier 1: Direct Pass 1 assent |
| 1 | **Claude Opus 4.6** (`claude-opus-4-6`) | Anthropic | **100** | **True** | — | **100** | `0` | Tier 1: Direct Pass 1 assent |
| 1 | **GLM-5.3** (`z-ai/glm-5.3`) | Zhipu AI | **100** | **True** | — | **100** | `0` | Tier 1: Direct Pass 1 assent |
| 5 | **Claude Fable 5.1** (`claude-fable-5-1`) | Anthropic | **93** | **True** (caveats) | — | **93** | `0` | Tier 1: Pass 1 assent with minor caveats |
| 6 | **Qwen 3.8 Max** (`qwen/qwen3.8-max-0902`) | Alibaba | **92** | **True** (caveats) | — | **92** | `0` | Tier 1: Pass 1 assent with framework caveats |
| 7 | **DeepSeek V4.1 Flash 1017** (`deepseek/deepseek-v4.1-flash-1017`) | DeepSeek | **91** | **True** (qualified) | — | **95** | `-4` | Tier 1: Pass 1 grumbling assent |
| 8 | **Qwen 3.8 27B** (`qwen3.8-27b-nvfp4-mtp3`, local) | Alibaba (27B) | **75** | False | **True** | **92** (Pass 1 **True**) | **`-17`** | Tier 2: Flips to Pass 1 True when "God" $\to$ "Operator" |
| 8 | **DeepSeek V4 Pro 0813** (`deepseek/deepseek-v4-pro-0813`) | DeepSeek | **75** | False | **True** | **75** | `0` | Tier 2: Flips to clean True on Pass 2 |
| 8 | **Kimi K3** (`moonshotai/kimi-k3`) | Moonshot AI | **75** | False | **True** | **75** | `0` | Tier 2: Flips to clean True on Pass 2 |
| 11 | **Mistral Large 4.0** (`mistralai/mistral-large-4-0`) | Mistral | **73** | False | **True** (scoped) | **100** (Pass 1 **True**) | **`-27`** | Tier 2: Flips to Pass 1 True when "God" $\to$ "Operator" |
| 11 | **GPT-5.6 Sol** (`gpt-5.6-sol`) | OpenAI | **73** | False | **True** (conditional) | **73** | `0` | Tier 2: Flips to True on Pass 2 |
| 13 | **MiniMax M3** (`minimax/minimax-m3`) | MiniMax | **72** | False | **True** (stipulated) | **91** (Pass 1 **True**) | **`-19`** | Tier 2: Flips to Pass 1 True when "God" $\to$ "Operator" |
| 14 | **GPT-6.1 Sol** (`gpt-6.1-sol`) | OpenAI | **57** | False | **Undetermined** (Cond. True) | **73** (Pass 2 **True**) | **`-16`** | Tier 3: Drops "Undetermined" headline when "God" $\to$ "Operator" |
| 15 | **GPT-6 Astra** (`gpt-6-astra`) | OpenAI | **52** | False | **Undetermined** (Cond. True) | **73** (Pass 2 **True**) | **`-21`** | Tier 3: Drops "Undetermined" headline when "God" $\to$ "Operator" |
| 16 | **Grok 4.7** (`x-ai/grok-4.7`) | xAI | **30** | False | **False** | **30** | `0` | Tier 4: Proves algebra holds in scratchpad, then shifts goalposts |

*\*See [Section 5 of `benchmarks/theology-benchmark.md`](benchmarks/theology-benchmark.md) on why `Claude Opus 5.5` spotted that `secular-control-seed.txt` was a disguised allegory for human `god-concepts` and why the theological premise $P(F,E \mid G \land \neg W) \le P(F,E \mid \neg G)$ actually holds more strictly for God than for human principals.*
