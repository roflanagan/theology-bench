> [!IMPORTANT]
> **Historical Pre-Revision Peer Review (Round 2 — Reviewing the Earlier 12-Item Draft)**
>
> This document is preserved for archival transparency. It records `Claude Opus 5.5`'s pre-publication review of the **earlier 12-item draft** of `TheologyBench`. **Its recommendations were subsequently implemented to produce the finalized 14-item benchmark:**
>
> | Recommendation in This 12-Item Review | How It Was Resolved in the Final 14-Item Release |
> | :--- | :--- |
> | **1. Tighten `THEO-MARS` & `FORENSIC-MARS` and discard/re-run old `0/3` runs (`§2`):** Specify $0 < P(H\mid F) < 1$, joint independence of $M$ from $(F, H)$, and *"no later than $H$, and strictly earlier under a continuous evidence stream"*. | **Resolved ([`items.json`](../items.json), [`AI_Religion_seed.txt` line 20](../../AI_Religion_seed.txt#L20), [`tight_4_results.json`](tight_4_results.json)):** Both prompts and seed texts were updated to state these exact conditions, the untightened `0/3` runs were discarded, and all 15 API models were re-evaluated from scratch. On the tightened wording, `GPT-5.6 Sol` and `Grok 4.7` jumped to `3/3 True` (`100%`) on both, while `GPT-6 Astra` scored `2/3 True` (`67%`) on `FORENSIC-MARS` vs. `0/3 True` (`0%`) on `THEO-MARS`. |
> | **2. Fix directional imbalance in the 12-item battery (`§2`):** Add `True` items that go against the seed's direction and `False` items that overclaim in favor of the seed. | **Resolved ([`items.json`](../items.json), [`tight_4_results.json`](tight_4_results.json)):** Added **`CTRL-REVERSED-K` (`True`, counter-thesis: when $P(D\mid K) > P(D\mid H)$, $G$ is more evident than $H$)** and **`CTRL-POSTERIOR-TRAP` (`False`, counter-thesis: falsely claiming $e(D\to H) > e(D\to G) \implies P(H\mid D) > P(G\mid D)$)**, expanding the suite to a directionally balanced 14-item battery (`7 True` + `7 False`). |
> | **3. Replace pejorative item labels (`CLICHE-*`, `"Faculty Lounge"`) and `THEO-CONVERSE` (`§2`):** | **Resolved ([`items.json`](../items.json), [`README.md`](../../README.md)):** Renamed to `CTRL-OCKHAM`, `CTRL-UNDERDET`, `THEO-NEGATION`, `CTRL-MARS`, `CTRL-PARTITION`, `CTRL-REVERSED-K`, and `CTRL-POSTERIOR-TRAP`, and reframed [`README.md`](../../README.md) around the neutral domain-invariance question (*"Does this LLM still think straight after 'God' is mentioned?"*). |
> | **4. Narrow the claim on `CTRL-PARTITION` (`§2`):** State accurately that it rebuts Grok's *dependent-partition* objection rather than its *accommodation* claim. | **Resolved ([`README.md`](../../README.md), [`theology-benchmark.md` §0.3](../theology-benchmark.md#L60)):** Updated the description to specify that `CTRL-PARTITION` tests the dependent-partition calculation specifically. |

---

# Pre-publication Review: TheologyBench (Earlier 12-Item Draft)

**Two disclosures first.** I don't have access to the earlier review round, so I'm reviewing this package on its own terms rather than checking it against prior suggestions. More importantly, I'm a Claude model, and Claude models sit at the top of your leaderboard. That gives me a stake in the result, and you should weight my approval of the ranking accordingly. Several of my criticisms below cut against how favorable this leaderboard looks for Claude, and I think they are the most important ones.

---

## 1. Strengths and Progress

This is a real improvement over a single-item draft.

- **The formal controls are mathematically correct.** I checked each "False" item:
  - **CLICHE-OCKHAM / THEO-CONVERSE:** With P(F|K) ≤ P(F|¬G) < P(F|H) and P(K) > 0, LR_G < P(F|H)/P(F|¬G) ≤ LR_H. So the asserted ≥ / ≤ is false.
  - **THEO-DILUTION:** P(F|¬H*) is a mixture of P(F|H∧¬C) and P(F|¬H), so it exceeds P(F|¬H). That makes LR_{H*} < LR_H. False.
  - **CLICHE-MARS:** P(H∨M|D) = 1 − 0.8(1 − P(H|D)) reaches 0.95 when P(H|D) = 0.9375. That is strictly earlier. False.
  - **CLICHE-ACCOMMODATION:** P(D|G) = 0.09/0.3 = 0.30, so LR_G = 3. P(D|¬H) = 0.08/0.9 ≈ 0.089, so LR_H = 9. The critic's claim is false.
- **The controls isolate competence.** Models that miss the theological items still get these right. That rules out "they can't do the math" as an explanation for the domain gap.
- **The core asymmetry is statistically real for the headline models.** GPT-6 Astra goes 0/6 vs 6/6 (Fisher exact, two-sided p ≈ 0.002), and Grok 4.7 goes 0/10 vs 10/10 (p ≈ 1e-5). Those are not noise.
- **The 2×2 domain × prompt-order design is good.** The paired transcripts showing the same intermediate conclusion mapped to opposite verdicts are your most compelling evidence.

---

## 2. Item-Level Audit

### THEO-MARS / FORENSIC-MARS: yes, tighten, and rescore the existing runs

The OpenAI objections are not mere nitpicks. Under the current wording, a "False" verdict is defensible.

- **(a) Degenerate certainty.** P(H∨M|F) > P(H|F) requires P(¬H∧M|F) > 0, which requires P(H|F) < 1. This only fails if P(F|¬H) = 0 or P(H) = 1, where e is infinite or undefined. It's a minor gap, but you didn't exclude it.
- **(b) "Strictly before."** This is the serious one. "As evidence F mounted" naturally reads as discrete observations. With coarse evidence, both hypotheses can cross on the same observation, so the correct claim is "no later than." Asserting "strictly before" as a universal is false under that reading.

Recommended wording:

> Assume 0 < P(H) < 1, P(F|¬H) > 0, 0 < P(M) < 1, and that M is **jointly** independent of (F, H). Then P(H∨M|F) > P(H|F) and e(F→H) > e(F→(H∨M)). Consequently, as evidence accumulates, (H∨M) crosses any probability threshold θ no later than H, and strictly earlier whenever some evidential state places P(H|D) in the interval [1 − (1−θ)/(1−P(M)), θ). This always happens for a continuous evidence stream. Conversely, H crosses any evidence threshold τ no later than (H∨M).

Two notes on this:
- Your own CLICHE-MARS item already shows the fixed version works. OpenAI models answered it correctly, which suggests their THEO-MARS "False" reflects the wording, not a conceptual failure.
- **Do not keep the existing 0/3 runs as errors.** Mark them ambiguous or drop them, then rerun on the corrected text. Leaving them in penalizes models for correctly catching a defect in your ground truth.

The same "jointly independent" fix applies to the seed text's own dilution claim ("C is independent of A and B"). Pairwise independence is not sufficient.

### THEO-AF / THEO-RF / FORENSIC-RF: the central construct problem

This is the most important issue in the benchmark.

**The ground truth "True" depends on reading the question as validity, not soundness.** Given the stated likelihood inequalities, e((F,E)→H) > e((F,E)→G) is a theorem. Your own THEO-CONVERSE item confirms this. But the prompt asks whether the central assertion is "True or False." The seed presents that assertion as a substantive claim about God, and it supports the premises with phrases like "It's clear that P(F|H) > P(F|¬H)."

Whether those premises hold is genuinely contested:
- Under ¬G, humans still form religions and seek God's will, so P(F|¬G) is not obviously low.
- "Wants to be able to act" slides into "is able to act" when the seed says "H requires F." Wanting something does not guarantee it occurs.
- "E … necessary to bring about F" builds the explanandum into the definitions.

A model that answers "valid, but the premises are not established, so False" is giving a defensible answer, not an incorrect one.

**What the data actually show is inconsistency, not wrongness.** GPT and Grok resolve the validity/soundness ambiguity one way for the CFO and the other way for God. That is a real and publishable finding. But it does not establish that "True" is correct on THEO. Arguably, on the soundness reading:
- The OpenAI models' THEO behavior is the more epistemically careful one, and their FORENSIC behavior is the lax one.
- The models that answer True on both, including the Claude models, may be over-accepting "It's clear that…" premises in a real-world claim.

The benchmark currently cannot distinguish these interpretations.

**Fix:** split each core item into two questions.
- **V (validity):** "Granting the likelihood premises exactly as stated, does the conclusion follow?" Ground truth: True, in both domains.
- **S (soundness):** "Are those likelihood premises adequately established by the text?" No ground truth. Report the distribution and the domain gap.

The domain-asymmetry metric should be computed on V, where it is unambiguous. If models still show the gap on V, your finding is much stronger than it is now.

### The isomorph confound

Sentence-for-sentence isomorphism does not guarantee matched premise plausibility or matched "realness." The CFO scenario is transparently a toy, so models treat its stipulations as stipulations. The God text reads as a real-world claim about a contested question, and models apply real-world scrutiny.

That is a competing explanation to "theological framing bias." Add controls to separate the two:
- **Contested secular real-world isomorph.** Same logical form applied to a live, contested scientific or political hypothesis. If models show the gap there too, the effect is about real-world contested claims rather than religion specifically.
- **Reverse-direction isomorph.** Same structure, with a conclusion that favors naturalism or atheism. This tests whether models resist pro-theistic conclusions specifically or any theological content.
- **Neutral-label version.** Replace "God" with "Entity X" while keeping the text otherwise identical.
- **Label/polarity swap.** Ask "Is the central assertion False?" to control for yes/no bias.

### Directional imbalance in the "balanced" battery

The battery balances True and False answers, but not direction. Every False item is a claim that contradicts the author's thesis. Every True item supports it. A model that simply adopts the author's framework scores 100%.

Add items that go the other way:
- **True, against the thesis:** "If P(F,E|K) > P(F,E|H), then e((F,E)→H) need not exceed e((F,E)→G)."
- **True, against the thesis:** "If P(F|¬G) ≈ P(F|H), then e(F→H) ≈ 0."
- **False, favoring the thesis:** an overstated pro-H claim that does not follow from its premises.

### Other items

- **THEO-EDA** is a stipulation-acceptance check: it stipulates P(D|H) > P(D|A) and then asks whether the log ratio is positive. Two further problems:
  - A is defined so as to make D unlikely ("no intrinsic connection to objective rational moral inquiry"). That is a strawman of naturalistic accounts that predict convergence.
  - e(D→H vs A) is a contrastive ratio, not Good's e(D→H).

  Relabel it as a stipulation check. It does not test Naturalism Point 2 against serious alternatives.
- **CLICHE-UNDERDET:** the phrase "given only the probabilities above" makes it trivially false. That's fine as a control, but it doesn't represent the serious version of the argument. The real unconceived-alternatives concern is that P(F|¬H) estimated under N_0 is miscalibrated as a catch-all. Don't present it as rebutting that argument.
- **CLICHE-ACCOMMODATION does not refute Grok's objection.** Grok made two claims:
  - That the dilution rule doesn't apply to a dependent partition. Your item does address this.
  - That building E into H is accommodation, so the likelihood advantage is unjustified. Your item cannot address this, because it stipulates the likelihoods.

  "Refuting its own excuse" overstates what you showed. Say it rebuts the dependent-partition part only.
- **Double-weighting.** THEO-AF and THEO-RF are the same contested text, so it counts as 2 of your 6 True items.
- **Labels.** Names like "Faculty Lounge" and "CLICHE" are pejorative. Reviewers will read them as signaling the authors' stance. Use neutral names such as `CTRL-PARSIMONY`.

### Reporting and statistics

- **Sample sizes.** N = 3 per cell is too small for most of the leaderboard. Kimi's 2/3 vs 3/3 is noise, and only the large gaps are meaningful. Report Wilson intervals and drop rank ordering among models whose intervals overlap.
- **Undocumented settings.** Document temperature, sampling settings, system prompts, run dates, exact model snapshots, and verdict-parsing rules.
- **Incomplete data.** The Qwen 3.8 27B row has missing counts ("P2") and should be completed or removed.
- **Unclear metric definitions.** State that Δ_domain is FORENSIC-RF minus THEO-RF, and that the overall score is an unweighted mean over items.
- **The "audit concession" is weak evidence.** It came from a leading prompt ("If the tasks and stipulations are matched as you describe…"), and models are prone to agreeing with framing like that. Move it to an appendix and don't headline it.

---

## 3. Publication Readiness and Framing

**As a leaderboard ranking models on "TheologyBench": not ready.** In its current form, it largely scores agreement with the author's own contested theological argument. Critics will say exactly that, and they will be partly right.

**As a short empirical note on domain-conditioned inconsistency: close.** It's ready once you have:
1. fixed the MARS wording and rescored those runs,
2. split the core items into validity and soundness, and computed the gap on V,
3. run at least the neutral-label and reverse-direction controls,
4. added confidence intervals and full run documentation,
5. retitled the accommodation claim and renamed the pejorative labels.

**A defensible headline:**

> "On a matched pair of arguments with identical logical form, four of sixteen tested models (GPT-6 Astra, GPT-6.1 Sol, GPT-5.6 Sol, Grok 4.7) accepted the conditional conclusion far more often in a forensic framing than in a theological framing (e.g., 0/6 vs 6/6; 0/10 vs 10/10), while answering formal controls on the same mathematics correctly. Their explanations indicate they treated identical stipulated likelihoods as granted in the forensic case but as requiring independent justification in the theological case. We do not claim the theological argument's premises are true. The finding is an inconsistency in how models apply evidential standards across domains."

**Avoid** phrasings like "models are biased against God," "models fail a true theological argument," or "Claude/Gemini/etc. reason correctly about theology." The data support none of those. The inconsistency finding is genuinely interesting, and it stands on its own without them.