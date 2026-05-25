#!/usr/bin/env python3
"""Compute composite scores for accepted offers."""
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

WEIGHTS = {
    "pain_intensity": 0.20,
    "willingness_to_pay": 0.20,
    "ai_fit": 0.15,
    "buildability": 0.15,
    "market_signal": 0.10,
    "differentiation_potential": 0.10,
    "monetization_potential": 0.05,
    "compliance_risk": 0.05,
}


def composite(scoring):
    total = 0.0
    for field, weight in WEIGHTS.items():
        val = scoring.get(field, 5)
        if field == "compliance_risk":
            val = 11 - val
        total += val * weight
    return round(total, 2)


def main():
    path = DATA / "offers.yaml"
    if not path.exists():
        print("offers.yaml not found")
        return
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    updated = 0
    for offer in data.get("offers", []):
        if offer.get("scoring"):
            offer["composite_score"] = composite(offer["scoring"])
            updated += 1
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    print(f"Updated {updated} offer scores")
    offers = [o for o in data.get("offers", []) if "composite_score" in o]
    offers.sort(key=lambda x: x["composite_score"], reverse=True)
    print("\nTop offers by score:")
    for o in offers[:5]:
        print(f"  {o['composite_score']:.2f}  {o['title'][:70]}")


if __name__ == "__main__":
    main()
