# Final Audit

## 1. Chosen thesis

Robot grasp failures should be modeled as counterfactual contact fields: for each realized failed contact state, estimate the minimum physically executable contact edit that would cross a mechanical success boundary.

## 2. Field assumption broken

The broken assumption is that a scalar grasp success/failure score is a sufficient object for repair. In the constructed pinch family, identical scalar failure scores can require opposite signed contact repairs.

## 3. New central mechanism

The central mechanism is a contact-indexed minimum-norm projection from a failed contact state to the nearest wrench-feasible contact state. In the 2D pinch model, this field has the closed form `dy_right = g/2`, `dy_left = -g/2`, where `g = e - sign(e) h`.

## 4. Genuine novelty

The paper does not claim novelty for force closure, grasp quality, tactile slip detection, tactile servoing, or generic counterfactual explanations. The novelty boundary is the explicit representation of a realized failed grasp as an executable counterfactual contact field rather than a terminal scalar label or post hoc feature explanation.

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

The manuscript proves a narrow scalar-insufficiency proposition for a symmetric two-contact planar pinch family. The claim is a counterexample to scalar sufficiency for deterministic one-step repair, not a theorem that all scalar classifiers, all gradients, or all learned tactile policies fail.

## 8. Strongest evidence

Runnable evidence:

- Command: `python experiments/run_counterfactual_fields.py --n 20000 --seed 2`
- Feasible failed cases: 20,000
- Counterfactual field one-step success: 1.0
- Scalar random-sign one-step success: 0.5059
- Scalar global-sign one-step success: 0.50415
- Repair-sign entropy after scalarization: 0.99995 bits
- Same-score paired examples in `results/same_score_pairs.csv` show equal scalar failure scores with opposite contact-difference edits.

## 9. Biggest weaknesses

- No real-robot validation.
- The simulator is quasi-static, planar, and two-contact only.
- Contact compliance, object pose uncertainty, rolling contacts, high-speed slip, and tactile calibration are not modeled.
- A true differentiable mechanical margin with contact coordinates can reproduce the field by projection in this toy model; the claim is about scalar-label sufficiency, not impossibility of analytic gradients.
- Bibliography is representative and hostile-set guided, but not exhaustive manual full-text coverage.

## 10. Paper-readiness judgment

Workshop. The paper is clean as a mechanism/proof-of-concept and counterexample, but it needs real tactile or higher-fidelity simulation evidence before a strong ICLR/robot-learning submission.

## 11. Exact Downloads PDF path

`C:/Users/wangz/Downloads/02.pdf`

Verified with `pdfinfo`: 5 pages, 305,677 bytes.

## 12. GitHub URL

`https://github.com/Jason-Wang313/02_counterfactual_grasp_failure_fields`

## 13. Desktop copy status

`pending orchestrator copy`

The local check found no `C:\Users\wangz\OneDrive\Desktop\02.pdf` at audit time.

## Build and recovery notes

- Latest official ICLR template source found at runtime: ICLR 2026 Author Guide pointing to `https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip`.
- `latexmk` was unavailable in practice because MiKTeX could not find Perl.
- Recovery: compiled successfully with direct `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` passes.
- Final deliverable copied to the exact Downloads path. The generated `paper/main.pdf` and unpacked template archive were removed from the repo tree after delivery so the numbered Downloads PDF is the final PDF artifact.
