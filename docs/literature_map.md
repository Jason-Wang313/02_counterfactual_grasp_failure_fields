# Literature Map

## Retrieval protocol
The sweep queried OpenAlex works metadata with 46 query strings spanning robotic grasping, tactile perception, contact mechanics, failure prediction, counterfactual reasoning, and contact-rich manipulation. Rows were deduplicated by normalized title, abstracts were reconstructed from OpenAlex inverted indices when available, and all rows were scored with transparent keyword/citation/recency heuristics. The CSV is a landscape map rather than a claim of manual full-text review for all 1000 entries.

## Coverage summary
- Total entries in `docs/related_work_matrix.csv`: 14429
- Serious skim tier: first 300 rows by relevance.
- Deep-read tier: first 225 rows by relevance.
- Hostile prior-work tier: top 100 rows by hostile score.

## Field box
This paper stays inside robot grasping and tactile/contact-rich manipulation. The core field box is the intersection of:
- analytic grasp mechanics and force closure,
- learned grasp-quality/outcome prediction,
- tactile perception for contact localization, slip, and stability,
- failure detection and recovery in robot manipulation,
- counterfactual/causal representations only when the counterfactual variable is a physically executable robot contact intervention.

## Cluster counts
- `learning`: 5285
- `general-robotics`: 4297
- `planning-control`: 4268
- `dexterous`: 2500
- `tactile`: 1724
- `failure`: 1452
- `3d-perception`: 1413
- `simulation`: 1253
- `counterfactual`: 858
- `contact-field`: 171
- `grasp-quality`: 131

## Recent year distribution snapshot
- 2013: 354
- 2014: 461
- 2015: 456
- 2016: 576
- 2017: 636
- 2018: 796
- 2019: 993
- 2020: 1145
- 2021: 1340
- 2022: 1281
- 2023: 1741
- 2024: 1292
- 2025: 544
- 2026: 210
- unknown: 5

## Top landscape entries by relevance
| rank | paper | year | venue | tags | score |
| --- | --- | --- | --- | --- | --- |
| 1 | Grasping and tactile servoing of deformable objects | 2023 | theses.fr (ABES) | grasp-quality;tactile;failure;learning;planning-control;simulation;dexterous;3d-perception | 87.994 |
| 2 | TacFR-Gripper: A Reconfigurable Fin-Ray-Based Gripper with Tactile Skin for In-Hand Manipulation | 2024 | Actuators | tactile;failure;planning-control;dexterous | 85.083 |
| 3 | TacFR-Gripper: A Reconfigurable Fin Ray-Based Compliant Robotic Gripper with Tactile Skin for In-Hand Manipulation | 2023 | arXiv (Cornell University) | tactile;failure;learning;planning-control;dexterous | 82.312 |
| 4 | Grasp planning methodology for 3d arbitrary shaped objects | 2009 | Dialnet (Universidad de la Rioja) | grasp-quality;tactile;failure;contact-field;planning-control;dexterous;3d-perception | 81.344 |
| 5 | A Sensory Soft Robotic Gripper Capable of Learning-Based Object Recognition and Force-Controlled Grasping | 2022 | IEEE Transactions on Automation Science and Engineering | tactile;failure;learning;planning-control;dexterous | 80.611 |
| 6 | Adaptive Grasping of Moving Objects through Tactile Sensing | 2021 | Sensors | tactile;failure;contact-field | 74.006 |
| 7 | Robot Grasping System and Grasp Stability Prediction Based on Flexible Tactile Sensor Array | 2021 | Machines | tactile;learning;planning-control | 72.111 |
| 8 | NeuralTouch: Neural Descriptors for Precise Sim-to-Real Tactile Robot Control | 2026 | IEEE/ASME Transactions on Mechatronics | tactile;contact-field;learning;planning-control;simulation;dexterous;3d-perception | 70.9 |
| 9 | TacPalm: A Soft Gripper With a Biomimetic Optical Tactile Palm for Stable Precise Grasping | 2024 | IEEE Sensors Journal | tactile;planning-control | 70.575 |
| 10 | Learning Fine Pinch-Grasp Skills using Tactile Sensing from A Few Real-world Demonstrations | 2023 | arXiv (Cornell University) | tactile;learning;dexterous | 69.998 |
| 11 | Efficient Tactile Sensing-based Learning from Limited Real-world Demonstrations for Dual-arm Fine Pinch-Grasp Skills | 2024 | article | tactile;learning;dexterous | 69.556 |
| 12 | Measurement of shear and slip with a GelSight tactile sensor | 2015 | article | tactile;failure;dexterous | 67.708 |
| 13 | Robotic Manipulation of Environmentally Constrained Objects Using Underactuated Hands | 2017 | Scholarship@Western (Western University) | grasp-quality;tactile;failure;planning-control;dexterous | 67.337 |
| 14 | Design and Calibration of a Force/Tactile Sensor for Dexterous Manipulation | 2019 | Sensors | tactile;failure;dexterous | 66.056 |
| 15 | Tactile Dexterity: Manipulation Primitives with Tactile Feedback | 2020 | preprint | tactile;failure;planning-control;dexterous | 64.91 |
| 16 | Data-driven Tactile Sensing using Spatially Overlapping Signals | 2020 | article | tactile;failure;learning;planning-control;dexterous;3d-perception | 64.025 |
| 17 | Grasping Force Control of Multi-Fingered Robotic Hands through Tactile Sensing for Object Stabilization | 2020 | Sensors | tactile;learning;planning-control;dexterous | 63.549 |
| 18 | T-TD3: A Reinforcement Learning Framework for Stable Grasping of Deformable Objects Using Tactile Prior | 2024 | IEEE Transactions on Automation Science and Engineering | tactile;failure;learning;planning-control;simulation;dexterous | 63.394 |
| 19 | Modelling and Control for Soft Finger Manipulation and Human-Robot Interaction | 2010 | Università degli Studi di Napoli Federico II | planning-control;simulation;dexterous | 63.27 |
| 20 | Learning to estimate incipient slip with tactile sensing to gently grasp objects | 2024 | article | tactile;failure;learning;planning-control;3d-perception | 63.16 |
| 21 | On-Orbit Robotic Grasping of a Spent Rocket Stage: Grasp Stability Analysis and Experimental Results | 2021 | Frontiers in Robotics and AI | simulation;dexterous | 62.654 |
| 22 | MetaGraspNetV2: All-in-One Dataset Enabling Fast and Reliable Robotic Bin Picking via Object Relationship Reasoning and Dexterous Grasping | 2023 | IEEE Transactions on Automation Science and Engineering | learning;simulation;dexterous;3d-perception | 61.765 |
| 23 | Grasp Planning Pipeline for Robust Manipulation of 3D Deformable Objects with Industrial Robotic Hand + Arm Systems | 2020 | Applied Sciences | contact-field;planning-control;simulation;dexterous;3d-perception | 61.044 |
| 24 | On Alternative Uses of Structural Compliance for the Development of Adaptive Robot Grippers and Hands | 2019 | Frontiers in Neurorobotics | grasp-quality;planning-control;dexterous | 60.651 |
| 25 | Learning-Based Slip Detection for Dexterous Manipulation Using GelStereo Sensing | 2023 | IEEE Transactions on Neural Networks and Learning Systems | tactile;failure;learning;planning-control;dexterous;3d-perception | 60.587 |

## Hidden assumptions that may be false
1. A failed grasp can be adequately summarized by a scalar success/failure label.
2. The right corrective action can be recovered from the gradient or saliency of a scalar classifier.
3. Pre-contact geometry is a sufficient statistic for post-contact repair.
4. Tactile patches are observations, not variables in the action-repair space.
5. Friction is either known, fixed, or absorbed by robust training.
6. Contact locations are measured accurately enough that contact ambiguity is secondary.
7. Compliance and local deformation do not change the topology of the repair problem.
8. Object pose remains effectively fixed while tactile evidence is gathered.
9. The same failure score implies the same repair priority across objects.
10. A high-dimensional learned representation preserves contact-indexed causal variables.
11. Failure recovery is a policy problem rather than a representation problem.
12. Slip detection is enough to decide how to move contacts before catastrophic failure.
13. Counterfactual explanations over pixels/features correspond to executable robot interventions.
14. Force closure labels are useful even when they do not specify a minimal contact edit.
15. Dense grasp affordances do not need to represent the failed contact state that produced them.
16. Closed-loop grasping can treat previous failures as independent trials.
17. Contact normal, tangential direction, and normal force can be collapsed without losing repair direction.
18. Training data contains enough paired failures and successful repairs to learn the right intervention directly.
19. Multi-contact failures decompose into independent per-finger corrections.
20. A grasp simulator's success boundary has the same local geometry as real tactile failure boundaries.
21. Explanations should explain model decisions rather than the physical failure boundary.
22. Benchmark accuracy is an adequate proxy for repair usefulness.
23. A failure detector does not need to be contrastive against nearby successful contact configurations.
24. A planned grasp's identity is its pose, not its realized contact field.

## Candidate directions that break assumptions
### Counterfactual Grasp Failure Fields
- Broken assumption: Failure labels are enough; contact patches are only observations.
- Central mechanism: Represent each failed grasp as a contact-indexed field of minimal physically executable contact displacements that would restore force closure.
- Novelty pressure: Changes the object of modeling from outcome classification to contact-space repair geometry.

### Failure-Boundary Tactile Servoing
- Broken assumption: A tactile controller can be trained from successful demonstrations alone.
- Central mechanism: Estimate the local tangent/normal of the success boundary from failed tactile rollouts and servo along the normal.
- Novelty pressure: Interesting, but closer to existing tactile servoing and active correction work.

### Ambiguity-Aware Contact Attribution
- Broken assumption: Tactile localization is exact enough for grasp diagnosis.
- Central mechanism: Propagate contact localization ambiguity through wrench-space repair sets.
- Novelty pressure: Useful supporting analysis, but risks becoming an uncertainty wrapper.

### Counterfactual Friction Patches
- Broken assumption: Friction can be fixed in grasp quality labels.
- Central mechanism: Infer spatial friction edits that would flip failure to success.
- Novelty pressure: Mechanically grounded, but narrower and more material-estimation centered.


## Working conclusion
The strongest direction is `Counterfactual Grasp Failure Fields`: treat a realized failed grasp as a contact field and model the lowest-cost contact-field change that would cross the force-closure boundary. This makes the mechanism central, not a post hoc explanation attached to a classifier. It also creates a falsifiable distinction: two grasps can share the same scalar failure probability while requiring opposite repairs.
