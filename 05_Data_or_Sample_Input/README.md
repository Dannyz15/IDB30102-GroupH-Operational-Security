# 05_Data_or_Sample_Input

## Overview

With the Development Model now set to **Prototyping** (Chapter 3, Section 3.3), a working
preliminary tool has been developed (see `04_Source_Code/`) that takes technical and
human-factor risk scores as input and computes an Integrated Operational Risk Score (IORS)
for each risk area. This folder contains the sample input consumed by that prototype, plus
the secondary-literature indicator categories that informed how the input values were
derived.

Consistent with the Scope of the Research (Chapter 1, Section 1.6), no live or organisational
data is used. All input values are illustrative, constructed from the technical and
human-factor indicator layers identified in the group's Systematic Literature Review
(Assignment 1) and presented in Figure 3.1.

## Files in this folder

| File | Description |
|---|---|
| `prototype_input_sample.csv` | Sample input in the exact schema consumed by the prototype (`04_Source_Code/integrated_risk_assessment.py`) -- risk area name, technical risk score (0-100), human-factor risk score (0-100) |
| `technical_indicators_reference.csv` | Technical risk indicator categories and format drawn from the literature (Perdana et al., 2022; Zahran et al., 2026), used to inform realistic technical_risk values |
| `human_factor_indicators_reference.csv` | Human-factor risk indicator categories and format drawn from the literature (Nobles, 2022; Shah et al., 2023), used to inform realistic human_risk values |

## Input Schema (matches `RiskArea` in the prototype)

| Field | Type | Description |
|---|---|---|
| `name` | text | Risk area label (e.g., Access Control, Phishing, Patch Management, Data Handling) |
| `technical_risk` | 0-100 | Technical vulnerability/exposure score for this risk area |
| `human_risk` | 0-100 | Human-factor (awareness/stress/fatigue) score for this risk area |

## Original Data Sources

- Perdana, A., et al. (2022). NIST SP 800-26/800-30 based maturity assessment -- basis for
  technical_risk scaling
- Nobles, C. (2022). Human performance taxonomy -- stress, burnout, security fatigue -- basis
  for human_risk scaling
- Shah, F., et al. (2023). Cross-cultural security awareness survey -- basis for awareness
  scoring format

Full citation details are in `07_References/`.

## Note

Input values are illustrative and proposal-stage only, in line with Chapter 1 Scope (Section
1.6): no live or organisation-identifying data is included.
