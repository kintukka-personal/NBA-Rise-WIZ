#!/usr/bin/env python3
"""Refresh the NBA RISE card and pack-odds dataset from GRAVITY's official disclosure.

GRAVITY publishes per-pack odds (required by Korean law) at probability.gnjoy.com.
Each pack page lists every card it can drop with name, edition, rarity and per-card
rate, so it doubles as the most complete public card list for the global game.

Usage:
    python3 fetch_odds.py --out ../data                 # discover packs and fetch live
    python3 fetch_odds.py --out ../data --from-dir raw  # re-parse saved og<ID>.html files
    python3 fetch_odds.py --out ../data --save-raw raw  # fetch live and keep the HTML

Standard library only. Requests are sequential with a short delay.
"""
import argparse
import csv
import html
import json
import os
import re
import sys
import time
import urllib.request
from collections import Counter
from datetime import date

LIST_PAGES = [
    "https://probability.gnjoy.com/NBA/LIST1/LIST1/SCOUT-LIST",
    "https://probability.gnjoy.com/NBA/LIST3/LIST3/DIABOX-LIST",
]
PACK_URL = "https://prd-clutch-api.gnjoy.com/ext/news/offerrate?offerGroupId={}"
RARITY_ORDER = ["LEGEND", "EPIC", "ULTRARARE", "RARE", "UNCOMMON", "COMMON"]
UA = "nba-rise-companion-research/1.0"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def norm_rarity(r):
    r = r.replace(" ", "").upper()
    return "ULTRARARE" if r.startswith("ULTRA") else r


def parse_pack(gid, page):
    t = re.sub(r"<!--.*?-->", "", page, flags=re.S)
    t = re.sub(r"<(script|style)\b.*?</\1>", "", t, flags=re.S)
    title = re.search(r'<h1 class="title">(.*?)</h1>', t, re.S)
    head, _, body = t.partition("◆")
    rates = {}
    for tr in re.findall(r"<tr>(.*?)</tr>", head, re.S):
        r = re.search(r'<span class="rarity">\s*(LEGEND|EPIC|ULTRA ?RARE|RARE|UNCOMMON|COMMON)\s*</span>', tr)
        v = re.search(r"<span>([0-9.]+)</span>\s*%", tr)
        if r and v:
            rates.setdefault(norm_rarity(r.group(1)), float(v.group(1)))
    notes = [clean(x) for x in re.findall(r"<li[^>]*>(.*?)</li>", head, re.S)]
    cards = []
    for sec in ("◆" + body).split("◆")[1:]:
        hm = re.match(r"(?:&nbsp;|\s)*([A-Z]+(?: RARE)?)", sec)
        rarity = norm_rarity(hm.group(1)) if hm else ""
        for name, edition, rate in re.findall(
            r'<td class="rarity_name">\s*<p><span class="rarity">(.*?)</span></p>\s*'
            r'<p><span class="rarity">(.*?)</span></p>\s*</td>\s*<td class="rarity_rate">.*?<span>([0-9.]+)</span>%',
            sec, re.S):
            cards.append({"rarity": rarity, "name": clean(name), "edition": clean(edition), "rate_pct": float(rate)})
    return {
        "offerGroupId": gid,
        "title_ko": clean(title.group(1)) if title else "",
        "rarity_rates_pct": rates,
        "notes_ko": [n for n in notes if n and len(n) < 400][:12],
        "card_count": len(cards),
        "cards": cards,
        "source": PACK_URL.format(gid),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--from-dir", help="parse saved og<ID>.html files instead of fetching")
    ap.add_argument("--save-raw", help="directory to keep fetched HTML")
    ap.add_argument("--delay", type=float, default=0.5)
    a = ap.parse_args()

    pages = {}
    if a.from_dir:
        for fn in os.listdir(a.from_dir):
            m = re.match(r"og(\d+)\.html$", fn)
            if m:
                pages[int(m.group(1))] = open(os.path.join(a.from_dir, fn), encoding="utf-8", errors="replace").read()
    else:
        ids = set()
        for url in LIST_PAGES:
            ids |= {int(x) for x in re.findall(r"offerGroupId=(\d+)", get(url))}
        print(f"discovered {len(ids)} packs", file=sys.stderr)
        for gid in sorted(ids):
            pages[gid] = get(PACK_URL.format(gid))
            if a.save_raw:
                os.makedirs(a.save_raw, exist_ok=True)
                open(os.path.join(a.save_raw, f"og{gid}.html"), "w", encoding="utf-8").write(pages[gid])
            time.sleep(a.delay)

    packs = [parse_pack(gid, pages[gid]) for gid in sorted(pages)]
    unique = {}
    for p in packs:
        for c in p["cards"]:
            k = (c["name"], c["edition"], c["rarity"])
            unique.setdefault(k, {"name": c["name"], "edition": c["edition"], "rarity": c["rarity"], "packs": set()})["packs"].add(p["offerGroupId"])

    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "packs.json"), "w", encoding="utf-8") as f:
        json.dump({"fetched": date.today().isoformat(), "packs": packs}, f, ensure_ascii=False, indent=1)
    order = {r: i for i, r in enumerate(RARITY_ORDER)}
    with open(os.path.join(a.out, "cards.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["name", "edition", "rarity", "offer_group_ids"])
        for c in sorted(unique.values(), key=lambda c: (c["edition"], order.get(c["rarity"], 9), c["name"])):
            w.writerow([c["name"], c["edition"], c["rarity"], " ".join(map(str, sorted(c["packs"])))])
    print(f"{len(packs)} packs, {len(unique)} unique cards", file=sys.stderr)
    for (ed, r), n in sorted(Counter((c["edition"], c["rarity"]) for c in unique.values()).items()):
        print(f"  {ed:14} {r:10} {n}", file=sys.stderr)


if __name__ == "__main__":
    main()
