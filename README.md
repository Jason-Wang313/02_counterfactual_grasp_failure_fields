# Counterfactual Grasp Failure Fields

This repository contains paper 02 from the robotics/embodied-intelligence batch.

The working thesis is that a realized robot grasp failure should be represented as a counterfactual contact field: the minimum physically executable change in contact locations or forces that would cross a mechanical success boundary. The runnable evidence is intentionally small and mechanistic. It uses a 2D quasi-static pinch model to show that identical scalar failure scores can require opposite contact repairs.

## Reproduce the evidence

```powershell
python experiments/run_counterfactual_fields.py --n 20000 --seed 2
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

## Literature artifacts

The retry run reuses the existing OpenAlex-based sweep:

- `docs/related_work_matrix.csv` has 14,429 entries.
- `docs/literature_map.md` summarizes the 1000-paper landscape, 300-paper serious skim, and 225-paper deep-read tiers.
- `docs/hostile_prior_work.md` records the 100-paper hostile prior set.

## Scope

This is not a real-robot validation. The experiment is a counterexample and proof-of-concept for the representational claim that scalar failure labels can erase repair direction.

Submission-hardening v2 adds a signed-margin projection upper bound and a 30-seed parameter stress test. The narrowed claim is that scalar magnitude labels lose executable repair direction; signed mechanical margins can recover the field in the toy model.
