#!/usr/bin/env python3
"""Discover public pricing signals for AI services from public sources."""
import sys
import json
import argparse
import datetime
import time
import re
from pathlib import Path
from urllib.request import urlopen, Request

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

HN_SEARCH_API = "https://hn.algolia.com/api/v1"

PRICE_PATTERN = re.compile(r'\$[\d,]+(?:k)?(?:\s*/\s*(?:month|mo|hr|hour|project|day))?', re.IGNORECASE)


def fetch_json(url):
    try:
        req = Request(url, headers={"User-Agent": "awesome-ai-monetization/1.0"})
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  Fetch error: {e}", file=sys.stderr)
        return None


def extract_price_signals(text):
    return PRICE_PATTERN.findall(text or "")


def discover_pricing_from_hn(mode):
    print("\n[HN] Searching for pricing signals...")
    signals = []
    days = 7 if mode == "weekly" else 1
    from_ts = int((datetime.datetime.utcnow() - datetime.timedelta(days=days)).timestamp())

    queries = [
        "AI service charge per month",
        "freelance AI rate",
        "AI consulting pricing",
        "LLM automation price",
    ]

    for q in queries:
        url = f"{HN_SEARCH_API}/search?query={q.replace(' ', '+')}&numericFilters=created_at_i>{from_ts}&hitsPerPage=10"
        data = fetch_json(url)
        if not data:
            continue
        for hit in data.get("hits", []):
            title = hit.get("title", "")
            text = (hit.get("story_text") or "") + " " + title
            prices = extract_price_signals(text)
            if prices:
                story_url = hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}"
                signals.append({
                    "title": title,
                    "prices_observed": prices,
                    "source": story_url,
                    "type": "observed_public_price",
                    "discovered_at": datetime.datetime.utcnow().isoformat()
                })
                print(f"  {title[:60]} — prices: {prices}")
        time.sleep(0.5)

    return signals


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["weekly", "daily"], default="weekly")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print(f"=== Discovering pricing signals (mode={args.mode}) ===")
    signals = discover_pricing_from_hn(args.mode)
    print(f"\nFound {len(signals)} pricing signal(s)")
    if args.dry_run:
        for s in signals:
            print(f"  {s['title'][:60]} → {s['prices_observed']}")
        return

    if signals:
        import yaml
        log_path = DATA / "updates_log.yaml"
        data = {}
        if log_path.exists():
            with open(log_path, encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
        data.setdefault("updates", []).append({
            "date": datetime.datetime.utcnow().isoformat(),
            "action": "pricing_signal_discovery",
            "signals_found": len(signals),
            "signals": signals[:10]
        })
        with open(log_path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        print(f"Logged {len(signals)} pricing signals to updates_log.yaml")

    print("Done")


if __name__ == "__main__":
    main()
