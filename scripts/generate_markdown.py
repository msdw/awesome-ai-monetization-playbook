#!/usr/bin/env python3
"""Generate browseable index pages from YAML data."""
import argparse
import yaml
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OFFERS_DIR = ROOT / "offers"

HEADER = "<!-- AUTO-GENERATED — do not edit manually. Run: python scripts/generate_markdown.py -->\n\n"


def load_yaml(path):
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def write_page(path, content, check_only):
    path.parent.mkdir(parents=True, exist_ok=True)
    full = HEADER + content
    if path.exists() and path.read_text(encoding="utf-8") == full:
        return False
    if check_only:
        print(f"  WOULD WRITE: {path.relative_to(ROOT)}")
        return True
    path.write_text(full, encoding="utf-8")
    print(f"  WROTE: {path.relative_to(ROOT)}")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    print(f"=== {'Checking' if args.check else 'Generating'} Markdown pages ===")

    data = load_yaml(DATA / "offers.yaml")
    offers = [o for o in (data or {}).get("offers", []) if o.get("status") == "accepted"] if data else []
    print(f"Loaded {len(offers)} accepted offers")

    if offers:
        # By monetization model
        by_model = defaultdict(list)
        for offer in offers:
            for model in offer.get("monetization_models", ["other"]):
                by_model[model].append(offer)

        lines = ["# Offers by Monetization Model\n\n"]
        for model in sorted(by_model):
            lines.append(f"## {model.replace('_', ' ').title()}\n\n")
            for offer in by_model[model]:
                lines.append(f"- [{offer['title']}](../data/offers.yaml) — {offer.get('summary','')[:100].strip()}\n")
            lines.append("\n")
        write_page(OFFERS_DIR / "by-model.md", "".join(lines), args.check)

        # Index
        idx_lines = ["# All Offers\n\n"]
        for offer in offers:
            price = offer.get("pricing_hypotheses", {})
            price_str = ""
            if isinstance(price, dict) and price.get("min"):
                price_str = f" | ${price['min']}–${price['max']} {price.get('currency','USD')}"
            idx_lines.append(f"- [{offer['title']}](../data/offers.yaml){price_str}\n")
        write_page(OFFERS_DIR / "index.md", "".join(idx_lines), args.check)

    print("\nDone")


if __name__ == "__main__":
    main()
