# Hostile Reviewer Response

## Likely Decision

Final under the current batch standard as a simulation/mechanism paper. A top robotics or robot-learning submission would still need real tactile hardware evidence or higher-fidelity 3D compliant contact simulation.

## Core Responses

| Reviewer Objection | Response in v3 |
|---|---|
| This is grasp quality with gradients. | Conceded for calibrated signed mechanics: exact signed-margin projection matches the field in the linear model. The contribution is scalar-label insufficiency and explicit executable repair representation. |
| The result is just a missing sign bit. | The 2D pinch proof exposes a sign loss; the v3 linear family also tests contact allocation, active masks, travel limits, bias, and noise. |
| The simulator is synthetic. | Conceded. The final manuscript reports 253,080 streamed baseline evaluations but does not claim hardware validation. |
| Tactile servoing already fixes grasps. | The paper is about represented repair objects and audits, not a claim to be the first tactile servo controller. |
| Counterfactual explanations already exist. | The paper restricts counterfactuals to executable contact edits that cross a mechanical success set. |
| A biased dataset could make scalar global sign work better. | True on average. The v3 biased grid shows high average scalar success at strong priors but 0.0 percent worst-group success for the minority repair sign. |
| The field fails under contact masks or travel limits. | The manuscript reports infeasible cases explicitly rather than hiding them as successful repairs. |
| Noisy signed margins can fail too. | Conceded and measured; boundary-targeted one-step repair has no slack under mismatch. |

## Claims We Should Not Make

- Do not claim real-robot readiness.
- Do not claim all scalar or gradient methods fail.
- Do not claim generic novelty for counterfactual explanations.
- Do not claim 3D or compliant-contact generality.
- Do not claim the field dominates exact signed mechanics in this model.
