# Submission Attack Log

Paper: 02_counterfactual_grasp_failure_fields

Hardening version: v2
Date: 2026-06-12 19:22:00 +01:00

## Attack Rounds

| Round | Attack | Action | Residual Risk |
|---:|---|---|---|
| 1 | This is just grasp quality with gradients. | Added signed-margin projection upper bound and narrowed claims. | High; analytic signed margin matches field in toy model. |
| 2 | The result is only a missing sign bit. | Conceded explicitly in paper and docs. | The contribution is small but clean. |
| 3 | One seed is not enough. | Added 30-seed randomized parameter stress test. | Still synthetic. |
| 4 | Scalar baselines are too weak. | Added scalar global sign and signed-margin upper bound. | No learned scalar policy baseline. |
| 5 | Dataset balance makes scalar policies look bad. | Logged sign fraction and entropy per stress seed. | Biased deployment distributions may differ. |
| 6 | No hardware. | Marked `workshop-only`. | Non-recoverable locally. |
| 7 | 2D pinch does not generalize to 3D. | Kept proof as counterexample only. | No 3D simulation. |
| 8 | Counterfactual explanations already exist. | Narrowed to executable contact edits, not generic feature explanations. | Recent explainability work remains hostile. |
| 9 | Tactile servoing already repairs grasps. | Clarified representation vs controller distinction. | Real tactile policies may implicitly learn repairs. |
| 10 | Non-unique fields are hidden. | Kept discussion that richer settings should report repair sets. | Not implemented. |
| 11 | Reproducibility lacks stress outputs. | README and paper now list stress CSV/JSON. | No locked environment. |
| 12 | Venue fit is weak. | Marked workshop-only / strong-revise for main conference. | Main-conference path needs real data. |

## Stop Condition

Stopped before 50 rounds because recoverable issues converged on the same boundary: the toy result is a scalar-magnitude insufficiency counterexample, not a deployment-ready tactile grasp repair method. Recoverable stress, baseline, documentation, and claim-scope fixes were completed.
