## 04_Source_Code

This folder will contain the source code and snippet of the source code. The snippet of the the source code contains the main logic of the Integrated Operational Risk Scoring system. 

```python
# R_overall = wT * R_T + wH * R_H

def compute_integrated_risk(technical_risk, human_risk, wT=0.5, wH=0.5):
    """Combine technical and human-factor risk into one score (0-100)."""
    integrated = wT * technical_risk + wH * human_risk
    if integrated >= 65:
        priority = "High"
    elif integrated >= 40:
        priority = "Medium"
    else:
        priority = "Low"
    return round(integrated, 1), priority


# Example
score, priority = compute_integrated_risk(technical_risk=75, human_risk=60)
print(score, priority)  # 67.5 High
```

The full implementation of the system including the priority ranking, recommended controls, CVS / JSON report export : [`integrated_risk_assessment.py`](./integrated_risk_assessment.py)
