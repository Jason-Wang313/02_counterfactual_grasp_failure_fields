# Submission Version Log

| Version | Date | Changes | PDF |
|---|---|---|---|
| v1 | 2026-06-10 | Generated batch paper with 2D pinch counterexample and initial PDF. | `C:/Users/wangz/Downloads/02.pdf` |
| v2 | 2026-06-12 | Added signed-margin upper bound, 30-seed parameter stress suite, stress figure, narrowed claims, visible hardening note, and submission-readiness docs. | `C:/Users/wangz/Downloads/02.pdf` |
| v3 | 2026-06-13 | Expanded to a 26-page full-scale simulation manuscript with 253,080 streamed baseline evaluations, linear multi-contact fields, biased scalar grids, mask/limit infeasibility, noise/mismatch studies, stronger baselines, generated tables/figures, and updated reproducibility docs. | `C:/Users/wangz/Downloads/02.pdf` |

## v2 Evidence Delta

- `results/seed_stress_summary.csv`: 30 parameter seeds.
- `results/stress_summary.json`: stress means and 95 percent confidence intervals.
- `results/stress_success_rates.png`: stress plot.
- `results/counterfactual_field_summary.json`: now includes signed-margin projection success and stress links.

## v3 Evidence Delta

- `experiments/run_full_scale_fields.py`: full-scale streamed runner plus summarize-only path.
- `results/full_scale/full_scale_summary.json`: 253,080 streamed baseline rows, no raw trajectories.
- `results/full_scale/leaderboard.csv`: aggregate metrics by suite and baseline.
- `paper/figures/full_scale_success_leaderboard.png`: large stress-suite success.
- `paper/figures/bias_worst_group_curve.png`: scalar majority failure under biased repair signs.
- `paper/figures/mask_limit_feasibility_map.png`: field infeasibility under contact masks and tight limits.
- `paper/figures/noise_mismatch_success.png`: noisy signed-margin degradation.
- `paper/tables/*.tex`: generated full-scale leaderboard, bias, mask, noise, and baseline information tables.
- Final local PDF build verified at 26 pages, copied to `C:/Users/wangz/Downloads/02.pdf`, and re-verified there before removing the local build artifact.
