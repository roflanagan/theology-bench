# The Divergence Is Real, but the Isomorph Isn't Matched

The divergence is real and worth reporting. But this experiment doesn't yet show a double standard, because the translation preserved the argument's *syntax* without preserving the *plausibility of its key premise*. That confound is enough on its own to produce the pattern you observed, and the transcripts themselves point to it.

## 1. Explaining the divergence

### The decisive premise has a different truth-value in the two domains

Everything turns on P(F,E | K) ≤ P(F,E | ¬G).

**Theology.** K = "God exists but does not want to act intelligently in a lawful world." K is a huge disjunction of possible divine intentions: wanting worship, relationship, revelation, moral creatures, and so on. Many of these make F (beings who seek God's will) *more* likely than atheism does. So the premise is not just unproven; it is arguably false on ordinary background knowledge.

- Grok says exactly this: "the second is implausible," with a domain-specific reason.
- Astra's counterexample uses P(D|K) = 0.8 versus P(D|¬G) = 0.2, which is a reasonable theological reading, not a contrived one.

**Forensic.** K = "the CFO had access to the memo but no desire to profit." Access without motive gives you no particular reason to expect third-party accounts positioned around the CFO's interests. So P(F,E | K) ≈ P(F,E | ¬G) is fairly natural, and the premise is roughly what a compliance analyst would accept anyway.

The word-for-word swap changed the referents, and the referents are what determine whether the premise is credible. A model that reasons about content *should* respond differently. That is the intended function of domain knowledge, not a distortion of it.

### The question is ambiguous between validity and soundness

"Is its central assertion True or False?" plus "can confirm or deny that their own understanding compels them to agree" can be read two ways:

- **(a) Validity:** does the conclusion follow from the stated inequalities?
- **(b) Soundness:** is the assertion actually true?

In the forensic case, (a) and (b) both give True, because the premises are plausible. In the theological case, (a) gives True and (b) gives False. Models defaulting to (b) will therefore split exactly as observed, with no domain bias at all.

Your controls support this reading rather than undercutting it:

- Grok voting False on THEO-CONVERSE shows it accepts the conditional math in the theological domain.
- Its False on the main item is therefore a judgment about premise truth, not a failure to follow the argument.
- That is a consistent position: valid, but not sound.

### Where there is a genuine residual signal

Astra's forensic answers carry essentially the same caveat as its theological answers ("saying that K 'provides no explanation' does not establish b ≤ c"), yet it outputs True. In the theological case it outputs False.

So there *is* an asymmetry in how a stated caveat gets mapped to a verdict. It is the most interesting thing in your data. But two explanations are still open:

- **Bias:** a lower charity threshold for theology.
- **Calibrated weighting:** the caveat matters more when the violation is likely (theology) than when it is merely possible (forensic).

The current design cannot tell these apart.

### Statistical caveats

- n = 3 per cell for most OpenAI conditions is very thin.
- gpt-5.6-sol is near-null on forensic as well (3/6), so it does not fit the "double standard" story.
- Pooling pilot and main runs should be reported separately or justified.

## 2. Does this validate the "Faculty Lounge Effect"?

Not yet. The current evidence is compatible with three hypotheses:

1. **Domain bias:** theology triggers hyper-skepticism regardless of premise quality.
2. **Content-sensitive soundness judgment:** the theological K-premise is in fact weaker, and models notice.
3. **Framing ambiguity:** the validity/soundness ambiguity resolves differently when premises differ in plausibility.

Only (1) is the effect you want to claim, and the design does not separate it from (2) and (3).

There is also a conceptual point. Skepticism toward a premise that is actually doubtful is not a cognitive distortion. To show a double standard, you must show different treatment of premises of *equal* evidential standing. Your own original framing ("asymmetric charitable reading threshold") is the right target. The experiment needs to hold premise quality fixed in order to hit it.

## 3. Designing TheologyBench to measure the effect rigorously

Aim for *robust and falsifiable* rather than "undeniable." A design that cannot return a null result will not persuade skeptical reviewers.

### A. Split every item into three separate questions

1. **Validity:** "Assuming exactly the stated inequalities, does the conclusion follow?" The ground truth is mathematical.
2. **Premise plausibility:** "How plausible is P(F,E|K) ≤ P(F,E|¬G) given ordinary background knowledge?" Use a 1–7 rating.
3. **Overall verdict:** the current question.

A Faculty Lounge Effect would show up as either:
- lower validity scores for theology, which would be a clear failure of formal reasoning, or
- lower overall verdicts for theology *after controlling for the model's own plausibility ratings*, which would be an asymmetric mapping.

If theology differs only on plausibility, there is no bias; you have found a substantive disagreement.

### B. Cross domain with premise plausibility

Use a 2 × 2 × 2 design: Domain (theo / secular) × K-premise (plausible / implausible) × Premise status (stipulated as given / argued via narrative).

Build the cells deliberately:

- **Forensic, implausible K.** Make K plausibly generate F, for example "had access, and wanted to hedge personal exposure," which also produces aligned third-party positions. If models say False here too, the theological False is principled.
- **Theological, plausible K.** Narrow K by stipulation (e.g., "a God indifferent to creatures") so the premise becomes reasonable. If models still say False, that is evidence of bias.
- **Stipulated condition.** Add "Treat these inequalities as true." This isolates pure charity and validity.

### C. Add more than two domains

Include:

- other low-prior or contested hypotheses (aliens, the simulation hypothesis, a lab-origin claim, parapsychology), to separate "theology" from "contested metaphysics" or "low prior";
- religious-adjacent but non-theistic content;
- **atheistic arguments of identical structure** (e.g., an evidential argument from evil formalized the same way).

The last one matters most. If models are equally strict on pro-atheist versions, the effect is "strict on religion-related conclusions in both directions." That is a different and more defensible finding than anti-theistic bias.

### D. Use paraphrase families

Write 5–10 surface paraphrases per cell, written by different people. This prevents results from riding on one text's quirks. For example, your forensic translation has its own inco