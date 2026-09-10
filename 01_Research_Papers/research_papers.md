# 01_Research_Papers - Literature Search Evidence Base

**Research Title:** An Integrated Technical and Human Factor Risk Assessment Framework for Operational Security (Group H)

Compiled by Member 2 (Haziq Danial Bin Nor Azan) for Group H (Operational Security).

This supports Chapter 2 (Literature Review) of the Research Proposal. All 40 papers were
screened and included in Assignment 1's systematic literature review and are carried over
here per the lecturer's instruction, refined for the proposal's research gap. Each paper
below is presented as an Item / Required Information table, matching the assignment brief's
format.

**This file is now the single, authoritative source for the full 40 paper findings table.**
Chapter 2 of the Research Proposal (Word report) summarises the three literature themes,
the existing approaches/tools tables, and the research gap, and points back to this file
rather than reproducing all 40 papers in the report itself.

> **Status:** Verified consistent with the latest Research Proposal draft (Chapter 2, prose
> refined/reworded; citations, tables and research gap unchanged). Last checked against
> report update on 10 Sept 2026.


> **Note on access:** full text copies are not uploaded here. See `07_References/` for the
> full APA reference list and official DOI/source links, in line with the assignment brief's
> copyright guidance (do not redistribute copyrighted articles).

---

### Paper 1

| Item | Required Information |
|---|---|
| **Paper Title** | Security and Risk Assessment of Academic Information System By Using NIST Framework (A Case Study Approach) |
| **Author(s)** | Perdana, R. S., Effendy, A., Garnida, H., Fidayan, A., Nazar, F., & Saepudin, D. |
| **Year** | 2022 |
| **Research Problem** | Assess an academic information system's security posture and risk using a compliance framework. |
| **Method / Technique** | NIST SP 800-26 control assessment combined with SP 800-30 risk stages; Acunetix vulnerability scanning. |
| **Dataset / Tools** | 40 respondent survey (rectorate/faculty/IT) plus an automated scan of Universitas Sangga Buana's system. |
| **Main Findings** | 72.43% control maturity (Level 3 - Implemented Procedures); 600 vulnerabilities found (4 high, 40 medium, 13 low, 543 informational). |
| **Limitation** | Single institution, subjective self report survey, no re assessment over time; training effectiveness untested. |
| **Relevance to Proposed Research** | Baseline example of a purely technical/compliance risk score with no human factor dimension motivates Theme 1 vs Theme 2 divide. |

### Paper 2

| Item | Required Information |
|---|---|
| **Paper Title** | Cybersecurity as a Business Process: Developing a Multi Level Dashboard System for Information Security Risk Management |
| **Author(s)** | Yakupov, N., Bazhayev, N., Tashenova, Z., & Shaikhanova, A. |
| **Year** | 2025 |
| **Research Problem** | Unify cybersecurity metrics across strategic, tactical and operational layers via a single dashboard model. |
| **Method / Technique** | SLR plus requirements analysis, conceptual model and scenario validation using GQM methodology. |
| **Dataset / Tools** | No empirical dataset; validated against 4 conceptual scenarios (incident, vulnerability, threat escalation, maturity). |
| **Main Findings** | Dashboard concept held consistent across all 4 scenarios; with IoT monitoring, detection accuracy improved by roughly 10%. |
| **Limitation** | Purely conceptual, no real deployment or field testing. |
| **Relevance to Proposed Research** | Supports the quantitative/governance theme shows demand for a shared reporting layer, but not evaluated with real analysts. |

### Paper 3

| Item | Required Information |
|---|---|
| **Paper Title** | Evaluating LLMs for Operational Technology (OT) Cybersecurity Risk Assessment Across Structured and Unstructured Inputs |
| **Author(s)** | Iyenghar, P., Messerknecht, J., Zimmer, C., Gregorio, C., & Pulvermüller, E. |
| **Year** | 2026 |
| **Research Problem** | Test whether large language models can automate IEC 62443 OT risk assessment from device documentation. |
| **Method / Technique** | Six LLMs evaluated against the IEC 62443-3-2 ZCR5 workflow and MITRE EMB3D, using zero shot, few-shot and rule-based prompting. |
| **Dataset / Tools** | Device manuals (HMI/PLC/drives) and the EmbSoftOTBench benchmark; 7,038 evaluations across the six models. |
| **Main Findings** | Threat identification was reliable (63-86%); structured scenario input outperformed raw document input; likelihood estimation was the weakest capability. |
| **Limitation** | Underestimation bias on unstructured documents; authors conclude human in the loop oversight is still required. |
| **Relevance to Proposed Research** | Directly relevant to the identified gap shows AI/LLM tools are evaluated on technical accuracy, not on how they change a human analyst's judgement. |

### Paper 4

| Item | Required Information |
|---|---|
| **Paper Title** | Inclusive Cybersecurity and Safety Risk Assessment Model for Cyber Physical Systems Using Mamdani Fuzzy Inference System |
| **Author(s)** | Noor, M. M., Selamat, A., & Hussain, N. A. |
| **Year** | 2025 |
| **Research Problem** | Build a quantifiable risk model that combines cybersecurity, safety and human factor inputs for cyber-physical systems. |
| **Method / Technique** | Mamdani Fuzzy Inference System (three cascaded blocks) combined with multiple linear regression analysis. |
| **Dataset / Tools** | SLR, standards and expert interviews; 43 threat events benchmarked against the 2023 Dragos OT industry report. |
| **Main Findings** | 90% accuracy matching real top OT threats (versus 60-80% in prior benchmarks); top risk identified was insider privilege abuse. |
| **Limitation** | Uses public, not real, industry data; no real-time detection; heavy manual fuzzy rule input required. |
| **Relevance to Proposed Research** | One of the few studies that explicitly tries to combine human and technical risk inputs a reference point for the proposed integration. |

### Paper 5

| Item | Required Information |
|---|---|
| **Paper Title** | Towards Developing a Scalable Cyber Risk Assessment and Mitigation Framework |
| **Author(s)** | Malik, A. A., & Tosh, D. K. |
| **Year** | 2024 |
| **Research Problem** | Build an adaptable, continuous cyber risk assessment tool (CyVIA) covering vulnerability ID, prioritisation and mitigation. |
| **Method / Technique** | Linear SVC with PCA for attack classification; NLP based abstractive summarisation; Flask REST API. |
| **Dataset / Tools** | 20 years of CVE/CWE data (MITRE/NVD); 15-node test network (Raspbian, Debian, Windows, CentOS, Ubuntu). |
| **Main Findings** | Raspbian was the most vulnerable OS (133,298 CVEs); Code Injection was the most common attack type (34,511 occurrences). |
| **Limitation** | Tested only on a controlled network, not production; classifier accuracy not independently benchmarked. |
| **Relevance to Proposed Research** | Supports Theme 1 (OT/ICS frameworks) technical automation with no human factor or analyst facing evaluation component. |

### Paper 6

| Item | Required Information |
|---|---|
| **Paper Title** | All Hands on Tech: Effectively Addressing Maritime Operational Technology Risks Through Cybersecurity Awareness Training |
| **Author(s)** | D'Amelio, E., & Abuzneid, S. |
| **Year** | 2024 |
| **Research Problem** | Combine maritime workers' risk perception with known OT vulnerabilities to recommend awareness training. |
| **Method / Technique** | Literature synthesis and secondary analysis of risk perception paradigms applied to the maritime OT context. |
| **Dataset / Tools** | Synthesis of a 9 officer interview study, a 293 respondent deck officer survey, and a University of Michigan risk perception study. |
| **Main Findings** | Maritime workers consistently underestimate OT risk relative to IT risk; training, experience and incident exposure raise risk perception most. |
| **Limitation** | Synthesis only, no new empirical validation of the recommended training framework. |
| **Relevance to Proposed Research** | Supports Theme 2 (human factors) sector specific evidence that awareness/perception is measured separately from technical control audits. |

### Paper 7

| Item | Required Information |
|---|---|
| **Paper Title** | A Study on the Classification of OT Security Risk Mitigation Measures |
| **Author(s)** | Kanamaru, H., Fujita, J., & Arai, T. |
| **Year** | 2023 |
| **Research Problem** | Classify non IT OT risk mitigation measures (physical, safety, recovery) since existing OT discussion is IT heavy. |
| **Method / Technique** | Conceptual classification per the IEC 62443 framework across two axes: risk factor (damage vs probability) and timing (proactive vs reactive). |
| **Dataset / Tools** | No empirical dataset; output is a classification table built from prior related work. |
| **Main Findings** | IT style measures mainly reduce probability, not damage; physical, safety and recovery measures are needed alongside IT controls for OT mitigation. |
| **Limitation** | No empirical validation of the classification or of each measure's real world impact. |
| **Relevance to Proposed Research** | Supports Theme 1 - reinforces that OT risk mitigation research remains conceptual and technically framed. |

### Paper 8

| Item | Required Information |
|---|---|
| **Paper Title** | Prescriptive Analytics-based Robust Decision Making Model for Cyber Disaster Risk Reduction |
| **Author(s)** | Ponnoly, J., Puthenveetil, J., & D'Urso, P. |
| **Year** | 2024 |
| **Research Problem** | Propose a prescriptive analytics Robust Decision Making (RDM) model for cyber disaster risk reduction under uncertainty. |
| **Method / Technique** | RDM framework combined with Monte Carlo simulation (FAIR model) and reinforcement learning for adversarial decision scenarios. |
| **Dataset / Tools** | Conceptual model built from literature and prior doctoral research on early warning sensemaking; no primary dataset. |
| **Main Findings** | Structures risk treatment options (mitigate/transfer/accept) under deep uncertainty where standard probability models fail. |
| **Limitation** | Purely theoretical, not implemented; authors note human factors are hard to quantify within the model. |
| **Relevance to Proposed Research** | Supports Theme 3/5 (AI assisted, decision oriented risk assessment) illustrates the quantification gap discussed in the proposal. |

### Paper 9

| Item | Required Information |
|---|---|
| **Paper Title** | Automated Risk Assessment Process for Government Agencies & Industry Leaders: Cybersecurity Protection for Operational Technology |
| **Author(s)** | Campara, D., Seiden, S., & Johnson, L. |
| **Year** | 2023 |
| **Research Problem** | Propose automated, model based risk assessment (Blade Risk Manager) to replace slow, inconsistent manual assessment. |
| **Method / Technique** | Model Based Systems Engineering (MBSE): top down operational risk assessment combined with bottom up systems vulnerability assessment. |
| **Dataset / Tools** | No public dataset; commercial platform applied across aeronautics, defence, healthcare and IoT contexts. |
| **Main Findings** | Addresses manual process failings such as informality, inconsistency, lack of repeatability, and missed multi stage attacks. |
| **Limitation** | Vendor solution, not independently validated; requires a high fidelity system model, limiting organisations with less mature engineering practice. |
| **Relevance to Proposed Research** | Supports Theme 1 - automation aimed at technical risk assessment, without an explicit human factor evaluation layer. |

### Paper 10

| Item | Required Information |
|---|---|
| **Paper Title** | The Impact of Purchasing Cyber Insurance on the Enhancement of Operational Cyber Risk Mitigation of U.S. Banks - A Case Study |
| **Author(s)** | Watson, T. F., Thakur, K., & Ali, M. L. |
| **Year** | 2022 |
| **Research Problem** | Test whether purchasing cyber insurance is associated with stronger operational cyber risk mitigation in large US banks. |
| **Method / Technique** | Mixed methods case study: relative frequency and regression analysis, triangulated, using the NIST CSF as a proxy for mitigation maturity. |
| **Dataset / Tools** | 10 CISO interviews at large New Jersey banks (over $1B in assets), drawn from a pool of 34 eligible institutions. |
| **Main Findings** | 3 of 9 insurance related variables were significantly linked to better mitigation practices across the NIST CSF's 5 functions. |
| **Limitation** | Small sample (10 banks), New Jersey only; findings need replication in other regions and sectors. |
| **Relevance to Proposed Research** | Supports Theme 5 (economic/governance perspective) links a financial mechanism to operational risk outcomes at organisation scale. |

### Paper 11

| Item | Required Information |
|---|---|
| **Paper Title** | Leveraging GPT for Tail Risk Identification in Operational Risk Management |
| **Author(s)** | Svensson, C., Jezzini, M., Hvolby, H.-H., Steger-Jensen, K., Vestergaard, S., Chen, T., & El Hajj, M. |
| **Year** | 2026 |
| **Research Problem** | Test whether integrating GPT into Risk and Control Self Assessment (RCSA) improves identification of low probability, high impact ('tail') risks. |
| **Method / Technique** | Practitioner case study embedding GPT into the RCSA lifecycle through prompt engineering. |
| **Dataset / Tools** | Internal policy and incident documents plus a literature synthesis; no formal benchmark dataset. |
| **Main Findings** | GPT surfaced previously undocumented 'taboo' risks and cut RCSA completion time by an estimated 50-75%. |
| **Limitation** | Single organisation, largely qualitative evidence; needs validation against external risk databases. |
| **Relevance to Proposed Research** | Directly relevant to the proposed gap an AI tool evaluated mainly on efficiency, not on the quality of the resulting human risk judgement. |

### Paper 12

| Item | Required Information |
|---|---|
| **Paper Title** | Operational Risk Management in E-Commerce: A Platform Perspective |
| **Author(s)** | Tabares Urrea, N., Maleki Vishkaei, B., & De Giovanni, P. |
| **Year** | 2024 |
| **Research Problem** | Identify, prioritise and mitigate the operational risks facing e commerce platform owners. |
| **Method / Technique** | Three phase framework: risk identification via literature review, Fuzzy QFD prioritisation, mitigation via structured brainstorming. |
| **Dataset / Tools** | Case study of an anonymised e commerce firm, with surveys and interviews of internal experts and customers. |
| **Main Findings** | A cybersecurity first weakness in day to day operations ranked as the top risk, above hacker attacks and data loss. |
| **Limitation** | Single case study; no distinction made across different industries or platform types. |
| **Relevance to Proposed Research** | Supports Theme 4 (sector-specific risk) shows operational integration, not just technical control, drives platform level risk. |

### Paper 13

| Item | Required Information |
|---|---|
| **Paper Title** | Security of IT/OT Convergence: Design and Implementation Challenges |
| **Author(s)** | Zahran, B., Hussaini, A., & Ali-Gombe, A. |
| **Year** | 2026 |
| **Research Problem** | Address the lack of a unified risk assessment framework for converged IT/OT environments. |
| **Method / Technique** | Agentless, simulation-driven automated risk assessment (IIoT-ARAS) based on OCTAVE Allegro and ISO/IEC 27000-series controls. |
| **Dataset / Tools** | Simulated IT/OT network built in OMNeT++, combining wired, wireless and embedded devices. |
| **Main Findings** | The framework detected exploitable vulnerabilities and quantified attack impact through a simulated IP dropping attack scenario. |
| **Limitation** | Tested only in simulation, not on physical infrastructure; the information gathering phase still needs manual input. |
| **Relevance to Proposed Research** | Supports Theme 1 - reinforces that even recent IT/OT frameworks remain simulation-only and technically scoped. |

### Paper 14

| Item | Required Information |
|---|---|
| **Paper Title** | Risk Assessment of Cybersecurity IoT Anomalies Through Cyber Value at Risk (CVaR) |
| **Author(s)** | Vajpayee, P., & Hossain, G. |
| **Year** | 2024 |
| **Research Problem** | Translate IoT anomaly detection output into a quantifiable, actionable cyber risk value. |
| **Method / Technique** | Cyber Value at Risk (CVaR) formula adapted from finance, combining machine learning anomaly scores with asset value. |
| **Dataset / Tools** | Synthetic 'Cybersecurity Attacks Dataset' from Kaggle, covering device, network and security attributes. |
| **Main Findings** | Windows devices had the highest aggregated anomaly score; Mac OS devices had the highest CVaR despite fewer devices. |
| **Limitation** | Asset and control values are manually assigned, not derived from real financial data. |
| **Relevance to Proposed Research** | Supports Theme 5 - a quantification approach that could anchor a common technical/economic risk metric, referenced in the proposed gap. |

### Paper 15

| Item | Required Information |
|---|---|
| **Paper Title** | Observability as a Key Component of Kubernetes Cluster Security in DevSecOps Pipeline |
| **Author(s)** | Mahida, A. |
| **Year** | 2026 |
| **Research Problem** | Improve continuous, runtime security observability for Kubernetes clusters in DevSecOps pipelines. |
| **Method / Technique** | KOSEC Pipeline: an observability driven security algorithm fusing logs, metrics, traces and audit events. |
| **Dataset / Tools** | Controlled hybrid cloud Kubernetes testbed with simulated production like microservice traffic and attacks. |
| **Main Findings** | Outperformed baselines with 92% detection effectiveness, 85ms mean response time. |
| **Limitation** | Tested only in a single cluster/tenant setup; multi cluster environments left as future work. |
| **Relevance to Proposed Research** | Supports Theme 3 - automated technical detection evaluated purely on system metrics, not analyst decision quality. |

### Paper 16

| Item | Required Information |
|---|---|
| **Paper Title** | Medical Device Security Process Framework for Secondary Hospitals |
| **Author(s)** | Parkpean, B., & Nirapai, A. |
| **Year** | 2025 |
| **Research Problem** | Develop a medical device security framework suited to secondary level district hospitals. |
| **Method / Technique** | Documentary/qualitative study integrating ISO/IEC 27799, HIPAA and ISO 31000 risk assessment. |
| **Dataset / Tools** | Internal hospital documents (IT policies, access control, incident records) from one unnamed secondary hospital. |
| **Main Findings** | All six high impact control areas improved from High to Medium/Low risk after the framework's implementation. |
| **Limitation** | Single hospital, self reported study; generalisability beyond this context is untested. |
| **Relevance to Proposed Research** | Supports Theme 4 - a sector specific case where compliance is assessed but analyst/human decision making is not directly measured. |

### Paper 17

| Item | Required Information |
|---|---|
| **Paper Title** | Cyber Security of an Industrial IoT Gateway Device - A Threat Model View and Security Aspects |
| **Author(s)** | Tatavarthi, A. P. K., & Panigrahi, B. K. |
| **Year** | 2023 |
| **Research Problem** | Identify and mitigate cybersecurity threats in Industrial IoT edge gateway devices. |
| **Method / Technique** | STRIDE threat modelling applied via Microsoft's threat modelling tool across defined trust boundaries. |
| **Dataset / Tools** | Conceptual design based study using a generic, high level edge gateway architecture; no real dataset. |
| **Main Findings** | Proposes a layered 'defence in depth' model with mitigations mapped to spoofing and tampering risks. |
| **Limitation** | Purely conceptual; no real world deployment or empirical validation of the proposed mitigations. |
| **Relevance to Proposed Research** | Supports Theme 1 - a threat modelling example directly relevant to the Group H methodology choice (Threat Modelling and Risk Assessment). |

### Paper 18

| Item | Required Information |
|---|---|
| **Paper Title** | Risk Based Optimization of Cryptoperiods to Minimize Impact of Data Siphoning Attacks on ICSs |
| **Author(s)** | Cianfarani, G., Vlajic, N., & Noce, R. |
| **Year** | 2025 |
| **Research Problem** | Determine the optimal encryption key rotation (crypto) period for OPC UA security groups in industrial control systems. |
| **Method / Technique** | Risk based analytical framework combining technical (CVE) and procedural vulnerability factors; the ARC C tool. |
| **Dataset / Tools** | Simulated ICS water treatment plant modelled on real Siemens SIMATIC devices, using CVE data from the NVD. |
| **Main Findings** | The shortest optimal crypto period (12 days) occurs where procedural security is weak and data rate is high. |
| **Limitation** | No established benchmarks exist to validate ARC C outputs; tested in one simulated environment only. |
| **Relevance to Proposed Research** | Supports Theme 1 - technical parameter optimisation with procedural (human/process) security treated only as an input variable, not measured directly. |

### Paper 19

| Item | Required Information |
|---|---|
| **Paper Title** | Application of Cloud Computing Technology in Student Information System Security Processing |
| **Author(s)** | Ye, W. |
| **Year** | 2022 |
| **Research Problem** | Address personal information leakage risk in university cloud based student information systems. |
| **Method / Technique** | Three part cloud architecture (private, public, security cloud) with a five layer platform spanning physical to security layers. |
| **Dataset / Tools** | No external dataset; self built platform load tested with 10-100 concurrent users. |
| **Main Findings** | Response time stayed under 2 seconds even at 100 concurrent users, with no service exceptions as load increased. |
| **Limitation** | Measures system performance, not security effectiveness; no penetration testing or access control validation was performed. |
| **Relevance to Proposed Research** | Supports Theme 4 - illustrates how operational/performance metrics are sometimes substituted for genuine security evaluation. |

### Paper 20

| Item | Required Information |
|---|---|
| **Paper Title** | Security Enhanced Operational Architecture for Decentralized Industrial Internet of Things: A Blockchain based Approach |
| **Author(s)** | Yao, P., Yan, B., Yang, T., Wang, Y., Yang, Q., & Wang, W. |
| **Year** | 2024 |
| **Research Problem** | Address single point of failure and data-tampering risk in centralised IIoT operational management. |
| **Method / Technique** | SecureArchi-IIoT: a decentralised blockchain architecture with granular permission management and a reputation mechanism. |
| **Dataset / Tools** | Prototype built with Raspberry Pi IoT nodes and Intel Core i5 edge nodes on a private Ethereum network. |
| **Main Findings** | Reduced theoretical attack success by 17.1% and detected 96.5%/93.8% of simulated attacks (Monte Carlo simulation). |
| **Limitation** | Small scale prototype (6 nodes); relies on Ethereum/ECDSA, introducing side channel and quantum attack risk. |
| **Relevance to Proposed Research** | Supports Theme 1 - a technically strong architectural solution with no accompanying human factor or analyst evaluation. |

### Paper 21

| Item | Required Information |
|---|---|
| **Paper Title** | Protecting Small and Medium Enterprises: A Specialized Cybersecurity Risk Assessment Framework and Tool |
| **Author(s)** | El-Hajj, M., & Mirza, Z. A. |
| **Year** | 2024 |
| **Research Problem** | Develop an SME tailored cyber risk assessment framework, since NIST/ISO 27001-style frameworks are too complex or costly for SMEs. |
| **Method / Technique** | Threat based risk assessment combined with SDT and an LCCI tiered framework (Business/Admin/Employee levels); a Random Forest URL classifier for phishing. |
| **Dataset / Tools** | Kaggle URL dataset (120,000 URLs, 4 classes); usability testing with 10 SME participants. |
| **Main Findings** | 98% classifier accuracy (precision 0.96-1.0, recall 0.97-1.0); the framework was rated positively but covers only 3 threat types. |
| **Limitation** | Only qualitative validation (expert review plus a 10-user test); no real world pilot; a 6-8 month pilot study is proposed as future work. |
| **Relevance to Proposed Research** | Directly relevant to the proposed gap a technical classifier embedded in a human facing framework, but the two are evaluated separately. |

### Paper 22

| Item | Required Information |
|---|---|
| **Paper Title** | Operations-informed Incident Response Playbooks |
| **Author(s)** | Shaked, A., Cherdantseva, Y., Burnap, P., & Maynard, P. |
| **Year** | 2023 |
| **Research Problem** | Address the gap where incident response playbooks fail to show operational impact, especially in Critical National Infrastructure (CNI). |
| **Method / Technique** | 'Operations informed playbooks' linking incident response to a Dependency Model, using the SecMoF tool and a novel MTU Change in Operations (CiO) metric. |
| **Dataset / Tools** | Case study: a ransomware scenario on a SCADA system, adapted from a Scottish Government playbook and a validated SCADA dependency model. |
| **Main Findings** | Serial containment kept the system operational (status '1'); a parallel containment plan crossed the critical threshold (status '0'). |
| **Limitation** | Single, simplified, binary case study; not tested across other organisations or incident types. |
| **Relevance to Proposed Research** | Supports Theme 1/Group H methodology fit an incident response case study aligned with the Case Study option suggested for Group H. |

### Paper 23

| Item | Required Information |
|---|---|
| **Paper Title** | A Unified Framework for Human-AI Collaboration in Security Operations Centers with Trusted Autonomy |
| **Author(s)** | Mohsin, A., Janicke, H., Ibrahim, A., Sarker, I. H., & Camtepe, S. |
| **Year** | 2025 |
| **Research Problem** | Address the lack of structure for human oversight, trust and AI autonomy across SOC tasks, since existing frameworks assume static automation. |
| **Method / Technique** | Five level AI autonomy framework mapped to human in the loop (HITL) roles and SOC tiers, using the 'CyberAlly' RAG LLM SOC assistant with SIEM/SOAR/knowledge graphs. |
| **Dataset / Tools** | Simulated SOC cyber range (55 virtual machines, maritime port IT/OT); 5 wargames run over 2 years across 3 attack scenarios. |
| **Main Findings** | False positives halved (70% to 35%); investigation time cut by 67%; mean time to resolution cut by over 60%; automated ticketing rose from 10% to 75%. |
| **Limitation** | Simulated range only, not a live SOC; needs continuous retraining; explainability remains unresolved. |
| **Relevance to Proposed Research** | Central to the proposed gap directly models human AI collaboration, but success is measured in SOC throughput, not analyst judgement accuracy. |

### Paper 24

| Item | Required Information |
|---|---|
| **Paper Title** | Towards Human AI Teaming to Mitigate Alert Fatigue in Security Operations Centres |
| **Author(s)** | Chhetri, M. B., Tariq, S., Singh, R., Jalalvand, F., Paris, C., & Nepal, S. |
| **Year** | 2024 |
| **Research Problem** | Address SOC alert fatigue by proposing a human AI teaming vision as an alternative to full automation. |
| **Method / Technique** | The Automate Augment Collaborate (A2C) Framework, with dynamic mode switching mediated by shared situational awareness. |
| **Dataset / Tools** | Conceptual/vision paper grounded in SOC literature and industry alert fatigue statistics; no primary dataset. |
| **Main Findings** | Mode switching human AI collaboration is proposed to reduce alert fatigue while keeping humans in control for novel threats. |
| **Limitation** | Conceptual vision, not empirically validated; deployment challenges (legacy tooling, trust calibration) are left as future work. |
| **Relevance to Proposed Research** | Directly relevant to the proposed gap names the human technical integration problem explicitly but offers no empirical test of it. |

### Paper 25

| Item | Required Information |
|---|---|
| **Paper Title** | Technical Performance Metrics of a Security Operations Center |
| **Author(s)** | Forsberg, J., & Frantti, T. |
| **Year** | 2023 |
| **Research Problem** | Address the gap where existing SOC metrics measure operational aspects but not technical/defensive performance. |
| **Method / Technique** | Design Science Research (DSR) methodology, following Peffers et al., to design and validate a SOC technical metrics framework. |
| **Dataset / Tools** | Design Science Research cycle; 4 novel metrics validated against SOC detection data. |
| **Main Findings** | Existing SOC metrics are overwhelmingly operational; the study produces 4 validated technical performance metrics. |
| **Limitation** | Validated via a DSR cycle rather than a large scale field study; remains a proof of concept. |
| **Relevance to Proposed Research** | Methodologically relevant a DSR based approach to closing a measurement gap, comparable in structure to this proposal's aim. |

### Paper 26

| Item | Required Information |
|---|---|
| **Paper Title** | Analyzing Cybersecurity Risks and Threats in IT Infrastructure based on NIST Framework |
| **Author(s)** | Aljumaiah, O., Jiang, W., Reddy Addula, S., & Amin Almaiah, M. |
| **Year** | 2025 |
| **Research Problem** | Assess whether the NIST Cybersecurity Framework adequately addresses common critical infrastructure threats, and identify gaps. |
| **Method / Technique** | Systematic literature review; threats categorised and frequency counted against the 5 NIST CSF functions. |
| **Dataset / Tools** | Literature review corpus mapped to the 5 NIST CSF functions. |
| **Main Findings** | Human vulnerabilities were the leading threat category (12 instances) error, negligence, low awareness, and social engineering. |
| **Limitation** | Bounded by the search terms and databases used; no empirical test against real incident data. |
| **Relevance to Proposed Research** | Key supporting evidence for the proposed gap independently confirms human factors are the top cited risk but are handled separately from technical frameworks. |

### Paper 27

| Item | Required Information |
|---|---|
| **Paper Title** | Impact of Cybersecurity on Operations and Supply Chain Management: Emerging Trends and Future Research Directions |
| **Author(s)** | Kumar, S., & Mallipeddi, R. R. |
| **Year** | 2022 |
| **Research Problem** | Chart future Production and Operations Management (POM) research directions for cybersecurity risk arising from Industry 4.0/5.0 technology. |
| **Method / Technique** | Conceptual, agenda setting analysis across 6 POM domains (global operations strategy, healthcare, policy, technology management, supply chain, disruptive technology). |
| **Dataset / Tools** | Conceptual/agenda setting article; no primary dataset. |
| **Main Findings** | Frames cybersecurity as an operational risk and a major open research opportunity for POM scholars. |
| **Limitation** | Proposes research directions, not hypotheses or field results; a framing paper only. |
| **Relevance to Proposed Research** | Supports the overall framing of the proposal cybersecurity risk positioned explicitly as an operations problem, not only a technical one. |

### Paper 28

| Item | Required Information |
|---|---|
| **Paper Title** | Smart Grid Cyber Physical Situational Awareness of Complex Operational Technology Attacks: A Review |
| **Author(s)** | Nafees, M. N., Saxena, N., Cardenas, A., Grijalva, S., & Burnap, P. |
| **Year** | 2023 |
| **Research Problem** | Review smart grid cyber physical security through a collaborative situational awareness (SA) lens, since real world attack impact remains largely anecdotal. |
| **Method / Technique** | Threat modelling framework review covering advanced persistent, coordinated and cascading attacks, IDS/MTD/co simulation defences, and operator SA/human factor needs. |
| **Dataset / Tools** | Systematic review/survey of smart grid cyber physical attack literature, IDS/defence tooling, and co simulation studies. |
| **Main Findings** | Real world impact of targeted attacks (e.g. the Ukraine grid incident) remains largely anecdotal; a human factor and SA training gap is highlighted. |
| **Limitation** | Review/survey only no new defence system tested; gaps in human factors, SA training and benchmarks are left open. |
| **Relevance to Proposed Research** | Directly supports the proposed gap explicitly names the missing link between technical situational awareness and operator/human factors. |

### Paper 29

| Item | Required Information |
|---|---|
| **Paper Title** | Stress, Burnout, and Security Fatigue in Cybersecurity: A Human Factors Problem |
| **Author(s)** | Nobles, C. |
| **Year** | 2022 |
| **Research Problem** | Argue that stress, burnout and security fatigue are under addressed human performance risks, with the root cause being a lack of human factors integration. |
| **Method / Technique** | Narrative literature synthesis combined with industry survey statistics (ISACA, Nominet, Deloitte, ENISA); a Taxonomy of Human Performance Issues and an HRCO (5-pillar) framework. |
| **Dataset / Tools** | Narrative synthesis plus third party industry statistics; no primary study conducted. |
| **Main Findings** | 91% of CISOs report stress, 77% report burnout, 88% work 40+ hours/week; estimated cost around $500B/year (US). |
| **Limitation** | Narrative/conceptual only, with no primary data or empirical test of the proposed HRCO model. |
| **Relevance to Proposed Research** | Core evidence for Theme 2 (human factors) shows the scale of the human performance problem that technical frameworks (Theme 1) do not capture. |

### Paper 30

| Item | Required Information |
|---|---|
| **Paper Title** | Data driven Secure, Resilient and Sustainable Supply Chains: Gaps, Opportunities, and a New Generalised Data Sharing and Data Monetisation Framework |
| **Author(s)** | Bechtsis, D., Tsolakis, N., Iakovou, E., & Vlachos, D. |
| **Year** | 2022 |
| **Research Problem** | Address the need for data driven risk management paradigms in supply chains exposed to disruption (e.g. COVID 19). |
| **Method / Technique** | Critical literature taxonomy, validated through an organic food supply chain case study; a new data sharing/monetisation framework built from 3 identified gaps. |
| **Dataset / Tools** | Literature taxonomy and a single organic food supply chain case study; no primary quantitative dataset. |
| **Main Findings** | Data driven technology is needed to jointly achieve supply chain security, resilience and sustainability, as validated through the food supply chain case. |
| **Limitation** | Single case study (organic food); not tested across other sectors; the framework remains conceptual. |
| **Relevance to Proposed Research** | Supports Theme 4/5 - broadens the operational risk lens beyond a single organisation toward supply chain level governance. |

### Paper 31

| Item | Required Information |
|---|---|
| **Paper Title** | A Holistic Evaluation Model for Information Security Awareness Programs in Work Environment |
| **Author(s)** | Alharbi, T. |
| **Year** | 2023 |
| **Research Problem** | Propose a framework to assess employees' security behaviour more directly than existing self report methods allow. |
| **Method / Technique** | Built on Gundu's model, combining Deterrence Theory and the Theory of Planned Behaviour; classifies non compliant users via knowing doing scores. |
| **Dataset / Tools** | Behavioural classification approach; type/action based scoring rather than a fixed external dataset. |
| **Main Findings** | Recommends targeted training enrolment for staff who fail simulated (e.g. phishing) tests, based on their classification. |
| **Limitation** | Has not been field tested. |
| **Relevance to Proposed Research** | Core evidence for Theme 2 - explicitly critiques self report as a measurement method, motivating a more integrated evaluation approach. |

### Paper 32

| Item | Required Information |
|---|---|
| **Paper Title** | Cybersecurity and Financial Systems: A Global Perspective on Research Fragmentation and Innovation Gaps |
| **Author(s)** | Sopko, J., & Šafár, L. |
| **Year** | 2026 |
| **Research Problem** | Examine the research output on cybersecurity in financial institutions from 2000 to mid 2025 to identify fragmentation and gaps. |
| **Method / Technique** | Bibliometric analysis using the Web of Science database and standard bibliometric measures (via RStudio), rather than security performance metrics. |
| **Dataset / Tools** | 2,005 publications from the Web of Science Core Collection. |
| **Main Findings** | Documents a shift in the field from information security/risk management topics toward data driven cybersecurity applications. |
| **Limitation** | Does not test or validate any specific operational risk framework, dataset, or human factors mechanism. |
| **Relevance to Proposed Research** | Supports Theme 5 - field level evidence that measurement approaches across the literature are fragmented and not standardised. |

### Paper 33

| Item | Required Information |
|---|---|
| **Paper Title** | A Game Theory Based Risk Assessment Method for Industrial Control Systems via Bayesian Attack Graphs |
| **Author(s)** | Yang, W., Hou, F., Jia, Z., Zhang, C., Zhao, S., Song, Y., & Li, N. |
| **Year** | 2025 |
| **Research Problem** | Model attacker defender dynamics in industrial control systems using a game theoretic framework. |
| **Method / Technique** | Game theoretic modelling of ICS security using Bayesian attack graphs. |
| **Dataset / Tools** | Simulated ICS network built from publicly available databases. |
| **Main Findings** | Reduced subjectivity and improved the accuracy of risk estimation compared to traditional methods. |
| **Limitation** | Scaling the framework to large ICS networks remains an open challenge. |
| **Relevance to Proposed Research** | Supports Theme 1 - a probabilistic technical model, again without a corresponding human decision evaluation. |

### Paper 34

| Item | Required Information |
|---|---|
| **Paper Title** | Risk Assessment of SCADA Cyber Attack Methods: A Technical Review on Securing Automated Real time SCADA Systems |
| **Author(s)** | Urooj, B., Ullah, U., Shah, M. A., Sikandar, H. S., & Stanikzai, A. Q. |
| **Year** | 2022 |
| **Research Problem** | Show potential future research directions and available methods for manufactured system (SCADA) risk assessment. |
| **Method / Technique** | Comparative review of existing SCADA cybersecurity risk assessment methods. |
| **Dataset / Tools** | Reviewed literature on SCADA risk assessment; no primary dataset. |
| **Main Findings** | Provides a structured comparison of existing risk assessment approaches and identifies potential research gaps in the SCADA literature. |
| **Limitation** | Does not propose or validate a novel risk assessment method. |
| **Relevance to Proposed Research** | Supports Theme 1 - a review level source useful for framing the technical side of the literature landscape. |

### Paper 35

| Item | Required Information |
|---|---|
| **Paper Title** | Pharma Supply Chain Cyber Risk Dashboard: Visualizing Threats and Applying CNSS Controls Across Suppliers, Manufacturers, and Distributors |
| **Author(s)** | Gummadivelli, P., & Hossain, G. |
| **Year** | 2026 |
| **Research Problem** | Propose a dashboard to monitor cyber risk across pharmaceutical supply chains. |
| **Method / Technique** | Three part design: a threat intelligence layer, CNSS control mapping, and a Dashboard Visibility Layer. |
| **Dataset / Tools** | Public datasets from real world supply chain cyber incidents combined with simulated data. |
| **Main Findings** | Evaluates threat exposure across interoperating supply chain partners rather than individual nodes; finds significant control gaps in integrity, especially among upstream suppliers. |
| **Limitation** | Lacks real world pharmaceutical OT telemetry. |
| **Relevance to Proposed Research** | Supports Theme 4 - sector specific dashboard based risk visualisation, technically framed. |

### Paper 36

| Item | Required Information |
|---|---|
| **Paper Title** | Enhancing Third Party Risk Management in Aviation: A Comprehensive Framework for Modern Challenges |
| **Author(s)** | Al-Hussaeni, K., & Bin Hammad, S. |
| **Year** | 2025 |
| **Research Problem** | Identify third party risk and propose a Third Party Risk Management (TPRM) framework for airlines. |
| **Method / Technique** | Triangulated qualitative methodology; content analysis of structured observation sessions. |
| **Dataset / Tools** | 40 interviewees from Etihad and Emirates airlines. |
| **Main Findings** | The cybersecurity team showed the highest TPRM awareness among the groups studied. |
| **Limitation** | Does not take current Industry 5.0 technology into account. |
| **Relevance to Proposed Research** | Supports Theme 4 - awareness measured at team/organisational level, complementing the individual level human factor studies in Theme 2. |

### Paper 37

| Item | Required Information |
|---|---|
| **Paper Title** | A Enhancing Cybersecurity Resilience for Low Income Farmers in Developing Nations: A Fuzzy Cognitive Mapping Approach |
| **Author(s)** | Bissadu, K., Hossain, G., & Velagala, L. P. |
| **Year** | 2024 |
| **Research Problem** | Introduce a streamlined approach for evaluating cybersecurity risk for low income farmers with limited technical resources. |
| **Method / Technique** | Seven step hybrid methodology combining Asset Added Value Tree (AAVT) and Fuzzy Cognitive Mapping (FCM). |
| **Dataset / Tools** | Case context: the 'Ferme Ecole' farming project, Tsevie, Togo. |
| **Main Findings** | Assets involving human interaction were found to be the most concerning; a combined automated and non automated assessment approach is recommended. |
| **Limitation** | Risk weighting relies heavily on subjective expert judgment. |
| **Relevance to Proposed Research** | Supports Theme 2/4 - a resource constrained context where human interaction is the dominant risk factor, relevant to accessible risk assessment design. |

### Paper 38

| Item | Required Information |
|---|---|
| **Paper Title** | Human Factors in Cybersecurity Awareness |
| **Author(s)** | Sangwan, A. |
| **Year** | 2024 |
| **Research Problem** | Analyse the human aspects related to cybersecurity awareness. |
| **Method / Technique** | Analytical review examining psychological, behavioural and sociocultural aspects of cybersecurity awareness. |
| **Dataset / Tools** | Case studies and real world incidents, including the 2013 Target data breach. |
| **Main Findings** | Psychological, behavioural and sociocultural factors shape both risk perception and the implementation of security measures. |
| **Limitation** | No empirical data collected. |
| **Relevance to Proposed Research** | Core evidence for Theme 2 - reinforces that human factor risk is analysed qualitatively and separately from technical risk metrics. |

### Paper 39

| Item | Required Information |
|---|---|
| **Paper Title** | A Comparative Assessment of Human Factors in Cybersecurity: Implications for Cyber Governance |
| **Author(s)** | Shah, M. U., Iqbal, F., Rehman, U., & Hung, P. C. K. |
| **Year** | 2023 |
| **Research Problem** | Identify which specific human factors affect cybersecurity behaviour across culturally diverse populations. |
| **Method / Technique** | Causal comparative research design using a custom built, 14 item Likert scale cybersecurity awareness questionnaire. |
| **Dataset / Tools** | Two independent online surveys: 157 respondents from the USA and 165 from the UAE. |
| **Main Findings** | Scale reliability confirmed via Cronbach's alpha; only 1 of 14 awareness items showed a significant difference between the UAE and USA samples. |
| **Limitation** | Sample is not broad enough to generalise across other regions or cultures. |
| **Relevance to Proposed Research** | Core evidence for Theme 2 - cross cultural human factor measurement, entirely survey based and separate from technical assessment. |

### Paper 40

| Item | Required Information |
|---|---|
| **Paper Title** | The Influence of Human Factors in Ensuring Cybersecurity in Organizations: Effectiveness of PDPA and GDPR Implementation |
| **Author(s)** | Sharifi, A. Z., Walid, M. A., Momand, M. D., Safi, I. U. H., Safi, H. K., & Hossain, S. |
| **Year** | 2024 |
| **Research Problem** | Explore employees' perception of the effectiveness of data protection legislation (PDPA/GDPR). |
| **Method / Technique** | Literature based taxonomy combined with an anonymous structured questionnaire. |
| **Dataset / Tools** | Peer reviewed literature, reports and legislation, plus survey data from 30 randomly selected US employees. |
| **Main Findings** | 70% of respondents understood cybersecurity concepts; 66.7% reported a reduction in human error attributable to BYOD/GDPR/PDPA regulation. |
| **Limitation** | Small sample size. |
| **Relevance to Proposed Research** | Core evidence for Theme 2 - shows legal/governance compliance is perceived to reduce human error, but the link is self reported, not measured technically. |
