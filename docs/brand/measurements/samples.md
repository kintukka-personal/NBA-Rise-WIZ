# Measurement log

Every game-side value in `../tokens.css` and `../NBARiseWiz_Visual_System.html` comes from one of these samples. A sample is either:
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
| AS-PH-7 | App Store PH screenshot 7, in-match gameplay with the SET PLAY countdown | 1260×2736 | same, `[6]` |
| NB-02 / 17 / 25 / 27 / 28 / 29 / 31 / 32 / 33 | Player blog captures: home hub, tactic change, card back, Condition info panel, synergy list (closed and open), Scout, The Edition pack result, Auction | 1080×1920 (27: 886×779, 33: 886×836) | `blog.naver.com/12512512/224449341627` |
| NG-08 | Launch-day player capture of a tactic change | 1080×2340 | `blog.naver.com/ngga32472/224449909504` |
| DK-13 / 18 | Player blog captures of SET PLAY: defence action select, offence select with the auto pill | 1399×3000, 358×765 | `blog.naver.com/dekiruho123/224451027691` |
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
| of / of-ink | `#6C5322` / `#FFECA0` (label, ball, cross and arrow) | NB-17 chip 950,305–1030,342 and label 680,310–840,338; NG-08 agrees (`#6B5422`). AS-PH-4 store art reads the text as `#DECB87` under its marketing overlay, so the in-game capture wins |
| df / df-ink / df-peak | `#175B42` / `#3DFF9E` / `#3DFF8F` | NB-17 chip 450,305–520,342, label 200,310–380,338, shield 55,305–85,340; NG-08 agrees (`#165A41`). AS-PH-4 read `#225542` under the overlay |
| gr | `#00C10D` | AS-PH-6 stamina segment |
| gr-peak | `#39FF35` | AS-KR-7 SET PLAY countdown digit |
| stam-low / stam-mid | `#FFCE16` / `#86CD00` | NB-17 280,807–330,815 and 710,807–760,815 |
| load | `#FDD800` on `#000000` | NB-17 365,760–420,792 |
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

## Match-prep lineup

Source: NB-14, a lossless 1080×1920 Match Preparation capture from launch week. The lineup in the document is this screen's real roster. Starters: B. Miller UR 182, K. Irving Epic 186 (Starter), N. Reid UC 117, D. Vassell UR 157, S. Mamukelashvili UC 111. Bench: O. Anunoby UR 163, B. Carrington R 133, N. Queta UC 90 (Starter), V. Edgecombe UR 156 (Starter).

| Part | Values | Sample |
|---|---|---|
| Starter slot | body `#143D88` / `#133A84`, top `#154091`, rim `#1C50B2`, inner shadow `#0E2E6D` | SF slot body 30,1060–36,1100; horizontal profile at y=1100 |
| Tab | rises about 32 px above the slot's left shoulder | vertical profiles at x=40 (top at y≈900) and x=120 (top at y≈868) |
| Position disc | `#0D2758`, text `#EDF5FF` | tab disc 110,880–140,895 |
| S-chip | `#CC8A22`, shadow `#A06D20`, text `#F1EDE3` | 180,890–200,905 |
| Mini-card frames | UR `#C5AF77 / #BDA359 / #DBD078`; Epic `#BD32E5 / #A129CE`, dark `#380F54`; UC `#76996F / #678C5F` | frame strips at x=38–42, 248–252, 452–456 |
| Nameplates | standard `#1E1F21`; Epic `#202736` | plate regions |
| Stamina | track `#000000`, segments `#00BE0D` | 70,1192–215,1196 |
| Box score | grade well `#16213D` / `#0A0C20`, bronze `#BA9267` / `#8F6B4C`; PTS/AST `#0C2A65`, label `#BFC5CE`, value `#EBF0F4` | footer regions |
| Bench | box `#212427`, grade well `#1D1F21`; label `#EBF0F4` with sub-position `#999EA5` | bench footer and label |
| Ground · tally | `#1C1D1F`; tally pill `#0D0D0D`, text `#999EA5` | 500,1290–560,1300; 350,1320–420,1340 |

## In-match HUD

Sources:
- **Scorebug and shot clock:** AS-PH-7, the gameplay screenshot from the App Store PH set (iPhone 1260×2736; the iPad 2048×2732 copy matches).
- **Two-digit shot clock:** IN-z4, the iNews24 SET PLAY sequence ("18", "08").
- **Header scoreboard:** AS-PH-6 for Match Preparation and IN-z3 for the live simulation.

| Part | Values | Sample |
|---|---|---|
| Scorebug panel | `#2A2E32`, rim `#3D424A` (2 px), radius ≈ 18 px at phone scale | 360,2380–560,2420; left-edge profile at y=2300 |
| Scorebug stripes | home `#2666B8`, away `#E64126` (orange-red, scorebug only), lower corners only | 100,2335–108,2390 and 879,2335–887,2390 |
| Quarter chip · clock | `#C70D32`, ink `#E8E5E8`; clock `#EAEDEF` | 415,2255–425,2280; 500,2255–580,2285 |
| Second row | user ID `#F6F8FA`; city `#9EA3AA`; team `#EDF0F2` | 135,2350–300,2375; 765,2335–855,2353; 790,2360–855,2390 |
| Shot clock | radial: centre `#103E4E` → `#103746` → `#0E2832` → `#0E1F27` → edge `#0D1519`; rim `#19202A` | horizontal profile at y=2300 and vertical at x=1040 |
| Shot clock digits · label | `#03EEFE`, halo `#0D6575`; label `#A5A7AD` | 1000,2260–1100,2340; 960,2355–1130,2380 |
| Header board | ground `#2A2E32`; full-height stripes home `#168CFB`, away `#DF263D`; clock `#C5C9CC`; ID `#B8BCBF`; name `#ADB1B4` | AS-PH-6 stripe profile at x=4 (y 440–590); text regions |
| Header divider · pill | divider `#1C1D1F`; pill `#1C1C1C`, text `#E9EDF1` | vertical profile at x=630 |

## Set play, card back and hubs

Sources:
- **Countdown:** AS-PH-7. Ring centre ≈ (630, 1367); vertical scan at x=630 and horizontal scan at y=1367.
- **Action select:** DK-13 (value chips and action discs), DK-18 (auto pill).
- **Timing tap and result:** IN-z4. **Toast:** IN-z3.
- **Card back:** NB-25, a Starter Epic K. Irving at 148 (+8), level 14/30.
- **Condition info panel:** NB-27. Its five steps read 최상 +10, 상 +5, 중 no change, 하 −5, 최하 −10, applied to attack and defence. Condition then rises, holds or falls by a set chance at the end of each match, depending on the result.
- **Home bar:** NB-02. **Scout tiles:** NB-31.

| Part | Values | Sample |
|---|---|---|
| Countdown disc · inner ring | disc `#0D0D1C`; thin inner ring `#24272F` / `#22282D` | 600,1300–640,1320; scan y≈1264 and x≈732 |
| Countdown track · arc · digit | track `#3C4146` (outer edge `#444A4E`); arc `#3BD738` / `#3FEE3A`; digit `#38FF35` | 700,1240–730,1255; 555,1225–600,1240; bright-green median in 580,1300–690,1450 |
| Value chips | home `#015FC1`, away `#C22600` | DK-13 212,1530–232,1600 and 1028,1528–1046,1590 |
| Action disc | face `#2E2F35` (clusters `#40434A` → `#34363B` → `#26262A`), rim `#373B41`, label `#D8E1E3` | DK-13 200,1900–240,1920; 150,1800–160,1840; 250,1860–330,1885 |
| Auto pill | `#021027`, icon and text `#14A3B5` | DK-18 150,650–240,665 |
| Tap ring · button | ring `#BB3C39`; button `#2E7824` / `#255F1E`, edge `#0F3C0D`, icon `#A9D7A7` | IN-z4 543,140–553,190; 560,140–600,175 |
| Tap timer · label | timer ground `#171F24`, arc `#2E9B43`; label pill `#161E2C`, rim `#273040` | IN-z4 562,255–575,290; 560,213–600,230 |
| Banner text | `#ECFEFD`, glow `#A7FDFD` | IN-z4 150,215–230,245 |
| Success · bubble | success `#1CA5D8`, rim `#ACDDED`; bubble `#0C6AC8`, rim `#558FC5`, mic disc `#A4C7DE` | IN-z4 910,40–1020,75; 120,295–290,320 |
| Toast | `#B80B0B`, rim `#DFBABA`; icon disc `#850D0D`, icon `#F2EAEA` | IN-z3 250,700–500,730; 120,700–150,725 |
| Card-back frame · header | frame `#5C6063` → `#878E96` (horizontal profile at y=900, x 40–110); header `#333E52`, top `#28344A` | NB-25 930,320–960,345; vertical profile at x=540 |
| Card-back cells | cell `#1D2532`, divider `#2E384A`; level bar `#2AC2E7` on `#0D1119` | 110,560–130,580; 384,520–388,560; 410,584–470,590; 520,584–580,590 |
| Fatigue · condition | cell `#252629`; Recover `#0AA0DD`; fatigue bar `#16BEE7`; condition pill `#254229`, text `#00FF58` | 200,615–240,640; 110,760–130,780; 240,705–300,715; 840,725–900,745 |
| Ability rings | offence `#D5AC2B`, defence `#16C988`, mental `#B1C1D4`, track `#363739`; boosted value `#00E3FF`, plain `#EBF0F4` | 244,925–256,935; 533,918–548,932; 821,918–836,932; 215,985–275,1035; 790,985–860,1035 |
| Abilities ground · band | ground `#232527`; section band `#1C1E20` | 100,1010–140,1030; 180,855–220,870 |
| Header details | magnifier `#F0F4FA` on `#444A54`; position pill `#191E26`; +8 chip `#173548`, text `#00E2FD` | 770,245–780,255; 420,330–440,350; 270,525–295,545 |
| Skill medal | `#C7B427`, shade `#36300B` | 500,1300–520,1320 |
| Condition panel | header `#2A2D32`; divider `#50575D` / `#4E555B`; body `#222629`; card `#2E3235` | NB-27 300,40–600,90; vertical profile at x=400; 40,170–700,173; 60,300–100,320 |
| Condition panel text | chip `#2C3F3B`, text `#34BD8B`; description `#B3B5BE`; rows `#ECF0F4` | 108,228–118,236; bright-pixel medians in 110,225–225,280, 100,300–760,395 and 175,425–490,700 |
| Home bar | rim `#2F3142`, then `#1D1F2C` falling to `#15161D`; hump rim `#3A3B4B`; icons and labels `#8B94A2` | NB-02 vertical profiles at x=150 (y 1660–1712) and x=330 (y 1662); 140,1870–180,1900; 85,1720–95,1740 |
| Scout buttons | `#00AEEF`; price inset `#00729E`, gold bar `#D8A325` / `#F6E154` | NB-31 90,1200–110,1280; 200,1225–300,1258 |
| Scout pity · tooltip | pity chip `#231430`; track `#4B535A`; Free bar `#768478`; tooltip `#EBF0F4`, text `#2C3034` | 890,1090–905,1115; 100,1148–300,1156; 900,640–980,700; 600,585–620,600 |

## Tactics and synergy

Sources:
- **Tactic change:** NB-17, a lossless launch-week capture. NG-08 is a second capture that cross-checks the chip fills.
- **Synergy list:** NB-28 (closed) and NB-29 (open, with the Western Conference Boost card).

| Part | Values | Sample |
|---|---|---|
| Team header | ground `#2A2E32`; labels `#B0B3BE`; figures `#F4FAFF`; bonus `#285A65`, text `#07C1D9`; stripes home `#168DFD` (left), away `#DF263D` (right) | NB-17 400,1030–450,1050; 170,1035–290,1060; 170,1080–265,1125; 278,1082–372,1122; 0,1030–8,1100; 1072,150–1080,280 |
| Defence chip | `#175B42`; shield `#3DFF8F` with inner outline `#15563E`; label `#3DFF9E`; cross `#3DFF8F` | 450,305–520,342; 55,305–85,340; label bright-pixel median in 200,310–380,338; 488,880–518,920 |
| Offence chip | `#6C5322`; ball `#FFECA0`, seams `#664F20`; label `#FFECA0`; share pill `#403011`, text `#5FEB31`; cross `#FFECA0` | 950,305–1030,342; 560,305–600,340; 680,310–840,338; 850,312–910,338; 995,880–1025,920 |
| Player tags | defence `#175940`, text `#55E49D`; offence `#695122`, text `#F5E296`; ▲ `#FEEB9F` outlined `#493815`; ▼ `#FD5B4B` | 395,530–420,555; 270,525–380,560; 230,580–270,605; 270,570–340,620; 340,582–365,600; 135,675–160,692 |
| Player furniture | position disc `#265AA5`, ring and text `#F4F5F7`; grade metal bronze `#967F62`, silver `#74868F`, outline `#110E0E`; load `#FDD800` on `#000000`; stamina `#FFCE16` / `#86CD00` on `#000000` | 240,680–285,720; mid-tone medians of the grade letters at 232,735–292,790 (C+) and 15,780–85,840 (B+); 365,760–420,792; 280,807–330,815; 710,807–760,815 |
| Court | `#1F2022` | 600,480–640,510 |
| Selection list | bar `#454B53`, chevron pill `#D9DFE5`; column heads offence `#CCBD82`, defence `#37CC74`; ground `#2A2E32` | 50,1160–300,1170; 590,1168–670,1198; 115,1235–480,1260; 665,1235–980,1260; 535,1290–545,1350 |
| List rows | row `#3D454B`, label `#F0F0F0`; picked offence `#6A552A`, picked defence `#1C5D45`; ⚡ `#E2B837`; divider `#32383D` | 200,1290–320,1310; 50,1310–170,1340; 200,1390–320,1405; 760,1390–840,1405; 345,1305–380,1345; 410,1300–416,1345 |
| Matchup | offence ▲ `#FFECA0`; ▼ `#FD5B4B`; defence ▲ `#3DFF8F`; even `#A2A6AB` | 450,1315–485,1335; 450,1510–485,1530; 975,1608–1005,1628; 980,1320–1000,1330 |
| Buttons | Auto swap `#3D454B`; Confirm `#00AEEF` | 100,1800–380,1820; 450,1800–950,1815 |
| Synergy header | bar `#2A2E32`; checkbox `#515559`; S glyph `#EBF0F4`, outline `#1F2225`; count `#F2C22E` on `#1C1F21`; Expand all `#3D454B` | NB-28 450,280–800,340; 55,290–100,330; 120,295–150,325; 160,290–198,330; 840,290–1020,335 |
| Synergy rows | list `#1C1C1C`; row `#2E3235` with a 3 px `#373C3C` top rim; title `#EBF0F4`; sub `#C2C3C4`; TP label `#BBBBBB`; TP `#F2C22E` on `#1F2123`; chevron `#3D454B`, arrow `#D9DFE5` | 5,830–30,850; 420,870–600,890; vertical profile at x=500 (y 835–880); 95,875–390,915; 90,930–340,955; 635,900–810,925; 830,892–915,932; 945,880–1010,945 |
| Event tags | EVENT `#169567`, text `#FDFDFD`; countdown `#0D0D1C`, text `#DBE1E5` | 85,378–205,410; 222,378–425,410 |
| Active synergy | fill `#35322E`; rim `#DBB745` (inner `#C2A240`, outer `#7D6326`); glow rising to `#48331C` over about 20 px; open chevron `#555F67` | NB-29 850,690–1000,720; horizontal profile at y=800 (x 30–80); vertical profile at x=500 (y 1160–1200); 945,1205–1010,1270 |
| Open boost | divider `#52504E`; tick `#D89B16` with `#FAF4E9`; text `#D9DFE5`; target box `#24211F`, label `#ACAFBC` | 100,660–1000,666; 103,682–140,718; 160,690–790,715; 800,950–980,990; 120,960–240,995 |
| Stat chips | offence `#514322` / `#D0A92D`; defence `#264836` / `#2AD898`; mental `#44484F` / `#B5C8DF` | 120,1012–345,1062; 357,1012–578,1062; 592,1012–780,1062 (fills by cluster, text by bright-pixel median) |

## Absent-colour search

`../tools/absent.py` scores candidate colours against 34 game accents. The grid covers hue in 2° steps, HSL lightness 0.38–0.64 and saturation 0.75–1.0. Each candidate gets its minimum OKLab ΔE×100 under normal vision and Machado-2009 protan, deutan and tritan simulation.
- **Best overall:** `#C41C9D`, 6.3 ΔE from the nearest game accent.
- **Best that is also ≥3:1 on the white board and on slate:** `#BA5EE8` (5.5) and `#1B86BB` (5.5). Both are game-family hues.
- **Result:** no ownable hue exists, and NBARiseWiz is black and white.

## Hue occupancy

`hue_occupancy.json` holds the share of saturated UI pixels (S > 0.45, 0.22 < L < 0.85) per degree of hue across 32 images. Two bands are nearly empty:
- **60–139°:** small but meaningful greens only — stamina, condition, countdown.
- **300–339°:** the event-bar pink.

The rest of the wheel is occupied.

## Typefaces

**Words: Open Sans.** See `font_fit.json`. 32 faces were scored against two in-game crops. The result is Open Sans: Bold for interface text and ExtraBold for titles, rendered through TextMeshPro with a thin dark outline.

**Numbers: Anton.** See `font_fit_numerals.json`. 35 condensed faces were scored against Team Power, and 26 faces against the score, OVR and shot clock.

| Target | Anton IoU | Width ratio (game / Anton) | Next best |
|---|---|---|---|
| Team Power "18545" / "11717" | 0.878 / 0.880 | 2.649 / 2.576 | Teko 600, 0.796 |
| Scores "37" / "55" | 0.904 / 0.934 | 1.089 / 1.080 | Teko 600, 0.822 |
| OVR "119" | 0.790 | 1.281 / 1.290 | Russo One, 0.786 |

Oswald, the face GRAVITY's website loads, reaches only 0.711. The shot clock "17" is unresolved: Open Sans 800 comes closest at 0.727 but runs 10% narrow.
