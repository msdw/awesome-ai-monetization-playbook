#!/usr/bin/env python3
"""Discover new AI offer candidates from public sources."""
import sys
import json
import argparse
import datetime
import time
from pathlib import Path
from urllib.request import urlopen, Request

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

HN_SEARCH_API = "https://hn.algolia.com/api/v1"
GITHUB_API = "https://api.github.com"


def fetch_json(url):
    try:
        req = Request(url, headers={"User-Agent": "awesome-ai-monetization/1.0"})
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  Fetch error: {e}", file=sys.stderr)
        return None


def load_active_sources() -> dict:
    """Load active sources from data/sources.yaml."""
    try:
        import yaml
        sources_path = DATA / "sources.yaml"
        if not sources_path.exists():
            return {"github": [], "hn": []}
        with open(sources_path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        github_queries, hn_queries = [], []
        for src in data.get("sources", {}).values():
            if src.get("status", "active") != "active":
                continue
            if src.get("type") == "github" and "search_query" in src:
                github_queries.append(src["search_query"])
            elif src.get("type") == "hn" and "search_query" in src:
                hn_queries.append(src["search_query"])
        return {"github": github_queries, "hn": hn_queries}
    except Exception as e:
        print(f"  Warning: could not load sources.yaml: {e}", file=sys.stderr)
        return {"github": [], "hn": []}


def discover_from_github(mode):
    print("\n[GitHub] Searching AI monetization repos...")
    candidates = []
    days = 7 if mode == "weekly" else 1
    since = (datetime.datetime.utcnow() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")

    active = load_active_sources()
    queries = active["github"] if active["github"] else ["saas pricing OR ai monetization language:python"]
    queries = list(dict.fromkeys(queries))

    seen_repos: set = set()
    for query in queries:
        url = f"{GITHUB_API}/search/repositories?q={query.replace(' ', '+')}+created:>{since}&sort=stars&per_page=10"
        data = fetch_json(url)
        if not data:
            time.sleep(1)
            continue
        for repo in data.get("items", []):
            name = repo.get("full_name", "")
            if name in seen_repos:
                continue
            stars = repo.get("stargazers_count", 0)
            if stars < 30:
                continue
            desc = repo.get("description") or "No description"
            candidates.append({
                "id": f"candidate_gh_{name.replace('/', '_').lower()}",
                "title": repo.get("name", ""),
                "summary": desc[:120],
                "monetization_models": ["subscription_saas"],
                "target_buyers": ["developer"],
                "target_users": ["developer"],
                "industries": ["software_dev"],
                "pain_points": ["See repository"],
                "value_delivered": ["See repository"],
                "offer_scope": {"included": ["See README"], "excluded": []},
                "pricing_hypotheses": {"min": None, "max": None, "currency": "USD", "notes": ""},
                "delivery_process": ["See repository"],
                "sales_channels": ["community"],
                "validation_steps": ["Review README and issues"],
                "risks": [],
                "scoring": {
                    "pain_intensity": 5, "willingness_to_pay": 5, "ai_fit": 7,
                    "buildability": 6, "market_signal": stars // 100,
                    "differentiation_potential": 5, "monetization_potential": 5,
                    "compliance_risk": 3
                },
                "tags": repo.get("topics", [])[:5] or ["automation"],
                "source": repo.get("html_url", ""),
                "status": "candidate",
                "_meta": {"stars": stars, "source": "github", "query": query,
                          "discovered_at": datetime.datetime.utcnow().isoformat()}
            })
            seen_repos.add(name)
            print(f"  {name} ({stars} stars)")
        time.sleep(0.3)
    return candidates


def discover_from_hn(mode):
    print("\n[HN] Searching for AI service/offer posts...")
    candidates = []
    days = 7 if mode == "weekly" else 1
    from_ts = int((datetime.datetime.utcnow() - datetime.timedelta(days=days)).timestamp())

    active = load_active_sources()
    hn_queries = active["hn"] if active["hn"] else [
        "AI service pricing", "freelance AI", "AI consulting offer"
    ]
    hn_queries = list(dict.fromkeys(hn_queries))

    seen_ids: set = set()
    for kw in hn_queries:
        url = f"{HN_SEARCH_API}/search?query={kw.replace(' ', '+')}&numericFilters=created_at_i>{from_ts}&hitsPerPage=10"
        data = fetch_json(url)
        if not data:
            continue
        for hit in data.get("hits", []):
            obj_id = hit.get("objectID", "")
            if obj_id in seen_ids:
                continue
            points = hit.get("points", 0)
            if points < 10:
                continue
            title = hit.get("title", "")
            story_url = hit.get("url") or f"https://news.ycombinator.com/item?id={obj_id}"
            candidates.append({
                "id": f"candidate_hn_{obj_id}",
                "title": title,
                "summary": f"Discovered from HN: {title}",
                "monetization_models": ["productized_service"],
                "target_buyers": ["smb_owner"],
                "target_users": ["consultant"],
                "industries": ["marketing"],
                "pain_points": ["See source"],
                "value_delivered": ["See source"],
                "offer_scope": {"included": ["See source"], "excluded": []},
                "pricing_hypotheses": {"min": None, "max": None, "currency": "USD",
                                       "notes": f"Source: {story_url}"},
                "delivery_process": ["See source"],
                "sales_channels": ["community"],
                "validation_steps": ["Review source post"],
                "risks": [],
                "scoring": {
                    "pain_intensity": 5, "willingness_to_pay": 5, "ai_fit": 6,
                    "buildability": 7, "market_signal": min(10, points // 15),
                    "differentiation_potential": 5, "monetization_potential": 5,
                    "compliance_risk": 3
                },
                "tags": ["b2b"],
                "source": story_url,
                "status": "candidate",
                "_meta": {"points": points, "source": "hacker_news", "query": kw,
                          "discovered_at": datetime.datetime.utcnow().isoformat()}
            })
            seen_ids.add(obj_id)
            print(f"  {title[:70]} ({points} pts)")
        time.sleep(0.5)
    return candidates


def save_candidates(candidates, dry_run):
    if not candidates:
        print("No candidates found")
        return
    print(f"Found {len(candidates)} candidates")
    if dry_run:
        return

    import yaml
    path = DATA / "offers.yaml"
    data = {}
    if path.exists():
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    existing_ids = {o["id"] for o in data.get("offers", [])}
    new = [c for c in candidates if c["id"] not in existing_ids]
    if not new:
        print("All candidates already exist")
        return
    data.setdefault("offers", []).extend(new)
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    print(f"Added {len(new)} new candidates")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["weekly", "daily"], default="weekly")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print(f"=== Discovering new offers (mode={args.mode}) ===")
    candidates = []
    candidates.extend(discover_from_github(args.mode))
    candidates.extend(discover_from_hn(args.mode))
    save_candidates(candidates, args.dry_run)
    print("Done")


if __name__ == "__main__":
    main()
