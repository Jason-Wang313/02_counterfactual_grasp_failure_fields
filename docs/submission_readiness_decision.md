# Submission Readiness Decision

Paper: 02_counterfactual_grasp_failure_fields

Decision: final under the current batch standard; simulation/mechanism paper; not hardware-ready.

Date: 2026-06-13 18:30:00 +01:00

## Rationale

The v3 paper is now a 26-page full-scale manuscript rather than the earlier short counterexample. It includes the original 2D pinch proof, a linear contact-balance generalization, 253,080 streamed baseline evaluations, biased-distribution tests, contact-mask and actuator-limit stress, noise/mismatch tests, stronger scalar and allocation baselines, paper-ready figures/tables, explicit limitations, and reproducibility details.

The claim is intentionally narrow and honest. Scalar terminal labels and scalar magnitude scores discard repair direction, contact allocation, and feasibility information. A calibrated signed mechanical projection can recover the field in this model, so the paper does not claim that signed analytic mechanics fails.

The paper is not real-robot or high-fidelity 3D contact evidence. For a top robotics target, the next step would be hardware or a richer contact simulator. Under the current batch requirement, Paper 02 satisfies the final-version gate.

## Terminal Condition

Paper 02 is complete for this batch once the final 26-page PDF is verified at `C:/Users/wangz/Downloads/02.pdf`, repo docs/logs are updated, and the final repo state is committed and pushed.

## 2026-06-21 VLA Highlight Gate

Passed. The canonical PDF at `C:/Users/wangz/Downloads/02.pdf` remains 26 pages and now has an explicit VLA-v4 boxed-link policy in source.

- Size: 883,125 bytes
- SHA256: `CB74476B2C5C663057880B01E80C4854F674D45209F36DBDE48B98AB71B0EC59`
- Link annotations: 33 total; green = 25, red = 8, cyan = 0
- Link-bearing pages: `[(2, 25), (3, 1), (4, 2), (5, 1), (7, 1), (9, 1), (15, 1), (18, 1)]`
- Border widths: `(0, 0, 1)` for all annotations
- Visual audit: pages 2, 3, 4, 5, 7, 9, 15, and 18 rendered and inspected
- Cleanup: zero malformed page-edge annotations, no duplicate `2.pdf`, and no local `paper/main.pdf`
