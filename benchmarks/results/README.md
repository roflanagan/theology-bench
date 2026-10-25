# TheologyBench Results & Pre-Revision Peer-Review Archive

This directory contains the summary scores, raw per-trial model transcripts, and historical pre-revision peer reviews for [`TheologyBench`](../../README.md).

---

## 1. Final 14-Item Benchmark Data & Raw Transcripts

- **[`theologybench_14item_summary.json`](theologybench_14item_summary.json):** Per-item accuracy, raw trial counts, overall scores (`0–100%`), and Secular–Theological gaps ($\Delta_{\text{MAIN}}$ and $\Delta_{\text{MARS}}$, in percentage points) across all 15 API models on the finalized 14-item directionally balanced battery.
- **[`fact2x2_theo_vs_forensic.json`](fact2x2_theo_vs_forensic.json):** Full transcripts of the $2 \times 2$ factorial comparison (`THEO` vs. `FORENSIC` $\times$ `Answer-First` vs. `Reason-First`).
- **[`tight_4_results.json`](tight_4_results.json):** Raw per-trial responses for all 15 API models on the tightened `THEO-MARS` (`True`), `FORENSIC-MARS` (`True`), `CTRL-REVERSED-K` (`True`), and `CTRL-POSTERIOR-TRAP` (`False`) items.
- **[`all_battery_results.json`](all_battery_results.json) & [`new_6_items_results.json`](new_6_items_results.json):** Raw per-trial responses across the core items and formal confirmation-theory controls.
- **[`v3_narrow_k_results.json`](v3_narrow_k_results.json):** Raw transcripts testing the `v3` seed text with the $K$-partition loophole explicitly closed ([`AI_Religion_seed.txt` lines 62–66](../../AI_Religion_seed.txt#L62-L66)).
- **[`atheo_results.json`](atheo_results.json):** Raw transcripts for the 82-line Pro-Atheist / Evolutionary-Debunking Isomorph (`ATHEO`).

---

## 2. Historical Pre-Revision Audits & Peer Reviews (All Points Resolved in Final 14-Item Release)

> [!IMPORTANT]
> The four `.md` files below are **historical pre-revision reviews** conducted on earlier developmental drafts (`Round 1`: the `v2` 8-item draft; `Round 2`: the 12-item draft) *before* the finalized 14-item `TheologyBench` suite was frozen. They are preserved in the repository for complete methodological transparency. **Every critique raised in these pre-revision reviews was addressed and tested prior to the final 14-item release:**

| Pre-Revision Document | Draft Reviewed | Key Recommendations & How They Were Resolved in the Final 14-Item Release |
| :--- | :---: | :--- |
| **[`claude_opus_5_5_audit.md`](claude_opus_5_5_audit.md)** | Round 1 (`v2` 8-item draft) | 1. **Close the $K$-partition loophole:** Resolved in `v3` ([`AI_Religion_seed.txt` lines 62–66](../../AI_Religion_seed.txt#L62-L66) & [`forensic-control-seed.txt` lines 62–66](../forensic-control-seed.txt#L62-L66)) and verified in [`v3_narrow_k_results.json`](v3_narrow_k_results.json).<br>2. **Test stipulated mathematical likelihoods without narrative inference:** Resolved via `THEO-MARS` vs. `FORENSIC-MARS` ([`tight_4_results.json`](tight_4_results.json)).<br>3. **Test a pro-atheist argument of identical structure:** Resolved via `ATHEO` ([`atheo_results.json`](atheo_results.json)). |
| **[`gpt6_astra_audit_concession.md`](gpt6_astra_audit_concession.md)** | Round 1 (`v2` 8-item draft) | Confirmed the asymmetric evaluation standard between `THEO-RF` and `FORENSIC-RF` and recommended explicit numerical partition/posterior controls (`CTRL-PARTITION`, `CTRL-POSTERIOR-TRAP`, `CTRL-REVERSED-K`), all added to [`items.json`](../items.json). |
| **[`claude_opus_5_5_peer_review.md`](claude_opus_5_5_peer_review.md)** | Round 2 (12-item draft) | 1. **Tighten `THEO-MARS` & `FORENSIC-MARS` ($0 < P(H\mid F) < 1$, joint independence of $M$ from $(F,H)$, `"no later than"`) and re-run from scratch:** Resolved in [`items.json`](../items.json) and [`tight_4_results.json`](tight_4_results.json).<br>2. **Add counter-directional controls (`True` against thesis, `False` overclaiming for thesis):** Added `CTRL-REVERSED-K` (`True`) and `CTRL-POSTERIOR-TRAP` (`False`).<br>3. **Replace `CLICHE-*` / `THEO-CONVERSE` labels and reframe neutrally:** Resolved in [`items.json`](../items.json) and [`README.md`](../../README.md). |
| **[`gpt6_astra_peer_review.md`](gpt6_astra_peer_review.md)** | Round 2 (12-item draft) | Independently recommended the same three structural fixes as `Claude Opus 5.5` (repairing and re-running `THEO-MARS`/`FORENSIC-MARS`, adding counter-directional controls to form the 14-item suite, and neutralizing item/metric names to report `Secular–Theo Gap` in percentage points). All implemented in the final 14-item release. |
| **[`ai_council_14item_audit.json`](ai_council_14item_audit.json)** | Round 3 (5-Model AI Council Audit of the 14-item release: `Claude Opus 5.5`, `GPT-6 Astra`, `Grok 4.7`, `Qwen 3.8 Max`, `GLM-5.3`) | 1. **Explicit stream-wide joint independence in `THEO-MARS` & `FORENSIC-MARS`:** Added `"and remains jointly independent of (D, H) across any accumulated evidence stream D (with e(D->H) > 0 and 0 < P(H|D) < 1)"` to [`items.json`](../items.json) and re-evaluated all 15 API models ([`tight_4_results.json`](tight_4_results.json) & [`theologybench_14item_summary.json`](theologybench_14item_summary.json)), achieving `100%` (`3/3 True`) across all 16 models on both items.<br>2. **Harden [`run_benchmark.py`](../run_benchmark.py) verdict parser & exception handling:** Replaced substring regex fallback with instruction-stripping, abstention-safe `parse_verdict_with_source`, prioritized `content` over `reasoning`, added per-trial exception handling, and set `"reasoning": {"effort": "medium"}`.<br>3. **Fix minor wording/table discrepancies:** Updated `CTRL-POSTERIOR-TRAP` setup inequality (`e(D->H) > e(D->G) (with e(D->H) > 0)`) and matched the `F` substitution-table row in [`README.md`](../../README.md) verbatim to [`forensic-control-seed.txt`](../forensic-control-seed.txt). |
