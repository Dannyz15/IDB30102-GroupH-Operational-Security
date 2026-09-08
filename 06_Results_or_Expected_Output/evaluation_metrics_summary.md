# Evaluation Metrics Summary

This summarises the three evaluation metrics defined in Chapter 3, Section 3.10 (Proposed
Evaluation Plan) of the Research Proposal, applied to the illustrative output in
`expected_iors_output_sample.csv`.

## 1. Risk-Coverage Comprehensiveness

Counts the number and type of distinct risk dimensions (technical, human-factor) captured
by each scoring approach. Single-dimension baselines (NIST CSF, OCTAVE Allegro) capture
only the technical dimension (1 risk-indicator type); the proposed IORS captures both
technical and human-factor dimensions (2 risk-indicator types) for every case.

## 2. Granularity

Assesses whether a scoring approach can distinguish between cases that appear similar on
technical indicators alone but differ on human-factor indicators. For example, CASE-03 shows
a high technical-only score (0.90 NIST CSF) but a comparatively lower IORS (0.68) once low
behavioural-data reliability is factored in -- a distinction the single-dimension baselines cannot
make.

## 3. Comparative Consistency

Checks whether IORS outputs move in the expected direction relative to the underlying case
evidence (e.g., a case with both high technical exposure and high security fatigue should
produce a comparatively higher combined risk signal than a case with only one dimension
elevated).

These three metrics collectively support answering Research Objective 3 (RO3): evaluating
the proposed integrated framework against existing single-dimension risk assessment
approaches.
