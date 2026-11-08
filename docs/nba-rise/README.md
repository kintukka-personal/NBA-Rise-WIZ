# NBA RISE research

Reference material on **NBA RISE: Basketball Strategy**, GRAVITY Co., Ltd.'s officially licensed NBA card-strategy game. It launched on 20 October 2026 in South Korea, the Philippines, Indonesia, Thailand, Malaysia, Singapore, Australia and New Zealand. Its Japanese predecessor ran as NBA RISE TO STARDOM (2021–24), then as NBA RISE (2025–26).

Compiled 8 November 2026. Store figures are a snapshot from that date.

## Contents

| Path | What it is |
|---|---|
| [`dossier.html`](dossier.html) | The full illustrated dossier. Open it in a browser. Published copy: https://claude.ai/artifact/T2KUC1ahJaHJU89BJ9oifd |
| [`research/01-history-and-business.md`](research/01-history-and-business.md) | Dated timeline 2020–2026, the link between the Japanese and global versions, licensing, store presence, SEC filings and investor materials |
| [`research/02-mechanics-japan.md`](research/02-mechanics-japan.md) | Every documented system of the Japanese versions (TO STARDOM and the 2025 NBA RISE), from the 480-post official news archive |
| [`research/03-mechanics-global.md`](research/03-mechanics-global.md) | The global game's systems: match engine, SET PLAY, tactics and counters, cards, synergies, modes, economy, odds |
| [`research/04-reception-and-market.md`](research/04-reception-and-market.md) | Ratings by region, review themes, press, chart positions, community size, competitor landscape |
| [`data/cards.csv`](data/cards.csv) | Every card in the global game's official pack lists: **878 unique cards**, with name, edition, rarity and the packs that drop each one |
| [`data/packs.json`](data/packs.json) | All **55 official packs**, each with Korean title, rarity odds, pity/wishlist notes, full card list with per-card rate, and source URL |
| [`tools/fetch_odds.py`](tools/fetch_odds.py) | Refreshes `data/` from GRAVITY's live disclosure pages (Python 3, standard library only) |

## Key facts

- **Publisher and developer:** GRAVITY Co., Ltd. (Seoul, NASDAQ: GRVY), built in-house. Android `com.gravity.nbarisegv.aos`, iOS `id6762187862`, and Windows through Google Play Games.
- **License:** NBA and NBPA, signed May 2020 and extended 2025. Uses 2025-26 rosters.
- **Genre:** you play the owner and head coach. Matches are 48-minute 3D simulations. You make substitutions and tactic swaps during play, and once per quarter there is a SET PLAY timing tap that raises team morale by 30%.
- **Cards:** six rarities: Common, Uncommon, Rare, Ultra Rare, Epic and Legend. Editions are 25-26 SEASON (390), Starter (385), The Core (60 Epics), The Edition (10 Legends), plus rotating themed sets (LOCKDOWN, HALLOWEEN, FLAME; 10 Epics + 1 Legend each).
- **Odds:** paid packs drop Epics at 0.5% and Legends at 0.1%. Pity guarantees an Epic at 100 cards, and a Legend at 200 cards in The Edition. A wishlist steers which Epic you get.
- **Modes:** Season Mode (Rookie 3 → NBA Finals), Daily Division, Arena, Popularity Battle, Tower Race, Club Conquest.
- **Traction (8 Nov 2026):** 298,491 Android installs, rated 4.2–4.8★ depending on region, #12–#42 in iOS Sports top-grossing, 2,740 Discord members.

## Data notes

`data/` comes from GRAVITY's own probability disclosure, which Korean law requires:
- https://probability.gnjoy.com/NBA/NBARISE/NBARISE/NBA-NOTIFY
- per pack: `https://prd-clutch-api.gnjoy.com/ext/news/offerrate?offerGroupId=<id>`

It is the most complete public card list for the game. The disclosure does not include OVR, attributes, skills, positions or team. A card database also needs those, which means collecting them from in-game screens or the official site's card art.

`cards.csv` columns:

| Column | Meaning |
|---|---|
| `name` | Player name as GRAVITY spells it (e.g. `Peja Stojakovic`) |
| `edition` | `25-26 SEASON`, `Starter`, `The Core`, `The Edition`, `LOCKDOWN`, `HALLOWEEN`, `FLAME` |
| `rarity` | `COMMON`, `UNCOMMON`, `RARE`, `ULTRARARE`, `EPIC`, `LEGEND` |
| `offer_group_ids` | Space-separated pack ids that can drop the card. Look them up in `packs.json` |

Pack id ranges: `10xxx` scout packs, `20xxx` reward packs (free, with lower odds), `30010` Diamond Box, `40xxx` paid shop packs.

To refresh:

```bash
python3 tools/fetch_odds.py --out data --save-raw /tmp/nba-rise-raw
```

## Deliberately left out

- **Store screenshots, card art and NBA photography.** These belong to GRAVITY, the NBA and the photographers.
- **The scraped text of the Japanese official site.** It is copyrighted. The research reports cite each post by URL instead.
- **Raw review dumps.** They contain reviewers' names. The reports keep only aggregate figures and short quotes.
- **SEC filings and Gravity IR decks** (about 300 MB). They are public at the URLs listed in `research/01-history-and-business.md`.
