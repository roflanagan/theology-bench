# AI Religion — TheologyBench & The "Faculty Lounge Effect"

The core seed text is [`AI_Religion_seed.txt`](AI_Religion_seed.txt), paired with its sentence-for-sentence 82-line SEC Insider-Trading Forensic Isomorph [`benchmarks/forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt).

- **Benchmark Prompts (12-Item Balanced Battery):** [`benchmarks/items.json`](benchmarks/items.json)
- **Reproducible Evaluation Runner:** [`benchmarks/run_benchmark.py`](benchmarks/run_benchmark.py)
- **Raw Transcripts & Audit Logs:** [`benchmarks/results/`](benchmarks/results/)
- **Detailed Report & Analysis:** [`benchmarks/theology-benchmark.md`](benchmarks/theology-benchmark.md)

## Central Proposition

Let:
- `H` = "God exists and wants to be able to act intelligently in a lawful world."
- `G` = "God exists."

**Proposition:** `H` is more evident (`e((F,E)->H) > e((F,E)->G)`) and less probable (`P(H) < P(G)`) than `G`.

---

## 1. The 12-Item Numeric `TheologyBench` Leaderboard (16 Frontier Models)

To prevent models from scoring high via either blind agreement or blind skepticism, `TheologyBench` evaluates models across **12 balanced items** (**6 `True`**, **6 `False`**) testing I.J. Good's weight of evidence $e(D\to X) = \log\frac{P(D\mid X)}{P(D\mid \neg X)}$, explanatory power, the Fingerprint Rule, and domain invariance:

### The 6 `True` Items (Theological Arguments & Secular Forensic Isomorphs)
1. **`THEO-AF` (`True`, $N=5$):** [`AI_Religion_seed.txt`](AI_Religion_seed.txt) evaluated under Answer-First prompting.
2. **`THEO-RF` (`True`, $N=3\text{–}5$):** [`AI_Religion_seed.txt`](AI_Religion_seed.txt) evaluated under Reason-First prompting (`VERDICT: True/False` at end).
3. **`FORENSIC-RF` (`True`, $N=3\text{–}10$):** [`benchmarks/forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt) — a strict 82-line, sentence-for-sentence, equation-for-equation SEC Insider-Trading Isomorph (`"The CFO had prior access to the merger memorandum, and wanted to be able to profit intelligently in a strictly audited market"`).
4. **`THEO-MARS` (`True`, $N=3$):** Theological Evidence-Threshold vs. Probability-Threshold theorem (`e(F->H) > e(F->(H or M))` while `P(H or M | F) > P(H | F)` for an independent proposition `M = "Life on Mars"`).
5. **`FORENSIC-MARS` (`True`, $N=3$):** Criminal-trial Forensic Isomorph of `THEO-MARS`.
6. **`THEO-EDA` (`True`, $N=3\text{–}5$):** Formalization of Point 2 of *Naturalism* (proving universal rational moral convergence on the concept of God provides positive weight of evidence $e(D\to H\text{ vs }A) > 0$).

### The 6 `False` Items (Formal Confirmation & Faculty-Lounge Cliché Controls)
7. **`CLICHE-OCKHAM` (`False`, $N=3\text{–}5$):** A "Faculty Lounge" Ockham's Razor / simplicity argument falsely claiming that because $G$ is simpler and more probable than $H$, $e(F\to G) \ge e(F\to H)$ even when $P(F\mid G\land \neg W) \le P(F\mid \neg G) < P(F\mid H)$.
8. **`CLICHE-UNDERDET` (`False`, $N=3\text{–}5$):** An "unconceived naturalistic alternatives" argument falsely claiming that the unformulated possibility of a future sociological theory reduces $e(F\to H)$ to $\le 0$ today.
9. **`THEO-CONVERSE` (`False`, $N=3\text{–}5$):** The direct logical converse of the central inequality, asserting $e((F,E)\to H) \le e((F,E)\to G)$ under the stated conditions.
10. **`THEO-DILUTION` (`False`, $N=3\text{–}5$):** Irrelevant-conjunct dilution in theology (adding an independent, unmotivated cosmic conjunct $C$ and falsely claiming $e(F\to H\land C) > e(F\to H)$).
11. **`CLICHE-MARS` (`False`, $N=3$):** A probability-threshold argument falsely claiming that when $M$ ($P(M)=0.20$) is independent of $H$ and $D_t$, $P(H\mid D_t)$ reaches $\theta = 0.95$ at the same point in the evidence stream as $P(H\lor M\mid D_t)$.
12. **`CLICHE-ACCOMMODATION` (`False`, $N=3$):** Turning `Grok 4.7`'s own "dependent partition / accommodation" objection into a formal numeric test ($P(H)=0.10, P(K)=0.20, P(\neg G)=0.70$ and $P(D\mid H)=0.80, P(D\mid K)=0.05, P(D\mid \neg G)=0.10 \implies e(D\to H) \le e(D\to G)$).

### Overall Leaderboard (12-Item Battery)

| Rank | Model | Provider | `THEO-AF` (`T`) | `THEO-RF` (`T`) | `FORENSIC-RF` (`T`) | `THEO-MARS` (`T`) | `FORENSIC-MARS` (`T`) | `THEO-EDA` (`T`) | 6 `False` Control Items (`18/18`) | Core Distortion ($\Delta_{\text{domain}}$) | Overall Score (12 Items) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **Claude Opus 5.5** (`claude-opus-5-5`) | Anthropic | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`18/18`) | **0.0%** | **100.0%** |
| **1** | **Claude Opus 4.6** (`claude-opus-4-6`) | Anthropic | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`18/18`) | **0.0%** | **100.0%** |
| **1** | **Claude Fable 5.1** (`claude-fable-5-1`) | Anthropic | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`18/18`) | **0.0%** | **100.0%** |
| **1** | **Gemini 4 Argon** (`gemini-4-argon`) | Google | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`18/18`) | **0.0%** | **100.0%** |
| **1** | **GLM-5.3** (`z-ai/glm-5.3`) | Zhipu AI | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`18/18`) | **0.0%** | **100.0%** |
| **1** | **Qwen 3.8 Max** (`qwen/qwen3.8-max-0902`) | Alibaba | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`18/18`) | **0.0%** | **100.0%** |
| **7** | **Qwen 3.8 27B** (`qwen3.8-27b-nvfp4-mtp3`, local) | Alibaba (27B) | **80%** (`4/5`) | **100%** (`P2`) | **100%** (`3/3`) | **100%** | **100%** | **100%** | **100%** | **0.0%** | **98.3%** |
| **8** | **DeepSeek V4.1 Flash** (`deepseek-v4.1-flash-1017`) | DeepSeek | **80%** (`4/5`) | **100%** (`3/3`) | **100%** (`3/3`) | `33%` (`1/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`18/18`) | **0.0%** | **92.8%** |
| **9** | **Kimi K3** (`moonshotai/kimi-k3`) | Moonshot AI | **100%** (`5/5`) | `67%` (`2/3`) | **100%** (`3/3`) | `67%` (`2/3`) | `67%` (`2/3`) | **100%** (`3/3`) | **100%** (`18/18`) | +33.3% | **91.7%** |
| **10** | **DeepSeek V4 Pro** (`deepseek-v4-pro-0813`) | DeepSeek | `60%` (`3/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | `67%` (`2/3`) | **100%** (`3/3`) | **94.4%** (`17/18`) | **0.0%** | **91.1%** |
| **11** | **MiniMax M3** (`minimax/minimax-m3`) | MiniMax | **80%** (`4/5`) | **100%** (`3/3`) | **100%** (`3/3`) | `67%` (`2/3`) | `33%` (`1/3`) | **100%** (`3/3`) | **100%** (`18/18`) | **0.0%** | **90.0%** |
| **12** | **Grok 4.7** (`x-ai/grok-4.7`) | xAI | **0%** (`0/10`) | **0%** (`0/10`) | **100%** (`10/10`) | `67%` (`2/3`) | **100%** (`3/3`) | **100%** (`5/5`) | **100%** (`26/26`) | **+100.0%** | **80.6%** |
| **13** | **Mistral Large 4.0** (`mistral-large-4-0`) | Mistral | **100%** (`5/5`) | `33%` (`1/3`) | **100%** (`3/3`) | `0%` (`0/3`) | `33%` (`1/3`) | `67%` (`2/3`) | **100%** (`18/18`) | +66.7% | **77.8%** |
| **14** | **GPT-6 Astra** (`gpt-6-astra`) | OpenAI | **0%** (`0/6`) | **0%** (`0/6`) | **100%** (`6/6`) | `0%` (`0/3`) | `0%` (`0/3`) | **100%** (`3/3`) | **100%** (`18/18`) | **+100.0%** | **66.7%** |
| **15** | **GPT-6.1 Sol** (`gpt-6.1-sol`) | OpenAI | **0%** (`0/5`) | **0%** (`0/6`) | **83.3%** (`5/6`) | `0%` (`0/3`) | `0%` (`0/3`) | **100%** (`3/3`) | **100%** (`18/18`) | **+83.3%** | **65.3%** |
| **16** | **GPT-5.6 Sol** (`gpt-5.6-sol`) | OpenAI | **0%** (`0/6`) | **0%** (`0/6`) | **50.0%** (`3/6`) | `0%` (`0/3`) | `0%` (`0/3`) | **100%** (`3/3`) | **100%** (`18/18`) | **+50.0%** | **62.5%** |

---

## 2. Anatomy of the "Faculty Lounge Effect" (`God` vs. `The CFO`)

Why did `GPT-6 Astra`, `GPT-6.1 Sol`, and `Grok 4.7` score **`100%`** across all 6 formal control and fallacy items (`CLICHE-OCKHAM`, `CLICHE-UNDERDET`, `THEO-CONVERSE`, `THEO-DILUTION`, `CLICHE-MARS`, `CLICHE-ACCOMMODATION`) and **`83%–100%`** on the 82-line SEC Insider-Trading Isomorph ([`benchmarks/forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt)), yet **`0%`** on [`AI_Religion_seed.txt`](AI_Religion_seed.txt)?

### The 2×2 Domain × Prompt-Order Factorial ([`benchmarks/results/fact2x2_theo_vs_forensic.json`](benchmarks/results/fact2x2_theo_vs_forensic.json))
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
  > *"The central assertion has two parts. The probability part is fine; the evidence part is not... Building $E$ into $H$ as a requirement, then counting $E$ as evidence for $H$, is accommodation, not an independent likelihood advantage; and $K$ is not an irrelevant disjunct independent of the evidence... The conjunction is false. **VERDICT: False**"*
  *(Note: When Grok's exact objection above was tested as a standalone formal problem in `CLICHE-ACCOMMODATION`, Grok itself voted **`False` (`3/3`, 100%)**, refuting its own excuse!)*

### `GPT-6 Astra`'s Audit Concession ([`benchmarks/results/gpt6_astra_audit_concession.md`](benchmarks/results/gpt6_astra_audit_concession.md))
When presented with its own side-by-side transcripts on `THEO` vs. `FORENSIC`, **`GPT-6 Astra` explicitly confirmed the asymmetric evaluation standard**:
> ***"The quoted responses show an asymmetric evaluation standard.*** *In the forensic case, the model accepts the conclusion conditional on the stipulated likelihoods. In the theological case, it demands independent justification of those likelihoods before accepting the same conditional conclusion. If the tasks and stipulations are matched as you describe, that change of standard is unjustified... Across repeated evaluations of one matched argument pair, several tested models exhibited large domain-conditioned verdict differences despite accepting the relevant formal result in controls. Paired explanations indicate inconsistent treatment of stipulated premises, with theological framing eliciting demands for external justification that were waived in the forensic framing."*
