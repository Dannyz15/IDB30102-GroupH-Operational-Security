# 02_Literature_Review - Analysis, Comparison and Research Gap

**Research Title:** An Integrated Technical and Human-Factor Risk Assessment Framework for Operational Security (Group H)

Compiled by Member 2 (Haziq Danial Bin Nor Azan) for Group H (Operational Security).

This content must stay consistent with Chapter 2 of the Research Proposal and with
`01_Research_Papers/research_papers.md`. It refines the Assignment 1 SLR synthesis into
the specific research gap this proposal responds to.

> **Status:** Verified consistent with the latest Research Proposal draft (Chapter 2, prose
> refined/reworded; citations, tables and research gap unchanged). Last checked against
> report update on 10 Sept 2026.

---

## 1. Comparison of Existing Techniques (Thematic Synthesis)

| Theme | Representative Studies | Common Dataset / Source | Methods / Approaches | Key Trend | Gap Relevant to This Proposal |
|---|---|---|---|---|---|
| **1. Operational risk & OT/ICS assessment frameworks** | Perdana et al. (2022); Zahran et al. (2026); Yang et al. (2025); Kanamaru et al. (2023); Cianfarani et al. (2025); Campara et al. (2023); Malik & Tosh (2024); Tatavarthi & Panigrahi (2023); Yao et al. (2024); Urooj et al. (2022) | Simulated ICS/SCADA testbeds, benchmark attack graphs, illustrative case systems | Bayesian attack graphs, game theory, fuzzy inference, standards based frameworks (OCTAVE, ISO/IEC 27k), blockchain architecture | Shift from qualitative checklists toward probabilistic/fuzzy quantification and architecture level solutions | Validated mainly through simulation or single organisation case studies; quantifies technical risk without a corresponding measure of human factors |

| **2. Human factors and security awareness** | Aljumaiah et al. (2025); Nobles (2022); Sangwan (2024); Shah et al. (2023); Sharifi et al. (2024); Alharbi (2023); D'Amelio & Abuzneid (2024); Bissadu et al. (2024) | Employee/mariner/farmer surveys, self reported behavioural data | Cross cultural comparison, behavioural analytics, fuzzy cognitive mapping, awareness training evaluation | Humans consistently identified as the leading risk factor; awareness effectiveness varies by culture, sector and legislation | Measured almost entirely through self report; not linked back to the technical control assessments in Theme 1 |

| **3. AI/LLM enabled risk assessment & SOC support** | Iyenghar et al. (2026); Mohsin et al. (2025); Chhetri et al. (2024); Forsberg & Frantti (2023); Mahida (2026); Ponnoly et al. (2024); Shaked et al. (2023); El-Hajj & Mirza (2024) | Device manuals, structured benchmark inputs, SOC telemetry (logs, metrics, traces) | LLM based reasoning, tiered human AI autonomy, observability/telemetry fusion, prescriptive analytics | AI increasingly embedded across detection, triage and response; trust calibration and human oversight remain essential | Automation is evaluated on its own technical accuracy, not on whether it improves human risk assessment outcomes |

| **4. Sector-specific & third-party/supply-chain risk management** | Al-Hussaeni & Bin Hammad (2025); Bechtsis et al. (2022); Gummadivelli & Hossain (2026); Tabares Urrea et al. (2024); Parkpean & Nirapai (2025); Ye (2022) | Single organisation case studies (airlines, hospitals, e commerce platforms) | NIST/ISO compliance audits, fuzzy QFD, dashboard based vendor/threat mapping | Sector context strongly shapes risk priorities; operational integration, not only cybersecurity, drives platform risk | Findings are mainly single case; limited generalisability across industries |

| **5. Quantitative, economic and governance perspectives** | Vajpayee & Hossain (2024); Watson et al. (2022); Sopko & Šafár (2026); Yakupov et al. (2025); Kumar & Mallipeddi (2022); Svensson et al. (2026) | IoT anomaly scores, bank case data, bibliometric records | Cyber Value at Risk, insurance case analysis, bibliometric mapping, multi level dashboards | Field is expanding toward data driven, AI enabled research; growing demand for financially meaningful risk metrics | No common quantification standard; metrics (CVaR, insurance scores, dashboards) are not mutually comparable |


## 2. Existing Approaches Identified from the Literature

| # | Approach | Description | Example Studies |
|---|---|---|---|
| 1 | Compliance/standards based assessment (NIST SP 800-26/800-30, ISO/IEC 27k, OCTAVE Allegro) | Scores an organisation's controls against a recognised standard to produce a maturity or compliance rating. | Perdana et al. (2022); Zahran et al. (2026); Parkpean & Nirapai (2025) |
| 2 | Threat modelling (STRIDE, IEC 62443 workflow) | Systematically enumerates threats against system trust boundaries to guide mitigation design. | Tatavarthi & Panigrahi (2023); Kanamaru et al. (2023); Iyenghar et al. (2026) |
| 3 | Probabilistic / game theoretic modelling (Bayesian attack graphs) | Models attacker defender interaction to estimate exploitation probability and expected loss. | Yang et al. (2025) |
| 4 | Fuzzy inference / fuzzy cognitive mapping | Represents uncertain, expert judgement based risk relationships mathematically. | Noor et al. (2025); Bissadu et al. (2024) |
| 5 | Case study research | In depth investigation of a single organisation or incident to build contextual, real world evidence. | Watson et al. (2022); Shaked et al. (2023); Tabares Urrea et al. (2024) |
| 6 | Survey / self report instruments | Structured questionnaires (often Likert scale) used to measure awareness, perception or behaviour. | Shah et al. (2023); Alharbi (2023); Sharifi et al. (2024) |
| 7 | Design Science Research (DSR) | Iteratively designs and evaluates an artefact (framework, metric set, tool) against defined objectives. | Forsberg & Frantti (2023) |
| 8 | Machine learning classification | Trains a classifier (e.g. Random Forest, SVC) to detect or score threats from labelled data. | El-Hajj & Mirza (2024); Malik & Tosh (2024) |
| 9 | LLM assisted / human AI collaborative assessment | Uses large language models to process unstructured input and support (not replace) analyst decisions. | Iyenghar et al. (2026); Svensson et al. (2026); Mohsin et al. (2025); Chhetri et al. (2024) |
| 10 | Systematic literature review / bibliometric analysis | Synthesises an existing body of published work to identify trends and gaps rather than collecting new primary data. | Aljumaiah et al. (2025); Sopko & Šafár (2026); Nafees et al. (2023) |

**Observation:** approaches 1-4 and 8 treat risk as a technical/procedural quantity; approaches 5-6
treat risk as a human/behavioural quantity; only approach 9 (LLM assisted assessment) sits between
the two, which is why it is central to the research gap identified in Section 6.

## 3. Existing Technology / Tools Identified from the Literature

| # | Technology / Tool | Purpose | Example Studies |
|---|---|---|---|
| 1 | Acunetix (automated vulnerability scanner) | Scans a live system for known technical vulnerabilities. | Perdana et al. (2022) |
| 2 | Microsoft Threat Modeling Tool | Supports structured STRIDE based threat modelling and diagramming. | Tatavarthi & Panigrahi (2023) |
| 3 | Random Forest classifier | Machine learning model used for phishing-URL and threat classification. | El-Hajj & Mirza (2024) |
| 4 | Linear SVC with PCA | Classifier and dimensionality reduction pipeline used for CVE/attack type classification. | Malik & Tosh (2024) |
| 5 | Large Language Models (GPT, RAG LLM assistants) | Processes unstructured technical documents and supports SOC/RCSA decision making. | Iyenghar et al. (2026); Svensson et al. (2026); Mohsin et al. (2025) |
| 6 | SIEM / SOAR platforms | Aggregates security logs and automates alert triage and response workflows. | Mohsin et al. (2025) |
| 7 | OMNeT++ network simulator | Simulates IT/OT network behaviour for safe, non production risk testing. | Zahran et al. (2026) |
| 8 | Blockchain / Ethereum smart contract platform | Provides decentralised, tamper resistant architecture for IIoT management. | Yao et al. (2024) |
| 9 | ARC-C tool | Analyses CVE and procedural vulnerability factors to optimise ICS crypto periods. | Cianfarani et al. (2025) |
| 10 | Kubernetes / DevSecOps observability pipeline (KOSEC Pipeline) | Fuses logs, metrics, traces and audit events for continuous runtime security monitoring. | Mahida (2026) |

**Observation:** tools 1-4 and 7-10 are purely technical instruments with no human facing evaluation
built in; tools 5-6 (LLMs, SIEM/SOAR) are the only ones positioned to sit directly in an analyst's
workflow, reinforcing why AI assisted, human in the loop tooling is the focus of the proposed gap.

## 4. Relevant Datasets and Data Sources Identified

| Category | Examples in the Literature | Use for This Proposal |
|---|---|---|
| Public vulnerability/threat feeds | MITRE CVE/CWE (Malik & Tosh, 2024); NVD CVE data (Cianfarani et al., 2025) | Candidate source for technical vulnerability inputs |
| Benchmark / synthetic attack datasets | Kaggle Cybersecurity Attacks Dataset (Vajpayee & Hossain, 2024); Kaggle URL dataset (El-Hajj & Mirza, 2024); EmbSoftOTBench (Iyenghar et al., 2026) | Candidate source for controlled, repeatable technical test scenarios |
| Simulated ICS/SCADA/IT OT testbeds | OMNeT++ simulated network (Zahran et al., 2026); simulated water treatment plant (Cianfarani et al., 2025) | Reference for building a safe, non production evaluation environment |
| Survey/interview instruments | 14-item Likert questionnaire (Shah et al., 2023); NIST CSF based interview protocol (Watson et al., 2022) | Reference for eliciting the human judgement side of the evaluation |
| Bibliometric/secondary records | Web of Science Core Collection, 2,005 records (Sopko & Šafár, 2026) | Context only; not used directly, informs how fragmented current metrics are |

## 5. Evaluation Metrics Identified from Previous Research

| Metric Type | Examples | Source Studies |
|---|---|---|
| Classifier performance | Precision, recall, F1 score, accuracy | El-Hajj & Mirza (2024); Iyenghar et al. (2026) |
| Detection/response performance | False positive rate, detection effectiveness, mean time to resolution (MTTR), response time | Mahida (2026); Mohsin et al. (2025) |
| Risk model fit | R², standard error, ANOVA significance | Noor et al. (2025) |
| Maturity / control coverage scoring | Percentage maturity score against a standard | Perdana et al. (2022) |
| Behavioural/survey reliability | Cronbach's alpha, Shapiro Wilk/Levene's tests | Shah et al. (2023); Watson et al. (2022) |
| Financial/economic | Cyber Value at Risk (CVaR), self reported time savings | Vajpayee & Hossain (2024); Svensson et al. (2026) |

**Observation:** metrics cluster tightly within each theme (technical accuracy in Theme 1/3, survey
reliability in Theme 2, financial value in Theme 5) but no study in the reviewed set reports a metric
that spans both technical and human judgement dimensions of the same risk assessment.

## 6. Research Gap Analysis

Three structural gaps are consistent across the 40 reviewed studies:

1. **Real world validation gap.** Most OT/ICS, fuzzy and AI/LLM models (e.g. Zahran et al., 2026; Noor
   et al., 2025; Iyenghar et al., 2026) are tested only in simulation or against benchmark datasets, not
   in live operational environments.
2. **Human technical integration gap.** Human vulnerabilities are consistently the most cited risk
   category (Aljumaiah et al., 2025), yet human factor studies (Theme 2) are validated almost entirely
   through self report and are analysed separately from the technical frameworks in Theme 1. The
   AI/LLM studies in Theme 3 sit closest to bridging this divide but evaluate automation on its own
   technical accuracy, not on how it changes human risk judgement (Mohsin et al., 2025; Chhetri et
   al., 2024; El-Hajj & Mirza, 2024).
3. **No common risk quantification standard.** Studies report accuracy scores, maturity levels,
   CVaR estimates and bibliometric counts that are not mutually comparable (Theme 5), making it
   difficult to benchmark cyber risk the way financial risk is benchmarked.

**Selected gap for this proposal:** Gap 2 — the human technical integration gap — is adopted as the
primary research gap. It is well evidenced (present across roughly 15 of the 40 reviewed studies),
is assessment oriented rather than build oriented, and fits Group H's suggested Chapter 3
methodology (Threat Modelling and Risk Assessment, or Case Study, per the Research Methodology
Selection Handbook).

## 7. References Supporting the Proposed Methodology

The following studies most directly support a Threat Modelling and Risk Assessment / Case Study
approach for Group H, and should be cross checked against Chapter 3 once the group finalises the
methodology:

- Tatavarthi, A. P. K., & Panigrahi, B. K. (2023). *Cyber security of an industrial IoT gateway device
  a threat model view and security aspects.* IET Conference Proceedings, 2023(6), 3440-3444.
  https://doi.org/10.1049/icp.2023.0828
- Shaked, A., Cherdantseva, Y., Burnap, P., & Maynard, P. (2023). *Operations informed incident
  response playbooks.* Computers & Security, 134, 103454. https://doi.org/10.1016/j.cose.2023.103454
- Kanamaru, H., Fujita, J., & Arai, T. (2023). *A study on the classification of OT security risk
  mitigation measures.* 2023 62nd Annual Conference of the SICE, 274-279.
  https://doi.org/10.23919/sice59929.2023.10354205
- Mohsin, A., Janicke, H., Ibrahim, A., Sarker, I. H., & Camtepe, S. (2025). *A unified framework for
  human AI collaboration in security operations centers with trusted autonomy.* ACM Transactions on
  Internet Technology. https://arxiv.org/abs/2505.23397
- Aljumaiah, O., Jiang, W., Reddy Addula, S., & Amin Almaiah, M. (2025). *Analyzing cybersecurity
  risks and threats in IT infrastructure based on NIST framework.* Journal of Cyber Security and
  Risk Auditing, 2025(2), 12-26. https://doi.org/10.63180/jcsra.thestap.2025.2.2

*(Full reference list for all 40 papers is maintained in `07_References/`.)*
