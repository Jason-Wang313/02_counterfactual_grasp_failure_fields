# Novelty Decision

## Chosen thesis
Robot grasp failures should be modeled as counterfactual contact fields: for each realized failed contact configuration, estimate the lowest-cost spatial change in contact locations/forces/normals that would cross the mechanical success boundary.

## Why this direction wins
The seed survives the hostile literature because it changes the modeled object. Existing work usually asks `will this grasp succeed?`, `where should I grasp?`, or `did slip/failure occur?`. The proposed paper asks `what contact-field edit would have made this failed grasp succeed?` This turns failure from a terminal class label into a repairable geometric object.

## Candidate comparison
| direction | assumption broken | mechanism | decision pressure |
| --- | --- | --- | --- |
| Counterfactual Grasp Failure Fields | Failure labels are enough; contact patches are only observations. | Represent each failed grasp as a contact-indexed field of minimal physically executable contact displacements that would restore force closure. | Changes the object of modeling from outcome classification to contact-space repair geometry. |
| Failure-Boundary Tactile Servoing | A tactile controller can be trained from successful demonstrations alone. | Estimate the local tangent/normal of the success boundary from failed tactile rollouts and servo along the normal. | Interesting, but closer to existing tactile servoing and active correction work. |
| Ambiguity-Aware Contact Attribution | Tactile localization is exact enough for grasp diagnosis. | Propagate contact localization ambiguity through wrench-space repair sets. | Useful supporting analysis, but risks becoming an uncertainty wrapper. |
| Counterfactual Friction Patches | Friction can be fixed in grasp quality labels. | Infer spatial friction edits that would flip failure to success. | Mechanically grounded, but narrower and more material-estimation centered. |

## Rejected weak moves
- Bigger model: rejected because scale would not change the scalar-label bottleneck.
- Better data: rejected because paired failures/successes still need a representation of the repair variable.
- New benchmark only: rejected because the paper needs a mechanism.
- Add uncertainty: rejected unless uncertainty is over the contact-field repair set; uncertainty alone is not central.
- Add active learning: rejected because it does not define what a failure is.
- Add verifier: rejected because force-closure verification is old; the novelty is the counterfactual field.
- Combine modules: rejected because tactile plus grasp quality is already common.
- LLM planner: out of scope for contact mechanics and not needed.
- Reinforcement learning: out of scope for the core representational claim.

## Final decision
Proceed with `Counterfactual Grasp Failure Fields` and demonstrate it in a controlled 2D grasp mechanics simulator. The runnable evidence now shows that scalar failure scores conflate repair directions in symmetric paired failures, while the counterfactual field identifies the minimum contact change and repairs all feasible failed examples in one step in this simulator.

## Evidence status
- Experiment command: `python experiments/run_counterfactual_fields.py --n 20000 --seed 2`
- Feasible failed cases: 20,000
- Counterfactual field one-step repair success: 1.0
- Scalar-only random-sign one-step repair success: 0.5059
- Scalar-only global-sign one-step repair success: 0.50415
- Repair-sign entropy after scalarization: 0.99995 bits
- Scope: 2D quasi-static pinch counterexample, not real-robot validation.
