"""
Enterprise Risk Assessment Matrix & Scoring Engine
Aligning ISO/IEC 27001:2022 and NIST SP 800-53 Control Frameworks
"""

class RiskCalculator:
    def __init__(self, likelihood: int, impact: int, control_factor: float = 1.0):
        """
        Likelihood: 1 (Rare) to 5 (Almost Certain)
        Impact: 1 (Negligible) to 5 (Critical)
        Control Factor: 0.0 (Fully Mitigated) to 1.0 (No Controls)
        """
        self.likelihood = max(1, min(5, likelihood))
        self.impact = max(1, min(5, impact))
        self.control_factor = max(0.0, min(1.0, control_factor))

    def calculate_inherent_risk(self) -> int:
        """Computes Inherent Risk score without mitigations."""
        return self.likelihood * self.impact

    def compute_residual_risk(self) -> float:
        """Computes Residual Risk score factoring in control effectiveness."""
        inherent = self.calculate_inherent_risk()
        residual = inherent * self.control_factor
        return round(residual, 2)

    def get_risk_level(self) -> str:
        """Categorizes residual risk into compliance risk tiers."""
        score = self.compute_residual_risk()
        if score >= 20:
            return "CRITICAL - Immediate ISO 27001 Non-Conformity Risk"
        elif score >= 12:
            return "HIGH - Requires NIST SP 800-53 Remediation Plan"
        elif score >= 6:
            return "MEDIUM - Acceptable with Continuous Monitoring"
        else:
            return "LOW - Minimal Risk Exposure"


if __name__ == "__main__":
    # Test sample assessment
    sample_risk = RiskCalculator(likelihood=4, impact=5, control_factor=0.6)
    print(f"Inherent Risk Score: {sample_risk.calculate_inherent_risk()}")
    print(f"Residual Risk Score: {sample_risk.compute_residual_risk()}")
    print(f"Risk Rating: {sample_risk.get_risk_level()}")
