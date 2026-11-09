# Measurement log

Every game-side value in `../tokens.css` and `../RiseWiz_Visual_System.html` comes from one of these samples. A sample is either:
- the **median colour** of a component region; or
- one of the top clusters from a **four-colour median-cut** of that region.

Both are computed with `../tools/sample.py`. Coordinates are in the source image's own pixels. Measured 8–9 November 2026, global build 1.1.x.

## Sources

| Key | Image | Size | Origin |
|---|---|---|---|
| AS-PH-2 | App Store PH screenshot 2, "Build your collection" (Team Formation) | 1260×2736 | `itunes.apple.com/lookup?id=6762187862&country=ph` → `screenshotUrls[1]` |
| AS-PH-3 | App Store PH screenshot 3, "Create your lineup" (Starting Lineup) | 1260×2736 | same, `[2]` |
| AS-PH-4 | App Store PH screenshot 4, "Play with strategy" (Tactical) | 1260×2736 | same, `[3]` |
| AS-PH-6 | App Store PH screenshot 6, Match Preparation (full-bleed UI) | 1260×2736 | same, `[5]` |
| AS-KR-7 | App Store KR iPhone screenshot 7, in-match SET PLAY | 1260×2736 | `country=kr`, `screenshotUrls[6]` |
| NB-02 / 25 / 31 / 32 / 33 | Player blog captures: home hub, card back, Scout, The Edition pack result, Auction | 1080×1920 (33: 886×836) | `blog.naver.com/12512512/224449341627` |
| IN-z3 / z4 / z9 | iNews24 hands-on: live match, SET PLAY sequence, home hub | 780×880, 1160×478, 900×1170 | `m.inews24.com/v/2021080` |
| SITE-card | Official site card art (Epic, Ultra Rare, Rare) | 377×497 | `imgc.gnjoy.com/games/nbarise/official/card/card-N.webp` |

## Grounds

| Token | Value | Sample |
|---|---|---|
| ground | `#2A2E32` | AS-PH-6 header band 300,270–1260,300 (96% cluster). The median-cut over the whole UI puts it at 31.0% of pixels |
| dark-pixel bias | mean R−B −9.70, 89.0% bluer than red | AS-PH-6, 1,876,589 pixels with luminance < 60 |
| letterbox | `#1A1B1E` | AS-PH-6 0,0–1260,230 |
| well-blue | `#0F141C` | AS-KR-7 letterbox |
| well | `#1C1D1F` | AS-PH-6 nameplate 52,1565–70,1600 |
| well-2 | `#202125` | AS-PH-6 OVR box 50,1355–60,1380 |
| raised | `#3D454B` | AS-PH-6 MENU fill. Vertical profile is flat from 2335 to 2445 |
| tab-off | `#40474B` | NB-31 unselected tab |
| bench | `#363A40` / rim `#6F7479` | AS-PH-2 bench slot frame |
| pill | `#0D0D0D` | AS-PH-6 bench tally pill |

## Ramps and components

| Token | Value | Sample |
|---|---|---|
| cy | `#00AEEF` | AS-PH-6 Q1 START, 98% cluster. Vertical profile is flat from 2333 to 2445. NB-31 tab on: same value |
| cy-rim | `#21F9FD` | IN-z9 event progress fill |
| cy-peak | `#CAFFFF` | AS-KR-7 away OVR digits (leading) |
| cy-clock | `#03EBFD` | AS-KR-7 shot clock digits |
| cy-glow | `#39EFFB` | IN-z3 selected comparison row ring |
| cy-tab | `#39D3FF` | AS-PH-2 formation position tab |
| cy-bar | `#16BEE7` | NB-25 fatigue bar; AS-PH-2 formation bar |
| hm | `#158EFD` | IN-z3 home bar; AS-PH-6 left team stripe `#168DFD` |
| hm-body / hm-mid | `#143B85` / `#1C57C3` | AS-PH-6 starter card frame body and edge |
| hm-disc | `#1E4484` | AS-PH-4 home position disc |
| hm-box | `#0C2A65` | AS-PH-6 PTS box |
| aw | `#DF263D` | IN-z3 away bar; AS-PH-6 right stripe `#DF263D` |
| aw-nba | `#C70D2E` | AS-PH-6 Q1 chip; AS-KR-7 Q2 chip `#CE0B31` |
| aw-body | `#B80B0B` | IN-z3 tactic-change toast |
| aw-sel | `#DD4A7F` | IN-z3 away half of the selected row |
| aw-deep | `#6A1414` | AS-KR-7 away matchup card frame |
| aw-disc | `#D01B1B` | AS-PH-4 opponent position disc |
| gd-peak | `#F6C526` | AS-PH-6 TP figure |
| gd-mid / gd-body / gd-deep | `#C28422` / `#A77422` / `#523206` | AS-PH-6 synergy chip and synergy pill clusters |
| gd-rim / gd-light | `#DEAE1E` / `#F8E1A2` | AS-PH-6 TP badge clusters |
| of / of-ink / of-peak | `#6C5322` / `#DECB87` / `#FEF1A3` | AS-PH-4 "PG Drive Priority" chip fill, text, icon. Profile is flat from 1392 to 1440 |
| df / df-ink / df-peak | `#225542` / `#6FE9A4` / `#3DFE8F` | AS-PH-4 "Pass Interception (Mid)" chip fill, text, shield |
| gr | `#00C10D` | AS-PH-6 stamina segment |
| gr-peak | `#39FF35` | AS-KR-7 SET PLAY countdown digit |
| stam-low | `#FFD617` | AS-PH-4 yellow stamina |
| load | `#E4C401` on `#000000` | AS-PH-4 ⚡ chip |
| ball (PLAY) | `#FFA64F` → `#DE6624` → `#BD452B` → `#FF5D1D` | NB-02 vertical profile through the PLAY button, 1620 → 1860 |

## Sets

| Set | Values | Sample |
|---|---|---|
| Condition | ↑ `#01D64B` · ↗ `#AEFE01` · → `#F5F300` · ↘ `#FFAE01` · ↓ `#F50100` | AS-PH-2 arrows on A. Newell, L. Shamet, B. McGowens, M. Diawara and A. Hukporti. The steps (+10 / +5 / 0 / −5 / −10 to attack and defence) come from the in-game Condition info panel |
| Matchup OVR | ahead `#CAFFFF` · behind `#E02540` | AS-KR-7 card pair (89 vs 77) |
| Card stats | Offence `#E3B72A` · Defence `#16C988` · Mental `#B1C1D4` | NB-25 ring strokes |
| Bonus chips | `#29485B` / `#02BBD0`; `#044048` / `#00DCF1` | AS-PH-6 "+2184" and "+300" |
| Notices | new `#FD5B4B` · alert `#D63018` | NB-32 new-card dot; IN-z9 home badge |
| Packs | Free `#026429` · The Core `#422A58` · The Edition `#4E4330` | NB-31 tiles. Free tile profile is flat from 340 to 700 |
| Event bar | `#6DD2FD` → `#FE75D0`, fill `#21F9FD`, track `#0D0C0C` | IN-z9 |
| Home hub sky | `#093750` → `#388AA9` → `#B7C9CF`; HUD pill `#EBF0F4` | IN-z9, NB-02 |

## Rarities

| Rarity | Values | Sample |
|---|---|---|
| Common | frame `#828990 / #71767D / #63676D`, badge `#353B3C` | NB-32 horizontal profile across T. Watford's frame |
| Uncommon | face border `#81B76C`, badge `#7A9F73` on `#244020` | AS-PH-6 M. Moody; AS-KR-7 D. Melton |
| Rare | frame `#88B9CC / #839EB4 / #6E8FA9`, badge `#2B89CC` | NB-32 R. Gobert; SITE-card 19 |
| Ultra Rare | `#DECB98 → #C1A863 → #B79F53 → #E4CF79`, inner `#473508` | SITE-card 10 horizontal profile at y=250 |
| Epic | `#9D67C2 → #A34ACA → #9F27C6`, inner `#4E006E / #3B075B`, neon `#4AE3F8`, OVR disc `#B145CB` | SITE-card 1 horizontal profile at y=250 |
| Legend | not measured | No Legend card appears in any public screenshot as of 9 Nov 2026 |

## Card art: frame by rarity, field by edition

| Part | Values | Sample |
|---|---|---|
| Epic frame | `#F6D9FF` → `#D292F5` → `#BA68D9` → `#9F27C6` → `#571E82` (top-left to bottom-right) | SITE-card 1 corners (`#BA68D9` top-left, `#571E82` bottom-right) plus horizontal profile |
| Epic OVR disc | digits `#EDF1F5` on `#151920`, ring `#52E2F7` / `#A5E8FB`, halo `#723B94` | SITE-card 1, OVR region |
| Epic crest | hexagon `#40015A` → `#652A7B`, letters `#F6FBFF`, cyan gem `#1AF9FA` | SITE-card 1, badge top / mid / low |
| UR crest | dark hexagon `#08080A`, letters `#FFFBFA` → `#F7C3BE`, wing `#F5DB7C` / `#A7783E` | SITE-card 10, badge regions |
| OVR rim (non-Epic) | `#E1D5B3` / `#F9F4CE` | SITE-card 10 and 19 |
| The Core field | `#710384` (top right) into `#231660` / `#1B043B`, shards `#CEC8EC`, beams `#8ACAD7` | SITE-card 1 field regions |
| 25-26 SEASON field | `#21252A`, ring watermark `#373E47` | SITE-card 10 |
| Starter field | `#D7D6E6` / `#C2C1D6`, rings `#E1DFED`; nameplate `#232B3B`, rim `#9FAAB4` | NB-23 Starter Epic card (K. Irving) |
| Edition labels | Starter `#B9EBFF` upright, outline `#393C4D` · 25-26 SEASON `#FEFBDC` italic · THE Core `#82E3FC` italic, glow `#A130CA`, outline `#4E1A89` | NB-23 label region (bright and dark pixel medians); SITE-card 10; SITE-card 1 |

## Absent-colour search

`../tools/absent.py` scores candidate colours against 34 game accents. The grid covers hue in 2° steps, HSL lightness 0.38–0.64 and saturation 0.75–1.0. Each candidate gets its minimum OKLab ΔE×100 under normal vision and Machado-2009 protan, deutan and tritan simulation.
- **Best overall:** `#C41C9D`, 6.3 ΔE from the nearest game accent.
- **Best that is also ≥3:1 on the white board and on slate:** `#BA5EE8` (5.5) and `#1B86BB` (5.5). Both are game-family hues.
- **Result:** no ownable hue exists, and RiseWiz is black and white.

## Hue occupancy

`hue_occupancy.json` holds the share of saturated UI pixels (S > 0.45, 0.22 < L < 0.85) per degree of hue across 32 images. Two bands are nearly empty:
- **60–139°:** small but meaningful greens only — stamina, condition, countdown.
- **300–339°:** the event-bar pink.

The rest of the wheel is occupied.

## Typeface

See `font_fit.json`. 32 faces were rendered and scored against two in-game crops. The result is Open Sans: Bold for interface text, ExtraBold for titles, rendered through TextMeshPro with a thin dark outline.
