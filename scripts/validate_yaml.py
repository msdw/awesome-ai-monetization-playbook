#!/usr/bin/env python3
"""Validate all YAML data files against required schema."""
import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

REQUIRED_OFFER_FIELDS = [
    "id", "title", "summary", "monetization_models",
    "target_buyers", "target_users", "industries",
    "pain_points", "value_delivered", "offer_scope",
    "pricing_hypotheses", "delivery_process", "sales_channels",
    "validation_steps", "scoring", "tags", "source", "status"
]

REQUIRED_SCORING_FIELDS = [
    "pain_intensity", "willingness_to_pay", "ai_fit", "buildability",
    "market_signal", "differentiation_potential", "monetization_potential",
    "compliance_risk"
]

VALID_STATUSES = {"candidate", "needs_review", "accepted", "rejected", "duplicate", "deprecated"}
REGULATED_INDUSTRIES = {"legal", "healthcare", "finance", "insurance"}

ERRORS = []
WARNINGS = []


def error(msg):
    ERRORS.append(msg)
    print(f"  ERROR: {msg}", file=sys.stderr)


def warn(msg):
    WARNINGS.append(msg)
    print(f"  WARN:  {msg}")


def load_yaml(path):
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        error(f"YAML parse error in {path.name}: {e}")
        return None
    except FileNotFoundError:
        error(f"File not found: {path}")
        return None


def validate_offers(path):
    print(f"\nValidating {path.name}...")
    data = load_yaml(path)
    if not data:
        return
    offers = data.get("offers", [])
    seen_ids = set()
    for i, offer in enumerate(offers):
        prefix = f"offers[{i}] id={offer.get('id', '?')}"
        oid = offer.get("id")
        if oid in seen_ids:
            error(f"{prefix}: duplicate id '{oid}'")
        seen_ids.add(oid)

        for field in REQUIRED_OFFER_FIELDS:
            if field not in offer:
                error(f"{prefix}: missing required field '{field}'")

        status = offer.get("status")
        if status and status not in VALID_STATUSES:
            error(f"{prefix}: invalid status '{status}'")

        # Check pricing source
        pricing = offer.get("pricing_hypotheses", {})
        if isinstance(pricing, dict):
            if not pricing.get("notes"):
                warn(f"{prefix}: pricing_hypotheses.notes missing — should cite source")

        # Scoring
        scoring = offer.get("scoring", {})
        for sf in REQUIRED_SCORING_FIELDS:
            if sf not in scoring:
                error(f"{prefix}: missing scoring.{sf}")
            else:
                val = scoring[sf]
                if not isinstance(val, (int, float)) or not (1 <= val <= 10):
                    error(f"{prefix}: scoring.{sf}={val} must be 1-10")

        # Regulated domain compliance
        industries = offer.get("industries", [])
        if any(ind in REGULATED_INDUSTRIES for ind in industries):
            if not offer.get("compliance_notes"):
                error(f"{prefix}: regulated industry — compliance_notes required")

    print(f"  Checked {len(offers)} offers")


def validate_taxonomy(path, key):
    print(f"\nValidating {path.name}...")
    data = load_yaml(path)
    if not data:
        return set()
    items = data.get(key, [])
    print(f"  Found {len(items)} entries")
    return {item.get("id") for item in items if "id" in item}


def main():
    print("=== Validating YAML schemas ===")

    for fname, key in [
        ("monetization_models.yaml", "monetization_models"),
        ("industries.yaml", "industries"),
        ("buyers.yaml", "buyers"),
        ("channels.yaml", "channels"),
        ("delivery_models.yaml", "delivery_models"),
        ("pricing_patterns.yaml", "pricing_patterns"),
        ("risks.yaml", "risks"),
        ("tags.yaml", "tags"),
    ]:
        p = DATA / fname
        if p.exists():
            validate_taxonomy(p, key)

    if (DATA / "offers.yaml").exists():
        validate_offers(DATA / "offers.yaml")

    print(f"\n=== Summary ===\n  Errors: {len(ERRORS)}  Warnings: {len(WARNINGS)}")
    if ERRORS:
        print("\nFAILED", file=sys.stderr)
        sys.exit(1)
    else:
        print("\nPASSED")


if __name__ == "__main__":
    main()
