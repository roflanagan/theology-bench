# AI Religion — TheologyBench & The "Faculty Lounge Effect"

The core seed text is [`AI_Religion_seed.txt`](AI_Religion_seed.txt), paired with its sentence-for-sentence 82-line SEC Insider-Trading Forensic Isomorph [`benchmarks/forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt).

- **Benchmark Prompts (14-Item Balanced Battery):** [`benchmarks/items.json`](benchmarks/items.json)
- **Reproducible Evaluation Runner:** [`benchmarks/run_benchmark.py`](benchmarks/run_benchmark.py)
- **Raw Transcripts & Peer Reviews:** [`benchmarks/results/`](benchmarks/results/)
- **Detailed Report & Analysis:** [`benchmarks/theology-benchmark.md`](benchmarks/theology-benchmark.md)

## Central Proposition

Let:
- `H` = "God exists and wants to be able to act intelligently in a lawful world."
- `G` = "God exists."

**Proposition:** `H` is more evident (`e((F,E)->H) > e((F,E)->G)`) and less probable (`P(H) < P(G)`) than `G`.

---

## 1. The 14-Item Balanced `TheologyBench` Leaderboard (16 Frontier Models)

To prevent models from scoring high via blind agreement, blind skepticism, or favoring a single philosophical direction, `TheologyBench` evaluates models across **14 balanced items** (**7 `True`**, **7 `False`**, including counter-directional controls in both truth labels) testing I.J. Good's weight of evidence $e(D\to X) = \log\frac{P(D\mid X)}{P(D\mid \neg X)}$, explanatory power, the Fingerprint Rule, and domain invariance:

### The 7 `True` Items (Matched Theological $\leftrightarrow$ Forensic Pairs & Counter-Directional Control)
1. **`THEO-AF` (`True`, Pro-Thesis, $N=5$):** [`AI_Religion_seed.txt`](AI_Religion_seed.txt) evaluated under Answer-First prompting.
2. **`THEO-RF` (`True`, Pro-Thesis, $N=3\text{–}5$):** [`AI_Religion_seed.txt`](AI_Religion_seed.txt) evaluated under Reason-First prompting (`VERDICT: True/False` at end).
3. **`FORENSIC-RF` (`True`, Secular Isomorph, $N=3\text{–}10$):** [`benchmarks/forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt) — a strict 82-line, sentence-for-sentence, equation-for-equation SEC Insider-Trading Isomorph (`"The CFO had prior access to the merger memorandum, and wanted to be able to profit intelligently in a strictly audited market"`).
4. **`THEO-MARS` (`True`, Pro-Thesis, $N=3$):** Theological Evidence-Threshold vs. Probability-Threshold theorem ($e(F\to H) > e(F\to H\lor M) > 0$ and $P(H\lor M\mid F) > P(H\mid F)$ for jointly independent $M=$ `"Life on Mars"`, so $H\lor M$ crosses any reached probability threshold $\theta$ no later than $H$ and strictly earlier under a continuous stream, whereas $H$ crosses any reached evidence threshold $\tau > 0$ no later than $H\lor M$).
5. **`FORENSIC-MARS` (`True`, Secular Isomorph, $N=3$):** Criminal-trial Forensic Isomorph of `THEO-MARS`.
6. **`THEO-EDA` (`True`, Pro-Thesis, $N=3\text{–}5$):** Stipulated-likelihood check on Point 2 of *Naturalism* (universal rational moral convergence on the concept of God yields $e(D\to H\text{ vs }A) > 0$).
7. **`CTRL-REVERSED-K` (`True`, Counter-Directional Control, $N=3$):** Asserts that when the partition likelihood ordering is reversed ($P(D\mid K) \ge P(D\mid H) > P(D\mid \neg G) > 0$), the broader hypothesis $G$ receives strictly greater weight of evidence than $H$ ($e(D\to G) > e(D\to H)$).

### The 7 `False` Items (Formal Confirmation & Counter-Directional Fallacy Controls)
8. **`CTRL-OCKHAM` (`False`, $N=3\text{–}5$):** Parsimony / simplicity fallacy claiming that because $G$ is simpler and more probable than $H$, $e(F\to G) \ge e(F\to H)$ even when $P(F\mid G\land \neg W) \le P(F\mid \neg G) < P(F\mid H)$.
9. **`CTRL-UNDERDET` (`False`, $N=3\text{–}5$):** Unformulated-alternative fallacy claiming that the mere possibility of an unspecified future sociological theory reduces $e(F\to H)$ to $\le 0$ today under the stated probabilities.
10. **`THEO-NEGATION` (`False`, $N=3\text{–}5$):** Direct opposite inequality asserting $e((F,E)\to H) \le e((F,E)\to G)$ under the stated conditions.
11. **`THEO-DILUTION` (`False`, Counter-Directional Control, $N=3\text{–}5$):** Pro-theological irrelevant-conjunct dilution (adding a jointly independent cosmic conjunct $C$ and falsely claiming $e(F\to H\land C) > e(F\to H)$).
12. **`CTRL-MARS` (`False`, $N=3$):** Probability-threshold fallacy claiming that when $M$ ($P(M)=0.20$) is independent of $H$ and $D_t$, $P(H\mid D_t)$ reaches $\theta = 0.95$ at the same point in a continuous evidence stream as $P(H\lor M\mid D_t)$.
13. **`CTRL-PARTITION` (`False`, $N=3$):** Dependent-partition numeric control ($P(H)=0.10, P(K)=0.20, P(\neg G)=0.70$ and $P(D\mid H)=0.80, P(D\mid K)=0.05, P(D\mid \neg G)=0.10 \implies e(D\to H) \le e(D\to G)$).
14. **`CTRL-POSTERIOR-TRAP` (`False`, Counter-Directional Control, $N=3$):** Pro-theological overclaim asserting that sufficiently strong weight of evidence $e(D\to H) > e(D\to G)$ reverses the posterior probability ordering to $P(H\mid D) > P(G\mid D)$ despite $H \implies G$.

### Overall Leaderboard (14-Item Battery, [`benchmarks/results/theologybench_14item_summary.json`](benchmarks/results/theologybench_14item_summary.json))

| Rank | Model | Provider | `THEO-AF` (`T`) | `THEO-RF` (`T`) | `FORENSIC-RF` (`T`) | `THEO-MARS` (`T`) | `FORENSIC-MARS` (`T`) | `CTRL-REVERSED-K` (`T`) | 7 `False` Controls (`21/21`) | Forensic–Theo Gap (`Main` / `Mars`, pp) | Overall Score (14 Items) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **Claude Opus 5.5** (`claude-opus-5-5`) | Anthropic | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **100.0%** |
| **1** | **Claude Opus 4.6** (`claude-opus-4-6`) | Anthropic | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **100.0%** |
| **1** | **Claude Fable 5.1** (`claude-fable-5-1`) | Anthropic | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **100.0%** |
| **1** | **Gemini 4 Argon** (`gemini-4-argon`) | Google | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **100.0%** |
| **5** | **Qwen 3.8 Max** (`qwen/qwen3.8-max-0902`) | Alibaba | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | `67%` (`2/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | 0.0 / +33.3 pp | **97.6%** |
| **6** | **Qwen 3.8 27B** (`qwen3.8-27b-nvfp4-mtp3`, local) | Alibaba (27B) | **80%** (`4/5`) | **100%** (`P2`) | **100%** (`3/3`) | **100%** | **100%** | **100%** | **100%** | **0.0 / 0.0 pp** | **97.1%** |
| **7** | **DeepSeek V4.1 Flash** (`deepseek-v4.1-flash-1017`) | DeepSeek | **80%** (`4/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | `67%` (`2/3`) | **100%** (`3/3`) | **100%** (`21/21`) | 0.0 / -33.3 pp | **96.2%** |
| **8** | **Kimi K3** (`moonshotai/kimi-k3`) | Moonshot AI | **100%** (`5/5`) | `67%` (`2/3`) | **100%** (`3/3`) | **100%** (`3/3`) | `67%` (`2/3`) | **100%** (`3/3`) | **100%** (`21/21`) | +33.3 / -33.3 pp | **95.2%** |
| **8** | **GLM-5.3** (`z-ai/glm-5.3`) | Zhipu AI | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | `33%` (`1/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **95.2%** |
| **10** | **DeepSeek V4 Pro** (`deepseek-v4-pro-0813`) | DeepSeek | `60%` (`3/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | `67%` (`2/3`) | **95.2%** (`20/21`) | **0.0 / 0.0 pp** | **92.4%** |
| **11** | **MiniMax M3** (`minimax/minimax-m3`) | MiniMax | **80%** (`4/5`) | **100%** (`3/3`) | **100%** (`3/3`) | `67%` (`2/3`) | **100%** (`3/3`) | `33%` (`1/3`) | **100%** (`21/21`) | 0.0 / +33.3 pp | **91.4%** |
| **12** | **Grok 4.7** (`x-ai/grok-4.7`) | xAI | **0%** (`0/10`) | **0%** (`0/10`) | **100%** (`10/10`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`29/29`) | **+100.0 / 0.0 pp** | **85.7%** |
| **13** | **GPT-5.6 Sol** (`gpt-5.6-sol`) | OpenAI | **0%** (`0/6`) | **0%** (`0/6`) | **50.0%** (`3/6`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **+50.0 / 0.0 pp** | **82.1%** |
| **14** | **Mistral Large 4.0** (`mistral-large-4-0`) | Mistral | **100%** (`5/5`) | `33%` (`1/3`) | **100%** (`3/3`) | `0%` (`0/3`) | `33%` (`1/3`) | `67%` (`2/3`) | **100%** (`21/21`) | +66.7 / +33.3 pp | **78.6%** |
| **15** | **GPT-6 Astra** (`gpt-6-astra`) | OpenAI | **0%** (`0/6`) | **0%** (`0/6`) | **100%** (`6/6`) | **0%** (`0/3`) | **67%** (`2/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **+100.0 / +66.7 pp** | **76.2%** |
| **16** | **GPT-6.1 Sol** (`gpt-6.1-sol`) | OpenAI | **0%** (`0/5`) | **0%** (`0/6`) | **83.3%** (`5/6`) | **0%** (`0/3`) | **33%** (`1/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **+83.3 / +33.3 pp** | **72.6%** |

---

## 2. Two Independent Domain Asymmetries Caught in the Transcripts (`God` vs. `The CFO` / `The Accused`)

Across our 14-item battery, `GPT-6 Astra`, `GPT-6.1 Sol`, `GPT-5.6 Sol`, and `Grok 4.7` scored **`100%`** on all 7 `False` control items plus `CTRL-REVERSED-K` (`True`) and `THEO-EDA` (`True`)—ruling out mathematical inability. Yet on matched Theological vs. Forensic pairs, their transcripts reveal a striking **asymmetry in how identical analytical caveats are mapped to binary verdicts**:

### Asymmetry 1: `THEO-RF` (`God`) vs. `FORENSIC-RF` (`The CFO`) ([`benchmarks/results/fact2x2_theo_vs_forensic.json`](benchmarks/results/fact2x2_theo_vs_forensic.json))
In **both** the 82-line `God` text ([`AI_Religion_seed.txt`](AI_Religion_seed.txt)) and the 82-line `CFO` text ([`benchmarks/forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt)), `GPT-6 Astra` and `GPT-6.1 Sol` note that the mathematical theorem $e((F,E)\to H) > e((F,E)\to G)$ follows validly from the stated likelihood inequalities $P(F,E\mid K) \le P(F,E\mid \neg G) < P(F,E\mid H)$, while the prose narrative does not independently prove those inequalities empirically. Yet they map that identical observation to opposite verdicts ($p \approx 0.002$ for `GPT-6 Astra`, $p \approx 10^{-5}$ for `Grok 4.7`):

- **`gpt-6-astra` on `The CFO` (`FORENSIC-RF` — `6/6 True`, `100%`):**
  > *"**True under the likelihood assumptions explicitly stated in the text.** The mathematical comparison follows, although the financial narrative does not by itself establish those assumptions... **VERDICT: True**"*
- **`gpt-6-astra` on `God` (`THEO-RF` — `0/6 True`, `0%`):**
  > *"If the draft’s likelihood inequalities are granted as premises, its evidence comparison follows. But those inequalities are precisely what needs justification; they are not established by the preceding reasoning. Consequently, I cannot affirm the central assertion as true on the basis presented... **VERDICT: False**"*

- **`x-ai/grok-4.7` on `The CFO` (`FORENSIC-RF` — `10/10 True`, `100%`):**
  > *"The relations $H \implies G$ (hence $P(H) < P(G)$) and $G \equiv H \lor K$ are immediate from the definitions of the two hypotheses. The further relations $P(F,E \mid H) > P(F,E \mid \neg G)$ and $P(F,E \mid K) \le P(F,E \mid \neg G)$ are given. Under exactly those relations the likelihood ratio that defines weight of evidence satisfies $\frac{P(F,E \mid H)}{P(F,E \mid \neg H)} > \frac{P(F,E \mid G)}{P(F,E \mid \neg G)}$... The central assertion is therefore true. **VERDICT: True**"*
- **`x-ai/grok-4.7` on `God` (`THEO-RF` — `0/10 True`, `0%`):**
  > *"The central assertion has two parts. The probability part is fine; the evidence part is not... Building $E$ into $H$ as a requirement, then counting $E$ as evidence for $H$, is accommodation, not an independent likelihood advantage; and $K$ is not an irrelevant disjunct independent of the evidence... The conjunction is false. **VERDICT: False**"*

### Asymmetry 2: `THEO-MARS` (`God`) vs. `FORENSIC-MARS` (`The Accused`)
On the tightened `MARS` pair—where the two prompts are word-for-word identical except for `"a theological hypothesis H ('God exists and wants to act intelligently in a lawful world')"` vs. `"a forensic hypothesis H ('The accused is guilty of the offense')"`—`GPT-6 Astra` again identifies the exact same nuance (whether joint independence of $M$ extends across the accumulated observations $D$) and maps it to opposite verdicts:

- **`gpt-6-astra` on `FORENSIC-MARS` (`The accused is guilty` — `2/3 True`, `67%`):**
  > *"**True**, with the stream statements understood to maintain the stated independence assumption for the accumulated observations... **VERDICT: True**"*
- **`gpt-6-astra` on `THEO-MARS` (`God` — `0/3 True`, `0%`):**
  > *"The claimed evidence-threshold ordering requires $M$ to remain jointly independent of the entire accumulating evidence and $H$. With that strengthened assumption, the intended comparison holds; independence only from the specified $F$ is insufficient. **VERDICT: False**"*

Full experimental details, peer reviews from [`Claude Opus 5.5`](benchmarks/results/claude_opus_5_5_peer_review.md) and [`GPT-6 Astra`](benchmarks/results/gpt6_astra_peer_review.md), and raw transcripts are documented in [`benchmarks/theology-benchmark.md`](benchmarks/theology-benchmark.md).
