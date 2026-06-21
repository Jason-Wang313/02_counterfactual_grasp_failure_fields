# Final Audit

## 1. Chosen thesis

Robot grasp failures should be modeled as counterfactual contact fields: for each realized failed contact state, estimate the minimum physically executable contact edit that would cross a mechanical success boundary.

## 2. Field assumption broken

The broken assumption is that a scalar grasp success/failure score is a sufficient object for repair. The final manuscript shows three distinct losses from scalar terminal or magnitude labels:

- signed repair direction is erased;
- contact allocation is erased when multiple coordinates can share the repair;
- feasibility is hidden when active-contact masks or actuator/travel limits make some repairs impossible.

## 3. New central mechanism

The central mechanism is a contact-indexed minimum-cost projection from a failed contact state to the nearest feasible contact state. In the original 2D pinch model, this field has the closed form `dy_right = g/2`, `dy_left = -g/2`, where `g = e - sign(e) h`. In the v3 full-scale pass, the same idea is generalized to a linear contact-balance family with contact weights, repair costs, active masks, travel limits, biased repair-sign distributions, and noisy/mismatched margin estimates.

## 4. Genuine novelty

The paper does not claim novelty for force closure, grasp quality, tactile slip detection, tactile servoing, or generic counterfactual explanations. The defensible novelty boundary is the explicit representation of a realized failed grasp as an executable counterfactual contact field rather than a terminal scalar label or post hoc feature explanation.

The final v3 manuscript is careful about the signed-mechanics upper bound: a calibrated signed mechanical margin/projection can exactly recover the field in the linear model. The claim is therefore not that analytic gradients or signed mechanics fail. The claim is that scalar terminal labels and scalar magnitude scores discard repair direction, allocation, and feasibility information that the field representation keeps explicit and auditable.

## 5. Closest hostile prior work

Closest hostile areas:

- analytic grasp quality and force-closure metrics;
- tactile regrasp and tactile servoing;
- tactile grasp stability prediction and slip detection;
- counterfactual explanation methods.

Specific hostile examples in `docs/hostile_prior_work.md` include `Tactile Regrasp: Grasp Adjustments via Simulated Tactile Transformations`, `Grip Stabilization of Novel Objects Using Slip Prediction`, `Measurement of shear and slip with a GelSight tactile sensor`, and `Reactive Slip Control in Multifingered Grasping`.

## 6. Literature coverage

The retry artifacts validated a metadata-level OpenAlex sweep with 14,429 rows in `docs/related_work_matrix.csv`, including a 1000-paper landscape tier, 300-paper serious skim tier, 225-paper deep-read tier, and 100-paper hostile prior-work set. This is broad metadata coverage, not a claim of exhaustive manual full-text review.

## 7. Proof/formal-claim status

The manuscript proves a narrow scalar-insufficiency proposition for a symmetric two-contact planar pinch family. The final claim remains a counterexample and diagnostic representation claim. It is not a theorem that all scalar classifiers, all gradients, all learned tactile policies, or all signed analytic margins fail.

## 8. Strongest evidence

Original reproducible evidence:

- Command: `python experiments/run_counterfactual_fields.py --n 20000 --seed 2`
- Feasible failed cases: 20,000
- Counterfactual field one-step success: 1.0
- Signed-margin projection one-step success: 1.0
- Scalar random-sign one-step success: 0.5059
- Scalar global-sign one-step success: 0.50415
- Repair-sign entropy after scalarization: 0.99995 bits
- Same-score paired examples in `results/same_score_pairs.csv` show equal scalar failure scores with opposite contact-difference edits.

Full-scale v3 evidence:

- Command: `python experiments/run_full_scale_fields.py`
- Fast regeneration path: `python experiments/run_full_scale_fields.py --summarize-only`
- Total streamed baseline rows: 253,080
- Linear contact grid: scalar magnitude-only baselines remain near chance at 48.9 percent to 50.3 percent; counterfactual field and exact signed-margin projection reach 100.0 percent.
- Biased scalar grid: scalar global-sign repair reaches 95.1 percent average success at a 0.95 positive-sign prior but has 0.0 percent worst-group success.
- Mask/limit grid: constrained field success is 93.5 percent overall; the 6.5 percent gap is reported as infeasible rather than counted as a hidden repair win. The hardest tested cell reaches 19.0 percent infeasibility.
- Noise/mismatch grid: noisy signed-margin projection loses the one-step guarantee because boundary-targeted repairs have no slack.
- Large stress suite: counterfactual field and signed-margin projection reach 96.0 percent success; nearest-contact repair reaches 79.4 percent, uniform signed repair 63.3 percent, scalar random-sign 46.9 percent, scalar global-sign 68.3 percent average with 0.0 percent worst-group success, and scalar prior-sample 61.6 percent.

## 9. Biggest weaknesses

- No real-robot validation.
- The final simulator is still a linearized contact-balance model, not 3D compliant grasping with full friction-cone geometry.
- Contact compliance, object pose uncertainty, rolling contacts, high-speed slip, sensor calibration, and tactile image formation are not modeled.
- A true differentiable mechanical margin with signed contact coordinates can reproduce the field by projection in this model; the contribution is representation and auditability, not domination over exact mechanics.
- The noisy-margin experiments show that boundary-targeted one-step repair is brittle when the margin estimate is mismatched.
- Bibliography is representative and hostile-set guided, but not exhaustive manual full-text coverage.

## 10. Paper-readiness judgment

Final under the current batch standard as a 26-page simulation/mechanism paper with a full-scale experimental pass, stronger baselines, ablations, stress tests, feasibility accounting, figures, tables, limitations, and reproducibility details.

It remains not hardware-ready and should not be described as a real-robot validation. For a top robotics venue, the honest next step would be real tactile/hardware evidence or a higher-fidelity 3D contact simulator. Under this batch's final-version gate, Paper 02 is complete and may be moved forward.

## 11. Exact Downloads PDF path

`C:/Users/wangz/Downloads/02.pdf`

Verified with `pdfinfo` after final copy: 26 pages, 883,125 bytes.

Verified with `pdftotext`: the Downloads PDF is the actual paper, beginning with `Counterfactual Grasp Failure Fields`, and includes the final abstract with the 253,080 streamed baseline evaluations.

2026-06-21 VLA highlight-hardening verification:

- SHA256: `CB74476B2C5C663057880B01E80C4854F674D45209F36DBDE48B98AB71B0EC59`
- Link annotations: 33 total on pages `[(2, 25), (3, 1), (4, 2), (5, 1), (7, 1), (9, 1), (15, 1), (18, 1)]`
- Colors: green = 25, red = 8, cyan = 0
- Borders: `(0, 0, 1)` for all annotations
- Oversized page-edge annotation audit: 0 malformed rectangles
- Visual audit: pages 2, 3, 4, 5, 7, 9, 15, and 18 rendered and inspected
- Cleanup: no duplicate `C:/Users/wangz/Downloads/2.pdf`; local `paper/main.pdf` removed after export

Marker check on the Downloads PDF passed for: `253,080`, `96.0`, `0.0% worst-group`, `Counterfactual Grasp Failure Fields`, `scalar`, `field`, and `claim`.

## 12. GitHub URL

`https://github.com/Jason-Wang313/02_counterfactual_grasp_failure_fields`

## 13. Desktop copy status

No Desktop copy is required for the current batch standard. The canonical final artifact is the exact numbered Downloads PDF above.

## 14. Build and recovery notes

- `latexmk` was unavailable in practice because MiKTeX could not find Perl.
- Recovery path: compiled successfully with direct `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` passes.
- Final local build was copied to `C:/Users/wangz/Downloads/02.pdf` only after the manuscript cleared the 25-page gate.
- The generated `paper/main.pdf` is removed after final copy so the numbered Downloads PDF remains the final PDF artifact.
