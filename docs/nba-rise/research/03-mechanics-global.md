<!-- Research report compiled 2026-11-08. Source links inside; working-file paths refer to a temporary session folder that was not preserved (the official pack data is preserved in ../data/). -->

# NBA RISE (global, GRAVITY): gameplay mechanics from English- and Korean-language sources

Research date: 2026-11-08. Tags: **[E]** means a source states it outright or a screenshot shows it. **[I]** means I inferred it, with the reasoning given. Source tags such as [S6] map to the URL list at the end.

## 0. Key identifiers and status

- **Android package and title:** `com.gravity.nbarisegv.aos`, listed as "NBA RISE: Basketball Strategy" [E][S6].
  - Google Play lists the release as Oct 19, 2026 and the last update as Oct 28, 2026, at version 1.1.1 [E][S6][S32].
  - It is listed as available on Android and on Windows through Google Play Games, with 100K+ installs [E][S6].
- **iOS:** App ID 6762187862. The English title is "NBA RISE: Basketball Cards" with subtitle "Build a Team. Win by Strategy." The Korean title is "NBA RISE: 농구 카드 전략" [E][S8][S9][S11].
  - Version history: 1.0 (15 Sept), 1.0.3 (8 Oct), 1.1.1 (around 5 Nov 2026) [E][S8].
  - Requires iOS 15. Size 265 MB. Languages: EN, ID, KO, ZH (two variants), TH. Age advisories include "Loot Boxes" [E][S11].
- **Launch:** Oct 20, 2026 at 2:00 PM KST in South Korea, the Philippines, Indonesia, Thailand, Malaysia, Singapore, Australia and New Zealand [E][S3][S4][S23].
  - The developer replies to reviews that access is IP-restricted to those 8 regions [E][S32].
  - GameMeca's English text says "August 20". That is a translation error; its Korean original says only "20일" (the 20th), and other outlets give October [E][S19].
- **CBT:** July 21–29, 2026, ending 4:00 PM KST. Google Play only, same 8 regions [E][S1][S2][S21][S28].
- **Pre-registration:**
  - The official site's text still contains the line "Sep 17, 2026 11:00 (UTC+9) – Official Launch". This looks like a stale plan [E][S12].
  - GamingOnPhone wrote that the iOS listing suggested a launch "by 3rd March 2027" [E][S29].
- **Ratings at time of check:**
  - Google Play, by storefront: PH 4.57, KR 4.70, AU 4.17, from 1,120 ratings [E][S32].
  - App Store: PH 4.8 (41 ratings), KR 4.8 (48), AU 4.27 (22), TH 4.9 (63), SG 4.2 (10).
  - App Store charts: No. 11 Sports in PH and TH; #31 Card in KR [E][S8][S9][S10].
- **Official site and channels:**
  - Site: nbarise.gnjoy.com, in KO/EN/TH/TL/ID/ZH-CN/ZH-TW, with "Game Features", "Player Cards" and "Probability Guide" sections [E][S12].
  - Discord discord.gg/Sz4Za6ZrMy has about 2,740 members [E][S34].
  - Also Facebook (profile id 61590508838426), Instagram @playnbarise and YouTube [E][S12].
- **Lineage:** the Japanese predecessor "NBA RISE" (formerly NBA RISE TO STARDOM) ended service Aug 31, 2026 [E][S37]. Gravity's global marketing calls the new title "self-developed / in-house" [E][S1][S3]. Any carry-over of systems from the Japanese game is outside my scope.
- **Tagline:** "Collect. Build. Rise." The store caption sequence is Collect your stars, Build your collection, Create your lineup, Play with strategy, Rise to the top [E][S6][S8].

## 1. Core loop

1. **Collect.** Open packs ("Scout"), take daily free packs and login rewards, recruit at the Auction [E][S6][S17].
   - Store text: "Open card packs, train players, and collect premium and season-themed cards. New cards based on current season rosters are added regularly." [E][S6]
2. **Develop.** Training (훈련), promotion (승급) and grade enhancement (등급 강화), plus club facilities (구단 시설) [E][S1][S2][S17][S18].
3. **Build the lineup.** Starters and bench, synergies, tactics [E][S6].
4. **Play.** Simulated matches with real-time substitutions and tactic changes, plus a timing mini-game ("SET PLAY") [E][S6][S17][S18].
5. **Compete.** Season-mode leagues, PvP Arena, Popularity Battle, Tower Race, Daily Division, and the club mode RvR Club Conquest [E][S3][S4].

Google Play FAQ quotes [E][S6]:
- "Real-time controls? No. Set your lineup and tactics, then adjust substitutions and strategy during simulated games."
- "Solo play? Yes. Build your team in Season Mode, then join PvP and league rankings whenever you want."
- "Genre? A sports simulation combining player-card collection, team building, card game, and management elements."

Korean Google Play short description [E][S7]: "선수 별 포지션 배치와 상성에 맞는 뇌지컬 전술이 승리의 치트키!" ("Placing each player by position and using brainy tactics that fit the matchups/counters is the cheat code to victory!")

## 2. Match simulation and presentation

- **3D rendering.** Store text: "Detailed 3D player models and dynamic set plays bring your strategy to life. Coach from the sideline as each game plays out as a simulation." [E][S6] Store gameplay screenshots show 3D players on a full arena court with crowd [E][S8].
- **Broadcast-style interface.** Quarter info, team power, points and rebounds are shown in real time (CBT and launch press: "스포츠 중계 방식", sports-broadcast style) [E][S1][S2][S3][S4].
- **Game clock is full NBA length.** Screens show "Q1 12:00" and a 24-second "SHOT CLOCK" (values 17, 18 and 08 seen) [E][S8][S18]. That implies four 12-minute quarters of simulated clock [I].
  - Real-world match duration is not published.
  - One AU App Store review: "The games take way too long with animation… you have to manually subs tired players" [E][S33].
  - One Korean review: "플레이 텀이 길긴한데 자동가능" ("the play time is long, but auto is possible") [E][S32].
- **Match screen elements** [E][S18 screenshot][S8 screenshot]:
  - QUIT, pause, SKIP and settings buttons.
  - A score bar and a "Performance comparison" (경기력 비교) panel with bars for ALL, PG, SG, SF, PF and C.
  - A "Team morale" (팀 사기) bar showing a "능력치 +5%" (stats +5%) badge.
  - Player cards showing live PTS/AST and event pop-ups such as "REBOUND".
  - An AUTO PLAY toggle.
  - Buttons for "상세 보기" (details), "선수 교체" (substitution) and "전술 교체" (tactic change).
  - The AI announces "상대 팀이 전술을 교체하였습니다" ("The opposing team has changed its tactics") with the opposing coach's portrait.
- **SET PLAY (timing mini-game).**
  - ConsumerNews: "'SET PLAY' 시스템… 한 쿼터마다 발동되는 시스템으로 '슛', '블록', '드라이브' 등 지정된 미션에 성공하면 사기가 30% 오른다. SET PLAY가 시작되면 3D 선수 모델이 직접 세트 플레이를 펼쳐…" ("triggers once per quarter; succeeding at a designated mission such as Shoot, Block or Drive raises morale by 30%. When it starts, the 3D player models perform the set play…") [E][S17]
  - iNews24: "정해진 구간에 맞춰 정확한 타이밍에 화면을 터치하는 방식이다. 선수의 체력이 떨어질수록 타이밍을 맞춰야 하는 구간이 좁아져…" ("You touch the screen at the right moment within a set window. The lower the player's stamina, the narrower the window…") [E][S18]
  - Screenshots show a 3-2-1 countdown, a "DRIVE!" banner with commentary ("말도 안 되는 개인기! 수비가 완전히 무너졌습니다!", "Unbelievable individual skill! The defense has completely collapsed!"), a "LAYUP" button with a closing ring and a "1.9" timer, then "성공" (Success) [E][S18].
  - The store screenshot "02_gameplay" shows the same countdown ring over a one-on-one matchup with both players' cards (D. Melton 77 UC vs O. Agbaji 89 R) [E][S8].
  - Players describe it as "슛, 블락등 수동기술" ("manual techniques like shoot and block"), and the developer reply repeats it. Another review mentions "중간에 기술선택이랑 뭐 누르는거" ("mid-game technique selection and button presses") [E][S32].
  - One reviewer asks for an option to skip the forced "특수연출" (special cutscenes) [E][S32].
- **Skip and auto.**
  - SKIP is shown padlocked on the match-prep screen, so it is probably unlocked by progression [E screenshot][I].
  - An EN review: "if you don't really have much time to play, you can use the skip button" [E][S32].
  - An Arena review claims different results when skipping from the start versus skipping mid-game [E][S32].
  - Auto-play and auto tactic selection exist ("전술도 자동으로 선택할 수 있어서") [E][S32][S17].

## 3. Decisions before and during a match

**Before the match** [E][S8 screenshots][S18]:
- STARTING LINEUP / VS screen. Shows both rosters with their coach card, TP, "Rank" and "Wins". Buttons: SKIP, READY, TEAM FORMATION.
- TEAM FORMATION. Shows team name, Team Power (TP), active synergy count, Team Morale, and Offense and Defense ratings. A strategy panel ("SELECT STRATEGY") sets tactic chips, and an AUTO SUBSTITUTION toggle is available.
- MATCH PREPARATION. Shows the performance comparison, TP with synergy bonus, the starters and bench with stamina bars, and buttons for MENU, AUTO SUBSTITUTION and "Q1 START".

**During the match:**
- Real-time substitutions and tactic changes [E][S6].
- Players and reviewers report that stamina and condition change during the game, so substitution and tactic timing matter [E][S17][S18]. iNews24: "주전 선수에게만 의존하기보다 벤치 선수까지 활용해 로테이션을 운영해야 했다" ("you have to run a rotation using the bench rather than relying only on starters") [E][S18].
- Adjust to the opponent's tactics. iNews24: "상대가 어떤 전술을 사용하는지에 따라 대응 방법을 고민하는 과정이 흥미로웠다… 경기 중 상대 전술에 맞춰 공격과 수비 전략을 변경할 수 있어" ("deciding how to respond to the tactics the opponent uses was interesting… you can change offensive and defensive strategy mid-game to counter them") [E][S18]. It compares this to Football Manager [E][S18].
- An Indonesian review asks for PvP where tactic changes are limited to one per quarter. That implies changes are currently not limited this way, but this is unconfirmed [I][S32].
- **Timeouts and clutch:** I found no evidence of a timeout or clutch-moment system. "클러치" (Clutch) does appear as a stat boosted by synergies (Section 5). Not confirmed.

## 4. Tactics system

Sources: Korean tactic-change screenshots [S18], the English TACTICAL and TEAM FORMATION store screenshots [S8], and store text [S6].

**Offensive "priority" tactics** (gold chips, 공격 전술) [E]:
| Korean UI | English |
|---|---|
| 패스 우선 | Pass Priority |
| 돌파 우선 | Drive Priority |
| 3점슛 우선 | 3-Point Shot Priority |
| 미들슛 우선 | Mid-Range Shot Priority |
| 골밑슛 우선 | Paint/inside shot priority (no English label seen) |

Offensive chips target a position and show a percentage, for example "PG Drive Priority 60%", "PG Mid-Range Shot Priority 63%", "SG 돌파 우선 73%", "PG 패스 우선 64%", "SF Pass Priority", "PF Pass Priority" [E]. The percentage's meaning is not documented.

**Defensive tactics** (green shield chips, 수비 전술) [E]:
| Korean UI | English |
|---|---|
| 골밑 사수 | Protect the Paint |
| 패스 차단 | Pass Interception |
| 돌파 차단 | Drive Defense |
| 3점슛 봉쇄 | 3-point shot lockdown (no English label seen) |
| 미들슛 봉쇄 | Mid-Range Defense |

- **Intensity levels.** Defensive chips show "(하)" (low), "(Mid)/(Medium)" and "(강)" (strong) [E]. In the selection list, "미들슛 봉쇄(강)" has two lightning icons where others have one. The column header is "체력 소모" (stamina consumption) [E]. So stronger intensity costs more stamina [I, strongly supported].
- **Counters (상성).** The tactic list has a "상성" (matchup/counter) column with ▲, ▼ or "–" per option [E]. In the example, the opponent prioritised SF paint and mid-range shots. Our "mid-range lockdown (strong)" and "protect the paint" show ▲, and our "mid-range shot priority" shows ▼ [E].
  - Inferred counter pairs: each defensive tactic mirrors one offensive priority (Pass ↔ Pass Interception, Drive ↔ Drive Defense, 3PT ↔ 3PT lockdown, Mid-range ↔ Mid-range lockdown, Paint shot ↔ Protect the Paint). The arrows show advantage against the opponent's current setting [I, from name mirroring plus arrows].
- **Per-player assignments.** Each player shows chips like "Pass Interception / Drive Defense / Mid-Range Sh… ▲", "골밑슛 ▼", "패스 ▲", "Drive" or "Pass", plus a "N⚡" number (1⚡ to 6⚡) [E].
  - Players with more or stronger chips show higher ⚡. This suggests ⚡ is the stamina drain from assigned tactics [I].
- **Tactic slots.** Every screenshot shows 4 tactic chips per team, split variously: 1 defensive + 3 offensive, 3 + 1, 2 + 2 [E]. That suggests 4 tactic slots split freely [I].
- **Coach shown.** Coach names appear beside the tactics: Erik Spoelstra, JJ Redick, Brian Keefe, Mark Daigneault [E]. Coach effects are not documented.
- **"Pick & Roll" and "Pace Interception".** I could not find these in any current store or official-site screenshot (EN/KO/TH/FIL/ID sets checked). The visible label is "Pass Interception (Mid)". "Pace Interception" is likely a misreading, and I could not verify "Pick & Roll" [E, absence].

## 5. Card system

**Six rarities** [E][S17][S16]:
- COMMON (C), UNCOMMON (UC), RARE (R), ULTRA RARE (UR), EPIC, LEGEND.
- ConsumerNews: "커먼, 언커먼, 레어, 울트라레어, 에픽, 레전드 등 총 6개 등급" ("six grades in total: Common, Uncommon, Rare, Ultra Rare, Epic, Legend") [E][S17].
- Badges seen in screenshots: C, UC, R, UR (gold frame) and EPIC (purple frame) [E][S8][S40].

**Editions/themes** [E][S14][S16]:
- **"25-26 SEASON" base set.** The official rate tables list exactly 390 players, each in one rarity: 119 C, 91 UC, 88 R, 63 UR, 29 EPIC [E][S16; tally from offerGroupId 40060].
- **"The Core".** 60 EPIC-tier versions of stars, many of whom are UR or Rare in the base set (e.g. Brunson, Towns, Harden, Paul George) [E][S16 id 20350].
- **"The Edition".** LEGEND-tier retired players. The 10 listed: Bill Laimbeer, Jermaine O'Neal, Dell Curry, Larry Johnson, Tony Parker, Detlef Schrempf, Jeff Hornacek, Zaza Pachulia, Derek Fisher, Peja Stojaković [E][S16 id 10050].
- **Limited themed editions**, each with 10 EPIC players and 1 LEGEND [E][S16]:
  - LOCKDOWN (defenders: Wembanyama, Gobert, Adebayo, Derrick White…; Legend Horace Grant).
  - HALLOWEEN (Curry, LeBron, Brunson, Tatum, Zion, Embiid…; Legend Kevin Garnett).
  - FLAME (Luka, Edwards, Durant, Giannis, Jokić, SGA…; Legend Amar'e Stoudemire).
- **Starter sets:** "Starter" reward packs (26 EPIC eligible) [E][S16 ids 20240, 20280].

**Card face** (official site and store art) [E][S8][S40]:
- OVR number, position(s) (single or dual, e.g. PG/SG, SF/SG, PF/C), team logo, level, edition label ("THE Core", "25-26 SEASON") and rarity badge.
- Formation screens also show a condition arrow (green up, yellow right, orange diagonal, red down), a stamina bar, and an "S n" badge [E].
  - The arrows are probably condition/form. iNews24 confirms "선수의 컨디션에 따라 능력치가 달라지는 시스템" ("stats change with player condition") [E][S18], so the arrow mapping is [I].
  - The "S n" badge uses the same "S" icon as the synergy counter, so it probably counts the synergies a player contributes to [I]. Nothing suggests a salary.

**OVR and level** [E][S8][S40]:
- OVR rises steeply with level. Epic "The Core" cards at Lv.30 show 228–245 on the site and 300–335 on store art. UR Lv.1 shows 123–145. R Lv.20 shows 126. C/UC Lv.1 shows about 61–120.
- Lv.30 is the highest level I saw; the true cap is unknown.
- A reviewer complains that a UR at level 1 can out-rate a lower-level Epic ("ur rank below epic but in level 1 ur has more ovr") [E][S32].
- One screenshot shows a card at 120 in match prep but 77 in the in-match matchup card. The relationship between these numbers is unexplained.

**Attributes:** Synergy effects name three stats [E][S18 screenshot]:
- 기회 창출 (chance/opportunity creation)
- 수비 압박 (defensive pressure)
- 클러치 (clutch)

The full attribute list and per-card skills are not published. "Manual techniques" in set plays (shoot, block, layup, drive) are confirmed [E][S17][S18][S32]. Per-card skills are not confirmed.

**Growth:**
- Level-up and "grade enhancement" (레벨업 / 등급 강화) [E][S1][S2][S21].
- "Card training and promotion" (카드 훈련 및 승급) [E][S3][S4][S19].
- Items: Intermediate and Advanced Training Manuals (from coupon contents) [E][S30]; EXP cards [E][S32 (TH review)].
- A Thai review says upgrades cost a lot of Silver, which is scarce [E][S32].
- The CBT gave rewards for "선수 강화 5회" (enhancing players five times) [E][S21].

**Duplicates and unused cards:**
- A Thai reviewer asked for duplicates to be fusable to level up skills. The developer said it would "share your idea of using duplicate characters to enhance skills" [E][S32]. That implies duplicates are not currently used that way [I].
- Unused players feed the **Exchange (교환소)**. A Korean App Store review describes trading 3 players at a time for one "소형 드링크" (small drink), one exchange per action [E][S9].
- Players and coaches can also be **sold (판매하기)** [E][S18].

**Collection bonus ("Build your collection"):** I found no documented collection-completion bonus. The caption sits on the TEAM FORMATION screenshot [E][S8].

**Coaches:** Real NBA coach cards exist ("players and coaches") [E][S6]. The team menu has "보유 감독" (owned coaches) [E][S18], and coaches appear in the lineup row and on tactic screens [E]. Coach mechanics are not documented. Coaches are absent from all published pack rate tables [E][S16], so how they are obtained is unclear.

## 6. Lineup and team building

- **Roster size.**
  - Five starters plus a bench [E][S6][S17].
  - The bench header tallies positions, e.g. "PG: 3, SG: 1, SF: 1, PF: 2, C: 1" and "PG: 2, SG: 1, SF: 2, PF: 1, C: 2". Both total 8 [E][S8]. That suggests an 8-man bench and a 13-player roster [I].
- **Team ratings** [E][S8]:
  - Team Power (TP), e.g. 12,154 (+2,545 bonus) and 24,754.
  - Offense, e.g. 6,226 (+1,693), and Defense, e.g. 3,739 (+752).
  - Team Morale, e.g. 710.
- **Synergy system** (시너지; screen tabs 전체 = All, 이벤트 = Event) [E][S18 screenshot][S8]:
  - Categories include "지역 연합" (Regional Alliance), with Eastern and Western Conference Boost.
    - Activates when 5 players from that conference are fielded ("동부 컨퍼런스 선수 5명 편성 시 활성화됩니다").
    - Applies to "all matches" (적용 경기: 전체) and to that conference's players.
    - Effects: 기회 창출 +10, 수비 압박 +10, 클러치 +10. Extra TP: +30 per player.
  - Division synergies, e.g. "SOUTHEAST / 사우스이스트 디비전 부스트": 3 players required, +20 TP per player, with a "+" tier giving +140.
  - Team synergies, e.g. "Warriors Teamwork" +300, "Warriors Teamwork+" +300, "호크스 팀워크" (Hawks Teamwork) +100.
  - Counters seen: "10 SYNERGY", "11 활성화된 시너지" (11 active synergies). An "Event" synergy tab exists.
  - An Indonesian reviewer: "the hardest part is looking for players from same club" [E][S32].
  - Store text: "The same player can deliver different results depending on the lineup." [E][S6]
- **Condition, fatigue, injury** [E]:
  - "Manage fatigue, condition, training, and rotations" [S6].
  - GamingOnPhone (CBT): "manage player fatigue, injuries, rotations, and training" [S28].
  - Exchange items include 소형 에너지 드링크 (small energy drink), 소형 구급함 (small first-aid kit) and 컨디션 부스터 (condition booster) [E][S18 screenshot].
  - Reviews complain stamina drains faster than the opponent's, and mention a "stamina and player form" system needing refills or waiting [E][S32]. Whether a separate account-level energy for entering matches exists is unclear.
- **Club facilities (구단 시설).** A team-growth system [E][S17][S18]. Effects are not documented.
- **Salary cap or cost limit:** no evidence found.
- **Team menu (내 팀)** [E][S18][S17]: Team Formation, Owned Players, Owned Coaches, Inventory, Training, Promotion, Club Facilities, Exchange, Sell.
- **Bottom navigation:** MY TEAM, SCOUT, PLAY/home, CLUB, AUCTION [E].

## 7. Modes

The official mode list, from press releases [E][S1–S4][S19][S25]:
- **PvP:** Arena (아레나), Popularity Battle / Popularity Contest (인기 쟁탈전), Tower Race (타워 레이스).
- **PvE:** Season Matches (시즌 경기), Daily Division (데일리 디비전).
- **RvR:** Club Conquest (클럽 점령전).

No source explains the rules of Tower Race, Popularity Battle or Daily Division.

**Season Mode and leagues:**
- ConsumerNews: "리그는 루키3을 시작으로 여러 단계로 구분되며 각 리그에서 우승하면 다음 단계가 순차적으로 개방" ("leagues start at Rookie 3, across several tiers; winning each league unlocks the next") [E][S17].
- Also: "루키3 기준 3경기와 파이널을 치르면 한 섹터가 종료" ("at Rookie 3, three games plus a Final complete a sector") [E][S17].
- Screens show "Regular Schedule 5/5" and "NBA FINALS – GAME 1/1" [E][S8][S18].
- An App Store reviewer describes winning the Finals "by a sweep 4-0", and the developer reply confirms it [E][S8].
  - Read together, Finals series may get longer at higher tiers [I].
- A Korean review complains that "플레이도 결국 리그 몇경기뿐" ("play ends up being just a few league games") [E][S9].

**PvP:**
- "Face players worldwide in PvP and climb the leagues… Rankings reset each season" [E][S6].
- The Korean App Store promo says "실시간 전략 PVP" ("real-time strategy PvP") [E][S9].
- ConsumerNews describes PvP as matches "다른 유저들이 구성한 덱과의 경기" ("against decks built by other users") [E][S17].
  - This suggests asynchronous play against stored decks, but it is unconfirmed [I].
- Players complain about matchmaking against much higher-scored opponents [E][S32].

**Clubs:**
- Guild-style, with member chat and inter-club competition [E][S1][S3].
- The home screen shows "CLUB CLASH" (status 신청 중, "applying/registration") [E][S17 screenshot]. This is probably the Club Conquest entry point [I].
- A Thai player recruiting for a club mentions a 30,000-power requirement [E][S32].

**Other home-screen features** [E][S17 screenshot]:
- EVENT BOARD.
- MATCH PREDICTION (on a timer). One review says "the match prediction is glitch this week rewards all gone", and the developer acknowledges it [E][S32]. Whether it predicts real NBA games is unconfirmed [I].
- TAKEOVER (ended at the time of the screenshot; rules unknown).
- ARENA (4 days 15 hours remaining).
- SHOP, SEASON PASS (3 days 16 hours), STEP UP, NEW PACKAGE.
- A progress banner: "66/90 – 3점슛 콘테스트 (3-Point Contest) – REWARD 200 Gold".

**Missions and dailies:**
- Quests give player packs [E][S17].
- "Free daily card packs and login rewards" [E][S6]. A Korean review says login gives 10 cards per day [E][S32].
- CBT events rewarded playing Arena, Popularity Battle and Club Conquest 1, 3, 5, 7 and 10 times [E][S21][S26].

**Launch events:**
- 14-day check-in through Dec 31.
- Training and promotion missions until Nov 4.
- Match-count rewards.
- "Pre-Season" and "Best 5 Pick-Up".
- Discord sign-up bonus: 500 Gold and 10,000 Silver, until Nov 10.
[E][S3][S4][S19]

**Onboarding:**
- Players pick a favourite NBA team's starter pack and a chosen Epic player. The developer reply confirms: "시작할 때 좋아하는 농구팀 팩과 원하는 에픽 선수를 직접 선택할 수 있는 점" ("at the start you can choose a pack of your favourite basketball team and the Epic player you want") [E][S32].
- iNews24 describes rerolling ("리롤") by grade until you get the player you want [E][S18].
- The tutorial attaches to every menu, and reviewers find it heavy [E][S32].

**Live NBA tie-ins:**
- Uses the 2025-26 roster [E][S1][S3].
- "New cards based on current season rosters are added regularly" [E][S6].
- Seasonal themed packs (Halloween) [E][S16].
- On Oct 28 a Korean user asked when the 26-27 rosters would arrive [E][S9].

## 8. Economy

**Currencies:**
- **Gold:** premium currency, sold as an IAP ("100,000 Gold" for ₩19,000 / A$20.49 / S$18.00) [E][S9][S10].
- **Silver:** soft currency used for upgrades [E][S32][S3].
- **Diamond (다이아):**
  - The Diamond Box pays out 15,000–100,000 Dia [E][S16 id 30010].
  - A Thai review says the player auction uses Diamond, which it calls unobtainable [E][S32].

**Market and Auction:**
- "The 'Market' supports trading for all items, including player cards" (KO: 거래소) [E][S3][S2].
- AUCTION is a bottom-nav tab; ConsumerNews: "옥션을 통한 신규 선수 영입" ("recruiting new players through the auction") [E][S17].
- A Korean review: "카드 경매 시스템도 있어서" ("there's also a card auction system") [E][S32].

**Pack rates.** These come from the official probability pages, linked from the site's "Probability Guide" [E][S13][S14][S16].

Paid packs (25-26 Season, The Core, single-card and 10-card versions):
| Rarity | Rate |
|---|---|
| EPIC | 0.5% |
| UR | 7.5% |
| R | 15% |
| UC | 27% |
| C | 50% |

- In The Core packs, an Epic pull is always a The Core card.
- Within a rarity, every card has equal odds. For example, each 25-26 EPIC is 0.01724%.

The Edition, LOCKDOWN, HALLOWEEN and FLAME packs:
| Rarity | Rate |
|---|---|
| LEGEND | 0.1% |
| EPIC | 0.5% |
| UR | 7.5% |
| R | 15% |
| UC | 27% |
| C | 49.9% |

- In themed packs, Epic and Legend pulls are always the themed versions: each themed Epic 0.05%, the Legend 0.1%.

Reward (free) packs are worse:
- 25-26 and The Core reward packs: EPIC 0.1%, UR 7.6%, R 15%, UC 27.1%, C 50.2%.
- The Edition, FLAME and other themed reward packs: LEGEND 0.02%, EPIC 0.1%, UR 7.55%, R 15%, UC 27.1%, C 50.23%.
- Guaranteed-floor reward packs exist: UC+, R+, UR+, Epic and Legend [E][S16 ids 20xxx].

**Pity and wishlist** [E][S16]:
- 25-26, The Core and themed packs: "구매한 카드 장수가 100장에 도달하면 [EPIC 1장 확정] 버튼이 나타납니다… 게이지는 초기화" ("when the number of cards purchased reaches 100, an 'EPIC 1 guaranteed' button appears… then the gauge resets").
  - Themed packs guarantee Epic or better: Legend 16.67%, Epic 83.33%.
- The Edition: a LEGEND guarantee at 200 cards.
- Wishlist (25-26 pack): "위시리스트를 적용하면, EPIC 등급 당첨 시 위시리스트에 등록한 선수 중 1명이 동일한 확률로 결정" ("when a wishlist is set, an Epic hit picks one of your wishlisted players with equal probability").
- A Thai reviewer: "opened 200 [cards] got 2, guaranteed 1" [E][S32].

**Limited-pack schedule** (KST) [E][S16]:
- LOCKDOWN: 10/22–11/05.
- HALLOWEEN: 10/29–11/12.
- FLAME: 11/05–11/19.

Each runs 14 days and starts a week after the previous one [I, cadence].

**Diamond Box** [E][S16 id 30010]:
- 10 single packs per box, each containing a The Core EPIC (0.5%) or Dia: 15,000 (56.5%), 30,000 (26%), 60,000 (12%), 100,000 (5%).
- It costs ₩1,200 / ₱55 / A$1.39 [E][S9][S8][S10].

**Top IAPs listed on App Store pages** [E][S8][S9][S10]:
- Diamond Box, Beginner Package, Training Package, Currency Pack I, Rookie Package, Veteran Package.
- Light / Regular / MVP Core Support Package; Light / Regular / MVP New Arrival Pack; Core Value Package.
- Double-Double Package, Quadruple-Double Package, All-Star Package, Hall of Fame Package (명예의 전당 패키지, ₩22,000).
- Elite Pass (A$15.49), "Season Step Up Stage 4" (฿25), 100,000 Gold.

Example prices:
| Item | Price |
|---|---|
| Beginner Package | ₩1,200 / A$1.39 |
| Regular Core Support Package | ₩4,400 / A$4.69 |
| All-Star Package | A$7.69 |
| MVP Core Support Package | NZ$11.49 |

- Google Play price range: ₩1,200–₩55,000 / ₱54–₱2,150 / A$1.39–A$57.90 per item [E][S32].
- The "The Core EPIC guaranteed pack" comes with the Beginner Package [E][S16 id 40010].

**Season Pass:**
- "Season Pass with exclusive rewards" [E][S6].
- Monthly: "November Season Pass" appears in What's New [E][S6][S8].
- "Elite Pass" is the paid IAP [E]. It is probably the premium track [I].
- There is also a STEP UP feature (step-up purchase tiers) [E][S10][S17]. Its structure is not documented.
- **VIP:** no evidence.

**Coupons:**
- Pre-registration coupons NBARISEPRE / PRE30 / PRE50 / PRE70 include a "Pre-Registration Exclusive Starter Epic Player Choice Pack".
- Launch codes include The Core 10-card packs, Gold, Silver and Training Manuals.
- Redeem via Menu → Redeem Coupon.
- This is a third-party list [E-third-party][S30].

**Revenue estimate:** AppGoblin estimates 218K installs and $10K+ monthly revenue. This is a third-party estimate only [S35].

## 9. Story and narrative framing

- No story or campaign narrative was found.
- The framing is owner/coach: the developer addresses Korean players as "구단주님" ("team owner") and English players as "Riser" [E][S32].
- Store text: "Coach from the sideline" [E][S6].
- CBT site copy: "From rookie to legend, start your professional journey in the NBA Beta today!" [E][S12].

## 10. Update history and roadmap

- July 21–29 CBT [E][S1].
- iOS 1.0 (Sept 15), 1.0.3 (Oct 8) [E][S8].
- Oct 20 launch [E][S3].
- Probability page note: "SCOUT & PLAYER PACK 항목을 통합 (2026.10.22 추가)" ("Scout and Player Pack entries merged, added 2026-10-22") [E][S13].
- v1.1.1, Google Play updated Oct 28: "1. New Player Cards 2. New BM Products 3. November Season Pass". iOS notes are the same minus BM [E][S6][S8].
- Some users report the early-November update as incompatible with their devices [E][S32].
- No public roadmap was found. A developer reply says "More exciting updates and content are on the way" [E][S32].

## 11. Gaps (could not confirm)

- How Tower Race, Popularity Battle, Daily Division, Takeover and Match Prediction work.
- The full attribute list, per-card skills, maximum level and promotion cost tables.
- Coach effects and how coaches are acquired.
- Whether a timeout system or salary cap exists.
- Real-time match length.
- Whether PvP is synchronous.
- What club facilities do.
- How the Market/Auction currency rules work.
- Season-pass tiers.
- "Pick & Roll": not found in any current asset.
- No Reddit, BlueStacks or LDPlayer guides, Pocket Gamer coverage, or English tier lists exist yet.
- YouTube pages were captcha-blocked; only titles were obtainable [S36].
- APKPure, AppBrain and LDPlayer returned 403; apkcombo failed to connect; the Uptodown URL returned 404.
- Facebook and Instagram post content was not readable.

## Sources
- [S1] https://www.invenglobal.com/articles/24039/gravity-launches-cbt-for-nba-rise-an-officially-licensed-nba-card-game
- [S2] https://www.inven.co.kr/webzine/news/?news=318758
- [S3] https://www.invenglobal.com/articles/27412/gravity-officially-launches-nba-rise-across-8-regions
- [S4] https://www.inven.co.kr/webzine/news/?news=322325
- [S5] https://pr.nba.com/nba-nbpa-gravity-mobile-gaming-experience-asia-pacific (2021 partnership: "free-to-play online strategy and deck-building game")
- [S6] https://play.google.com/store/apps/details?id=com.gravity.nbarisegv.aos&hl=en
- [S7] https://play.google.com/store/apps/details?id=com.gravity.nbarisegv.aos&hl=ko&gl=kr
- [S8] https://apps.apple.com/ph/app/nba-rise-basketball-cards/id6762187862 (screenshots via https://itunes.apple.com/lookup?id=6762187862&country=ph)
- [S9] https://apps.apple.com/kr/app/id6762187862
- [S10] https://apps.apple.com/au/app/id6762187862 ; also /sg/, /my/, /th/, /id/, /nz/
- [S11] https://itunes.apple.com/lookup?id=6762187862&country=ph
- [S12] https://nbarise.gnjoy.com/ko/official ; https://nbarise.gnjoy.com/en/official
- [S13] https://probability.gnjoy.com/NBA/NBARISE/NBARISE/NBA-NOTIFY
- [S14] https://probability.gnjoy.com/NBA/LIST1/LIST1/SCOUT-LIST
- [S15] https://probability.gnjoy.com/NBA/LIST3/LIST3/DIABOX-LIST
- [S16] https://prd-clutch-api.gnjoy.com/ext/news/offerrate?offerGroupId=N (linked from S14/S15). Key IDs: 10020/10040/10050/10070/10080/10090 (Scout packs), 20xxx (reward packs), 40010–40120 (paid packs), 30010 (Diamond Box)
- [S17] https://www.consumernews.co.kr/news/articleView.html?idxno=767029 (hands-on review)
- [S18] https://m.inews24.com/v/2021080 (hands-on review with UI screenshots)
- [S19] https://www.gamemeca.com/en/view.php?gid=1782075
- [S20] https://www.gamemeca.com/en/view.php?gid=1778125
- [S21] https://www.ipnn.co.kr/news/articleView.html?idxno=416861 ; https://www.ipnn.co.kr/news/articleView.html?idxno=417946
- [S23] https://www.thisisgame.com/articles/431166 ; https://www.thisisgame.com/articles/428056
- [S25] https://gamefocus.co.kr/detail.php?number=179926 ; also reprints at https://www.khgames.co.kr/news/articleView.html?idxno=309489 , https://www.newstap.co.kr/news/articleView.html?idxno=336112 , https://www.insight.co.kr/news/578555 , https://kpenews.com/View.aspx?No=4271498 , https://news.bizwatch.co.kr/article/mobile/2026/07/22/0026 , https://m.inews24.com/v/2017022 , https://www.consumernews.co.kr/news/articleView.html?idxno=766328
- [S26] https://playcubic.com/gravity-memulai-cbt-global-card-game-basketball-nba-rise/
- [S27] https://mgronline.com/game/detail/9690000072347
- [S28] https://gamingonphone.com/news/nba-rise-hits-the-court-with-its-basketball-action-now-live-with-its-first-closed-beta-test-on-android
- [S29] https://gamingonphone.com/news/nba-rise-opens-pre-registration-on-mobile-as-the-basketball-card-strategy-game-prepares-for-launch
- [S30] https://ucngame.com/codes/nba-rise-codes/
- [S31] https://www.mgoddess.com/news/nba-f286376ca5/?lang=en
- [S32] Google Play user reviews and developer replies for com.gravity.nbarisegv.aos (EN/KO/TH/ID locales; about 370 reviews pulled via google-play-scraper)
- [S33] https://itunes.apple.com/au/rss/customerreviews/id=6762187862/sortBy=mostRecent/json (plus the ph/th feeds)
- [S34] https://discord.gg/Sz4Za6ZrMy
- [S35] https://appgoblin.info/apps/com.gravity.nbarisegv.aos
- [S36] https://www.youtube.com/watch?v=HGG8_t5ZKVE ("NBA RISE: Basketball Strategy Gameplay (Android, PC)", Lenzy Games); https://www.youtube.com/watch?v=TXHgQuEib8A (AetherFyre)
- [S37] https://gamebiz.jp/news/430264
- [S40] https://imgc.gnjoy.com/games/nbarise/official/card/card-1.webp … card-19.webp
- Also checked: https://www.mumuplayer.com/games/sports/nba-rise-basketball-strategy-on-pc.html (it repeats the store text)

Working files (screenshots, rate-table text, review dumps) are in (session scratchpad, not preserved)/scratchpad.
