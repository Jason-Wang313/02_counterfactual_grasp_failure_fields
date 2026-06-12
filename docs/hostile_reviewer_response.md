# Hostile Reviewer Response

## Likely Decision

Workshop accept / main-conference reject unless expanded with 3D, tactile, or hardware evidence.

## Core Responses

| Reviewer Objection | Response in v2 |
|---|---|
| This is grasp quality with gradients. | Conceded for the toy model: signed margin projection matches the field. The claim is scalar-magnitude insufficiency. |
| The result is just a missing sign bit. | Conceded. The missing sign is the executable contact-direction variable that scalar magnitude labels erase. |
| The simulator is synthetic. | Conceded. Added 30-seed stress but kept workshop-only decision. |
| Tactile servoing already fixes grasps. | The paper is about represented repair objects, not claiming first tactile servo controller. |
| Counterfactual explanations already exist. | The paper restricts counterfactuals to executable contact edits and a mechanical success set. |
| A biased dataset could make scalar global sign work better. | True. The paper reports sign entropy and does not claim arbitrary distribution behavior. |

## Claims We Should Not Make

- Do not claim real-robot readiness.
- Do not claim all scalar or gradient methods fail.
- Do not claim generic novelty for counterfactual explanations.
- Do not claim 3D or compliant-contact generality.
