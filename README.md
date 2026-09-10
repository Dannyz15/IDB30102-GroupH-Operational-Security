# An Integrated Technical and Human Factor Risk Assessment Module for Operational Security

## Group Information
- **Group Number:** H
- **Research Area:** Operational Security
- **Group Members and Student IDs:**
  - Muhammad Danial Bin Mohd Zaki (52215225204)
  - Tuan Muhammad Faris Bin Tuan Zukiman (52215225169)
  - Haziq Danial Bin Nor Azan (52215225213)
  - Azimudeen Bin Azahari (52215225421)

## Research Problem
Existing operational security risk assessment frameworks (e.g., NIST CSF, OCTAVE Allegro, fuzzy logic and probabilistic models) evaluate technical vulnerabilities and human factor risks (stress, burnout, security awareness) separately. Human factor risk is typically measured through subjective, self reported instruments that cannot be directly compared with objective technical risk scores, leaving organisations without a unified, comparable view of overall operational security posture.

## Research Aim
To develop an integrated operational security risk assessment approach that combines technical vulnerability indicators with human factor risk indicators into a single, measurable risk assessment model.

## Research Objectives
1. To identify and categorise the technical and human factor risk indicators most commonly used in existing operational security risk assessment studies.
2. To design an integrated risk assessment framework/model that combines technical vulnerability data with human factor behavioural indicators.
3. To evaluate the proposed integrated framework against existing single dimension (technical only or human only) risk assessment approaches.

## Proposed Solution (Brief Description)
This research proposes an integrated risk assessment framework that maps and combines technical vulnerability indicators (e.g., threat exposure, control maturity) with human factor behavioural indicators (e.g., security awareness scores, stress/fatigue indicators) drawn from existing literature and secondary/case evidence. A prototype scoring module (Integrated Operational Risk Score, IORS) is developed to demonstrate the feasibility of the integration approach, and is evaluated through comparative analysis against existing single dimension frameworks (e.g., NIST CSF, OCTAVE Allegro) rather than through live deployment.

## Selected Methodology and Development Model
- **Research Methodology:** Threat Modelling and Risk Assessment (NIST SP 800-30, STRIDE threat modelling), using secondary evidence from the group's 40 paper Systematic Literature Review
- **Development Model:** Prototyping - a proof of concept Integrated Operational Risk Score (IORS) scoring module is developed to demonstrate the feasibility of combining technical and human factor risk indicators into a single score.

## Proposed Evaluation Plan
- **Baseline:** Existing single dimension risk assessment frameworks (e.g., NIST CSF, OCTAVE Allegro) as reported in the literature.
- **Dataset / Test Environment:** Case based scenarios constructed from secondary data and published figures drawn from the group's Assignment 1 systematic literature review (2022-2026). No live system or human subject data is used.
- **Evaluation Metrics:** Comparative coverage and granularity of the IORS output against existing single dimension frameworks' reported outcomes.

## Proposed System Architecture
See `03_Architecture_and_Flowchart/` for the proposed architecture diagram (Figure 3.1) and process flowchart illustrating how technical and human factor indicators are normalised, weighted and combined into a single Integrated Operational Risk Score (IORS).

## Description of Technical Components
This repository contains both research/design materials and a working prototype scoring module:
- Literature and paper summaries supporting the identified research gap
- Comparative analysis tables of existing technical vs. human factor risk frameworks
- Proposed architecture diagram and process flowchart
- Prototype Python module (`RiskArea` and `IntegratedRiskAssessment` classes) that normalises technical and human factor risk scores, computes an Integrated Operational Risk Score (IORS), assigns a priority level, and recommends controls from a control library
- Supporting references and secondary data descriptions

## Programming Languages, Software, Frameworks, Tools
- **Language:** Python 3
- **Libraries:** Python standard library only (`dataclasses`, `typing`, `csv`, `json`)
- **Diagramming tool:** [tool used for Figure 3.1 / flowchart, e.g. draw.io / Lucidchart / Microsoft Visio]

## Instructions for Executing Preliminary Code
1. Ensure Python 3.x is installed.
2. Navigate to `04_Source_Code/`.
3. Run the script directly, e.g. `python risk_assessment.py`, to see example `RiskArea` objects normalised and scored via `IntegratedRiskAssessment`.
4. No external dependencies or installation steps are required - the prototype uses only Python's standard library.

## Repository Structure
```
IDB30102_GroupH_OperationalSecurity/
│
├── README.md
├── 01_Research_Papers/
├── 02_Literature_Review/
├── 03_Architecture_and_Flowchart/
├── 04_Source_Code/
├── 05_Data_or_Sample_Input/
├── 06_Results_or_Expected_Output/
└── 07_References/
```

## Mapping Technical Work to Research Objectives
| Research Objective | Supporting Component | GitHub Location |
|---|---|---|
| RO1 | Identify existing technical and human-factor risk indicators | `01_Research_Papers/`, `02_Literature_Review/` |
| RO2 | Design and prototype the integrated risk assessment framework | `03_Architecture_and_Flowchart/`, `04_Source_Code/` |
| RO3 | Evaluate against existing single-dimension frameworks | `05_Data_or_Sample_Input/`, `06_Results_or_Expected_Output/` |