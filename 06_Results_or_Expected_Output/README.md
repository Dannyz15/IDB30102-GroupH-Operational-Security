# 06_Results_or_Expected_Output

## Overview

Since the Development Model is now **Prototyping** (Chapter 3, Section 3.3) and a working
preliminary tool has been built (`04_Source_Code/integrated_risk_assessment.py`), this folder
contains the **actual output produced by running that prototype** on the sample input in
`05_Data_or_Sample_Input/prototype_input_sample.csv`, rather than purely hypothetical
figures. This demonstrates the technical feasibility of the proposed Integrated Operational
Risk Score (IORS) approach at proof-of-concept level, consistent with the proposal-stage
scope (Chapter 1, Section 1.6) -- no live or organisational deployment is involved.

## How this output was generated

Running the prototype (`python integrated_risk_assessment.py`) with the four sample risk
areas produces an Integrated Risk Score per area (`R_overall = wT*R_T + wH*R_H`, with
wT = wH = 0.5), a priority classification (High / Medium / Low), and recommended controls
per area. The console report, CSV and JSON outputs below are the direct, unedited output of
that run.

## Files in this folder

| File | Description |
|---|---|
| `risk_report.csv` | Actual prototype output -- integrated risk score, priority and recommended controls per risk area |
| `risk_report.json` | Same output in JSON format |
| `console_report_sample.txt` | Console report output from running the prototype |
| `comparison_vs_baseline.md` | Comparison of the prototype's integrated scoring approach against single-dimension baselines (NIST CSF, OCTAVE Allegro), per the Evaluation Plan (Chapter 3, Section 3.9) |
| `evaluation_metrics_summary.md` | Description of the three evaluation metrics used to assess the framework (Chapter 3, Section 3.9) |

## Sample Result (from actual prototype run)

| Risk Area | Technical | Human | Integrated | Priority |
|---|---|---|---|---|
| Access Control | 75% | 60% | 67.5% | High |
| Phishing | 45% | 85% | 65.0% | High |
| Data Handling | 40% | 75% | 57.5% | Medium |
| Patch Management | 80% | 30% | 55.0% | Medium |

Note that Phishing ranks as **High** priority under the integrated score despite a
comparatively low technical score (45%) -- a distinction a technical-only baseline (e.g., NIST
CSF scoring on technical indicators alone) would miss, illustrating the added value of
combining both dimensions (Research Objective 3).

## Note

This is preliminary, proof-of-concept output from a prototype-stage tool, not a validated
production system, consistent with the proposal-stage scope defined in Chapter 1.
