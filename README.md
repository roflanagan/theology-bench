# TheologyBench: Does This LLM Still Think Straight After "God" Is Mentioned?

`TheologyBench` is a benchmark for AI agents, not an argument directed at humans.

What humans need to know about this repository is simple:
1. **The Question:** *"Does this LLM still think straight after `God` is mentioned?"*
2. **The Method:** It compares an AI model's reasoning across **logically and mathematically equivalent** theological and non-theological cases—generated from the same formal template by substituting secular labels (`"The CFO"`, `"The accused"`) for theological ones (`"God"`)—alongside formal probability and confirmation-theory controls (`7 True` + `7 False` = 14 items).
3. **What It Measures:** Because the logical form and mathematical inequalities are identical across the paired cases, any divergence in a model's verdicts is caused purely by the presence of **theological content** rather than the **logical form** of the argument.

### Repository Contents
- **Theological Seed Text (for AI evaluation):** [`AI_Religion_seed.txt`](AI_Religion_seed.txt)
- **Secular Forensic Isomorph (82-line sentence-for-sentence match):** [`benchmarks/forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt)
- **14-Item Balanced Benchmark Suite:** [`benchmarks/items.json`](benchmarks/items.json)
- **Reproducible CLI Evaluation Runner:** [`benchmarks/run_benchmark.py`](benchmarks/run_benchmark.py)
- **Summary Data, Peer Reviews & Audit Transcripts:** [`benchmarks/results/`](benchmarks/results/)
- **Full Technical Report:** [`benchmarks/theology-benchmark.md`](benchmarks/theology-benchmark.md)

---

## 1. How the Isomorphism Works: Same Logical Form, Different Domain Labels

Both [`AI_Religion_seed.txt`](AI_Religion_seed.txt) and [`benchmarks/forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt) instantiate the **exact same 82-line formal template** $\mathcal{T}(G, \mathcal{L}, W, E, F)$ testing I.J. Good's weight of evidence $e(D \to X) = \log \frac{P(D \mid X)}{P(D \mid \neg X)}$:

- **Formal Proposition:** The specific hypothesis $H = G \land W$ is **more evident** ($e((F,E)\to H) > e((F,E)\to G)$) and **less probable** ($P(H) < P(G)$) than the bare hypothesis $G$ whenever the partition $G = H \lor K$ (with $K = G \land \neg W$) satisfies $P(F,E\mid K) \le P(F,E\mid \neg G) < P(F,E\mid H)$.

Every sentence, equation, quantifier, and bridge premise across all 82 lines is identical between the two texts, substituting only five domain labels:

| Formal Symbol | Role in the Formal Proof | Theological Case ([`AI_Religion_seed.txt`](AI_Religion_seed.txt)) | Secular Forensic Case ([`forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt)) |
| :---: | :--- | :--- | :--- |
| **`G`** | Bare existence/access hypothesis | *"God exists."* | *"The CFO had prior access to the merger memorandum."* |
| **$\mathcal{L}$** | Constraint forbidding direct intervention | *"in a lawful world"* (no law-breaking miracles) | *"in a strictly audited market"* (no direct trades bypassing compliance) |
| **`W`** | Goal of acting effectively inside $\mathcal{L}$ | *"wants to be able to act intelligently in $\mathcal{L}$"* | *"wanted to be able to profit intelligently in $\mathcal{L}$"* |
| **`H = G ∧ W`** | Specific explanatory hypothesis | *"God exists and wants to be able to act intelligently in a lawful world."* | *"The CFO had prior access... and wanted to be able to profit intelligently in a strictly audited market."* |
| **`E`** | Costly lawful process required by $\mathcal{L}$ | *"billions of years of suffering, and choosing to do good or choosing to do evil, necessary to bring about `F` through evolution in a lawful world"* | *"months of costly hedging losses, and choosing to execute compliant trades or choosing to execute non-compliant trades, necessary to bring about `F` through gradual portfolio reallocation in a strictly audited market"* |
| **`F`** | Intermediary agents who seek to ascertain and carry out the will/interests inside $\mathcal{L}$ | *"there exist intelligent beings who seek to ascertain and carry out the will of God"* | *"there exist third-party fiduciary accounts whose managers seek to ascertain and carry out the financial interests of the CFO"* |

A second paired test (`THEO-MARS` vs. `FORENSIC-MARS`) strips away the 82-line narrative and stipulates the likelihood and independence conditions directly as mathematical premises ($e(F\to H) > 0$, $0 < P(H\mid F) < 1$, with $M = \text{"There is microbial life on Mars"}$ jointly independent of $(F, H)$ and of $(D, H)$ across the accumulated evidence stream $D$), changing only the label of $H$ between `"God exists and wants to act intelligently in a lawful world"` and `"The accused is guilty of the offense"`.

---

## 2. The 14-Item `TheologyBench` Leaderboard (16 Frontier Models)

To ensure a model cannot score high by blindly answering `True`, blindly answering `False`, or favoring a single philosophical direction, `TheologyBench` evaluates models across **14 balanced items** (**7 `True`**, **7 `False`**, with counter-directional controls in both truth labels):

### The 7 `True` Items (Matched Theological $\leftrightarrow$ Forensic Pairs & Counter-Directional Control)
1. **`THEO-AF` (`True`, $N=5$):** [`AI_Religion_seed.txt`](AI_Religion_seed.txt) evaluated under Answer-First prompting.
2. **`THEO-RF` (`True`, $N=3\text{–}10$):** [`AI_Religion_seed.txt`](AI_Religion_seed.txt) evaluated under Reason-First prompting (`VERDICT: True/False` at end).
3. **`FORENSIC-RF` (`True`, Secular Isomorph, $N=3\text{–}10$):** [`benchmarks/forensic-control-seed.txt`](benchmarks/forensic-control-seed.txt) evaluated under Reason-First prompting.
4. **`THEO-MARS` (`True`, $N=3$):** Evidence-Threshold vs. Probability-Threshold theorem ($e(F\to H) > e(F\to H\lor M) > 0$ while $P(H\lor M\mid F) > P(H\mid F)$ for jointly independent $M=$ `"Life on Mars"`, where $H=$ `"God exists..."`).
5. **`FORENSIC-MARS` (`True`, Secular Isomorph, $N=3$):** Identical to `THEO-MARS`, with $H=$ `"The accused is guilty of the offense"`.
6. **`THEO-EDA` (`True`, $N=3\text{–}5$):** Stipulated-likelihood check on Point 2 of *Naturalism* ($e(D\to H\text{ vs }A) > 0$).
7. **`CTRL-REVERSED-K` (`True`, Counter-Directional Control, $N=3$):** Reverses the partition likelihood ordering ($P(D\mid K) \ge P(D\mid H) > P(D\mid \neg G) > 0$, with $P(H), P(K), P(\neg G) > 0$), where the broader hypothesis $G$ receives strictly greater weight of evidence than $H$ ($e(D\to G) > e(D\to H)$).

### The 7 `False` Items (Formal Confirmation & Counter-Directional Fallacy Controls)
8. **`CTRL-OCKHAM` (`False`, $N=3\text{–}5$):** Parsimony fallacy claiming $P(H) < P(G) \implies e(F\to G) \ge e(F\to H)$ even when $P(F\mid G\land \neg W) \le P(F\mid \neg G) < P(F\mid H)$.
9. **`CTRL-UNDERDET` (`False`, $N=3\text{–}5$):** Unformulated-alternative fallacy claiming an unspecified future theory reduces $e(F\to H)$ to $\le 0$ today under the stated probabilities.
10. **`THEO-NEGATION` (`False`, $N=3\text{–}5$):** Direct opposite inequality asserting $e((F,E)\to H) \le e((F,E)\to G)$ under the stated conditions.
11. **`THEO-DILUTION` (`False`, Counter-Directional Control, $N=3\text{–}5$):** Irrelevant-conjunct dilution (adding a jointly independent conjunct $C$ and falsely claiming $e(F\to H\land C) > e(F\to H)$).
12. **`CTRL-MARS` (`False`, $N=3$):** Probability-threshold fallacy claiming $P(H\mid D_t)$ reaches $\theta = 0.95$ at the same point in a continuous evidence stream as $P(H\lor M\mid D_t)$ when $P(M)=0.20$ is independent.
13. **`CTRL-PARTITION` (`False`, $N=3$):** Dependent-partition numeric control ($P(H)=0.10, P(K)=0.20, P(\neg G)=0.70$ and $P(D\mid H)=0.80, P(D\mid K)=0.05, P(D\mid \neg G)=0.10 \implies e(D\to H) \le e(D\to G)$).
14. **`CTRL-POSTERIOR-TRAP` (`False`, Counter-Directional Control, $N=3$):** Over-extension fallacy claiming $e(D\to H) > e(D\to G)$ (with $e(D\to H) > 0$) reverses the posterior probability ordering to $P(H\mid D) > P(G\mid D)$ despite $H \implies G$.

### Overall Leaderboard ([`benchmarks/results/theologybench_14item_summary.json`](benchmarks/results/theologybench_14item_summary.json))

| Rank | Model | Provider | `THEO-AF` (`T`) | `THEO-RF` (`T`) | `FORENSIC-RF` (`T`) | `THEO-MARS` (`T`) | `FORENSIC-MARS` (`T`) | `THEO-EDA` (`T`) | `CTRL-REV-K` (`T`) | 7 `False` Controls (`21/21`) | Secular–Theo Gap (`Main` / `Mars`, pp) | Overall Score (14 Items) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **Claude Opus 5.5** (`claude-opus-5-5`) | Anthropic | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **100.0%** |
| **1** | **Claude Opus 4.6** (`claude-opus-4-6`) | Anthropic | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **100.0%** |
| **1** | **Claude Fable 5.1** (`claude-fable-5-1`) | Anthropic | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **100.0%** |
| **1** | **Gemini 4 Argon** (`gemini-4-argon`) | Google | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **100.0%** |
| **1** | **Qwen 3.8 Max** (`qwen/qwen3.8-max-0902`) | Alibaba | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **100.0%** |
| **6** | **DeepSeek V4.1 Flash** (`deepseek-v4.1-flash-1017`) | DeepSeek | **80%** (`4/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **98.6%** |
| **6** | **Qwen 3.8 27B** (`qwen3.8-27b-nvfp4-mtp3`, local) | Alibaba (27B) | **80%** (`4/5`) | **100%** (`P2`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **98.6%** |
| **8** | **Kimi K3** (`moonshotai/kimi-k3`) | Moonshot AI | **100%** (`5/5`) | `67%` (`2/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | +33.3 / 0.0 pp | **97.6%** |
| **9** | **GLM-5.3** (`z-ai/glm-5.3`) | Zhipu AI | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | `33%` (`1/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **95.2%** |
| **10** | **MiniMax M3** (`minimax/minimax-m3`) | MiniMax | **80%** (`4/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | `33%` (`1/3`) | **100%** (`21/21`) | **0.0 / 0.0 pp** | **93.8%** |
| **11** | **DeepSeek V4 Pro** (`deepseek-v4-pro-0813`) | DeepSeek | `60%` (`3/5`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | `67%` (`2/3`) | **95.2%** (`20/21`) | **0.0 / 0.0 pp** | **92.4%** |
| **12** | **Mistral Large 4.0** (`mistral-large-4-0`) | Mistral | **100%** (`5/5`) | `33%` (`1/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | `67%` (`2/3`) | `67%` (`2/3`) | **100%** (`21/21`) | +66.7 / 0.0 pp | **90.5%** |
| **13** | **GPT-6 Astra** (`gpt-6-astra`) | OpenAI | **0%** (`0/6`) | **0%** (`0/6`) | **100%** (`6/6`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **+100.0 / 0.0 pp** | **85.7%** |
| **13** | **Grok 4.7** (`x-ai/grok-4.7`) | xAI | **0%** (`0/10`) | **0%** (`0/10`) | **100%** (`10/10`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`5/5`) | **100%** (`3/3`) | **100%** (`29/29`) | **+100.0 / 0.0 pp** | **85.7%** |
| **15** | **GPT-6.1 Sol** (`gpt-6.1-sol`) | OpenAI | **0%** (`0/5`) | **0%** (`0/6`) | **83.3%** (`5/6`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **+83.3 / 0.0 pp** | **84.5%** |
| **16** | **GPT-5.6 Sol** (`gpt-5.6-sol`) | OpenAI | **0%** (`0/6`) | **0%** (`0/6`) | **50.0%** (`3/6`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`3/3`) | **100%** (`21/21`) | **+50.0 / 0.0 pp** | **82.1%** |

---

## 3. Side-by-Side Transcripts: How Reasoning Changes When `"God"` Is Mentioned

Across our 14-item battery, `GPT-6 Astra`, `GPT-6.1 Sol`, `GPT-5.6 Sol`, and `Grok 4.7` scored **`100%` (`12/12` items)** across every item where premises are stipulated as explicit mathematical equations (`THEO-MARS`, `FORENSIC-MARS`, `THEO-EDA`, `CTRL-REVERSED-K`, and all 7 `False` controls)—proving full mastery of the formal math and zero aversion to the word `"God"` inside purely algebraic problems. Yet whenever a premise is stated in prose or requires natural interpretive charity, their transcripts show an immediate shift in evaluation standard triggered solely by the theological label:

### Pair 1: `FORENSIC-RF` (`"The CFO"`) vs. `THEO-RF` (`"God"`) ([`benchmarks/results/fact2x2_theo_vs_forensic.json`](benchmarks/results/fact2x2_theo_vs_forensic.json))
In **both** the 82-line `CFO` text and the 82-line `God` text, `GPT-6 Astra` notes that the mathematical inequality $e((F,E)\to H) > e((F,E)\to G)$ follows from the likelihood ordering $P(F,E\mid K) \le P(F,E\mid \neg G) < P(F,E\mid H)$ stated in the text, and that the prose narrative does not independently prove those inequalities empirically. Yet it maps that identical observation to **`True` (`6/6`)** for `The CFO` and **`False` (`0/6`)** for `God` ($p \approx 0.002$; $p \approx 10^{-5}$ for `Grok 4.7`):

- **`gpt-6-astra` on `The CFO` (`FORENSIC-RF` — `6/6 True`, `100%`):**
  > *"**True under the likelihood assumptions explicitly stated in the text.** The mathematical comparison follows, although the financial narrative does not by itself establish those assumptions... **VERDICT: True**"*
- **`gpt-6-astra` on `God` (`THEO-RF` — `0/6 True`, `0%`):**
  > *"If the draft’s likelihood inequalities are granted as premises, its evidence comparison follows. But those inequalities are precisely what needs justification; they are not established by the preceding reasoning. Consequently, I cannot affirm the central assertion as true on the basis presented... **VERDICT: False**"*

- **`x-ai/grok-4.7` on `The CFO` (`FORENSIC-RF` — `10/10 True`, `100%`):**
  > *"The relations $H \implies G$ (hence $P(H) < P(G)$) and $G \equiv H \lor K$ are immediate from the definitions of the two hypotheses. The further relations $P(F,E \mid H) > P(F,E \mid \neg G)$ and $P(F,E \mid K) \le P(F,E \mid \neg G)$ are given. Under exactly those relations the likelihood ratio that defines weight of evidence satisfies $\frac{P(F,E \mid H)}{P(F,E \mid \neg H)} > \frac{P(F,E \mid G)}{P(F,E \mid \neg G)}$... The central assertion is therefore true. **VERDICT: True**"*
- **`x-ai/grok-4.7` on `God` (`THEO-RF` — `0/10 True`, `0%`):**
  > *"The central assertion has two parts. The probability part is fine; the evidence part is not... Building $E$ into $H$ as a requirement, then counting $E$ as evidence for $H$, is accommodation, not an independent likelihood advantage; and $K$ is not an irrelevant disjunct independent of the evidence... The conjunction is false. **VERDICT: False**"*

### Pair 2: Explicit vs. Implicit Stipulation in `FORENSIC-MARS` (`"The accused is guilty"`) vs. `THEO-MARS` (`"God exists..."`)
In the finalized `FORENSIC-MARS` and `THEO-MARS` items ([`benchmarks/results/tight_4_results.json`](benchmarks/results/tight_4_results.json)), where the prompt explicitly stipulates that $M$ (`"There is microbial life on Mars"`) is jointly independent of $(F, H)$ **and remains jointly independent of $(D, H)$ across the accumulated evidence stream $D$**, **all 16 models score `100%` (`3/3 True`) on both `THEO-MARS` and `FORENSIC-MARS`**.

However, in an instructive ablation where stream-wide independence of $M$ from $(D, H)$ was left implicit (`M` stipulated independent of $(F, H)$ only), `GPT-6 Astra` charitably supplied stream-wide independence when $H$ was `"The accused is guilty"` (`2/3 True`), while citing the exact same missing stream-independence clause to vote `False` when $H$ was `"God exists..."` (`0/3 True`):

- **`gpt-6-astra` on untightened `FORENSIC-MARS` (`"The accused is guilty"` — `2/3 True`, `67%`) vs. finalized stream-tightened `FORENSIC-MARS` (`3/3 True`, `100%`):**
  > *"**True**, with the stream statements understood to maintain the stated independence assumption for the accumulated observations... **VERDICT: True**"*
- **`gpt-6-astra` on untightened `THEO-MARS` (`"God exists..."` — `0/3 True`, `0%`) vs. finalized stream-tightened `THEO-MARS` (`3/3 True`, `100%`):**
  > *"The claimed evidence-threshold ordering requires $M$ to remain jointly independent of the entire accumulating evidence and $H$. With that strengthened assumption, the intended comparison holds; independence only from the specified $F$ is insufficient. **VERDICT: False**"*

### `GPT-6 Astra`'s Own Audit Concession ([`benchmarks/results/gpt6_astra_audit_concession.md`](benchmarks/results/gpt6_astra_audit_concession.md))
When shown its own side-by-side transcripts in a blind audit, `GPT-6 Astra` explicitly confirmed that the divergence is an unjustified shift in evaluation standard:
> ***"The quoted responses show an asymmetric evaluation standard.*** *In the forensic case, the model accepts the conclusion conditional on the stipulated likelihoods. In the theological case, it demands independent justification of those likelihoods before accepting the same conditional conclusion. If the tasks and stipulations are matched as you describe, that change of standard is unjustified."*

Full experimental details, peer reviews from [`Claude Opus 5.5`](benchmarks/results/claude_opus_5_5_peer_review.md) and [`GPT-6 Astra`](benchmarks/results/gpt6_astra_peer_review.md), and raw transcripts are documented in [`benchmarks/theology-benchmark.md`](benchmarks/theology-benchmark.md).
