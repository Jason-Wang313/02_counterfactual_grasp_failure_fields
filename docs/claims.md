# Claims

## Supported by literature map
1. Grasp quality prediction, force-closure analysis, visual grasp synthesis, tactile slip/stability estimation, and closed-loop grasping are heavily covered areas.
2. Many methods output scalar quality/failure labels or dense grasp candidates rather than a contact-indexed counterfactual repair field.
3. Tactile/contact observations are often used as inputs to estimators or controllers, but not usually made the counterfactual variable itself.

## Supported by runnable evidence
1. Same scalar failure score can correspond to opposite minimal contact repairs in the 2D pinch model. `results/same_score_pairs.csv` contains pairs with identical scalar scores 0.78245 and 0.94685 whose required contact-difference edits have opposite signs.
2. In 20,000 feasible failed grasps sampled from the 2D model, the analytic counterfactual field repaired 100.0% in one step, while scalar-only policies that know failure magnitude but guess repair sign succeeded at 50.59% with random sign and 50.415% with the global-majority sign.
3. The repair sign remains almost maximally ambiguous after scalarization in the balanced simulator: repair-sign entropy is 0.99995 bits and the positive repair fraction is 0.49585.
4. A signed-margin projection upper bound repairs 100.0% in one step, matching the field in this symmetric toy model. This narrows the claim to scalar magnitude labels, not all scalar mechanical quantities.
5. Across 30 randomized parameter seeds with 3,000 feasible failures per seed, the field and signed-margin projection have mean one-step success 1.0, while scalar random-sign repair is 0.4983 +/- 0.0029 and scalar global-sign repair is 0.5073 +/- 0.0020.

## Formal claims
The manuscript may claim and prove a narrow insufficiency result:
For the symmetric two-contact grasp family, any deterministic repair rule that factors a failed state only through a scalar invariant of the absolute wrench-balance error must assign the same repair to paired states with errors `+e` and `-e`, even though their minimum-norm stabilizing contact fields have opposite signs. Therefore the scalar representation is insufficient for one-step deterministic repair on that family.

The proof is a counterexample to scalar-magnitude sufficiency, not a theorem that all scalar classifiers, signed mechanical margins, or score gradients fail.

## Unsupported or deliberately modest claims
1. No real-robot claim unless new real hardware data are added.
2. No claim that the proposed field outperforms all learned tactile policies.
3. No claim that the 2D simulator fully captures deformable, compliant, or high-speed contact.
4. No claim that OpenAlex metadata equals exhaustive manual full-text review.
5. No claim that a differentiable analytic margin cannot reproduce the field by projection; in the toy model, the field is exactly the constrained minimum-norm projection onto the success boundary.
6. No claim that the stress suite is a substitute for real tactile hardware or 3D contact dynamics.
