# Evaluation Metrics Summary

This summarises the three evaluation metrics defined in Chapter 3, Section 3.9 (Proposed
Evaluation Plan), applied to the actual prototype output in `risk_report.csv` /
`risk_report.json`.

## 1. Risk-Coverage Comprehensiveness

A single-dimension baseline (NIST CSF / OCTAVE Allegro) captures only the technical
dimension for each risk area. The prototype's IORS captures both technical and human-factor
dimensions for all four risk areas, as shown in `comparison_vs_baseline.md`.

## 2. Granularity

The prototype distinguishes risk areas that a technical-only score would rank similarly, or
misrank. For example, Access Control (75% technical) and Patch Management (80% technical)
look similarly high-risk on a technical-only view, but the integrated score separates them
(67.5% vs 55.0%) once human-factor exposure is included.

## 3. Comparative Consistency

The integrated score moves in the expected direction relative to the underlying evidence: risk
areas with both elevated technical and human-factor scores (Access Control, Phishing) rank
highest; areas with a high score on only one dimension (Patch Management: technical-only;
Data Handling: human-factor-only) rank lower and closer together, consistent with the intent
of combining both dimensions rather than letting either dominate.

These three metrics collectively support Research Objective 3 (RO3): evaluating the proposed
integrated framework against existing single-dimension risk assessment approaches.
