# Reviewer Attacks

## Attack 1: This is just grasp quality with gradients.
Response: A grasp-quality score says whether a candidate is good. A failure field is contact-indexed and asks for the minimal physical contact edit that crosses the success boundary. In the toy analytic model, projecting the true signed margin onto the feasible set recovers the same field; v2 now includes this signed-margin upper bound explicitly. The novelty claim is not "gradients can never work" but "a scalar magnitude label/score alone is an insufficient object for repair because same-score failures can require opposite executable contact edits."

## Attack 2: Tactile servoing already repairs grasps.
Response: Tactile servoing is the broad control objective. The proposed mechanism is a representation of failure as a counterfactual contact field. A controller can use it, but the paper is not claiming first tactile correction.

## Attack 3: Force closure already defines success.
Response: Force closure is the success predicate used here, not the novelty. The novelty is turning a failed realized contact configuration into the lowest-cost contact-field edit relative to that predicate.

## Attack 4: The evidence is synthetic.
Response: Correct. The paper is framed as a mechanism/proof-of-concept and counterexample paper. v2 adds 30 parameter-stress seeds, but the strongest empirical statement is still limited to a 2D quasi-static pinch simulator; real-robot validation remains future work.

## Attack 5: Counterfactual explanations are known.
Response: Existing counterfactuals often edit features or pixels. This paper restricts counterfactual variables to executable contact displacements/forces/normals and evaluates mechanical validity.

## Attack 6: A learned policy could implicitly learn this.
Response: Possibly, but implicit repair does not expose the failure boundary or same-score/opposite-repair ambiguity. The contribution is an explicit contact-field object that can audit and guide policies.

## Attack 7: The field may be non-unique.
Response: Non-uniqueness is a limitation and a useful signal. The method should report a repair set or minimum-norm representative; ambiguous sets are more honest than a scalar label.

## Attack 8: The 2D proof does not generalize to 3D.
Response: The proof is a counterexample to scalar sufficiency, not a full 3D theorem. The 3D extension is a research path, not an established result.

## Attack 9: OpenAlex query sweep misses key papers.
Response: Likely. The audit should mark literature coverage as broad metadata-level coverage, plus hostile curated additions, not exhaustive guarantee.

## Attack 10: The field is expensive to compute.
Response: The paper can present the field as an optimization target and use approximate/neural amortization as future work. Runtime is measured in the provided simulator only.

## Attack 11: You are only proving that a sign bit was lost.
Response: Mostly yes in the symmetric toy model, and v2 says so. The point is that the missing sign is an executable contact-direction variable, not a cosmetic label. The paper should use this as a clean counterexample rather than inflate it into a general impossibility theorem.

## Attack 12: A biased dataset would let a global scalar policy do better than chance.
Response: True. The current sampled family is deliberately balanced to isolate representation insufficiency. `results/seed_stress_summary.csv` reports the sign fraction and entropy for each stress seed; the paper should not claim chance performance for arbitrary deployment distributions.
