# Full-Scale Results Summary

## Final Gate

- Final manuscript target for this pass: at least 25 pages of real content.
- Verified local build before Downloads copy: 26 pages.
- No intermediate PDF was copied to Downloads before the final gate.
- 2026-06-21 canonical PDF after VLA boxed-link hardening: `C:/Users/wangz/Downloads/02.pdf`, 26 pages, 883,125 bytes, SHA256 `CB74476B2C5C663057880B01E80C4854F674D45209F36DBDE48B98AB71B0EC59`.
- Final link inventory: 33 annotations; green = 25, red = 8, cyan = 0; all borders `(0, 0, 1)`; zero malformed page-edge rectangles.

## Full-Scale Run

- Runner: `python experiments/run_full_scale_fields.py`
- Fast regeneration path: `python experiments/run_full_scale_fields.py --summarize-only`
- Total streamed baseline rows: 253,080
- Raw trajectories saved: no
- Claim scope: linearized contact-balance simulation, not hardware validation.

## Suite Rows

- `linear_contact_grid.csv`: 60,480 baseline rows
- `biased_scalar_grid.csv`: 45,000 baseline rows
- `mask_limit_grid.csv`: 57,600 baseline rows
- `noise_mismatch_grid.csv`: 36,000 baseline rows
- `large_seed_stress.csv`: 54,000 baseline rows

## Headline Findings

- Linear contact grid: scalar magnitude-only baselines remain near chance; counterfactual field and exact signed-margin projection reach 100.0%.
- Biased scalar grid: scalar global-sign repair reaches 95.1% average success at a 0.95 positive-sign prior but has 0.0% worst-group success.
- Large stress suite: counterfactual field and signed-margin projection reach 96.0% success; the missing 4.0% is reported as actuator/mask infeasibility.
- Contact allocation matters: uniform signed repair reaches 63.3% in the stress suite, nearest-contact repair 79.4%, field 96.0%.
- Noise matters: noisy signed-margin projection loses its one-step guarantee because boundary-targeted repair has no slack.

## Generated Paper Artifacts

- `paper/figures/full_scale_success_leaderboard.png`
- `paper/figures/effort_success_pareto.png`
- `paper/figures/bias_worst_group_curve.png`
- `paper/figures/mask_limit_feasibility_map.png`
- `paper/figures/noise_mismatch_success.png`
- `paper/figures/pair_failure_fields.png`
- `paper/tables/full_scale_leaderboard.tex`
- `paper/tables/baseline_access_table.tex`
- `paper/tables/bias_worst_group_table.tex`
- `paper/tables/mask_feasibility_table.tex`
- `paper/tables/noise_boundary_table.tex`

## Visual Delivery Check

- VLA-style boxed links are explicitly pinned in `paper/main.tex`.
- Link-bearing pages rendered and inspected: 2, 3, 4, 5, 7, 9, 15, and 18.
- Visual result matches the visible VLA-v4 role model: green citation/URL boxes and red internal-reference boxes, with no cyan boxes.
- No local `paper/main.pdf` remains after export, and no duplicate non-canonical `2.pdf` exists in Downloads.
