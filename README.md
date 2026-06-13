# Counterfactual Grasp Failure Fields

This repository contains paper 02 from the robotics/embodied-intelligence batch.

The working thesis is that a realized robot grasp failure should be represented as a counterfactual contact field: the minimum physically executable change in contact locations or forces that would cross a mechanical success boundary. The original evidence used a 2D quasi-static pinch model to show that identical scalar failure scores can require opposite contact repairs. The full-scale v3 evidence generalizes this to a linear contact-balance family with multiple contacts, biased repair-sign distributions, active-contact masks, travel limits, noise, and stronger baselines.

## Reproduce the evidence

```powershell
python experiments/run_counterfactual_fields.py --n 20000 --seed 2
python experiments/run_full_scale_fields.py
python experiments/run_full_scale_fields.py --summarize-only
```

Key outputs are written to `results/`:

- `counterfactual_field_summary.json`
- `counterfactual_field_cases.csv`
- `same_score_pairs.csv`
- `seed_stress_summary.csv`
- `stress_summary.json`
- `same_score_opposite_repairs.png`
- `repair_success_rates.png`
- `pair_failure_fields.png`
- `stress_success_rates.png`
- `full_scale/full_scale_summary.json`
- `full_scale/leaderboard.csv`
- `full_scale/linear_contact_grid.csv`
- `full_scale/biased_scalar_grid.csv`
- `full_scale/mask_limit_grid.csv`
- `full_scale/noise_mismatch_grid.csv`
- `full_scale/large_seed_stress.csv`
- `paper/figures/*.png`
- `paper/tables/*.tex`

## Literature artifacts

The retry run reuses the existing OpenAlex-based sweep:

- `docs/related_work_matrix.csv` has 14,429 entries.
- `docs/literature_map.md` summarizes the 1000-paper landscape, 300-paper serious skim, and 225-paper deep-read tiers.
- `docs/hostile_prior_work.md` records the 100-paper hostile prior set.

## Scope

This is not a real-robot validation. The final v3 paper is a 26-page full-scale simulation/mechanism manuscript. The narrowed claim is that scalar terminal labels and scalar magnitude scores erase executable direction, allocation, and feasibility information. Signed calibrated mechanics can recover the field in the linear model; the field representation makes that repair object explicit and auditable.
