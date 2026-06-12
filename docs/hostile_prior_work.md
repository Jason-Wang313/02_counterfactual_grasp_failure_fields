# Hostile Prior Work

This set contains the 100 papers most likely to make the proposed thesis look incremental, selected by contact/grasp/tactile/failure/counterfactual hostile score. Each entry records what it already covers and what remains outside its mechanism.

## 1. Grasping and tactile servoing of deformable objects (2023)
- Venue/authors: theses.fr (ABES); Peng Song
- Problem claimed: Estimate whether a proposed grasp has mechanically stable contact.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using contact mechanics or grasp quality as a stability target.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4398183475

## 2. Measurement of shear and slip with a GelSight tactile sensor (2015)
- Venue/authors: article; Wenzhen Yuan; Rui Li; Mandayam A. Srinivasan; Edward H. Adelson
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W1548071717

## 3. Grasp planning methodology for 3d arbitrary shaped objects (2009)
- Venue/authors: Dialnet (Universidad de la Rioja); Máximo A. Roa
- Problem claimed: Estimate whether a proposed grasp has mechanically stable contact.
- Actual mechanism introduced: Analytic wrench-space/contact mechanics criterion.
- Hidden assumptions: Contacts, friction cones, and object geometry are sufficiently known; stability is mostly captured by instantaneous mechanics.
- Variables treated as fixed: friction coefficient, contact locations, object rigidity, gripper kinematics
- Failure modes ignored: How a failed contact pattern should be minimally changed after real tactile evidence arrives.
- What it makes less novel: Using contact mechanics or grasp quality as a stability target.
- What it leaves open: A learned or computed counterfactual field that maps observed failure contacts to minimal stabilizing contact edits.
- URL/DOI: https://openalex.org/W3011427767

## 4. A Novel Tactile Sensor with Electromagnetic Induction and Its Application on Stick-Slip Interaction Detection (2016)
- Venue/authors: Sensors; Yanjie Liu; Haijun Han; Tao Liu; Jingang Yi; Qingguo Li; Yoshio INOUE
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2306688771

## 5. Robot Grasping System and Grasp Stability Prediction Based on Flexible Tactile Sensor Array (2021)
- Venue/authors: Machines; Tong Li; Xuguang Sun; Xin Shu; Chunkai Wang; Yifan Wang; Gang Chen; Ning Xue
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W3172211430

## 6. Grip Stabilization of Novel Objects Using Slip Prediction (2018)
- Venue/authors: IEEE Transactions on Haptics; Filipe Veiga; Jan Peters; Tucker Hermans
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2803104652

## 7. Tactile Sensors for Friction Estimation and Incipient Slip Detection—Toward Dexterous Robotic Manipulation: A Review (2018)
- Venue/authors: IEEE Sensors Journal; Wei Chen; Heba Khamis; Ingvars Birznieks; Nathan F. Lepora; Stephen J. Redmond
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2892010946

## 8. Tactile Regrasp: Grasp Adjustments via Simulated Tactile Transformations (2018)
- Venue/authors: preprint; Francois R. Hogan; Maria Bauzá; Oleguer Canal; Elliott Donlon; Alberto Rodríguez
- Problem claimed: Estimate whether a proposed grasp has mechanically stable contact.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using contact mechanics or grasp quality as a stability target.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2792953217

## 9. Grasp Stability Prediction with Sim-to-Real Transfer from Tactile Sensing (2022)
- Venue/authors: arXiv (Cornell University); Zilin Si; Zirui Zhu; Arpit Agarwal; Stuart Anderson; Wenzhen Yuan
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4300529843

## 10. Learning to estimate incipient slip with tactile sensing to gently grasp objects (2024)
- Venue/authors: article; Dirk-Jan Boonstra; Laurence Willemet; Jelle Luijkx; Michaël Wiertlewski
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4401413646

## 11. Reactive Slip Control in Multifingered Grasping: Hybrid Tactile Sensing and Internal-Force Optimization (2026)
- Venue/authors: ArXiv.org; Théo Ayral; Saifeddine Aloui; Mathieu Grossard
- Problem claimed: Estimate whether a proposed grasp has mechanically stable contact.
- Actual mechanism introduced: Analytic wrench-space/contact mechanics criterion.
- Hidden assumptions: Contacts, friction cones, and object geometry are sufficiently known; stability is mostly captured by instantaneous mechanics.
- Variables treated as fixed: friction coefficient, contact locations, object rigidity, gripper kinematics
- Failure modes ignored: How a failed contact pattern should be minimally changed after real tactile evidence arrives.
- What it makes less novel: Using contact mechanics or grasp quality as a stability target.
- What it leaves open: A learned or computed counterfactual field that maps observed failure contacts to minimal stabilizing contact edits.
- URL/DOI: https://openalex.org/W7130617408

## 12. Tactile Dexterity: Manipulation Primitives with Tactile Feedback (2020)
- Venue/authors: preprint; Francois R. Hogan; José Ballester; Siyuan Dong; Alberto Rodríguez
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W3005162594

## 13. Hybrid ViViT–TimeSformer Transformer Architecture for Multimodal Slip Detection in Robotic Manipulation (2025)
- Venue/authors: Trepo - Institutional Repository of Tampere University; Tanvir Hasan Shovon
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W7133050621

## 14. Implementing tactile behaviors using FingerVision (2017)
- Venue/authors: article; Akihiko Yamaguchi; Christopher G. Atkeson
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2783627282

## 15. Toward tactilely transparent gloves: Collocated slip sensing and vibrotactile actuation (2009)
- Venue/authors: article; João Marcos Travassos Romano; Stuart R. Gray; Nathan Jacobs; Katherine J. Kuchenbecker
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2115933504

## 16. BiGS: BioTac Grasp Stability Dataset (2016)
- Venue/authors: article; Yevgen Chebotar; Karol Hausman; Zhe Su; Artem Molchanov; Oliver Kroemer; Gaurav S. Sukhatme; Stefan Schaal
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2340307996

## 17. SCT-CNN: A Spatio-Channel-Temporal Attention CNN for Grasp Stability Prediction (2021)
- Venue/authors: article; Gang Yan; Alexander Schmitz; Satoshi Funabashi; Sophon Somlor; Tito Pradhono Tomo; Shigeki Sugano
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W3205355686

## 18. Enhancing Robotic Grasping Detection Using Visual–Tactile Fusion Perception (2026)
- Venue/authors: Sensors; Dongyuan Zheng; Yahong Chen
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W7125150656

## 19. A Soft Barometric Tactile Sensor to Simultaneously Localize Contact and Estimate Normal Force With Validation to Detect Slip in a Robotic Gripper (2022)
- Venue/authors: IEEE Robotics and Automation Letters; Thomas De Clercq; Anatolii Sianov; Guillaume Crevecoeur
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4295308349

## 20. Design of a 3-D Tactile Sensing Array for Incipient Slip Detection in Robotic Dexterous Manipulation (2024)
- Venue/authors: IEEE Transactions on Instrumentation and Measurement; Jianping Yu; Shengjie Yao; Xin Li; Abdul Ghaffar; Zhehe Yao
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.

- URL/DOI: https://openalex.org/W4401163822

## 21. Learning to Detect Slip through Tactile Estimation of the Contact Force Field and its Entropy (2023)
- Venue/authors: arXiv (Cornell University); Xiaohai Hu; Aparajit Venkatesh; Wan, Yusen; Guiliang Zheng; Jawale, Neel; Kaur, Navneet; Xu Chen; Birkmeyer, Paul
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4323066672

## 22. Perception of partial slips under tangential loading of the fingertip (2018)
- Venue/authors: Scientific Reports; Allan Barrea; Benoit P. Delhaye; Philippe Lefèvre; Jean‐Louis Thonnard
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2780233779

## 23. Methods and Sensors for Slip Detection in Robotics: A Survey (2020)
- Venue/authors: IEEE Access; Rocco Antonio Romeo; Loredana Zollo
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W3016926102

## 24. GelSlim3.0: High-Resolution Measurement of Shape, Force and Slip in a Compact Tactile-Sensing Finger (2021)
- Venue/authors: arXiv (Cornell University); Ian Taylor; Siyuan Dong; Alberto Rodríguez
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4285480035

## 25. Multifunctional biomimetic tactile system via a stick-slip sensing strategy for human–machine interactions (2022)
- Venue/authors: npj Flexible Electronics; Yue Li; Manjun Zhao; Yadong Yan; Luanxi He; Yingyi Wang; Zuoping Xiong; Shuqi Wang; Yuanyuan Bai; et al.
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4283009920

## 26. TacDexGrasp: Compliant and Robust Dexterous Grasping with Tactile Feedback (2026)
- Venue/authors: ArXiv.org; Yubin Ke; Jiayi Chen; Hang Lv; Xiao Zhou; He Wang
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W7134860771

## 27. Simultaneous Tactile Estimation and Control of Extrinsic Contact (2023)
- Venue/authors: arXiv (Cornell University); Sangwoon Kim; Devesh K. Jha; Diego Romeres; P. M. Patre; Alberto Rodríguez
- Problem claimed: Estimate whether a proposed grasp has mechanically stable contact.
- Actual mechanism introduced: Analytic wrench-space/contact mechanics criterion.
- Hidden assumptions: Contacts, friction cones, and object geometry are sufficiently known; stability is mostly captured by instantaneous mechanics.
- Variables treated as fixed: friction coefficient, contact locations, object rigidity, gripper kinematics
- Failure modes ignored: How a failed contact pattern should be minimally changed after real tactile evidence arrives.
- What it makes less novel: Using contact mechanics or grasp quality as a stability target.
- What it leaves open: A learned or computed counterfactual field that maps observed failure contacts to minimal stabilizing contact edits.
- URL/DOI: https://openalex.org/W4323572074

## 28. Improving the Representation and Extraction of Contact Information in Vision-based Tactile Sensors Using Continuous Marker Pattern (2023)
- Venue/authors: preprint; Mingxuan Li; Yen Hang Zhou; Tiemin Li; Yao Jiang
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4383723629

## 29. Grip Stabilization through Independent Finger Tactile Feedback Control (2020)
- Venue/authors: Sensors; Filipe Veiga; Benoni B. Edin; Jan Peters
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W3011137165

## 30. Incipient Slip Detection by Vibration Injection into Soft Sensor (2024)
- Venue/authors: arXiv (Cornell University); Naoto Komeno; Takamitsu Matsubara
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4391987682

## 31. Data-driven Tactile Sensing using Spatially Overlapping Signals (2020)
- Venue/authors: article; Pedro Piacenza
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2788427867

## 32. Tactile-Driven Grasp Stability and Slip Prediction (2019)
- Venue/authors: Robotics; Brayan S. Zapata-Impata; Pablo Gil; Fernando Torres
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2976973748

## 33. BaroTac: Barometric Three-Axis Tactile Sensor with Slip Detection Capability (2022)
- Venue/authors: Sensors; Gyuwon Kim; Donghyun Hwang
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4313472102

## 34. Slip Detection and Stable Grasping With Multi‐Fingered Robotic Hand Using Deep Learning Approach (2025)
- Venue/authors: IET Cyber-Systems and Robotics; Haoliang Xu; S. Arshad; Shichi Peng; Han Xu; Hang Yin; Qiang Li
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4416837401

## 35. Grasping Force Control of Multi-Fingered Robotic Hands through Tactile Sensing for Object Stabilization (2020)
- Venue/authors: Sensors; Zhen Deng; Yannick Jonetzko; Liwei Zhang; Jianwei Zhang
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W3006239966

## 36. Slip-actuated bionic tactile sensing system with dynamic DC generator integrated E-textile for dexterous robotic manipulation (2025)
- Venue/authors: Nature Communications; Vashin Gautham; Ashutosh Panpalia; Hamid Manouchehri; Krushang Gabani; Vinoop Anil; Shakunthala Yerneni; Rohit Thakar; Aayush Nayyar; et al.
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4412743782

## 37. Advanced polymer materials‐based electronic skins for tactile and non‐contact sensing applications (2023)
- Venue/authors: InfoMat; F Yin; Hongsen Niu; Eun‐Seong Kim; Young Kee Shin; Yang Li; Nam‐Young Kim
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4379743996

## 38. Ground Truth Force Distribution for Learning-Based Tactile Sensing: A Finite Element Approach (2019)
- Venue/authors: IEEE Access; Carmelo Sferrazza; Adam Wahlsten; Camill Trueeb; Raffaello D’Andrea
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2972319721

## 39. What can be inferred from a tactile arrayed sensor in autonomous in-hand manipulation? (2012)
- Venue/authors: article; Van Anh Ho; Tatsuya Nagatani; Akio Noda; Shinichi Hirai
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2090989197

## 40. Magnetic-based Soft Tactile Sensors with Deformable Continuous Force Transfer Medium for Resolving Contact Locations in Robotic Grasping and Manipulation (2019)
- Venue/authors: Sensors; Alireza Mohammadi; Yangmengfei Xu; Ying Tan; Peter Choong; Denny Oetomo
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2985416885

## 41. Extrinsic Contact Sensing with Relative-Motion Tracking from Distributed Tactile Measurements (2021)
- Venue/authors: article; Daolin Ma; Siyuan Dong; Alberto Rodríguez
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W3205981435

## 42. Tac2Pose: Tactile object pose estimation from the first touch (2023)
- Venue/authors: The International Journal of Robotics Research; Maria Bauzá; Antonia Bronars; Alberto Rodríguez
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4386607259

## 43. Efficient tactile encoding of object slippage (2022)
- Venue/authors: Scientific Reports; Laurence Willemet; Nicolas Huloux; Michaël Wiertlewski
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4289261165

## 44. Contact geometry and mechanics predict friction forces during tactile surface exploration (2018)
- Venue/authors: Scientific Reports; Marco Janko; Michaël Wiertlewski; Yon Visell
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2801107305

## 45. T-TD3: A Reinforcement Learning Framework for Stable Grasping of Deformable Objects Using Tactile Prior (2024)
- Venue/authors: IEEE Transactions on Automation Science and Engineering; Yanmin Zhou; Yiyang Jin; Ping Lu; Shuo Jiang; Zhipeng Wang; Bin He
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4401567816

## 46. Grasping Force Compensation Using a Fingertip Mechanism with Contact Point Estimation (2022)
- Venue/authors: JFPS International Journal of Fluid Power System; Kei Mikami; Kotaro Tadano
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4312559594

## 47. Multidirectional slip detection and avoidance using dynamic 3D tactile meshes from visuotactile sensors (2024)
- Venue/authors: article; Peng Song; Juan Antonio Corrales Ramón; Youcef Mezouar
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4405785399

## 48. Learning-Based Slip Detection for Dexterous Manipulation Using GelStereo Sensing (2023)
- Venue/authors: IEEE Transactions on Neural Networks and Learning Systems; Shaowei Cui; Shuo Wang; Rui Wang; Shaolin Zhang; Chaofan Zhang
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4377971206

## 49. Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation (2025)
- Venue/authors: article; Xue Han; Jieji Ren; Wendi Chen; Gu Zhang; Yuan Fang; Guoying Gu; Huazhe Xu; Cewu Lu
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4414050525

## 50. Visuo-Tactile-Based Slip Detection Using A Multi-Scale Temporal Convolution Network (2023)
- Venue/authors: arXiv (Cornell University); Junli Gao; Zhaoji Huang; Zhaonian Tang; Haitao Song; Wenyu Liang
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4322717192

## 51. TacPalm: A Soft Gripper With a Biomimetic Optical Tactile Palm for Stable Precise Grasping (2024)
- Venue/authors: IEEE Sensors Journal; Xuyang Zhang; Tianqi Yang; Dandan Zhang; Nathan F. Lepora
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4403182289

## 52. ViTacTip: Design and Verification of a Novel Biomimetic Physical Vision-Tactile Fusion Sensor (2024)
- Venue/authors: article; Wen Fan; Haoran Li; Weiyong Si; Shan Luo; Nathan F. Lepora; Dandan Zhang
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4401415473

## 53. Handling shape and contact location uncertainty in grasping two-dimensional planar objects (2007)
- Venue/authors: article; Vassilios N. Christopoulos; Paul Schrater
- Problem claimed: Estimate whether a proposed grasp has mechanically stable contact.
- Actual mechanism introduced: Analytic wrench-space/contact mechanics criterion.
- Hidden assumptions: Contacts, friction cones, and object geometry are sufficiently known; stability is mostly captured by instantaneous mechanics.
- Variables treated as fixed: friction coefficient, contact locations, object rigidity, gripper kinematics
- Failure modes ignored: How a failed contact pattern should be minimally changed after real tactile evidence arrives.
- What it makes less novel: Using contact mechanics or grasp quality as a stability target.
- What it leaves open: A learned or computed counterfactual field that maps observed failure contacts to minimal stabilizing contact edits.
- URL/DOI: https://openalex.org/W2165501312

## 54. A Non-Array Type Cut to Shape Soft Slip Detection Sensor Applicable to Arbitrary Surface (2020)
- Venue/authors: Sensors; Sung Joon Kim; Seung Ho Lee; Hyungpil Moon; Hyouk Ryeol Choi; Ja Choon Koo
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W3096386095

## 55. Improving Robotic Tactile Localization Super-resolution via Spatiotemporal Continuity Learning and Overlapping Air Chambers (2023)
- Venue/authors: Proceedings of the AAAI Conference on Artificial Intelligence; Xuyang Li; Yipu Zhang; Xuemei Xie; Jiawei Li; Guangming Shi
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4382239604

## 56. Passive Static Equilibrium with Frictional Contacts and Application to Grasp Stability Analysis (2018)
- Venue/authors: article; Maximilian Haas-Heger; Christos H. Papadimitriou; Mihalis Yannakakis; Garud Iyengar; Matei Ciocarlie
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Task-specific modeling pipeline for selecting or evaluating robot actions.
- Hidden assumptions: The key state variables needed for the method are observed, fixed, or learnable from the available data.
- Variables treated as fixed: object/task distribution, action space, sensing assumptions
- Failure modes ignored: Structured failure repair and contact-space identifiability.
- What it makes less novel: Robotic grasp evaluation and data-driven manipulation claims.
- What it leaves open: A central mechanism that makes failure repair a physically grounded contact-field object.
- URL/DOI: https://openalex.org/W2806673832

## 57. Manipulation of Unknown Objects to Improve the Grasp Quality Using Tactile Information (2018)
- Venue/authors: Sensors; Andrés Montaño; Raúl Suárez
- Problem claimed: Estimate whether a proposed grasp has mechanically stable contact.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using contact mechanics or grasp quality as a stability target.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2800092299

## 58. Gentle Grasping: A Method With Low-Cost Magnetic Tactile Sensors (2025)
- Venue/authors: IEEE Access; Yi Liu; Remko Proesmans; Andreas Verleysen; Francis wyffels
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4415883200

## 59. Learning Fine Pinch-Grasp Skills using Tactile Sensing from A Few Real-world Demonstrations (2023)
- Venue/authors: arXiv (Cornell University); Xiaofeng Mao; Yucheng Xu; Ruoshi Wen; Mohammadreza Kasaei; Wanming Yu; Efi Psomopoulou; Nathan F. Lepora; Zhibin Li
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4383993617

## 60. A Vision-Based Tactile Sensing System for Multimodal Contact Information Perception via Neural Network (2023)
- Venue/authors: arXiv (Cornell University); Wei Xu; Guoyuan Zhou; Yuanzhi Zhou; Zhibin Zou; Jiali Wang; Wenfeng Wu; Xinming Li
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4387356126

## 61. ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation (2025)
- Venue/authors: article; Jayjun Lee; Nima Fazeli
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4414050430

## 62. Soft Tactile Sensors Having Two Channels With Different Slopes for Contact Position and Pressure Estimation (2023)
- Venue/authors: IEEE Sensors Letters; Hirono Ohashi; Takuto Yasuda; Takumi Kawasetsu; Koh Hosoda
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4366667384

## 63. Assessing Grasp Stability Based on Learning and Haptic Data (2011)
- Venue/authors: IEEE Transactions on Robotics; Yasemin Bekiroglu; Janne Laaksonen; Jimmy Alison Jørgensen; Ville Kyrki; Danica Kragić
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2021473074

## 64. Learning Spatio Temporal Tactile Features with a ConvLSTM for the Direction Of Slip Detection (2019)
- Venue/authors: Sensors; Brayan S. Zapata-Impata; Pablo Gil; Fernando Torres
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2913153715

## 65. Slip Detection With a Biomimetic Tactile Sensor (2018)
- Venue/authors: IEEE Robotics and Automation Letters; Jasper W. James; Nicholas Pestell; Nathan F. Lepora
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2837391606

## 66. Interpreting and predicting tactile signals for the SynTouch BioTac (2021)
- Venue/authors: The International Journal of Robotics Research; Yashraj Narang; Balakumar Sundaralingam; Karl Van Wyk; Arsalan Mousavian; Dieter Fox
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W3119092717

## 67. Flexible Polymer-Ceramic Composite Materials for High Sensitive Pressure Sensing Applications in Harsh Environments (2017)
- Venue/authors: dissertation; Kavin Sivaneri Varadharajan Idhaiam
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W3139487011

## 68. A Sensory Soft Robotic Gripper Capable of Learning-Based Object Recognition and Force-Controlled Grasping (2022)
- Venue/authors: IEEE Transactions on Automation Science and Engineering; Zhanfeng Zhou; Runze Zuo; Binbin Ying; Junhui Zhu; Yong Wang; Xin Wang; Xinyu Liu
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4312384059

## 69. Efficient Tactile Sensing-based Learning from Limited Real-world Demonstrations for Dual-arm Fine Pinch-Grasp Skills (2024)
- Venue/authors: article; Xiaofeng Mao; Yucheng Xu; Ruoshi Wen; Mohammadreza Kasaei; Wanming Yu; Efi Psomopoulou; Nathan F. Lepora; Zhibin Li
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4405787334

## 70. Tactile Imprint Simulation of GelStereo Visuotactile Sensors (2023)
- Venue/authors: article; Shaowei Cui; Yu Wang; Shuo Wang; Qian Li; Rui Wang; Chaofan Zhang
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4386066043

## 71. Inferring Object Properties with a Tactile-Sensing Array Given Varying Joint Stiffness and Velocity (2017)
- Venue/authors: International Journal of Humanoid Robotics; Tapomayukh Bhattacharjee; James M. Rehg; Charles C. Kemp
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2767298308

## 72. HydroelasticTouch: Simulation of Tactile Sensors with Hydroelastic Contact Surfaces (2025)
- Venue/authors: ArXiv.org; David P. Leins; Florian Patzelt; Robert Haschke
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4406449685

## 73. Grasp stability assessment through unsupervised feature learning of tactile images (2017)
- Venue/authors: article; Deen Cockbum; Jean-Philippe Roberge; Thuy-Hong-Loan Le; Alexis Maslyczyk; Vincent Duchaine
- Problem claimed: Estimate whether a proposed grasp has mechanically stable contact.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using contact mechanics or grasp quality as a stability target.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2731057901

## 74. A Biomimetic Tactile Fingerprint Induces Incipient Slip (2020)
- Venue/authors: preprint; Jasper W. James; Stephen J. Redmond; Nathan F. Lepora
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W3049042495

## 75. NeuralTouch: Neural Descriptors for Precise Sim-to-Real Tactile Robot Control (2026)
- Venue/authors: IEEE/ASME Transactions on Mechatronics; Yijiong Lin; Bowen Deng; Chenghua Lu; Max Yang; Efi Psomopoulou; Nathan F. Lepora; Nathan F. Lepora
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4416619993

## 76. CONTACT: CONtact-aware TACTile Learning for Robotic Disassembly (2026)
- Venue/authors: ArXiv.org; Yosuke Saka; Jyun-Chi Hu; Adeesh Desai; Zhiyuan Zhang; B. Zhang; Quan Khanh Luu; Md Rakibul Islam Prince; Minghui Zheng; et al.
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W7134861450

## 77. HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning (2026)
- Venue/authors: arXiv (Cornell University); Amirhosein Alian; Yongqiang Zhao; Shiyi Gu; Xuyang Zhang; Zhuo Chen; Christopher E. Mower; Haitham Bou-Ammar; Shan Luo
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W7163719837

## 78. DexTac: Learning Contact-aware Visuotactile Policies via Hand-by-hand Teaching (2026)
- Venue/authors: Open MIND; Xingyu Zhang; Chaofan Zhang; Boyue Zhang; Zhinan Peng; Shaowei Cui; Shuo Wang
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W7126178018

## 79. MuxGel: Simultaneous Dual-Modal Visuo-Tactile Sensing via Spatially Multiplexing and Deep Reconstruction (2026)
- Venue/authors: ArXiv.org; Zhixian Hu; Zhengtong Xu; Sheeraz Athar; Juan Wachs; Yu She
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W7134992375

## 80. Tactile Perception and Control of a Soft Shear-Sensitive Optical Tactile Sensor ()
- Venue/authors: Bristol Research (University of Bristol); Kirsty Aquilina
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W7139228085

## 81. DelTact: A Vision-based Tactile Sensor Using Dense Color Pattern (2022)
- Venue/authors: arXiv (Cornell University); Guanlan Zhang; Yipai Du; Hongyu Yu; Michael Yu Wang
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4308895855

## 82. TactileAR: Active Tactile Pattern Reconstruction (2024)
- Venue/authors: preprint; Bing Wu; Qian Liu
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4401417408

## 83. High-fidelity marker-level 3D deformation simulation of visuotactile sensors (2026)
- Venue/authors: Biomimetic Intelligence and Robotics; Chaofan Zhang; Shaowei Cui; Yinghao Cai; Shaolin Zhang; Rui Wang; Shuo Wang
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W7140163608

## 84. FeelAnyForce: Estimating Contact Force Feedback from Tactile Sensation for Vision-Based Tactile Sensors (2024)
- Venue/authors: arXiv (Cornell University); Amir-Hossein Shahidzadeh; Gabriele M. Caddeo; Koushik Alapati; Lorenzo Natale; Cornelia Fermüller; Yiannis Aloimonos
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4403854226

## 85. From Reach to Insert: Tactile-Augmented Precision Assembly under Sub-Millimeter Tolerances (2026)
- Venue/authors: ArXiv.org; Xinpan Meng; Siyao Huang; JingPu Yang; Muyuan Ma; Zhenghua Ma; Lijun Han; Gao Yuan; Houcheng Li; et al.
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W7160670530

## 86. Vision-based Tactile Image Generation via Contact Condition-guided Diffusion Model (2024)
- Venue/authors: arXiv (Cornell University); Xi Lin; Weiliang Xu; Yu Mao; Jing Wang; Meixuan Lv; Lu Liu; Luo, Xihui; Xinming Li
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4405034424

## 87. A Virtual 2D Tactile Array for Soft Actuators Using Acoustic Sensing (2022)
- Venue/authors: arXiv (Cornell University); Vincent Wall; Oliver Brock
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4292947837

## 88. TacFR-Gripper: A Reconfigurable Fin-Ray-Based Gripper with Tactile Skin for In-Hand Manipulation (2024)
- Venue/authors: Actuators; Qingzheng Cong; Wen Fan; Dandan Zhang
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4405474337

## 89. PoseIt: A Visual-Tactile Dataset of Holding Poses for Grasp Stability Analysis (2022)
- Venue/authors: arXiv (Cornell University); Shubham Kanitkar; Helen Jiang; Wenzhen Yuan
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4295682974

## 90. A model-free approach to fingertip slip and disturbance detection for grasp stability inference (2023)
- Venue/authors: arXiv (Cornell University); Dounia Kitouni; Mahdi Khoramshahi; Véronique Perdereau
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4388963550

## 91. Action Conditioned Tactile Prediction: case study on slip prediction (2022)
- Venue/authors: article; Willow Mandil; Kiyanoush Nazari; Amir Ghalamzan
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4283787061

## 92. Maintaining Grasps within Slipping Bounds by Monitoring Incipient Slip (2019)
- Venue/authors: article; Siyuan Dong; Daolin Ma; Elliott Donlon; Alberto Rodríguez
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2967378496

## 93. Magnitude estimation of softness (2008)
- Venue/authors: Experimental Brain Research; Robert M. Friedman; Kim D. Hester; Barry G. Green; Robert H. LaMotte
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2074112147

## 94. Discrimination of Dynamic Tactile Contact by Temporally Precise Event Sensing in Spiking Neuromorphic Networks (2017)
- Venue/authors: Frontiers in Neuroscience; Wang Wei Lee; Sunil L. Kukreja; Nitish V. Thakor
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2580560845

## 95. An individual's skin stiffness predicts their tactile discrimination of compliance (2023)
- Venue/authors: The Journal of Physiology; Bingxu Li; Gregory J. Gerling
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4388530014

## 96. GelFinger: A Novel Visual-Tactile Sensor With Multi-Angle Tactile Image Stitching (2023)
- Venue/authors: IEEE Robotics and Automation Letters; Zhonglin Lin; Jiaquan Zhuang; Yufeng Li; Xianyu Wu; Shan Luo; Daniel Fernandes Gomes; Feng Huang; Yang Zheng
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4385569531

## 97. TactiGraph: An Asynchronous Graph Neural Network for Contact Angle Prediction Using Neuromorphic Vision-Based Tactile Sensing (2023)
- Venue/authors: Sensors; Hussain Sajwani; Abdulla Ayyad; Yusra Alkendi; Mohamad Halwani; Yusra Abdulrahman; Abdulqader Abusafieh; Yahya Zweiri
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Learned predictor or policy over sensory features.
- Hidden assumptions: Training labels and deployment contacts share a stable distribution; the learned score is actionable.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Cases where identical scalar scores require opposite contact repairs.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4384665892

## 98. Modeling and Design of a Soft Capacitive Slip Sensor with Fluid Dielectric Interlayer (2026)
- Venue/authors: Micromachines; Elia Landi; Tommaso Lisini Baldi; Michele Pallaoro; Federico Micheletti; Federico Carli; Ada Fort
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W7135047135

## 99. Object Exploration Using a Three-Axis Tactile Sensing Information (2011)
- Venue/authors: Journal of Computer Science; Abdullah
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W2159644096

## 100. L$^3$ F-TOUCH: A Wireless GelSight With Decoupled Tactile and Three-Axis Force Sensing (2023)
- Venue/authors: IEEE Robotics and Automation Letters; Wanlin Li; Meng Wang; J. Li; Yao Su; Devesh K. Jha; Xinyuan Qian; Kaspar Althoefer; Hangxin Liu
- Problem claimed: Use tactile/contact observations to infer grasp state or prevent failure.
- Actual mechanism introduced: Tactile sensing pipeline with contact-state inference.
- Hidden assumptions: Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities.
- Variables treated as fixed: sensor calibration, contact patch interpretation, object pose during contact
- Failure modes ignored: Counterfactual contact edits that explain which tactile patch change would avert failure.
- What it makes less novel: Using tactile signals for grasp-state estimation or feedback.
- What it leaves open: A representation where tactile failure is a contact-field displacement rather than a terminal class label.
- URL/DOI: https://openalex.org/W4383200202

## Submission-Hardening v2 Addendum

Checked on 2026-06-12 against targeted web search for counterfactual/explainable grasp-failure work.

| Year | Work | Why Hostile | Boundary Left Open |
|---:|---|---|---|
| 2025 | "Optimizing Local Explainability in Robotic Grasp Failure Prediction" | Directly hostile to the framing that grasp failure explanations are unstudied. It addresses local explainability for grasp-failure prediction. | The v2 paper should avoid claiming generic counterfactual/explainability novelty and instead focus on executable contact-field edits and the signed repair direction lost by scalar magnitude labels. |
| 2024-2026 | Slip detection, tactile stability, and visual-tactile grasping papers in the hostile set | Make tactile failure detection and closed-loop correction non-novel. | They typically score, classify, or control from tactile inputs rather than making the minimal executable contact edit the represented object. |

Hardening implication: the paper must not sell "counterfactual grasp failure" broadly. The defensible contribution is a tiny scalar-magnitude insufficiency counterexample plus a reproducible contact-field representation.
