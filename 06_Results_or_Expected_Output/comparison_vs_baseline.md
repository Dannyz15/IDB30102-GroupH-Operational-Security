# Comparison vs. Single-Dimension Baseline

This compares the prototype's integrated scoring output against what a single-dimension
(technical-only) baseline such as NIST CSF or OCTAVE Allegro would show for the same four
risk areas, per the Evaluation Plan (Chapter 3, Section 3.9).

| Risk Area | Technical-Only Score (baseline) | Technical-Only Priority | Integrated Score (IORS) | Integrated Priority | Shift? |
|---|---|---|---|---|---|
| Access Control | 75% | High | 67.5% | High | No change |
| Phishing | 45% | Low/Medium | 65.0% | **High** | **Escalated** |
| Data Handling | 40% | Low | 57.5% | **Medium** | **Escalated** |
| Patch Management | 80% | High | 55.0% | **Medium** | **De-escalated** |

## Interpretation

- **Phishing** would be under-prioritised by a technical-only baseline (45% -> Low/Medium)
  despite a high human-factor score (85%, elevated security fatigue). The integrated
  framework correctly escalates it to **High** priority.
- **Patch Management** would be over-prioritised by a technical-only baseline (80% -> High)
  despite a low human-factor score (30%). The integrated framework moderates it to
  **Medium**, reflecting lower behavioural risk exposure.
- This demonstrates the core contribution of Research Objective 3: single-dimension
  frameworks can both under- and over-estimate risk priority when human-factor
  indicators are not incorporated, supporting the research gap established in Chapter 2
  (Section 2.6).

Full evaluation metrics are described in `evaluation_metrics_summary.md`.
