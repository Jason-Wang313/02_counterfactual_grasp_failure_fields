# Experiment Rigor Checklist

| Item | Status | Evidence |
|---|---|---|
| Deterministic main experiment | Done | `results/counterfactual_field_summary.json`. |
| Original multi-seed stress | Done | `results/seed_stress_summary.csv`, 30 seeds. |
| Full-scale streamed evaluation | Done | `results/full_scale/*.csv`, 253,080 compact baseline rows. |
| Linear contact-balance generalization | Done | `results/full_scale/linear_contact_grid.csv`. |
| Biased repair-sign stress | Done | `results/full_scale/biased_scalar_grid.csv`; global scalar can reach high average success but fails the minority group. |
| Active-mask and travel-limit stress | Done | `results/full_scale/mask_limit_grid.csv`; infeasible cases reported explicitly. |
| Noise/mismatch stress | Done | `results/full_scale/noise_mismatch_grid.csv`; noisy signed margins lose the one-step guarantee. |
| Strong upper-bound baseline | Done | Exact signed-margin projection included and reported as matching the field when mechanics are calibrated. |
| Scalar baselines | Done | Random sign, global sign, prior-sample sign, noisy signed margin, uniform signed allocation, and nearest-contact allocation. |
| Uncertainty/aggregation | Done | Per-suite aggregation in `results/full_scale/full_scale_summary.json`, `leaderboard.csv`, and paper tables. |
| Failure/ambiguity examples | Done | `results/same_score_pairs.csv`; `paper/figures/pair_failure_fields.png`. |
| Paper-ready figures/tables | Done | `paper/figures/` and `paper/tables/`. |
| VLA boxed-link visual audit | Done | Final `C:/Users/wangz/Downloads/02.pdf`; 33 link annotations, green = 25, red = 8, cyan = 0; rendered pages 2, 3, 4, 5, 7, 9, 15, and 18. |
| Final artifact cleanup | Done | Canonical `02.pdf` only; no duplicate `2.pdf`; transient `paper/main.pdf` removed. |
| Hardware validation | Missing | Explicit limitation; not claimed. |
| 3D/compliant simulation | Missing | Explicit limitation; not claimed. |
| Claims narrowed to evidence | Done | Paper, final audit, readiness decision, and results summary updated. |

## Rigor Decision

Adequate for the current batch's final simulation/mechanism-paper standard. Still not a real-robot validation and not a substitute for high-fidelity 3D contact evidence.

2026-06-21 delivery metadata: 26 pages, 883,125 bytes, SHA256 `CB74476B2C5C663057880B01E80C4854F674D45209F36DBDE48B98AB71B0EC59`.
