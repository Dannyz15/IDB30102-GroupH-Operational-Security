# 05_Data_or_Sample_Input

## Overview

This research does not use a live, primary, or organisational dataset. Consistent with the
Scope of the Research (Chapter 1, Section 1.6) and the selected Threat Modelling and Risk
Assessment methodology (Chapter 3, Section 3.2), all input data is **secondary**, drawn from
the 40 peer-reviewed studies screened and catalogued in the group's Systematic Literature
Review (Assignment 1). No primary data collection from human respondents or live systems
is conducted.

Two parallel indicator layers are extracted from this secondary evidence base, consistent
with the architecture presented in Chapter 3 (Figure 3.1):

1. **Technical Indicator Layer** — vulnerability counts / CVSS scores, control maturity scores,
   attack-graph / threat-exposure probabilities
2. **Human-Factor Indicator Layer** — security awareness scores, stress / burnout indicators,
   self-reported behavioural data

## Files in this folder

| File | Description |
|---|---|
| `technical_indicators_sample.csv` | Illustrative technical risk indicators, format based on figures reported in Perdana et al. (2022) and Zahran et al. (2026) |
| `human_factor_indicators_sample.csv` | Illustrative human-factor risk indicators, format based on constructs in Nobles (2022) and Shah et al. (2023) |
| `case_scenario_input.csv` | Combined case-scenario input table used as illustrative input to the Indicator Normalisation and Weighting Engine (Chapter 3, Section 3.8, Stage 2) |

## Original Data Sources

- Perdana, A., et al. (2022). NIST SP 800-26/800-30 based maturity assessment. *(secondary
  figures used: vulnerability count, maturity score)*
- Zahran, M., et al. (2026). OCTAVE Allegro / ISO 27k simulation-based risk assessment for
  IT/OT environments. *(secondary figures used: risk simulation output)*
- Nobles, C. (2022). Human performance taxonomy — stress, burnout, security fatigue.
  *(construct basis for human-factor indicator categories)*
- Shah, F., et al. (2023). Cross-cultural security awareness survey (UAE/USA).
  *(construct basis for awareness scoring format)*

Full citation details are provided in `07_References/`.

## Note

No confidential, private, or organisation-identifying data is included in this folder. All figures
are illustrative, constructed from openly published findings for demonstration purposes only,
consistent with the proposal-stage scope defined in Chapter 1.
