# Novelty Boundary Map

## What is not novel
- Predicting grasp success or grasp quality from visual, tactile, or fused features.
- Using force closure, wrench-space metrics, Ferrari-Canny-style quality, or analytic labels.
- Closed-loop grasping and tactile servoing as broad objectives.
- Slip detection, tactile contact localization, and tactile grasp-state estimation.
- Counterfactual explanations if the counterfactual variables are generic image/features instead of executable contact changes.
- Generating dense grasp poses or contact affordance maps from point clouds.

## Proposed boundary
The paper is only novel if its central object is a `failure field`: a contact-indexed, physically executable, minimal displacement/force edit that maps a realized failed contact configuration to a nearby successful one. The field must be useful even when scalar outcome scores are identical, and it must expose repair direction that scalar classifiers or post hoc saliency cannot identify.

## Hostile examples and boundary
| hostile prior | covered territory | remaining boundary |
| --- | --- | --- |
| Grasping and tactile servoing of deformable objects | Using contact mechanics or grasp quality as a stability target. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Measurement of shear and slip with a GelSight tactile sensor | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Grasp planning methodology for 3d arbitrary shaped objects | Using contact mechanics or grasp quality as a stability target. | A learned or computed counterfactual field that maps observed failure contacts to minimal stabilizing contact edits. |
| A Novel Tactile Sensor with Electromagnetic Induction and Its Application on Stick-Slip Interaction Detection | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Robot Grasping System and Grasp Stability Prediction Based on Flexible Tactile Sensor Array | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Grip Stabilization of Novel Objects Using Slip Prediction | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Tactile Sensors for Friction Estimation and Incipient Slip Detection—Toward Dexterous Robotic Manipulation: A Review | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Tactile Regrasp: Grasp Adjustments via Simulated Tactile Transformations | Using contact mechanics or grasp quality as a stability target. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Grasp Stability Prediction with Sim-to-Real Transfer from Tactile Sensing | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Learning to estimate incipient slip with tactile sensing to gently grasp objects | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Reactive Slip Control in Multifingered Grasping: Hybrid Tactile Sensing and Internal-Force Optimization | Using contact mechanics or grasp quality as a stability target. | A learned or computed counterfactual field that maps observed failure contacts to minimal stabilizing contact edits. |
| Tactile Dexterity: Manipulation Primitives with Tactile Feedback | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Hybrid ViViT–TimeSformer Transformer Architecture for Multimodal Slip Detection in Robotic Manipulation | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Implementing tactile behaviors using FingerVision | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Toward tactilely transparent gloves: Collocated slip sensing and vibrotactile actuation | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| BiGS: BioTac Grasp Stability Dataset | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| SCT-CNN: A Spatio-Channel-Temporal Attention CNN for Grasp Stability Prediction | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Enhancing Robotic Grasping Detection Using Visual–Tactile Fusion Perception | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| A Soft Barometric Tactile Sensor to Simultaneously Localize Contact and Estimate Normal Force With Validation to Detect Slip in a Robotic Gripper | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Design of a 3-D Tactile Sensing Array for Incipient Slip Detection in Robotic Dexterous Manipulation | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Learning to Detect Slip through Tactile Estimation of the Contact Force Field and its Entropy | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Perception of partial slips under tangential loading of the fingertip | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Methods and Sensors for Slip Detection in Robotics: A Survey | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| GelSlim3.0: High-Resolution Measurement of Shape, Force and Slip in a Compact Tactile-Sensing Finger | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Multifunctional biomimetic tactile system via a stick-slip sensing strategy for human–machine interactions | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| TacDexGrasp: Compliant and Robust Dexterous Grasping with Tactile Feedback | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Simultaneous Tactile Estimation and Control of Extrinsic Contact | Using contact mechanics or grasp quality as a stability target. | A learned or computed counterfactual field that maps observed failure contacts to minimal stabilizing contact edits. |
| Improving the Representation and Extraction of Contact Information in Vision-based Tactile Sensors Using Continuous Marker Pattern | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Grip Stabilization through Independent Finger Tactile Feedback Control | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |
| Incipient Slip Detection by Vibration Injection into Soft Sensor | Using tactile signals for grasp-state estimation or feedback. | A representation where tactile failure is a contact-field displacement rather than a terminal class label. |

## Novelty test
A prior work collapses the claim if it already does all of the following:
1. starts from realized failed tactile/contact evidence, not only pre-contact geometry;
2. computes or learns a contact-indexed counterfactual field, not just a scalar quality/failure score;
3. grounds the counterfactual in a force-closure or contact-mechanics success boundary;
4. demonstrates that same-score failures require different repairs and that the field resolves the ambiguity.

The hostile set contains many papers satisfying one or two of these conditions, but the retrieved metadata did not reveal a paper satisfying all four.
