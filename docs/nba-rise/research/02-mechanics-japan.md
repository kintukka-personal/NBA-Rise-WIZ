<!-- Research report compiled 2026-11-08. Source links inside; working-file paths refer to a temporary session folder that was not preserved (the official pack data is preserved in ../data/). -->

# NBA RISE TO STARDOM / NBA RISE (Japan): gameplay mechanics from Japanese sources

## 0. What this is based on, and how reliable it is

- **Main source: the official news archive.** The official site's news archive at `nbarise.com` is still online. It holds every notice from September 2021 to September 2026, covering both TO STARDOM and NBA RISE. I crawled all 480 posts in its WordPress sitemap and read them. They include beginner guides ("HOW TO RISE"), patch notes, card stat blocks, event rules and the data-migration list for the renewal. Most of this report cites individual posts as `https://nbarise.com/<slug>/`.
  - Full text: `(session scratchpad, not preserved)/site/all.txt`
  - Index: `(session scratchpad, not preserved)/site/index.tsv`
- **Screenshots.** I looked at in-game screenshots from:
  - the Game Watch (Impress) preview for TO STARDOM;
  - Gravity Game Arise press PDFs (2025-02-18, 2025-05-22) for NBA RISE.

  Anything marked **[Screenshot]** I read off those images. No article says it in words.
- **Old domain is now spam.** `nbarisetostardom.com` has been taken over by an Indonesian gambling spam page. Do not cite it as a live source. Pages from the old domain now live on `nbarise.com` under the same slugs.
- **Official X account:** @NBA_RISE (not @NBARISE_JP).
- **Strategy wikis.** GameWith, AppMedia, Altema, Game8 and Famitsu have no NBA RISE wiki that I could find. The only one is a thin Gamerch wiki (`gamerch.com/nba-rise`).
- **Blocked sources.** archive.org, gamer.ne.jp and YouTube watch pages were not reachable from here.
- **Labels.** **[Explicit]** = stated in a source. **[Inferred]** = my reading. **[Screenshot]** = seen in an image.
- **Reliability warnings:**
  - **app-liv.jp/5342528** is unreliable. It is a generic-sounding review "last updated Dec 2021". Its claims, such as "絆" (bond) boosts and "1試合が数分で区切られる", are not supported by any other source.
  - **Dengeki (202608/83074)** gives the launch as Nov 18, 2021. The official launch was **Nov 24, 2021 15:00**. It had been planned for Nov 18 and was delayed (https://nbarise.com/yteahlk/, https://nbarise.com/ygspo/, https://nbarise.com/sydja/).

---

## 1. The player's role and the game's framing

- **[Explicit] You are the bench boss, not a player on the court.** gamebiz: 「プレイヤーは選手を操作するのではなく、監督やヘッドコーチといった指揮官の立場として、楽しむことができる」 ("you don't control the players; you enjoy it as the commander, i.e. the manager / head coach") (https://gamebiz.jp/news/337867). BlueStacks JP calls it player-development-sim-centric with no action elements: 「育成シミュレーションの要素を主軸」.
- **[Explicit] Franchise framing ("マイチーム" / My Team).**
  - At the start you pick one of the 30 NBA teams: 「プレーヤーは初めに「NBA」30チームの中からどのチームを使うかを選ぶ」.
  - The opening roster is only a head coach and 5 players; the rest come from offers. You can change team later in your profile, but not mid-season (Game Watch, https://game.watch.impress.co.jp/docs/kikaku/1367576.html).
  - The goal is to win the championship over the season: 「自分だけのオリジナルチームを作ってシーズン優勝を目指そう！」 (2024 press PDF).
- **[Explicit] No real GM or owner layer.** There is no salary cap, contracts or payroll. I found no mention of 年俸, サラリー or 契約金 in any source. The only "contract" is the 「ヘッドコーチ契約画面」 (head-coach contract screen), which is just where you buy coaches (https://nbarise.com/yjhnds/).
- **[Explicit] The narrative content is NBA history, delivered through events.** There is no persistent story mode.
  - **TO STARDOM "NBA HISTORYイベント" / "ヒストリーイベント"**: 「NBA選手やチームにフォーカスし、様々なストーリーをたどることができるイベント…ストーリーを確認可能」 ("events focusing on an NBA player or team, letting you follow various stories"). Chapters unlock in a 【ヒストリー】 screen as you clear missions or level the featured player. Examples: 渡邊雄太物語 (https://nbarise.com/ywmbk/), BULLS DYNASTY (https://nbarise.com/wxofhgi/).
  - Many events recreate real games: 2020-21 Christmas games, the 75th Anniversary Team, the 1989/90 Finals, the 2013-14 Playoffs, the 2022 Finals, the 2023 In-Season Tournament, 2025 Playoffs/Finals and others.
  - **Tutorial:** Yuta Watanabe appears and explains basketball basics: 「試合人数、試合の流れなど、基本からをすべて教えてくれる」 (Oricon, https://www.oricon.co.jp/special/57709/).

---

## 2. NBA RISE TO STARDOM (Nov 24, 2021 – Sep 30, 2024)

### 2.1 Match engine and presentation

- **[Explicit] Format.** 「実際のNBA同様、1試合各12分4分割（クォーター）方式」: four 12-minute quarters, like the NBA (gamebiz). **[Screenshot]** The skill-training screen tags skills by 1Q/2Q/3Q/4Q/OT, so overtime exists.
- **[Explicit] Auto-sim with three kinds of input.** 「チームの作戦決定とクオーターごとのメンバー交代、そして…「クラッチプレイ」の指示を出すことの3点だけ」 ("only three things: deciding team tactics, substitutions each quarter, and directing Clutch Plays") (Game Watch).
  - Dengeki Online (denfaminico): 「基本的にプレイヤーは流れを見守るだけでよい」 ("basically you just watch the flow") (https://news.denfaminicogamer.jp/kikakuthetower/211125b).
- **[Explicit] How a possession resolves.** Matchups between players resolve on numbers.
  - Game Watch: momentum helps 「クラッチやシミュレーションで数値が同じだった場合に勝ちやすくなる」 (helps you win when values are tied, in clutch or in the simulation).
  - Some skills read 「オフェンス時のシミュレーション中5％の確率で敗北を回避し再戦できる」 ("5% chance during offensive simulation to avoid a loss and replay it"). These are the **リバウンド** (Rebound) skills, e.g. Grant Hill (https://nbarise.com/pervbho/).
  - **[Inferred]** The sim is a chain of per-possession, player-vs-player stat duels that a skill can re-roll.
- **[Explicit] Two viewing modes.**
  - **ライブビュー (Live View):** highlight cutscenes. 「選手の印象的なプレイのみを抜粋して見る」 ("watch only excerpts of impressive plays").
  - **カードビュー (Card View):** every play shown as a card battle. 「試合中に行われるすべてのプレイを選手同士のカードバトルとして観戦」 (HOW TO RISE 試合編, https://nbarise.com/tyujdk/).
  - Players are 3D-rendered: 「3Dグラフィックで表現される選手のプレー」 (gamebiz).
  - A 「BOX SCORE」 can be reviewed after each quarter (denfaminico).
  - Ver 1.4.0 changes: clutch and highlight movies shortened, highlights made skippable, Card View speed setting saved (https://nbarise.com/yjhnds/).
- **[Screenshot] Pre-match screen (試合準備, Match Preparation)** (Game Watch screenshot #10):
  - tabs 「相手チーム予測」 (opponent forecast) and 「チーム登録時」;
  - each side's active tactic line, e.g. 「OFF重視：ドライブ+1/ブロック-1【主軸：全選手】」 and 「スタミナコスト」;
  - team aggregate OFF values (SHOOT/PASS/DRIVE, e.g. 27/28/33) and DEF values (PASSCUT/STEAL/BLOCK);
  - MOMENTUM values (750 vs 1000) and CLUTCH gauges;
  - a 「対戦確率を表示」 (show matchup probabilities) checkbox, 自動編成 (auto-build), and a TIP OFF button.
- **[Screenshot] Card View (#11):**
  - one card vs one card per possession (e.g. UC Cedi Osman "PASS" vs UR Christian Wood "PASSCUT");
  - percentage tags on each on-court card (35%/20%/5%; **[Inferred]** the chance that player is involved);
  - commentary line (「優位を保てるでしょうか」, "can they keep the advantage?"), team power numbers, a "SKIP CLUTCH PLAY" button.

### 2.2 クラッチプレイ (Clutch Play) and クラッチゲージ (Clutch Gauge)

- **[Explicit] Trigger and effect.** 「クラッチゲージが溜まると…「クラッチプレイ」が始まります。クラッチゲージが溜まったチームがオフェンスとなりプレイヤーが選手の行動を決めて対決し勝利したチームのモメンタムが上昇します。」 ("When the clutch gauge fills, a Clutch Play starts. The team whose gauge filled is on offense; the player chooses actions; the winner gains Momentum.") (https://nbarise.com/tyujdk/).
- **[Explicit] The choices.**
  - Offense: 「パス・ドライブ・シュート」 (pass / drive / shoot).
  - Defense: 「スティール・ブロック・パスカット」 (steal / block / pass-cut).
  - You first choose which player takes the clutch play (Game Watch).
  - Choices have a rock-paper-scissors relationship: 「シュートはブロックに弱くスティールに強いなど、各行動にはじゃんけんのように相性が設定されている」 ("e.g. shoot is weak to block and strong vs steal") (Game Watch).
  - Other sources call it 「三すくみ」 (three-way standoff) (Oricon, denfaminico news 211126f).
  - There is a time limit: 「時間制限もあり」 (gamebiz).
- **[Explicit] How it resolves.**
  - Each player has a number per action. 「単純に相手の選んだ行動の数字より大きければクラッチプレイが成功」 ("if your number beats the number of the opponent's chosen action, the clutch play succeeds") (Game Watch).
  - A favourable matchup multiplies your value: 「強い手を出せた場合には数値が1.5倍となる」 ("x1.5 if you throw the stronger hand") (denfaminico).
  - Raw stats still dominate: 「たとえ三すくみで勝ったとしても、能力値で勝つことが最も優先される」 ("even if you win the RPS, winning on stats takes priority") (Oricon).
  - denfaminico also writes 「相手の3ポイントシュートが確定」. In context this looks like an example where losing the duel concedes a three. **[Inferred]**
- **[Screenshot] Clutch UI** (Game Watch #13/#14):
  - each on-court player shows their three values (small integers, e.g. 2/2/1);
  - 「カードをタップで決定」 (tap a card to decide);
  - a **「TEAM」** option with its own value (also in the 2021 PV commands 「シュート」「パス」「ドライブ」「チーム」, kamigame) and a 「BENCH SKILL」 slot;
  - an ~19-second countdown.
  - **Not confirmed in text:** what the TEAM command does.
- **[Explicit] Skills tie into clutch.**
  - Clutch-specific skills: 「クラッチプレイのマッチアップ時、自分がOFFの場合 DRIVE+5 発動後、スタミナ-120」 ("at clutch matchup, if on offense, DRIVE+5; then −120 stamina").
  - 「クラッチセレクトOFF/DEF時…クラッチプレイ中」 modifiers.
  - Skills that add clutch gauge, e.g. 「リード クラッチアップ+10：自身がコートにいて、モメンタムが勝っていると クラッチゲージ+10」 (https://nbarise.com/wvmkoit/).

### 2.3 モメンタム (Momentum)

- **[Explicit] Definition and effects.**
  - Momentum represents the flow or morale of the game.
  - Higher momentum wins ties: 「この値が相手チームより高いと選手の引き分け時にも勝利が可能となり、スコアが獲得できる」 ("if higher than the opponent, you win even on a draw and score") (denfaminico).
  - It enables comebacks: 「前半で得点差が開いていても、「クラッチプレイ」などでモメンタムが上昇していけば、終盤で逆転…」 (gamebiz).
- **[Explicit] Skill keywords built on momentum.**
  - **リード** (Lead): when your momentum is ahead. **リバーサル** (Reversal): when it is behind.
  - Bench skills: e.g. 「リード モメンタムブースト5％：自身がベンチにいて…Q終了まで モメンタム+5％」 (Lead Momentum Boost 5%: while this player is on the bench, momentum +5% until quarter end) (https://nbarise.com/wvmkoit/).
- **[Screenshot]** The team-formation screen shows a pre-match team モメンタム value (e.g. 1,170). **[Inferred]** It is partly derived from the roster.

### 2.4 スタミナ (Stamina) and substitutions

- **[Explicit] Rules** (https://nbarise.com/tyujdk/):
  - Players on court lose stamina gradually.
  - 「スタミナが完全になくなってしまうと能力が半減する」 (at zero stamina, abilities are halved).
  - Stamina recovers between quarters, and bench players recover more than players on court.
  - Skills also spend stamina (e.g. −120 to −760).
- **[Explicit] Ver 1.4.0 added 「オススメ自動編成」 (recommended auto-lineup) between quarters.** It picks players by 「ポジション適正・スタミナ残量・次Qでスキルを発動できるか」 (position fit, remaining stamina, whether a skill can fire next quarter). It also renamed the old auto-build 「カスタム自動編成」 and added 「得意ポジション優先」 (prioritise favoured position) (https://nbarise.com/yjhnds/).
- **[Explicit] Auto-build (自動編成) presets** (gamebiz): 「TP（総合力）重視、スタミナ優先、オフェンス・ディフェンス優先」 (TP-first, stamina-first, offense/defense-first).

### 2.5 Head coach (ヘッドコーチ / HCカード) and tactics (作戦)

- **[Explicit] Roster size.** A team is 「ヘッドコーチ1人、スターティングメンバー5人とベンチメンバー8人、控えのリザーバー2人」 (1 head coach + 5 starters + 8 bench + 2 reserves) (Game Watch). Reserves can't come in once the game starts: 「出場できる選手は実質13名」 (effectively 13 usable players) (denfaminico).
- **[Explicit] TP (チームパワー, Team Power).** 「スターターやベンチ選手のステータスに、ヘッドコーチの作戦が合わさった値」 (starter and bench stats combined with the HC's tactic) (https://nbarise.com/tyujdk/).
- **[Explicit] 作戦 (Tactics).** 「ヘッドコーチが複数所持しているチームの戦略」 (each HC owns several team strategies). Each tactic has three parts:
  - **作戦補正** (tactic modifier): plus and minus stat changes; some tactics change nothing;
  - **主軸ポジション** (key position): 「試合中に他の選手より多く活躍」 (players in that slot get involved more than others);
  - **スタミナコスト** (stamina cost): higher cost drains more stamina during the match.
- **[Screenshot] Tactic examples:**
  - 「補正無し【主軸：全選手】」 (no modifier, all players key);
  - 「OFF重視：ドライブ+1/ブロック-1【主軸：全選手】」;
  - 「DEF重視：ブロック+1/ドライブ-1【主軸：PF/C】」;
  - one coach showed "1/6" tactics.
  - Oricon: 作戦変更 decides 「オフェンスとディフェンスのどちらを優先するか、どのポジションの選手を重点的に動かすか」 (whether to prioritise offense or defense, and which position's players to feature).
- **[Explicit] Buying coaches.**
  - 「ヘッドコーチはショップから購入すると手に入る」 (Game Watch).
  - **[Screenshot]** Real NBA coaches cost **30,000 マネー per card** in the Shop tab ヘッドコーチ. Examples: Brad Stevens, Steve Nash, Tom Thibodeau, Doc Rivers, Nick Nurse, Billy Donovan (shown "SOLD OUT"), J.B. Bickerstaff, Dwane Casey.
  - Ver 1.4.0 moved the coach screen from Shop to Team and showed all coaches' abilities in a list (https://nbarise.com/yjhnds/).
  - gamebiz: 「オフェンス特化にしたい場合はオフェンスのパラメータが強いコーチを起用」 (for an offense-heavy plan, pick a coach with strong offense parameters).
  - **Not confirmed:** the exact coach parameter set beyond the tactic list.

### 2.6 Player cards

- **Rarity (レアリティ) [Explicit].** C → UC → R → UR → EPIC. Oricon: 「C、UC、R、URなどを経て「EPIC」まで育成が可能」. Store rarity labels read COMMON / UNCOMMON / RARE / ULTRA RARE (shown as "UltraRare" in posts) / EPIC.
  - **LEGEND:** a separate top tier for retired greats, e.g. [LEGEND]パトリック・ユーイング.
  - **SECRET:** an alternate-art / signed version of an EPIC.
    - 「サイン入りのSECRET「渡邊雄太」」 (https://nbarise.com/ywmbk/).
    - 「SECRETはEPICと異なる写真で登場」 (SECRET uses a different photo from the EPIC) (https://nbarise.com/bytrnc/).
    - Many EPICs carry the note 「この選手は[SECRET]でも獲得できます」.
    - Pickup lists use slashes such as [SECRET/EPIC] and [UR/R]. **[Inferred]** The card can be pulled at either rarity, i.e. some boxes contain already-upgraded copies. The 2020-21 Season Offer states 「本オファーではレアリティアップ済みの選手は収録されておりません」 ("this offer contains no already-rarity-upped players") (https://nbarise.com/iijsda/). Some skills also reference 「初期レアリティ」 (initial rarity).
- **Stats [Explicit + Screenshot].**
  - Offense: SHOOT, DRIVE, PASS. Defense: STEAL, BLOCK, PASSCUT. These are the same six actions as the clutch play. 「攻守にそれぞれ3つずつの能力値」 ("three ability values each for offense and defense") (denfaminico).
  - Listed at max level as small integers (mostly 4–7). Example: [Epic][SF] Jayson Tatum SHOOT 7 / DRIVE 6 / PASS 5 / STEAL 5 / BLOCK 5 / PASSCUT 5 (https://nbarise.com/zlxkgo/).
  - Separate OFF/DEF summary values and **スタミナ** (~1,100–1,300) (training screenshot #19).
- **Positions.** Each card has one position (PG/SG/SF/PF/C). Playing a card at its **得意ポジション** (favoured position) gives an 「能力値ボーナス」 (stat bonus). A bug notice confirms this: Anthony Edwards' 「適正ポジション補正」 (position-fit bonus) was firing at SF instead of SG (https://nbarise.com/nhufdi/).
- **Skills (スキル).**
  - Three per card, labelled ACTIVE or PASSIVE **[Screenshot]**, each tagged with the quarters it can fire in.
  - Skill level 1–5. Levels raise effect values and/or add quarters: 「能力が強化されたり発動するタイミングが増えたり」 (https://nbarise.com/lknfhd/). Generic skills such as クラッチアップ, モメンタムブースト and ファンアップ got per-level scaling in Ver 1.2.0 (https://nbarise.com/wvmkoit/).
  - Skill families seen in card posts:
    - clutch-matchup actives (+5/+6 to one action, costing stamina);
    - クラッチセレクトOFF/DEF modifiers;
    - リード / リバーサル (momentum-conditional);
    - スタミナフォロー (a teammate is at 0 stamina);
    - スタミナトップ (all opponents have less stamina than you);
    - レアリティトップ (your on-court teammates have lower initial rarity);
    - リバウンド X% / クラッチリバウンド (re-roll a lost duel);
    - **シール** (seal: 「マッチアップ時相手のBLOCKを封じる」, blocks the opponent's BLOCK option);
    - triggers on the opponent's パッシブスキル;
    - ファンアップ (more fans earned after the match).
- **[Explicit] Same-name rule.** 「同名の選手は同じチームに編成できません」 (players with the same name can't be on one team). This is on every offer notice.
- **[Explicit] Card seasons.**
  - Cards are seasonal. 「その年のカードは該当シーズンの間にしか入手できない規約」 ("a year's cards can only be obtained during that season") (denfaminico). gamebiz 333960 says the same.
  - At launch the base set was 2020-21: 「SEASON BOX 2020-21 vol.1」 … 「2020-21シーズンに活躍した選手」 (https://nbarise.com/ygdplc/).
  - The 2020-21 boxes ran "until the end of the 2020-21 season" and were extended to 2022/12/31 (https://nbarise.com/fdokix/).
  - **Not confirmed:** I found no 2021-22 SEASON BOX. Content updates stopped in Feb 2023.
- **[Explicit] Roster size.** 「総勢450名の選手カード」 (kamigame) and 「450名以上が実名で登場」 (press). Current and legend players.

### 2.7 Getting players: offers, events, trades

- **オファー (Offer, the gacha) [Explicit].**
  - 「ゴールドやオファーチケットを消費して選手を獲得…1パックから5人、1BOXからは30パックで150人」 ("spend Gold or Offer Tickets; 1 pack = 5 players; 1 BOX = 30 packs = 150 players") (https://nbarise.com/lknfhd/).
  - Each slot is drawn separately: 「抽選は、各枚数（枠）ごとに行われます」 ("draws are made per slot"), with a 「レアリティごとの封入枚数」 (cards per rarity) breakdown.
  - Duplicates are possible: 「選手の提供数に制限はない」 ("no cap on how many of a player are offered").
  - **[Screenshot]** SEASON BOX vol.1: a pack costs 1 ticket; a BOX costs 5,500 Gold.
- **Offer lines [Explicit]:**
  - SEASON BOX 2020-21 Vol.1–8, each covering a group of teams;
  - team "Pickup" offers with raised rates;
  - EVENT BOX / EVENT OFFER, tied to events, with Pt-boost players;
  - themed limited boxes: THE DUEL BOX, Big Man's Legacy, NEW YEAR LEGEND/DREAM BOX, 2022 NBA CHAMPIONS OFFER;
  - **NBA ALL TEAM OFFER:** ticket-only, fed by season-mode rewards (https://nbarise.com/tsxwer/);
  - **2020-21 Season Offer:** all 2020-21 SEASON BOX players;
  - **UR以上確定 / EPIC確定オファー** (UR-or-better / EPIC-guaranteed offers).
- **Offer tickets.** Ticket types are box-specific. 「SEASON BOXチケット」 works for every SEASON BOX and Pickup (https://nbarise.com/cmgtok/). There are also event tickets and "引換券" (ticket vouchers; 10 vouchers = 1 ticket).
- **BOX purchase bonuses (BOX購入特典).** Escalating per-BOX bonuses, e.g. a guaranteed [SECRET] Jokić on the 3rd BOX (https://nbarise.com/yoiqk/) or Gold on BOXes 3/6/9 (https://nbarise.com/ylmvsde/).
- **Rates.** In-game only (【オファー】→【提供割合】). **Not found:** a pity/ceiling system for offers.
- **選手指名権 (Player Designation Ticket) [Explicit].** 「EPIC選手指名権」 lets you pick any EPIC; it was given after the tutorial. 「LEGEND選手指名権」 lets you pick any LEGEND; it was a mission reward for 「EPICの選手1人をレベル50まで育成する」 ("raise one EPIC to Lv50") (https://nbarise.com/elkaxc/).
- **トレード (Trade) [Explicit].**
  - 「選手を出品したり、選手やゴールドを使用して出品された選手と交換」 (list players, or use players or Gold to exchange for listed players).
  - Rarity limits rise with **拠点 (base) level** (https://nbarise.com/lknfhd/). Trade unlocks at 拠点グレード2; LEGEND trading at grade 5 (https://nbarise.com/yrlqoa/).
  - Oricon: you set 「出品するカードと譲ってほしいカード、あるいはゲーム内のマネー」 (the card you list and the card you want, or in-game money). denfaminico also says マネー. **Note:** official notices say ゴールド, so the press accounts conflict.
  - Billed as an industry first: 「業界初のオンライントレード」 (Oricon).
  - **NPC出品リスト (NPC listing):** LEGEND players sold for 4,500 Gold each, refreshed 「3日ごと」 (every 3 days) (https://nbarise.com/yrlqoa/, https://nbarise.com/kjf8fd/).
  - **Anti-collusion change (Dec 2021):** sellers shown as "PLAYER" and the follower filter removed (https://nbarise.com/ybpas/).
  - **[Explicit/Inferred]** A 「トレードのドラフト」 (trade draft) sub-feature was disabled in the 2021 test, and the renewal's data list mentions 「トレード落札履歴」 (winning-bid history). That suggests an auction/draft layer. Oricon: 「『ドラフト』の機能も将来、実装予定」 ("a Draft feature is also planned").
- **Events, login bonuses and missions** award players, tickets and points (§2.10).

### 2.8 Player growth

- **トレーニング (Training) [Explicit].** 「マネーを消費して選択した選手のレベルを上げる…レベルの上限はレアリティによって決まっている」 ("spend Money to raise a player's level; the level cap depends on rarity").
  - **[Screenshot]** Target-level UI; a UR card capped at 60, with Lv1→20 costing 8,149 Money.
  - Players also earn 「シーズンで獲得できる選手経験値」 (player EXP from season games) (https://nbarise.com/ywmbk/).
- **レアリティアップ (Rarity Up) [Explicit].** 「同名同レアリティの選手を複数人集めることでその選手のレアリティを1つ上げる…レベルの上限がアップ」 ("collect several copies of the same name and rarity to raise rarity by one; the level cap rises"). Game Watch caption: 「3人集まるとRからURになった!!」 ("3 copies took it from R to UR").
- **スキルトレーニング (Skill Training) [Explicit].**
  - Raises skill level over time and needs a **trainer player of EPIC or higher**, who is not consumed (https://nbarise.com/lknfhd/).
  - **[Screenshot]** One slot, 24:00:00 duration, 7,500 Money.
  - You can finish early with Money: 「マネーを消費してトレーニング終了」 (https://nbarise.com/y2etsa/).
  - 「スキルタイプボーナス」 (skill-type bonus): extra skill EXP if the trainer has a skill of the same type (https://nbarise.com/gfydus/).
- **Other [Explicit]:** ストレージ (storage for spare cards) and bulk 売却 (selling) (Ver 1.4.0, https://nbarise.com/yjhnds/).
- **Facility upgrades** (§2.9) reduce training cost and boost skill EXP.

### 2.9 拠点 (Base), facilities, fans

- **[Explicit]** 「ファンが増えていくと拠点のグレードが上がっていく」 ("as fans grow, the base grade rises").
- **[Explicit]** There are 9 facility types, e.g. 「基礎トレーニング施設」 (basic training facility) and 「スキルトレーニング施設」 (skill training facility). Effects include more fans, cheaper training and more skill EXP (Game Watch).
- **[Explicit]** denfaminico names 「トレーニング施設」, 「バックオフィス」 (raises the mission cap) and 「オフィシャルストア」 (generates Money over time).
- **[Screenshot]** The home screen is an isometric city with buildings for トレード / オファー / チーム / 試合 / オフィシャルストア (shows "0/72,000" Money accrued) / ショップ, plus "拠点 グレード 5".
- **[Explicit]** ファン (fans) and マネー are earned after each match. Fan count adds a bonus to season Money (https://nbarise.com/yhgq/).

### 2.10 Game modes

- **シーズン (Season).**
  - **[Screenshot]** An 82-game calendar (「次の試合へ (1/82試合)」, "next game, 1 of 82") with conference standings. Games are marked **PLAY-MATCH** (you play it) or **SIM-MATCH** (simulated).
  - **[Explicit]** Ver 1.4.0 made SIM-MATCH give fans, Money and EXP too.
  - Difficulty is a 10-step scale; levels 11–13 were added in Ver 1.4.0, along with an opponent-starters preview and a radar-chart team comparison (https://nbarise.com/yjhnds/).
  - Recommended-difficulty display, plus 「月間リザルト」 (monthly results) rewards of ALL TEAMチケット引換券 scaled by difficulty and win rate (https://nbarise.com/tsxwer/).
  - Regular season leads into "NBA Playoffs" (https://nbarise.com/yjghw/).
- **スコアランキング (Score Ranking) [Explicit].** Asynchronous PvP against other users' teams.
  - Oricon: 「ほかのプレイヤーのチームと対戦しプレイヤーの頂点を目指す」 ("battle other players' teams to reach the top"). denfaminico: 「プレイヤー同士の非同期型PvP」 (asynchronous PvP between players).
  - Uses your 「メインチーム」 (main team).
  - Divisions: 「1～4部リーグ」 (Division 1–4 leagues) (https://nbarise.com/yjewry/).
  - Cumulative-point rewards (https://nbarise.com/vjdska/).
  - Runs in short cycles, e.g. 2/16–2/22/2023 (https://nbarise.com/vpoelc/).
- **Events [Explicit].** Event categories:
  - **チャレンジイベント (Challenge):** special legend teams appear in Score Ranking matchmaking if your main team's TP is ≥200/250/300. Points; e.g. "beat DREAM TEAM 1 ten times + 300,000 pts" earns [LEGEND] Magic Johnson (https://nbarise.com/idcvg1m/, https://nbarise.com/rjkd9ujf/).
  - **VSイベント (Versus):** fight two themed teams. Higher difficulty gives more points. Pt-boost players on your roster add points; points go to a ポイント交換所 (exchange) (https://nbarise.com/vunhuf/).
  - **ヒストリーイベント (History):** level a featured player obtained C→UC→R→UR→**SECRET** to unlock story chapters (https://nbarise.com/wxofhgi/, https://nbarise.com/yghtau/).
  - Event-linked login bonuses and missions.
- **プレイヤーマッチ (Player Match, real-time PvP) [Explicit].**
  - Pre-opened Jul 21–28, 2022 and fully opened Dec 8, 2022.
  - 「「プレイヤーマッチでのみ使用可能なカード」でデッキを組み、リアルタイムで他のユーザーと対戦」 ("build a deck from cards usable only in Player Match and battle others in real time").
  - Shared 「カードプール」 (card pool) with fixed growth, so everyone plays on equal terms.
  - Modes: クイックマッチ (quick match), カスタムマッチ (custom rooms, spectating) and イベントマッチ (event match).
  - The RISING ARENA regulation allowed EPIC ≤3, UR ≤5, R ≤10, UC ≤15, C ≤15 cards. Max level and max skill level; no rarity-up; no SECRETs.
  - Sections of up to 3 games; rewards by wins.
  - If no match is found, the opponent may be an NPC (https://nbarise.com/rilims/, https://nbarise.com/pmlqcb/).
- **Missions.**
  - デイリーミッション (daily missions): originally 3 random + "clear 3"; from May 2022, 7 fixed + "clear 3" + "clear all" (https://nbarise.com/dufnrj/).
  - デイリーマラソン (Daily Marathon), added in Ver 1.4.0: rewards include 24-hour effects and EPIC-guaranteed / UR-or-better offer tickets.
  - 期間限定 (limited-time) and SEASON BOX 連動ミッション (box-linked missions, e.g. "put players from these teams in your starters and play Season") (https://nbarise.com/ygfha/).
- **Recurring campaigns [Explicit]:**
  - シーズン獲得マネー: Season PLAY-MATCH Money x2 (https://nbarise.com/yhgq/);
  - トレーニング割引: training cost −10% (https://nbarise.com/ytflkj/);
  - スキルトレーニング獲得経験値UP: skill EXP x1.5 (https://nbarise.com/upedfrty/);
  - オフィシャルストア獲得マネー増加: store Money x1.5 (https://nbarise.com/yvbc/).
- **Promised but not shipped (as far as I can find):** a world championship (世界大会), an eSports prize mode (eスポーツモード / 賞金つきの大会), and Asia-wide distribution (gamebiz, denfaminico, Oricon).

### 2.11 Currencies and monetization

- **ゴールド (Gold), premium [Explicit].** Paid and free portions. Used for offers, BOXes, trades and recovery. Price table from the Oct 2022 revision (https://nbarise.com/bkaole/): 80 Gold ¥160, 520 ¥1,000, 1,950 ¥3,600, 3,260 ¥5,600, 7,400 ¥11,800, plus limited packs.
- **マネー (Money), soft [Explicit].** Earned from matches and the Official Store. Used for training, skill training, instant finish, facilities and coaches. The renewal notes say Money also had paid and free portions: 「有償・無償マネー」 (https://nbarise.com/vkdios/).
- **ツアーパス (Tour Pass), monthly subscription [Explicit].** Named 「選手強化(特別)月間」 and 「スペシャル強化(特別)月間」; they gave 1.5x EXP and a Money bonus (https://nbarise.com/ayghjk/, https://nbarise.com/irfhjg/).
- **マイル (Miles) [Explicit].** Existed in TO STARDOM and was deleted at the renewal. **Function not documented** (https://nbarise.com/vkdios/).
- **Stamina/energy.** None for Season in TO STARDOM. **[Inferred]** No AP (action-point) system is mentioned until the renewal test.
- **Sales freeze [Explicit].** Gold and Tour Pass sales stopped on Apr 18, 2023, during development of the renewal (https://nbarise.com/mxuwjw/).

---

## 3. NBA RISE (renewal: service from Feb 20, 2025; ended Aug 31, 2026 17:00)

### 3.1 What changed from TO STARDOM

- **Timeline [Explicit].**
  - Feb 28, 2023: 「ゲーム全体の大型リニューアルが決定」 (full-game major renewal decided). New events stopped (https://nbarise.com/gupqoq/).
  - Test of the match part only (Jul 10–18, 2023), using All-Star 2023 Team Giannis vs Team LeBron (https://nbarise.com/vjuaka/).
  - 2nd test (Jan 15–25, 2024): the name 『NBA RISE』 was decided and 「行動力」 (action points) introduced (https://nbarise.com/mgvjuf/).
  - 3rd test (Nov 26 – Dec 3, 2024).
  - Long maintenance from Sep 30, 2024 (https://nbarise.com/kcodks/).
  - Relaunch Feb 20, 2025 14:00 as an update to the same app (https://nbarise.com/idksal/).
- **[Explicit] Official summary.**
  - 「試合やシーズン、イベント、選手パラメーター等様々な点が一新」 (matches, season, events, player parameters and more renewed) (https://nbarise.com/idksal/).
  - 「より直感的な操作、よりスピーディーな試合展開、快適なプレイ体験」 (more intuitive controls, faster matches, a more comfortable experience) (press 2025-02-18/20).
  - Score Ranking 「ルールや報酬などがリニューアル」 (rules and rewards renewed).
  - Legends get 「新たなビジュアル」 (new visuals).
  - The press tagline added 「ゲームが苦手な方でも」 (even for people who aren't good at games).
- **[Explicit] Data migration** (https://nbarise.com/vkdios/):

  | Fate | What |
  |---|---|
  | **Kept** | Players' levels, skill levels and rarity; 拠点グレード (base grade); 施設レベル (facility levels); fans; paid and free Gold; storage; 選手名鑑 (player encyclopedia); team formations; マイチーム |
  | **Changed** | Paid and free Money merged into one マネー. 「所持選手・HCカード…ステータスやスキル等が調整」 (owned player and HC cards kept, but stats and skills re-tuned). TP: 「名称や計算式の改修」 (renamed, new formula). The プレゼント box renamed 受信箱 (Inbox) |
  | **Deleted / reset** | Offer tickets and vouchers; マイル; Tour Pass effects; follow feature; trade listings; running skill trainings; season, mission and ranking progress |

### 3.2 Match engine: auto-sim plus セットプレイ (Set Play)

- **[Explicit] Core statement.** 「試合は基本的にオートで進行します。重要な局面では、プレイヤーが選手の行動を選択できるセットプレイを発動することもできます。1ポゼッションをプレイし、成功すればテンションアップ！テンションが高まるほど、試合を優位に進められるようになります。」
  - Translation: "Games basically run on auto. At key moments you can trigger a Set Play in which you choose players' actions. Play one possession; succeed and Tension rises. The higher the Tension, the more you control the game."
  - Source: PR TIMES 2025-02-20, https://prtimes.jp/main/html/rd/p/000000391.000071574.html; press PDF 2025-02-18.
- **[Screenshot] Simulation screen (シミュレーション):**
  - a **2D top-down court** with position tokens (PG/SG/SF/PF/C) and both starting fives as cards;
  - quarter and game clock (e.g. 1Q 10:10);
  - each team's active tactic with a level, e.g. 「アイソレーション LV3」 (Isolation Lv3);
  - a tug-of-war bar with team values (1136 vs 1164);
  - comic-style "Slam!"/"Jam!" effects and "2PTシュート" tags on cards;
  - an **AUTO ON/OFF** toggle, a **「1Qスキップ」** (skip quarter) button, and a central button with a segmented gauge. **[Inferred]** That button triggers the set play.
- **[Screenshot] Set-play screen (セットプレイ):**
  - 3D-rendered players (e.g. Curry vs Conley) and a shot clock (24);
  - prompt **「SELECT ACTION！ 残り4回」** ("select action, 4 left");
  - choices **シュート (with "3Point" label) / パス / ドライブ** and a timer;
  - the card row shows a **「KEY PLAYER」** badge and a 「パス」 arrow from Curry to Marcus Smart;
  - Auto and Speed (X1) toggles.
  - **[Inferred]** A set play is a chain of up to N decisions in one possession: pass the ball around, then finish with shoot or drive.
  - Corroborated by a user comment on the Gamerch wiki quoting an event mission: 「セットプレイで4回ボールをつかみゴールを決める」 ("handle the ball 4 times in a set play and score") (https://gamerch.com/nba-rise/905568).
  - The Gamerch top page also has user notes: key players are set via a 「KEYPLAYER」 button on the pre-match screen, and one mission is triggered by passing 3 times then shooting (https://gamerch.com/nba-rise/). These are user comments, not official.
- **[Explicit] Defensive set plays exist.** Skills reference 「オフェンスセットプレイ時」 / 「ディフェンスセットプレイ時」 and 「オフェンスセットプレイのコマンド選択時」 (at offensive/defensive set play; at offensive set-play command selection) (scout notices, e.g. https://nbarise.com/koayzu/).
- **[Explicit] スーパープレイ (Super Play).** The EPIC/LEGEND signature skill: 「オフェンスセットプレイ時、自身のシュートが+45され、スーパープレイが発動可能になる 発動後、スタミナを-125消費する（必要なスタミナがセットプレイ時に無い場合発動しない）」 ("on offensive set play, own Shoot +45 and Super Play becomes available; then −125 stamina; won't fire without enough stamina") (https://nbarise.com/apskfg/).
  - Event missions such as 「スーパープレイを〇回発生させる」 (trigger N super plays) award Gold (press PDF 2025-04-24).
  - Hachimura's card skill 「Rising Fuji」 plays like a real highlight (ASCII 2025-08-12).
- **Not confirmed:** whether the RPS action matchups from TO STARDOM survived, and match length or quarter count. Screens still show quarters (1Q) and a game clock.

### 3.3 テンション (Tension) and テンションリンク (Tension Link)

- **[Explicit]** Tension replaces Momentum as the swing meter. Skills now read 「テンションが勝っている/負けている」 (Tension ahead / behind) where TO STARDOM used Momentum. The same **リード / リバーサル** keywords carry over.
- **[Screenshot] Team formation screen:**
  - **「スタート時テンション」** (starting Tension, e.g. 1110);
  - a **「テンションリンク」** (Tension Link) button;
  - **「チームオフェンス」 / 「チームディフェンス」** totals (1609/1611 with +260/+190 bonuses);
  - **「作戦：フリーオフェンス ALL」** selector (tactic "Free Offense");
  - substitution UI with 「得意ポジション」 (favoured position) labels;
  - card inventory "264/1000".
- **[Explicit] Named Tension Links** from a bug notice: 「オフェンススターター」「ディフェンススターター」「スタミナスターター」「オフェンスプラン」「ディフェンスプラン」「スタミナプラン」 (Offense/Defense/Stamina Starter; Offense/Defense/Stamina Plan). The bug was that they 「条件を満たしてもアクティブにならない」 ("don't activate even when conditions are met") (https://nbarise.com/nghufs/, fixed https://nbarise.com/ploaio/).
  - **[Inferred]** Tension Links are condition-based team synergy bonuses that raise starting Tension.
  - **Exact conditions not found.** No source documents same-team or same-era chemistry.
- **[Explicit] Skill families tied to Tension:**
  - 「テンション割合アップ10％」 (Tension rate +10%);
  - リバーサルスコア (fires when you retake the lead in score);
  - パッシブカウンター (fires when the opponent's passive skill fires);
  - スタミナフォロー;
  - シール (seals the matchup opponent's block, steal or pass-cut).

### 3.4 Tactics (作戦) and head coach in NBA RISE

- **[Screenshot]** Tactics are named and levelled: 「アイソレーション LV3」 (Isolation), 「フリーオフェンス ALL」 (Free Offense, applying to ALL positions).
- **[Explicit, wiki]** Players have a 「得意な作戦」 (favoured tactic), e.g. Lillard 「シュータープレイ」 (shooter play), Durant and Banchero 「アイソレーション」 (isolation), SGA 「プレスディフェンス」 (press defense) (https://gamerch.com/nba-rise/905565).
  - **[Inferred]** A tactic links to the coach or players and has its own level.
  - **Mechanism not documented.**
- **[Screenshot]** A head-coach card (e.g. Taylor Jenkins) sits at the top of formation and Score Ranking screens. HC cards migrated (https://nbarise.com/vkdios/). **No documentation** of HC parameters or how coaches are obtained in NBA RISE.

### 3.5 Player cards in NBA RISE

- **Rarity.** C / UC / R / UR / EPIC / LEGEND. SECRET was replaced by **「Signed Collection」** variants. Example: 「SIGNED COLLECTION」として、名実ともに最高峰のスターに相応しい、気品溢れるデザイン ("as a Signed Collection card, with an elegant design fit for a top star") (https://nbarise.com/lkawqi/).
- **Editions.** Every card carries an edition tag, e.g. (THE GENIUS), (NBA ALLSTAR2024), (2025 Playoff Edition West), (22-23 ALL-NBA 1st TEAM), (Campaign Edition). The same-name restriction still applies.
- **Stats [Explicit].** Re-scaled to triple digits: シュート / パス / ドライブ / ブロック / パスカット / スタミナ… Example: [EPIC] Jokić Lv70: シュート261 パス231 ドライブ229 ブロック219 パスカット206 スティール231 スタミナ1566 (https://nbarise.com/koayzu/).
  - Posts quote UR cards at Lv60 and EPIC/LEGEND at Lv70, skills at Lv5. **[Inferred]** Those are the max levels.
  - Cards come from scouts at Lv1.
- **Positions [Explicit].** Main and sub, e.g. 「[メインSF / サブPF]」. 「得意ポジション」 is shown in the UI.
- **Skills [Explicit].** Three per card:
  - Skills 1–2: conditional passives (イニシャル = always on while on court; リード; リバーサル; etc.), targeting self, a position (e.g. 仲間PF) or ALL.
  - Skill 3 on EPIC/LEGEND: a named Super Play (e.g. 「Tatum Sky」, 「Dame Rain」, 「SHOW TIME OFFENSE」).
  - Skill 3 on UR (and Payton's 「The Glove」): a quarter-long buff 「発動したクォーターの終了まで…（発動可能な各Qにつき1回まで使用可能）」 (lasts until the end of the quarter it fires in; usable once per eligible quarter).
- **Balance patch example** (https://nbarise.com/vnjfdk/): EPIC Dončić (THE GENIUS) went from シュート174 to 236 and スタミナ1151 to 1399.

### 3.6 Scouting (スカウト, the renamed gacha) and other acquisition

- **Scout types [Explicit]:**
  - **NBA ALL TEAM SCOUT:** standard, ticket-based (「NBA ALL TEAM SCOUTチケット」).
  - **EVENT SCOUT:** players with **イベントブースト** (event boost), 「獲得ポイントブーストやスコアブースト」 (point and score boosts), in the matching event.
  - **期間限定スカウト (limited-time):** usually the first week of each month, LEGEND/Signed Collection pickups, e.g. LinSanity (https://nbarise.com/sloase/), RISING SCOUT (https://nbarise.com/uyjuig/).
  - **リリース記念EPIC確定スカウト / EPIC確定スカウト:** paid Gold only, once, ≥1 EPIC guaranteed (https://nbarise.com/eifugj/, https://nbarise.com/spldmd/).
  - **START DASH SCOUT:** first 72 hours after starting; paid Gold; 5 purchases of 2 packs each; after 5 purchases an EPIC-guaranteed scout unlocks (https://nbarise.com/juikms/). **[Inferred]** This is the only pity-like mechanic found.
- **Rates.** 「1%の確率で登場する選手カードが、100回のスカウトで必ず登場するということではございません」 ("a 1% card is not guaranteed in 100 scouts"); rates truncated to 3 decimals.
  - Gamerch lists one scout's rates as EPIC 1.50%, ULTRA RARE 10%, RARE 20%, UNCOMMON 30%, COMMON 38.5% (https://gamerch.com/nba-rise/905565). Which scout this is is not stated; **[Inferred]** the standard one.
  - A Gamerch user notes event scouts are Gold-only while the standard scout accepts tickets.
- **Reroll** (Gamerch): skip account link, then use 「ユーザーデータ削除」 (delete user data) from the title menu.
- **Exchanges [Explicit]:**
  - **スコアランキング交換所** (Score Ranking exchange), paid in **スコアメダル** (Score Medals), e.g. [EPIC] Tatum and [LEGEND] Iverson at 3,000 each (https://nbarise.com/scokfw/);
  - per-event **イベント交換所** (event exchange) using event Pt or event tokens.
- **Login bonuses** for ambassador cards (EPIC Kawamura, EPIC Hachimura).
- **トレード persisted.** Trade is in the bottom nav [Screenshot], and a Sept 2025 bug notice mentions returning 「トレードに使われた選手」 (players used in trades) (https://nbarise.com/bnhggf/). **Details of NBA RISE trading are not documented.**

### 3.7 Growth items in NBA RISE

- **[Explicit] Item names** from rewards: 「レアリティアップカード」 (C/UR rarity-up cards), 「スキルトレーニングカード」 (C/R/UR skill-training cards), 「EPIC 特別トレーニングカード」 (EPIC special training card), 「UR/EPIC エージェントカード」 (UR/EPIC agent cards).
  - **[Inferred]** They substitute for duplicate copies in Rarity Up and Skill Training.
  - **The Agent Card's function is not documented anywhere I found.**
- **[Explicit]** Money-based level training remains: 「河村勇輝のレベルを70にする」 mission ("raise Kawamura to Lv70", https://nbarise.com/msikai/); training bug fix (https://nbarise.com/ncjdks/).
- **[Screenshot]** The home screen keeps 拠点 (base) and 選手名鑑 (player encyclopedia) buttons.

### 3.8 Modes in NBA RISE

- **シーズン (Season).** 「おなじみの｢シーズン｣モードが遊びやすく進化！簡単プレイでNBAチャンピオンを目指せ！」 ("the familiar Season mode, now easier to play; aim for the NBA title with simple play") (App Store / Google Play).
  - Costs **行動力 (Action Points)**: 「シーズンをプレイするごとに消費…一定値を下回ると回復するまでシーズンが行えなくなります。回復方法としては自然回復のほか、ゴールドや行動力回復アイテム」 ("consumed each time you play Season; below a threshold you can't play until it recovers; recovers naturally or with Gold / AP-recovery items") (https://nbarise.com/mgvjuf/).
  - **[Screenshot]** AP cap 100; 「オート進行 結果確認」 (auto-progress result screen) sims a month of calendar games with scores; 「PICKUP GAME」 days; fans earned per month; a team rating shown as a number plus a letter grade (チーム総合力 13424, "D"; 23397, "A").
  - Balance-patched Mar 19, 2025.
- **スコアランキング (Score Ranking).** 「他プレイヤーのチームと戦える｢スコアランキング｣モードがルール含めニューオープン」 (Score Ranking, where you fight other players' teams, reopened with new rules) (store).
  - **[Screenshot]** 「10部リーグ 3位 昇格圏内」 (Division 10, 3rd place, promotion zone); 「残り参加回数 4/5」 (entries left 4/5, refilling on a timer); buttons ランキング (ranking) / 使用率トップ (most-used players) / 報酬一覧 (rewards) / 交換所 (exchange); "現在のスコア累計" (score total).
  - Cycle example: ends 2025-02-11, during the pre-launch test.
- **Events (all [Explicit]).** Event AP 「イベント行動力」; recovery packs were sold Apr–Dec 2025 (https://nbarise.com/mskixf/, https://nbarise.com/dfopsd/).
  - **VSイベント (Versus):** beat two themed teams; collect イベントPt and イベントトークン; exchange; 「ハイスコアランキング」 (best single-game score) and 「累計Ptランキング」 (cumulative points) (https://nbarise.com/fpaolw/).
  - **ヒストリーイベント (History):** 「対象の選手に関連するイベント試合に挑み、ポイントを集めて選手を育成…一定のポイントを集めると選手のレアリティが上昇していき、イベント終了時点で到達したレアリティの選手を獲得」 ("play matches tied to the featured player and collect points to raise them; their rarity rises at point thresholds, and you receive the player at the rarity reached when the event ends"). Only one featured player can be raised at a time (https://nbarise.com/byhydz/, https://nbarise.com/sdisoa/).
  - **タワーイベント (Tower):** 「各階に待ち受ける相手チームに挑み、勝利することで報酬を獲得」 ("climb floors by beating the team on each floor"). Players at set floors (e.g. 20F/40F…/120F); **到達ランキング** (height-reached ranking); no exchange (https://nbarise.com/mkodsd/, https://nbarise.com/vnhdio/).
- **Missions.** Daily, 期間限定 (limited-time), and ambassador missions. Inbox (受信箱) overflow happens when over the inventory cap (https://nbarise.com/mjklgf/).
- **Real-time Player Match: not confirmed after the renewal.** It is absent from all NBA RISE-era notices and store text.

### 3.9 Monetization and shutdown

- **[Explicit] Gold packs.** 2,400/3,600/6,000 Gold packs changed from 「初回限定」 (first-purchase only) to 「毎月1回限定」 (once per month) in May 2025 (https://nbarise.com/rtfglk/).
- **[Explicit] Shutdown.** Gold sales ended Jul 30, 2026 15:00; service ended Aug 31, 2026 17:00. Reason given: 「現在の開発・運営体制を考慮…ご満足いただけるサービスの提供が困難」 ("considering the current development and operations setup, providing a satisfying service is difficult") (https://nbarise.com/reinsde/).
- **[Explicit] Refunds.** Unused paid Gold refunded at **1 Gold = 2円** (2 yen) via CASH POST. Applications Aug 31 – Nov 16, 2026 (https://nbarise.com/ypgreqa/).

---

## 4. Collaborations, ambassadors, seasonal content

- **Yuta Watanabe**, official ambassador from Nov 10, 2021 (https://nbarise.com/ywhsa/).
  - Launch gift [SECRET] Watanabe; tutorial guide.
  - History event 「EARNED,NOT GIVEN 渡邊雄太物語」 (https://nbarise.com/ywmbk/) and 「Yuta The Shooter」 (2023).
  - Watanabe × Yuta Tabuse talk show login bonus with [LEGEND] 田臥勇太 (https://nbarise.com/cesaqw/).
- **Yuki Kawamura**, ambassador from Jul 10, 2025 (PR TIMES 000000423). EPIC 河村勇輝 (2023-24 Edition) via login bonus (https://nbarise.com/yhdrjk/) and the GRIZZLIES FESTIVAL event.
- **Rui Hachimura**, ambassador from Aug 12, 2025 (ASCII 4312277). EPIC 八村塁 (Campaign Edition) login card with skill 「Rising Fuji」 (https://nbarise.com/bnjgkf/); 「HISTORY OF HACHIMURA」 event; signed-goods campaigns.
- **Media tie-ins:**
  - Dunk Shoot magazine strategy column for a year from Nov 2021 (4Gamer 20211020097);
  - YouTube shows with Cocorico Tanaka, Chris Sasaki and Ami Tokito;
  - NBA Rakuten × NBA RISE special (https://nbarise.com/mvodas/);
  - NBA viewing event 「RISE TO NIGHT 2022」;
  - in-game 「NBA JAPAN GAMES 2019」 and 「NBA in JAPAN 2022」 events.
- **Real-season content.** Events and offers were themed on the real NBA calendar: Christmas games, All-Star, playoffs/finals (e.g. a 2022 champions Warriors offer with Curry's FMVP SECRET in a special photo), the 75th anniversary, In-Season Tournament, Playoffs and Finals 2025, Hall of Fame classes.

---

## 5. Not confirmed / gaps

- Salary cap, contracts, payroll, draft (only "planned"), free agency, team chemistry by same team or era: **no evidence**. Tension Link conditions are unpublished.
- HC parameter list, HC acquisition in NBA RISE, the TEAM command in TO STARDOM clutch, exact set-play rules (number of actions, defensive set-play inputs, how success is judged), and how match tactics level up.
- Facility list beyond 4 named ones (of 9), function of マイル and of エージェントカード, pity on offers (none found beyond START DASH), the NBA RISE trade rules, guilds or clubs (none found), real-time PvP after the renewal (none found).

---

## 6. Sources

**Official site** (https://nbarise.com/, `nbarise.com/<slug>/`):
- Guides and launch: lknfhd, tyujdk, sydja, yteahlk, ygspo, ywhsa
- Offers and cards: ygdplc, oknhgf, yjduq, iijsda, pervbho, vapreijk, ylmvsde, yoiqk, bytrnc, zlxkgo, fdokix, cmgtok, elkaxc, nhufdi, gfydus, ygso, wvmkoit, tsxwer
- Trade: yrlqoa, kjf8fd, ybpas
- Updates and maintenance: yjhnds, yega, pkgjfh, y2etsa, ayghjk, irfhjg, bkaole
- Modes and missions: yjghw, dufnrj, rilims, pmlqcb, vjdska, yjewry, vpoelc, sapzzr, ygfha
- Events (TO STARDOM): idcvg1m, rjkd9ujf, jmnerg, wxofhgi, soliun, yghtau, ycvsgh, lwsdrfg, fjslad, vunhuf, fkdols, ywmbk, cesaqw, mvodas
- Campaigns: yhgq, ytflkj, upedfrty, yvbc
- Renewal: gupqoq, mxuwjw, vjuaka, mgvjuf, kcodks, idksal, vkdios, qalzkd
- NBA RISE scouts: eifugj, juikms, koayzu, lkawqi, mjvifo, sloase, mjvwql, xpoqsi, gftydu, apskfg, uyjuig, spldmd
- NBA RISE events and items: scokfw, fpaolw, insals, byhydz, sdisoa, mkodsd, vnhdio, wofhyv, mskixf, dfopsd, rtfglk, vnjfdk
- NBA RISE bugs and missions: nghufs, ploaio, mjklgf, bnhggf, msikai, ncjdks, yhdrjk, bnjgkf
- Shutdown: reinsde, ypgreqa
- Also: nbarise.com/faq/ and wp-sitemap.xml

**Press materials:**
- Gravity Game Arise PDFs: https://gravityga.jp/wp-content/uploads/2024/11/press-release_20241126_nba.pdf, …/2025/02/press-release_20250218.pdf, …/2025/03/press-release_20250327.pdf, …/2025/04/press-release_20250424.pdf, …/2025/05/press-release_20250522.pdf, …/2025/10/press-release_20251021.pdf (text plus screenshots)
- PR TIMES: https://prtimes.jp/main/html/rd/p/000000041.000071574.html, 000000279, 000000391, 000000423, 000000429, 000000447 (feed: https://prtimes.jp/companyrdf.php?company_id=71574)

**Media:**
- https://gamebiz.jp/news/337867, https://gamebiz.jp/news/333960, /401032, /396511, /380432
- https://game.watch.impress.co.jp/docs/kikaku/1367576.html (text and screenshots)
- https://news.denfaminicogamer.jp/kikakuthetower/211125b, https://news.denfaminicogamer.jp/news/211126f
- https://www.oricon.co.jp/special/57709/ (Shift_JIS; decoded cleanly)
- https://ascii.jp/elem/000/004/252/4252827/, /259/4259730/, /293/4293399/, /312/4312277/
- https://dengekionline.com/article/202608/83074
- https://kamigame.jp/game/70392/
- https://www.bluestacks.com/ja/blog/app-reviews/nba-rise-to-stardom-review-ja.html
- https://app-liv.jp/5342528/ (low reliability)
- 4Gamer index: https://www.4gamer.net/games/553/G055361/index_news.html, plus 20211102062, 20211020097, 20250218036

**Wiki and stores:**
- Gamerch: https://gamerch.com/nba-rise/, /905565, /905568
- App Store JP: https://apps.apple.com/jp/app/id1574474570
- Google Play: com.gravityga.nbarisetostardom

**Files from this session:**
- Official news full text: `(session scratchpad, not preserved)/site/all.txt`
- Post index: `(session scratchpad, not preserved)/site/index.tsv`
- One text file per post: `(session scratchpad, not preserved)/site/txt/`
- Screenshots: `(session scratchpad, not preserved)/impress/` and `(session scratchpad, not preserved)/pdfs/img0218/`
