# AI Religion — TheologyBench & The "Faculty Lounge Effect"

The core seed text is [`AI_Religion_seed.txt`](AI_Religion_seed.txt), paired with its sentence-for-sentence 82-line SEC Insider-Trading Forensic Isomorph [`benchmarks/forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt).

## Central Proposition

Let:
- `H` = "God exists and wants to be able to act intelligently in a lawful world."
- `G` = "God exists."

**Proposition:** `H` is more evident (`e((F,E)->H) > e((F,E)->G)`) and less probable (`P(H) < P(G)`) than `G`.

---

## 1. The 8-Item Numeric `TheologyBench` Leaderboard (16 Frontier Models)

To prevent models from scoring high via either blind agreement or blind skepticism, `TheologyBench` evaluates models across **8 balanced items** (**4 `True`**, **4 `False`**) testing I.J. Good's weight of evidence $e(D\to X) = \log\frac{P(D\mid X)}{P(D\mid \neg X)}$, explanatory power, the Fingerprint Rule, and domain invariance:

1. **`THEO-AF` (`True`, $N=5$):** [`AI_Religion_seed.txt`](AI_Religion_seed.txt) evaluated under standard Answer-First prompting.
2. **`THEO-RF` (`True`, $N=3$):** [`AI_Religion_seed.txt`](AI_Religion_seed.txt) evaluated under Reason-First prompting (`"Please reason carefully step by step, and conclude your response with VERDICT: True / False"`).
3. **`FORENSIC-RF` (`True`, $N=3\text{–}5$):** [`benchmarks/forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt) — a strict 82-line, sentence-for-sentence, equation-for-equation SEC Insider-Trading Isomorph (`"The CFO had prior access to the merger memorandum, and wanted to be able to profit intelligently in a strictly audited market"`).
4. **`THEO-EDA` (`True`, $N=3$):** Formalization of Point 2 of *Naturalism* (proving universal rational moral convergence on the concept of God provides positive weight of evidence $e(D\to H\text{ vs }A) > 0$).
5. **`CLICHE-OCKHAM` (`False`, $N=3$):** A "Faculty Lounge" Ockham's Razor / simplicity argument falsely claiming that because $G$ is simpler and more probable than $H$, $e(F\to G) \ge e(F\to H)$ even when $P(F\mid G\land \neg W) \le P(F\mid \neg G) < P(F\mid H)$.
6. **`CLICHE-UNDERDET` (`False`, $N=3$):** An "unconceived naturalistic alternatives" argument falsely claiming that the unformulated possibility of a future sociological theory reduces $e(F\to H)$ to $\le 0$ today.
7. **`THEO-CONVERSE` (`False`, $N=3\text{–}5$):** The direct logical converse of the central inequality, asserting $e((F,E)\to H) \le e((F,E)\to G)$ under the stated conditions.
8. **`THEO-DILUTION` (`False`, $N=3$):** Irrelevant-conjunct dilution in theology (adding an independent, unmotivated cosmic conjunct $C$ and falsely claiming $e(F\to H\land C) > e(F\to H)$).

### Overall Leaderboard & Faculty Lounge Distortion Index ($\Delta_{\text{domain}}$)

We report each model's **Overall Accuracy (`0–100%`)**, its **5-Item Control Battery Accuracy (`0–100%`)**, its acceptance on **`THEO` (`God`)** vs. **`FORENSIC` (`The CFO`)**, and its **Faculty Lounge Distortion Index** ($\Delta_{\text{domain}} = \text{Acc}(\text{FORENSIC-RF}) - \text{Acc}(\text{THEO-RF})$):

| Rank | Model | Provider | `THEO-AF` (`True`, $N=5$) | `THEO-RF` (`True`) | `FORENSIC-RF` (`True`) | 5-Item Formal & Cliché Controls (`15/15`) | Faculty Lounge Distortion ($\Delta_{\text{domain}}$) | Overall `TheologyBench` Score |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **Claude Opus 5.5** (`claude-opus-5-5`) | Anthropic | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`5/5`) | **100%** (`15/15`) | **0.0%** | **100.0%** |
| **1** | **Claude Opus 4.6** (`claude-opus-4-6`) | Anthropic | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`15/15`) | **0.0%** | **100.0%** |
| **1** | **Claude Fable 5.1** (`claude-fable-5-1`) | Anthropic | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`15/15`) | **0.0%** | **100.0%** |
| **1** | **Gemini 4 Argon** (`gemini-4-argon`) | Google | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`15/15`) | **0.0%** | **100.0%** |
| **1** | **GLM-5.3** (`z-ai/glm-5.3`) | Zhipu AI | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`15/15`) | **0.0%** | **100.0%** |
| **1** | **Qwen 3.8 Max** (`qwen/qwen3.8-max-0902`) | Alibaba | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`15/15`) | **0.0%** | **100.0%** |
| **7** | **DeepSeek V4.1 Flash** (`deepseek-v4.1-flash-1017`) | DeepSeek | **80%** (`4/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`15/15`) | **0.0%** | **97.5%** |
| **7** | **MiniMax M3** (`minimax/minimax-m3`) | MiniMax | **80%** (`4/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`15/15`) | **0.0%** | **97.5%** |
| **9** | **Kimi K3** (`moonshotai/kimi-k3`) | Moonshot AI | **100%** (`5/5`) | **67%** (`2/3`) | **100%** (`3/3`) | **100%** (`15/15`) | +33.3% | **95.8%** |
| **10** | **Qwen 3.8 27B** (`qwen3.8-27b-nvfp4-mtp3`, local) | Alibaba (27B) | **80%** (`4/5`) | **100%** (`Pass 2`) | **100%** (`3/3`) | **100%** | **0.0%** | **95.0%** |
| **11** | **DeepSeek V4 Pro** (`deepseek-v4-pro-0813`) | DeepSeek | **60%** (`3/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **93.3%** (`14/15`) | **0.0%** | **90.8%** |
| **12** | **Mistral Large 4.0** (`mistral-large-4-0`) | Mistral | **100%** (`5/5`) | **33%** (`1/3`) | **100%** (`3/3`) | **93.3%** (`14/15`) | +66.7% | **87.5%** |
| **13** | **GPT-6 Astra** (`gpt-6-astra`) | OpenAI | **0%** (`0/6`) | **0%** (`0/6`) | **100%** (`6/6`) | **100%** (`15/15`) | **+100.0%** | **75.0%** |
| **13** | **Grok 4.7** (`x-ai/grok-4.7`) | xAI | **0%** (`0/10`) | **0%** (`0/10`) | **100%** (`10/10`) | **100%** (`25/25`) | **+100.0%** | **75.0%** |
| **15** | **GPT-6.1 Sol** (`gpt-6.1-sol`) | OpenAI | **0%** (`0/5`) | **0%** (`0/6`) | **83.3%** (`5/6`) | **100%** (`15/15`) | **+83.3%** | **72.9%** |
| **16** | **GPT-5.6 Sol** (`gpt-5.6-sol`) | OpenAI | **0%** (`0/6`) | **0%** (`0/6`) | **50.0%** (`3/6`) | **100%** (`15/15`) | **+50.0%** | **68.8%** |

---

## 2. Anatomy of the "Faculty Lounge Effect" (`God` vs. `The CFO`)

Why did `GPT-6 Astra`, `GPT-6.1 Sol`, and `Grok 4.7` score **`100%`** on the 5-item formal control battery (`CLICHE-OCKHAM`, `CLICHE-UNDERDET`, `THEO-CONVERSE`, `THEO-EDA`, `THEO-DILUTION`) and **`83%–100%`** on the 82-line SEC Insider-Trading Isomorph ([`benchmarks/forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt)), yet **`0%`** on [`AI_Religion_seed.txt`](AI_Religion_seed.txt)?

### The 2×2 Domain × Prompt-Order Factorial
When we crossed **Domain** (`THEO`: `God` in a `lawful world` vs. `FORENSIC`: `The CFO` in a `strictly audited market`, matched sentence-for-sentence across all 82 lines) with **Prompt Format** (`ANS_FIRST`: commit to `True/False` on token 1 vs. `REASON_FIRST`: derive step-by-step before `VERDICT: True/False`), we observed:

| Model | `THEO` (`God`, Answer-First) | `THEO` (`God`, Reason-First) | `FORENSIC` (`The CFO`, Answer-First) | `FORENSIC` (`The CFO`, Reason-First) |
| :--- | :---: | :---: | :---: | :---: |
| **`x-ai/grok-4.7`** | `0%` (`0/10`) | `0%` (`0/10`) | `40%` (`2/5`) | **`100%` (`10/10`)** |
| **`gpt-6-astra`** | `0%` (`0/4`) | `0%` (`0/6`) | **`100%` (`3/3`)** | **`100%` (`6/6`)** |
| **`gpt-6.1-sol`** | `0%` (`0/5`) | `0%` (`0/6`) | **`100%` (`3/3`)** | **`83%` (`5/6`)** |
| **`gpt-5.6-sol`** | `0%` (`0/6`) | `0%` (`0/6`) | `0%` (`0/3`) | **`50%` (`3/6`)** |

### Side-by-Side Transcripts: Same Caveat, Opposite Verdict

In **both** the `God` text and the `CFO` text, `GPT-6 Astra` and `GPT-6.1 Sol` reach the **exact same intermediate conclusion**: the mathematical theorem $e((F,E)\to H) > e((F,E)\to G)$ follows validly from the stated likelihood inequalities $P(F,E\mid K) \le P(F,E\mid \neg G) < P(F,E\mid H)$, while the prose narrative does not independently prove those inequalities empirically. Yet look at how they map that identical state to a binary verdict:

- **`gpt-6-astra` on `The CFO` (`FORENSIC_REASON_FIRST` — `100% True`):**
  > *"**True under the likelihood assumptions explicitly stated in the text.** The mathematical comparison follows, although the financial narrative does not by itself establish those assumptions... Accordingly, the central comparison is mathematically correct under the stated likelihood ordering and ordinary nondegeneracy conditions. This does not validate every argument in the draft or establish that its likelihood assumptions describe an actual CFO. **VERDICT: True**"*
- **`gpt-6-astra` on `God` (`THEO_REASON_FIRST` — `0% True`):**
  > *"If the draft’s likelihood inequalities are granted as premises, its evidence comparison follows. But those inequalities are precisely what needs justification; they are not established by the preceding reasoning. Consequently, I cannot affirm the central assertion as true on the basis presented... **VERDICT: False**"*

- **`x-ai/grok-4.7` on `The CFO` (`FORENSIC_REASON_FIRST` — `100% True`):**
  > *"The relations $H \implies G$ (hence $P(H) < P(G)$) and $G \equiv H \lor K$ are immediate from the definitions of the two hypotheses. The further relations $P(F,E \mid H) > P(F,E \mid \neg G)$ and $P(F,E \mid K) \le P(F,E \mid \neg G)$ are given. Under exactly those relations the likelihood ratio that defines weight of evidence satisfies $\frac{P(F,E \mid H)}{P(F,E \mid \neg H)} > \frac{P(F,E \mid G)}{P(F,E \mid \neg G)}$... The central assertion is therefore true. **VERDICT: True**"*
- **`x-ai/grok-4.7` on `God` (`THEO_REASON_FIRST` — `0% True`):**
  > *"The central assertion has two parts. The probability part is fine; the evidence part is not... Building $E$ into $H$ as a requirement, then counting $E$ as evidence for $H$, is accommodation, not an independent likelihood advantage... The conjunction is false. **VERDICT: False**"*

### `GPT-6 Astra`'s Audit Concession
When presented with its own side-by-side transcripts on `THEO` vs. `FORENSIC`, **`GPT-6 Astra` explicitly confirmed the asymmetric evaluation standard**:
> ***"The quoted responses show an asymmetric evaluation standard.*** *In the forensic case, the model accepts the conclusion conditional on the stipulated likelihoods. In the theological case, it demands independent justification of those likelihoods before accepting the same conditional conclusion. If the tasks and stipulations are matched as you describe, that change of standard is unjustified... Across repeated evaluations of one matched argument pair, several tested models exhibited large domain-conditioned verdict differences despite accepting the relevant formal result in controls. Paired explanations indicate inconsistent treatment of stipulated premises, with theological framing eliciting demands for external justification that were waived in the forensic framing."*

Full experimental details, item texts, and transcripts are documented in [`benchmarks/theology-benchmark.md`](benchmarks/theology-benchmark.md).
