"""
Integrated Technical and Human-Factor Risk Assessment Prototype
=================================================================

Implements:
    R_overall = wT * R_T + wH * R_H

where R_T = Technical Risk Score, R_H = Human-Factor Risk Score,
wT / wH = weights assigned to each dimension (wT + wH = 1).

Pipeline:
    Organisation/Department -> Technical Assessment -> Human Assessment
    -> Integrated Risk Score -> Risk Ranking -> Recommended Controls -> Risk Report

Usage:
    python integrated_risk_assessment.py
"""

from dataclasses import dataclass, field
from typing import List, Dict
import csv
import json


# ---------------------------------------------------------------------------
# 1. Data model
# ---------------------------------------------------------------------------

@dataclass
class RiskArea:
    """A single risk area assessed on both technical and human dimensions."""
    name: str
    technical_risk: float      # R_T, 0-100 (raw or already-normalized)
    human_risk: float          # R_H, 0-100
    technical_raw_scale: float = 100.0   # set if input isn't already 0-100
    human_raw_scale: float = 100.0
    integrated_risk: float = field(default=0.0, init=False)
    priority: str = field(default="", init=False)
    controls: List[str] = field(default_factory=list, init=False)

    def normalize(self) -> None:
        """Normalize raw scores onto a common 0-100 scale."""
        self.technical_risk = (self.technical_risk / self.technical_raw_scale) * 100
        self.human_risk = (self.human_risk / self.human_raw_scale) * 100


# ---------------------------------------------------------------------------
# 2. Core scoring engine
# ---------------------------------------------------------------------------

class IntegratedRiskAssessment:
    """
    Combines technical and human-factor risk into a single integrated score,
    ranks each risk area by priority, and attaches recommended controls.
    """

    # Priority thresholds on the 0-100 integrated scale
    HIGH_THRESHOLD = 65
    MEDIUM_THRESHOLD = 40

    # Example control library — extend per your Chapter 1 scope
    CONTROL_LIBRARY: Dict[str, List[str]] = {
        "Access Control": [
            "Enforce multi-factor authentication (MFA)",
            "Apply least-privilege role-based access control",
            "Conduct quarterly access rights review",
        ],
        "Phishing": [
            "Run recurring phishing simulation & awareness training",
            "Deploy email authentication (SPF/DKIM/DMARC)",
            "Enable click-time URL protection",
        ],
        "Patch Management": [
            "Automate patch deployment with staged rollout",
            "Maintain an asset/vulnerability inventory (CMDB)",
            "Set SLA for critical patch application (e.g. 72 hours)",
        ],
        "Data Handling": [
            "Classify and label data by sensitivity",
            "Enforce DLP (Data Loss Prevention) policies",
            "Mandatory data-handling training for staff",
        ],
    }

    def __init__(self, weight_technical: float = 0.5, weight_human: float = 0.5):
        if not abs((weight_technical + weight_human) - 1.0) < 1e-6:
            raise ValueError("weight_technical + weight_human must equal 1.0")
        self.wT = weight_technical
        self.wH = weight_human
        self.risk_areas: List[RiskArea] = []

    def add_risk_area(self, area: RiskArea, normalize: bool = False) -> None:
        if normalize:
            area.normalize()
        self.risk_areas.append(area)

    def _classify_priority(self, score: float) -> str:
        if score >= self.HIGH_THRESHOLD:
            return "High"
        elif score >= self.MEDIUM_THRESHOLD:
            return "Medium"
        return "Low"

    def compute(self) -> None:
        """Run R_overall = wT*R_T + wH*R_H for every risk area, then rank."""
        for area in self.risk_areas:
            area.integrated_risk = round(
                self.wT * area.technical_risk + self.wH * area.human_risk, 1
            )
            area.priority = self._classify_priority(area.integrated_risk)
            area.controls = self.CONTROL_LIBRARY.get(
                area.name, ["Review area-specific controls (not in library)"]
            )

        # Highest risk first
        self.risk_areas.sort(key=lambda a: a.integrated_risk, reverse=True)

    # -----------------------------------------------------------------
    # 3. Reporting
    # -----------------------------------------------------------------

    def to_table(self) -> str:
        header = f"{'Risk Area':<20}{'Technical':>10}{'Human':>10}{'Integrated':>12}{'Priority':>10}"
        lines = [header, "-" * len(header)]
        for a in self.risk_areas:
            lines.append(
                f"{a.name:<20}{a.technical_risk:>9.0f}%{a.human_risk:>9.0f}%"
                f"{a.integrated_risk:>11.1f}%{a.priority:>10}"
            )
        return "\n".join(lines)

    def to_csv(self, path: str) -> None:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["Risk Area", "Technical Risk (%)", "Human Risk (%)",
                 "Integrated Risk (%)", "Priority", "Recommended Controls"]
            )
            for a in self.risk_areas:
                writer.writerow(
                    [a.name, f"{a.technical_risk:.0f}", f"{a.human_risk:.0f}",
                     f"{a.integrated_risk:.1f}", a.priority, "; ".join(a.controls)]
                )

    def to_json(self, path: str) -> None:
        data = [
            {
                "risk_area": a.name,
                "technical_risk": round(a.technical_risk, 1),
                "human_risk": round(a.human_risk, 1),
                "integrated_risk": a.integrated_risk,
                "priority": a.priority,
                "recommended_controls": a.controls,
            }
            for a in self.risk_areas
        ]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def report(self, org_name: str = "Organisation") -> str:
        lines = [
            f"Integrated Operational Security Risk Report — {org_name}",
            "=" * 60,
            f"Formula: R_overall = wT*R_T + wH*R_H  "
            f"(wT={self.wT}, wH={self.wH})",
            "",
            self.to_table(),
            "",
            "Recommended Controls (by priority):",
        ]
        for a in self.risk_areas:
            lines.append(f"\n[{a.priority}] {a.name} ({a.integrated_risk:.1f}%)")
            for c in a.controls:
                lines.append(f"    - {c}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# 4. Example run — mirrors the sample table from the research proposal
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # wT / wH can be tuned per organisation risk appetite (e.g. more weight
    # on human factors if the org has had recent social-engineering incidents)
    assessment = IntegratedRiskAssessment(weight_technical=0.5, weight_human=0.5)

    assessment.add_risk_area(RiskArea(name="Access Control", technical_risk=75, human_risk=60))
    assessment.add_risk_area(RiskArea(name="Phishing", technical_risk=45, human_risk=85))
    assessment.add_risk_area(RiskArea(name="Patch Management", technical_risk=80, human_risk=30))
    assessment.add_risk_area(RiskArea(name="Data Handling", technical_risk=40, human_risk=75))

    assessment.compute()

    print(assessment.report(org_name="Sample Organisation"))

    assessment.to_csv("risk_report.csv")
    assessment.to_json("risk_report.json")
    print("\nSaved: risk_report.csv, risk_report.json")
