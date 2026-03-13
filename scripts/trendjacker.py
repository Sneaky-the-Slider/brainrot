#!/usr/bin/env python3
# Trendjacker v2.0 - hyper-optimized zero-dep CLI (stdlib only)
# Steal Reddit trends → master Grok prompt → 10 viral hooks OR JSON feed
# Production-ready: UA spoof, rate-safe, ANSI UI, auto-save .md/.json
# Run: python trendjacker.py --subreddit popular --limit 20 --niche "affiliate marketing"
# JSON mode: python trendjacker.py --json --subreddit popular --limit 50
# Watch mode: python trendjacker.py --watch --interval 300 --subreddit popular

import sys
import urllib.request
import json
import argparse
import textwrap
import time
import os
from urllib.error import HTTPError, URLError
from datetime import datetime

def fetch_trends(subreddit: str, limit: int) -> list:
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    headers = {'User-Agent': 'Trendjacker/2.0 (Turbo edition)'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
        return [
            {
                'id': p['data']['id'],
                'title': p['data']['title'],
                'sub': p['data']['subreddit'],
                'score': p['data']['score'],
                'url': p['data']['url'],
                'selftext': (p['data'].get('selftext') or '')[:400],
                'author': p['data'].get('author', 'unknown'),
                'created_utc': p['data'].get('created_utc', 0),
                'num_comments': p['data'].get('num_comments', 0),
                'permalink': f"https://reddit.com{p['data'].get('permalink', '')}"
            }
            for p in data['data']['children']
        ]
    except (HTTPError, URLError, json.JSONDecodeError, KeyError) as e:
        print(f"\033[1;31m[!] Reddit fetch failed: {e}\033[0m", file=sys.stderr)
        sys.exit(1)

def build_master_prompt(trend: dict, niche: str) -> str:
    return textwrap.dedent(f"""\
        [TRENDJACKER v2.0 - ELITE GROK SYSTEM PROMPT]
        You are the ultimate viral hook architect. Steal this exploding Reddit trend and turn it into pure monetization gold.

        REDDIT TREND PAYLOAD:
        Title: {trend['title']}
        Subreddit: r/{trend['sub']}
        Upvotes: {trend['score']}
        Link: {trend['url']}
        Snippet: {trend['selftext'] or 'Image/video post - no text'}

        TARGET NICHE: {niche or 'general content creators'}

        INSTRUCTIONS:
        - Generate EXACTLY 10 ready-to-post hooks (X/Twitter, IG, LinkedIn, email, newsletter)
        - Each hook ≤ 280 chars, curiosity/FOMO driven, strong CTA
        - Optimized for virality + affiliate/product sales
        - Number 1-10, NO extra text, NO explanations
        - Make them so good they print money on autopilot

        OUTPUT ONLY THE 10 HOOKS:
        """)

def load_feed_db(filepath: str) -> dict:
    """Load existing feed database or create new one"""
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"meta": {"total_updates": 0, "seen_ids": []}, "trends": []}

def save_feed_db(db: dict, filepath: str):
    """Save feed database atomically"""
    tmp_file = filepath + '.tmp'
    with open(tmp_file, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2)
    os.replace(tmp_file, filepath)

def get_quote_of_the_day(trends: list) -> dict:
    """Select the most viral trend as quote of the day"""
    if not trends:
        return {
            "text": "No trends available",
            "author": "Reddit",
            "source": "r/popular"
        }

    top_trend = max(trends, key=lambda x: x.get('viral_score', 0))
    return {
        "text": top_trend['title'],
        "author": f"u/{top_trend['author']}",
        "source": f"r/{top_trend['subreddit']}",
        "score": top_trend['score'],
        "url": top_trend['reddit_url'],
        "date": datetime.now().strftime("%Y-%m-%d")
    }

def merge_trends(existing_db: dict, new_trends: list, subreddit: str) -> tuple:
    """Merge new trends into existing database, return (updated_db, new_count)"""
    seen_ids = set(existing_db['meta'].get('seen_ids', []))
    existing_trends = {t['id']: t for t in existing_db.get('trends', [])}

    new_count = 0
    for trend in new_trends:
        if trend['id'] not in seen_ids:
            existing_trends[trend['id']] = {
                "id": trend['id'],
                "title": trend['title'],
                "subreddit": trend['sub'],
                "score": trend['score'],
                "url": trend['url'],
                "snippet": trend['selftext'][:200] if trend['selftext'] else None,
                "author": trend['author'],
                "created": trend['created_utc'],
                "comments": trend['num_comments'],
                "reddit_url": trend['permalink'],
                "viral_score": min(100, int((trend['score'] / 1000) * 10)),
                "first_seen": int(time.time())
            }
            seen_ids.add(trend['id'])
            new_count += 1
        else:
            # Update score/comments if already exists
            existing_trends[trend['id']]['score'] = trend['score']
            existing_trends[trend['id']]['comments'] = trend['num_comments']
            existing_trends[trend['id']]['viral_score'] = min(100, int((trend['score'] / 1000) * 10))

    # Sort by viral score, then by score
    sorted_trends = sorted(existing_trends.values(), key=lambda x: (x['viral_score'], x['score']), reverse=True)

    quote = get_quote_of_the_day(sorted_trends)

    return {
        "meta": {
            "source": "reddit",
            "subreddit": subreddit,
            "last_update": int(time.time()),
            "last_update_human": datetime.now().isoformat(),
            "total_updates": existing_db['meta'].get('total_updates', 0) + 1,
            "seen_ids": list(seen_ids)[:1000],  # Keep last 1000 to prevent bloat
            "total_trends": len(sorted_trends),
            "version": "2.0"
        },
        "quote_of_the_day": quote,
        "trends": sorted_trends[:100]  # Keep top 100
    }, new_count

def generate_json_feed(trends: list, subreddit: str) -> dict:
    """Generate structured JSON feed for frontend consumption (one-shot mode)"""
    trend_objects = [
        {
            "id": t['id'],
            "title": t['title'],
            "subreddit": t['sub'],
            "score": t['score'],
            "url": t['url'],
            "snippet": t['selftext'][:200] if t['selftext'] else None,
            "author": t['author'],
            "created": t['created_utc'],
            "comments": t['num_comments'],
            "reddit_url": t['permalink'],
            "viral_score": min(100, int((t['score'] / 1000) * 10))
        }
        for t in trends
    ]

    quote = get_quote_of_the_day(trend_objects)

    return {
        "meta": {
            "source": "reddit",
            "subreddit": subreddit,
            "fetched_at": int(time.time()),
            "fetched_at_human": datetime.now().isoformat(),
            "count": len(trends),
            "version": "2.0"
        },
        "quote_of_the_day": quote,
        "trends": trend_objects
    }

def main():
    parser = argparse.ArgumentParser(description="Trendjacker v2.0 - Reddit → Grok hooks or JSON feed")
    parser.add_argument('--subreddit', default='popular', help='Subreddit or "popular"/"all"')
    parser.add_argument('--limit', type=int, default=15, help='Number of hot trends')
    parser.add_argument('--niche', default='', help='Your monetization niche')
    parser.add_argument('--json', action='store_true', help='Output JSON feed instead of interactive mode')
    parser.add_argument('--watch', action='store_true', help='Continuously update feed (implies --json)')
    parser.add_argument('--interval', type=int, default=300, help='Update interval in seconds for --watch mode (default: 300)')
    parser.add_argument('--output', default='trendjacker_feed.json', help='Output file for JSON mode')
    args = parser.parse_args()

    # Watch mode - continuously update feed
    if args.watch:
        print(f"🔄 Watch mode: updating {args.output} every {args.interval}s from r/{args.subreddit}", file=sys.stderr)
        db = load_feed_db(args.output)

        try:
            while True:
                try:
                    trends = fetch_trends(args.subreddit, args.limit)
                    updated_db, new_count = merge_trends(db, trends, args.subreddit)
                    save_feed_db(updated_db, args.output)
                    db = updated_db

                    timestamp = datetime.now().strftime("%H:%M:%S")
                    print(f"[{timestamp}] ✅ Update #{db['meta']['total_updates']}: "
                          f"+{new_count} new trends | {db['meta']['total_trends']} total",
                          file=sys.stderr)
                except Exception as e:
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ Error: {e}", file=sys.stderr)

                time.sleep(args.interval)
        except KeyboardInterrupt:
            print(f"\n🛑 Stopped. Final stats: {db['meta']['total_trends']} trends, "
                  f"{db['meta']['total_updates']} updates", file=sys.stderr)
        return

    trends = fetch_trends(args.subreddit, args.limit)

    # JSON feed mode (one-shot)
    if args.json:
        feed = generate_json_feed(trends, args.subreddit)
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(feed, f, indent=2)
        print(f"✅ JSON feed saved to {args.output} ({len(trends)} trends)", file=sys.stderr)
        print(json.dumps(feed, indent=2))
        return

    # Interactive prompt mode
    print("\033[1;32m╔════════════════════════════════════════════╗")
    print("║         TRENDJACKER v2.0 - TURBO EDITION   ║")
    print("╚════════════════════════════════════════════╝\033[0m\n")

    print("\033[1;33mTOP EXPLODING TRENDS:\033[0m")
    for i, t in enumerate(trends, 1):
        print(f"\033[1;36m{i:2d}.\033[0m [{t['score']:,}] r/{t['sub']} → {t['title'][:70]}{'...' if len(t['title'])>70 else ''}")

    try:
        choice = int(input("\n\033[1;35mSelect trend # (0 = auto #1): \033[0m") or 1) - 1
        trend = trends[max(0, min(choice, len(trends)-1))]
    except ValueError:
        trend = trends[0]

    niche = args.niche or input("\033[1;35mTarget niche (e.g. affiliate, ghostwriting): \033[0m") or "content creators"

    prompt = build_master_prompt(trend, niche)

    print("\n\033[1;32m✅ MASTER GROK PROMPT READY (copy-paste to Grok):\033[0m\n")
    print(prompt)

    filename = "trendjacker_hooks.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(prompt)
    print(f"\n\033[1;32m💾 Saved to {filename} - ready for Obsidian/Notion\033[0m")

    print("\n\033[1;33m🚀 Next: Paste into Grok → post → profit. Commercial license active.\033[0m")

if __name__ == "__main__":
    main()
