# Paper 02 Full-Scale Execution Plan

## Current Claim

The current paper argues that a realized grasp failure should be represented as a counterfactual contact field: the minimum physically executable contact edit that would cross a mechanical success boundary. The existing evidence is a symmetric two-contact planar pinch counterexample. It proves that scalar magnitude labels can assign identical scores to failures that need opposite signed repairs. Existing runnable evidence includes 20,000 sampled failed cases and a 30-seed parameter stress suite.

The v2 narrowed claim is honest but too small for the new batch standard: signed mechanical margins exactly recover the field in the toy model, so the paper must not claim that all scalar or gradient information fails. The defensible final claim should be: scalar terminal labels and scalar magnitude scores erase executable repair direction and contact allocation; counterfactual fields make that lost action information explicit, auditable, and evaluable under contact constraints.

## Main Gaps

- The current mechanics are symmetric and two-contact only.
- Signed-margin projection is an upper bound but not analyzed deeply enough as hostile prior art.
- There is no multi-contact allocation study, so "field" currently means one signed difference rather than a real contact-indexed vector.
- There is no actuator/travel-limit study showing when a field is infeasible or should become a repair set.
- There is no biased-data study; scalar global-sign repair can look strong when repair signs are imbalanced, so balanced and worst-group metrics are needed.
- There is no noise or parameter-mismatch study for contact coordinates, friction/load estimates, or margin calibration.
- There is no baseline family between scalar labels and oracle fields: nearest-contact repair, uniform repair, signed scalar projection, noisy signed margin, gradient projection, learned linear repair, and contact-mask variants should be compared.
- The manuscript is only about six pages and lacks the expanded related work, protocol detail, failure taxonomy, tables, and appendices expected of a final 25-page version.

## Target Experiment Expansion

Build a RAM-light full-scale runner, probably `experiments/run_full_scale_fields.py`, that streams compact per-run metrics to `results/full_scale/` and writes paper-ready tables/figures. The runner should preserve the existing symmetric experiment as a sanity check and add these suites:

1. General linear contact-balance suite:
   - State has multiple contact edit coordinates.
   - Success is a signed balance interval `|target - w^T y| <= h`.
   - The counterfactual field is the minimum weighted-norm projection onto the interval under active contact coordinates.
   - Sweep 2, 3, 4, and 6 contact coordinates with unequal weights/costs.

2. Scalar insufficiency suite:
   - Generate same-score pairs and clusters with opposite repair signs and different repair allocations.
   - Report sign entropy, allocation entropy, and minimum field disagreement after scalarization.

3. Strong baseline suite:
   - no repair;
   - scalar random sign;
   - scalar global majority sign;
   - scalar trained sign prior;
   - signed scalar margin projection;
   - nearest-contact-only repair;
   - uniform repair across contacts;
   - noisy signed-margin projection;
   - full counterfactual field;
   - oracle constrained field when actuator masks and limits are known.

4. Biased distribution suite:
   - Vary repair-sign imbalance from balanced to 95/5.
   - Report accuracy, balanced accuracy, minority-group success, worst-group success, and expected repair effort.
   - Show that scalar majority sign can look good on average while failing the minority repair direction.

5. Contact-mask and actuator-limit suite:
   - Randomly block subsets of contacts or impose asymmetric travel limits.
   - Evaluate whether the unconstrained field remains feasible, whether constrained projection repairs the grasp, and when no one-step feasible repair exists.
   - Report "field infeasible" as a first-class outcome instead of hiding it as controller failure.

6. Noise and mismatch suite:
   - Add contact-coordinate noise, load/torque estimate error, friction/radius mismatch, and weight/cost mismatch.
   - Compare exact field, signed margin, noisy signed margin, and scalar baselines.
   - Report where fields become brittle and where conservative margins help.

7. Large seeded stress suite:
   - Use many seeds and compact streamed metrics, not in-memory trajectories.
   - Randomize contact count, contact weights, repair costs, friction/load margin, actuator masks, sign imbalance, and noise.
   - Target tens or hundreds of thousands of cases if runtime stays reasonable; prefer sequential streaming over memory-heavy arrays.

## Figures And Tables

Main figures should include:

- Same scalar score with opposite repair vectors.
- Full-scale baseline success and balanced success.
- Multi-contact field allocation examples.
- Biased-distribution worst-group failure plot.
- Noise/mismatch heatmap.
- Actuator-mask feasibility/failure map.
- Large stress-suite distribution of success, effort, and margin after repair.

Main or appendix tables should include:

- Baseline definitions and information access.
- Full-scale leaderboard with success, balanced success, minority success, infeasible rate, mean repair effort, and post-repair margin.
- Stress-suite aggregate table.
- Noise/mismatch boundary table.
- Contact-mask feasibility table.
- Tuning or prior-selection table for scalar/global baselines.
- Artifact map tying every claim to a generated CSV/figure/table.

## Writing Expansion Strategy

The final manuscript should be a real full-scale simulation/mechanism paper, not a padded version of the toy result. Expand:

- introduction around repair objects versus prediction labels;
- related work around grasp quality, tactile servoing/regrasp, counterfactual explanations, action-conditioned repair, and differentiable mechanics;
- formal setup for counterfactual contact fields, repair sets, feasible actions, costs, and scalarizations;
- propositions for scalar magnitude insufficiency and for signed-margin sufficiency in the linear model;
- experimental protocol with suite definitions and baseline information budgets;
- results that emphasize where the field helps, where signed mechanics matches it, and where constraints/noise make it fail;
- limitations: no hardware, linearized mechanics, no slip dynamics, no learned tactile estimator, synthetic distributions;
- appendices for derivations, baseline equations, stress-suite details, generated tables, and reproducibility.

## Page-Count Strategy

Target at least 26 pages to clear the 25-page gate with margin. Main text should carry the core claim and strongest figures. Appendices should carry derivations, suite descriptions, baseline equations, boundary tables, failure taxonomy, and artifact map. Do not use blank pages or formatting tricks. Length must come from new experiments, proofs, baselines, tables, figures, and honest limitations.

## RAM-Light Strategy

- Stream per-case or per-batch metrics to CSV.
- Keep only small example sets for plots.
- Use deterministic seeded generators.
- Aggregate metrics online where possible.
- Avoid raw trajectory dumps.
- Use standard library plus existing lightweight dependencies unless a dependency is already present and necessary.
- Add `--summarize-only` so figures/tables can be regenerated from existing CSVs.

## Final Acceptance Checklist

- Existing v2 evidence reproduced.
- Full-scale runner implemented with streamed outputs.
- Full-scale suites completed or intentionally scaled to fit runtime without reducing experimental quality.
- Generated figures and tables copied into `paper/`.
- Manuscript rewritten into a final, honest 25+ page paper.
- Local PDF compiled and verified at 25+ pages.
- PDF text checked to ensure it is the paper, not an audit/status document.
- No PDF copied to Downloads before the final gate.
- Final PDF copied to `C:\Users\wangz\Downloads\02.pdf` only after final verification.
- Docs/logs/reproducibility materials updated.
- Local generated `paper/main.pdf` removed after final copy.
- Repo committed and pushed clean before moving to Paper 03.

## 2026-06-21 VLA Highlight Addendum

- Explicit VLA-v4 boxed-link policy added to `paper/main.tex`.
- Final artifact remains `C:\Users\wangz\Downloads\02.pdf`.
- Verified final PDF: 26 pages, 883,125 bytes, SHA256 `CB74476B2C5C663057880B01E80C4854F674D45209F36DBDE48B98AB71B0EC59`.
- Verified link inventory: 33 annotations; green = 25, red = 8, cyan = 0; all borders `(0, 0, 1)`.
- Rendered and visually inspected all link-bearing pages: 2, 3, 4, 5, 7, 9, 15, and 18.
- Verified zero malformed page-edge rectangles, no duplicate `2.pdf`, and no leftover local `paper/main.pdf`.
