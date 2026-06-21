# Submission Attack Log

Paper: 02_counterfactual_grasp_failure_fields

Hardening version: v3
Date: 2026-06-13 18:35:00 +01:00

## Attack Rounds

| Round | Attack | Action | Residual Risk |
|---:|---|---|---|
| 1 | This is just grasp quality with gradients. | Added signed-margin projection upper bound and kept it in v3 as an exact-mechanics reference. | Analytic signed mechanics matches the field in the linear model, so the claim must stay representational. |
| 2 | The result is only a missing sign bit. | Kept the 2D proof but expanded v3 to allocation, masks, limits, bias, and noise. | The minimal proof remains intentionally simple. |
| 3 | One seed is not enough. | Added original 30-seed stress and v3 full-scale streamed suites. | Still synthetic. |
| 4 | Scalar baselines are too weak. | Added random sign, global sign, prior-sample sign, noisy signed margin, uniform signed allocation, and nearest-contact allocation. | No learned policy baseline. |
| 5 | Dataset balance makes scalar policies look bad. | Added biased repair-sign grid and worst-group reporting. | Biased deployment can improve average scalar success while still hiding minority repairs. |
| 6 | No hardware. | Kept as explicit limitation in paper and docs. | Non-recoverable locally. |
| 7 | 2D pinch does not generalize to 3D. | Added linear multi-contact contact-balance family, but did not claim 3D compliant generality. | No high-fidelity 3D contact simulator. |
| 8 | Counterfactual explanations already exist. | Narrowed to executable contact edits, not generic feature explanations. | Recent explainability work remains hostile. |
| 9 | Tactile servoing already repairs grasps. | Clarified representation vs controller distinction. | Real tactile policies may implicitly learn repairs. |
| 10 | Non-unique fields are hidden. | Added weighted/costed projection and contact-allocation baselines; discussion still notes repair-set generalization. | Full repair-set representation not implemented. |
| 11 | Feasibility failures are hidden. | Added active-mask and travel-limit suite with infeasible cases reported explicitly. | Real actuators/friction would need richer constraints. |
| 12 | Signed margins are brittle under noise. | Added noise/mismatch suite and reported degradation honestly. | Robust control with slack is future work. |
| 13 | Venue fit is weak. | Reclassified as final for the current batch's simulation/mechanism-paper standard, not hardware-ready. | Top robotics path still needs real tactile or richer simulation evidence. |
| 14 | PDF link boxes must visually match the visible VLA-v4 role model. | Added explicit hyperref boxed-link policy, rebuilt, rendered all link-bearing pages, and verified green citation/URL boxes plus red internal-reference boxes. | Visual style is verified for this artifact; future source edits must preserve the policy. |

## Stop Condition

The v3 pass completed the recoverable local scope: full-scale streamed experiments, stronger baselines, ablations, stress tests, paper-ready figures/tables, a 26-page final manuscript, and explicit limitations. Remaining concerns require external hardware or a different simulator rather than more local polishing.

The 2026-06-21 VLA highlight-hardening pass completed visual delivery scope: `C:/Users/wangz/Downloads/02.pdf` is 26 pages, 883,125 bytes, SHA256 `CB74476B2C5C663057880B01E80C4854F674D45209F36DBDE48B98AB71B0EC59`, with 33 role-model-style link annotations and zero malformed page-edge rectangles.
