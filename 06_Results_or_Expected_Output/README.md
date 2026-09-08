# 06_Results_or_Expected_Output

## Overview

As confirmed by the course lecturer, this proposal-stage submission does **not** require a
complete working system. The expected output for this research area is a **comparative
analysis** rather than experimental results from a built system. This folder therefore contains
**illustrative / expected outputs only**, generated from the sample case-scenario input in
`05_Data_or_Sample_Input/`, to demonstrate the intended output format of the proposed
Integrated Operational Risk Score (IORS) framework (Chapter 3, Section 3.6, Figure 3.1).

## Expected Output Description

The proposed framework combines the technical and human-factor indicator layers through
an Indicator Normalisation and Weighting Engine (Chapter 3, Section 3.5, Phase 3) to produce
a single **Integrated Operational Risk Score (IORS)** per case. This IORS is then benchmarked
against two single-dimension baseline frameworks identified in Chapter 2:

- **NIST CSF** (technical-only scoring)
- **OCTAVE Allegro** (technical-only scoring)

## Files in this folder

| File | Description |
|---|---|
| `expected_iors_output_sample.csv` | Illustrative IORS output per case, compared against the two single-dimension baselines |
| `evaluation_metrics_summary.md` | Description of the three evaluation metrics used to assess the framework (Chapter 3, Section 3.10) |

## Evaluation Metrics (summary)

1. **Risk-Coverage Comprehensiveness** — number/type of risk indicators captured by IORS vs. baseline
2. **Granularity** — ability to distinguish risk levels across combined technical + human-factor dimensions
3. **Comparative Consistency** — whether IORS outputs align sensibly with case-scenario evidence

Full detail is provided in Chapter 3, Section 3.10 (Proposed Evaluation Plan) of the Research
Proposal.

## Note

Figures in this folder are **expected/illustrative outputs**, not final experimental results,
consistent with the proposal-stage scope and lecturer's clarification that a complete system
is not required.
