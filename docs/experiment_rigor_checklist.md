# Experiment Rigor Checklist

| Item | Status | Evidence |
|---|---|---|
| Deterministic main experiment | Done | `results/counterfactual_field_summary.json`. |
| Multiple seeds | Done | `results/seed_stress_summary.csv`, 30 seeds. |
| Parameter stress | Done | Half-width, normal force, friction, weight, and finger travel limit varied. |
| Stronger upper-bound baseline | Done | Signed-margin projection, success 1.0. |
| Scalar baselines | Partial | Random-sign and global-sign scalar magnitude baselines. |
| Uncertainty estimates | Done | 95 percent CI in `results/stress_summary.json`. |
| Failure/ambiguity examples | Done | `results/same_score_pairs.csv`. |
| Hardware validation | Missing | Non-recoverable in this local repo. |
| 3D/compliant simulation | Missing | Non-recoverable without a larger simulator. |
| Claims narrowed to evidence | Done | Paper, claims ledger, and final audit updated. |

## Rigor Decision

Adequate for a workshop counterexample paper. Not adequate for a main robotics or ICLR submission.
