<!-- Research report compiled 2026-11-08. Source links inside; working-file paths refer to a temporary session folder that was not preserved (the official pack data is preserved in ../data/). -->

## NBA RISE (Gravity): history, corporate, licensing, regions, platforms and finance

**How the claims are marked:**
- **[P]**: confirmed by a primary source (Gravity or GGA press release, SEC filing, Gravity IR deck, the official game site, or live store and API data that I pulled on 2026-11-08).
- **[S]**: reported by secondary press only.
- **[U]**: unresolved.
- **[I]**: my own inference from the evidence.

Everything I downloaded is in the scratchpad: `(session scratchpad, not preserved)/` (subfolders `pdfs/`, `sec/`, `irpdf/`, `web/`).

### Key corrections to what was "already known"
1. **Nov 18 vs Nov 24, 2021 is resolved. The official Japan launch was Nov 24, 2021.**
   - GGA had announced Nov 18 on 2021-11-02. On 2021-11-15 it postponed to Nov 24 "for further service improvement" [P].
   - On 2021-11-18 the iOS build became downloadable early, at 00:00 JST, because the App Store release date was set wrongly. GGA apologised the same day on PR TIMES [P].
   - Apple's API still shows the JP app's `releaseDate` as 2021-11-18, which is why Dengeki Online uses Nov 18.
2. **The Japanese title did not run continuously.**
   - 2023-02-28: GGA announced a full renewal and paused new event updates [P].
   - 2024-09-30 14:00 JST: the game went into "long-term maintenance", meaning service was suspended [P].
   - 2025-02-20: service came back as "NBA RISE". The shutdown notice itself calls that date the point where service "was resumed" (サービスが再開された) [P].
3. **The 8-region launch date is 2026-10-20 at 14:00 KST** [S for the time; P for the date via the App Store `releaseDate` of 2026-10-20]. The global CBT ran from about July 21–22 to July 29, 2026 [S].
4. **No region expansion has been found beyond the 8 launch regions.** As of 2026-11-08 I found nothing for North America, Europe, Japan, Taiwan, Vietnam, Brazil or any "global" rollout. Google Play shows an Install button only in KR, PH, ID, TH, MY, SG, AU and NZ, and the iTunes lookup returns no app for the US, JP, GB, CA or TW storefronts [P].

---

### 1. Dated timeline

| Date | Event | Status | Source |
|---|---|---|---|
| May 2020 | Gravity signs an agreement with the NBA and NBPA "to obtain the right to develop and publish an NBA licensed game". | P | 20-F FY2020–FY2025 |
| as of 2020-12-31 | Gravity still owed "remaining license fees and guaranteed minimum royalties in installments based on the progress of the development of the games". | P | 20-F FY2020 |
| 2021-02-15 | NBA press release "NBA, NBPA and Gravity bring new mobile gaming experience to fans in Asia-Pacific": a free-to-play strategy deck-building card battler with active and retired stars, launching first in Japan via GGA and then across Asia-Pacific. Quotes from Yoshikazu Kanzaki (GGA Executive Producer) and Lesley Rulloda (NBA Asia). | P | pr.nba.com |
| 2021-02-16 | Gravity 6-K (Q4 2020): "NBA Project – Gravity has completed the Product License Agreement with the NBA and NBPA… published by Gravity Game Arise in Japan, and Gravity will expand its service to other markets in the contract regions in order." | P | SEC 6-K |
| 2021-02-17 | GGA names itself Japan publisher of "NBA RISE TO STARDOM (仮)". GGA handles "ゲーム企画・開発、日本国内におけるパブリッシング及びマーケティング" (game planning/development, Japan publishing and marketing). Plans to "use the GRAVITY group global network… to deliver to overseas fans in sequence". | P | GGA PR PDF |
| 2021-08-13 | Second PV released. Gravity 6-K: CBT planned for Sept 2021, Japan launch in Q4 2021. | P | GGA PR; 6-K |
| 2021-09-28 | Japan pre-registration opens (App Store pre-order; Google Play `com.gravityga.nbarisetostardom`) together with a public test (一般体験会). The Gravity IR deck calls it an "OBT in Japan from September 28th to October 5th". | P | GGA PR; IR Q3 2021 |
| 2021-11-01 | 50,000 pre-registrations. | P | GGA PR |
| 2021-11-10 | Yuta Watanabe named ambassador. | P | GGA PR |
| 2021-11-12 | Gravity 6-K: "expected to be launched in Japan in November, 2021 and in Korea in the first half of 2022" (the Korea launch did not happen). | P | 6-K |
| 2021-11-15 | Launch postponed from Nov 18 to Nov 24. | P | GGA PR |
| 2021-11-18 | Early iOS download caused by the release-date setting error. | P | PR TIMES |
| **2021-11-24** | **"NBA RISE TO STARDOM" officially launches in Japan** (iOS and Android, free-to-play). GlobeNewswire release the same day. | P | GGA PR; GlobeNewswire via Yahoo |
| 2021-11-26 | #1 in the Sports category on the JP App Store and Google Play (company claim). | P | GGA PR |
| 2021-12-01 | 200,000 downloads (company claim). | P | GGA PR |
| 2022-02-14 | IR deck: "Additional Launching 2H 2022 – Korea". | P | IR deck |
| 2022-03-31 | Major update. | P | GGA PR |
| 2022-05-24 | Half-anniversary; special programme co-produced with NBA Rakuten. | P | GGA PR |
| 2022-05 / 08 / 11 | IR decks: Korea launch now "TBD". | P | IR decks |
| 2022-10-28 | "RISE TO NIGHT 2022" NBA viewing event in Ginza. | P | GGA PR |
| 2022-11-24 | First anniversary. | P | GGA PR |
| 2023-02-14 | IR deck: "Additional Launching TBD – Southeast Asia, Korea". | P | IR deck |
| 2023-02-28 | Notice "【重要】大型リニューアル及び、更新の一時停止" (major renewal and temporary halt of updates): full-game renewal decided, new events paused, some products pulled; owned players and currency to carry over. | P | nbarise.com |
| 2023-05 / 08 / 11 | IR decks: "NBA RISE TO STARDOM – Additional Launching – TBD – Southeast Asia, Korea, Australia, New Zealand". This is the same footprint as the 2026 launch. | P | IR decks |
| 2023-07-10 → 07-18 | First 先行体験会 (preview test), covering matches only (All-Star 2023 Team Giannis vs Team LeBron). Separate test app `com.gravityga.nbarisetest` / TestFlight "NBA RISE TEST". | P | nbarise.com |
| 2024-01-15 → 01-25 | Second 先行体験会. "リニューアル後の正式名が『NBA RISE』に決定" (official post-renewal name set as NBA RISE). | P | nbarise.com; gamebiz |
| 2024-02-14 | IR deck (image-only, read visually): "NBA RISE TO STARDOM – Additional Launching – 2024 – Japan". | P | IR deck |
| 2024-05 / 2024-08 | IR decks: "NBA RISE – Renewal Launching – TBD", then "2H 2024 – Japan". | P | IR decks |
| 2024-08-30 | Long-term maintenance announced; data will carry over to the renewal. | P | nbarise.com |
| 2024-09-30 14:00 | Long-term maintenance starts, end date undetermined. | P | nbarise.com |
| 2024-11-26 → 12-03 | Third 先行体験会. | P | GGA PR; gamebiz |
| 2025-02-14 | IR deck: "NBA RISE is scheduled to be renewal launched in Japan in February, 2025". | P | IR deck |
| 2025-02-18 | Service start date announced. | P | GGA PR; gamebiz |
| **2025-02-20** | **Renewal "NBA RISE" goes live in Japan.** Delivered as a major update to the same app; Facebook login dropped. The FY2025 20-F lists "NBA Rise, Sports, Japan, February 2025". | P | GGA PR; 20-F |
| 2025 (month not stated) | "the agreement [with NBA/NBPA] was extended and additional license fees were committed". | P (month U) | 20-F FY2025 |
| 2025-06-19 / 07-10 | Yuki Kawamura login bonus starts (June 19); he is announced as ambassador on July 10. | P | nbarise.com; GGA PR |
| 2025-08-12 | Rui Hachimura named ambassador. | S (ASCII/PR TIMES); P that he held the role (GGA PR 2025-09-04, "八村 塁アンバサダー就任記念") | |
| 2025-12-19 | Notice that event-item shop sales will end at the Dec 23 maintenance. | P | nbarise.com |
| 2025-12-23 → 2026-01-13 | Last themed event ("DREAM TEAM vs WORLD STARS"). | P | GGA PR |
| 2026-01-01 | Last scout notice ("RISING SCOUT", no new players). After this the JP news feed is only maintenance and bug notices. | P | nbarise.com |
| 2026-04-30 | JP version 2.0.13 and a new app icon. | P | nbarise.com |
| ~2026-07-21/22 → 07-29 16:00 KST | Global CBT: Android only via Google Play, "8 regions incl. KR, PH, ID, TH, MY, SG". Survey July 24–30. | S | Inven Global; BizWatch |
| 2026-07-30 15:00 / 15:30 JST | Japan stops selling gold, then posts the shutdown notice. | P | nbarise.com |
| 2026-08-07 | Gravity Q2 2026 results and IR deck: no mention of NBA RISE. | P | 6-K; IR deck |
| **2026-08-31 17:00 JST** | **Japan service ends** (final version 2.0.14). | P | nbarise.com |
| 2026-08-31 → 2026-11-16 12:00 | Refund window for unused paid gold under Payment Services Act Art. 20(1). 1 paid gold = ¥2; payouts via CASH POST from mid-Dec 2026 to Jan 2027. | P | nbarise.com |
| **2026-10-20 14:00 KST** | **Global "NBA RISE" launches** in KR, PH, ID, TH, MY, SG, AU and NZ on Google Play and the App Store. | P (date via App Store API) / S (time) | Inven; KH Games; DDaily |
| 2026-10-28 / 11-05 | Google Play listing last updated Oct 28; iOS reaches v1.1.1 on Nov 5. | P | store data |
| as of 2026-11-08 | Q3 2026 results not yet filed. The latest Gravity 6-K on EDGAR is dated 2026-08-07. | P | EDGAR |

**Korean name.** Korean press uses both "NBA Rise" and "NBA 라이즈". The Korean App Store title is "NBA RISE: 농구 카드 전략" ("Basketball Card Strategy"). I found no separate Korean-only title [P/S].

### 2. How the global NBA RISE (2026) relates to the Japanese NBA RISE TO STARDOM / NBA RISE (2021–2026)

**Same license and franchise, different product release. Whether it is the same code base is [U].**

**Separate app and separate operator** [P]:

| | Japan | Global |
|---|---|---|
| Android package | `com.gravityga.nbarisetostardom` | `com.gravity.nbarisegv.aos` |
| iOS | id1574474570, bundle `com.gravityga.nbarisetostardomi` | id6762187862, bundle `com.gravity.nbarisegv.ios` |
| Publisher | GRAVITY GAME ARISE | GRAVITY Co., Ltd. (Korea) |
| Website | nbarise.com | nbarise.gnjoy.com |
| Logo and copyright | own logo, © GRAVITY GAME ARISE | different logo, © Gravity Co., LTD |

No account or data migration from Japan was announced.

**Developer attribution** [S]: Korean press consistently says Gravity developed the global game in-house ("그라비티가…라이선스를 확보해 자체 개발", i.e. Gravity secured the license and developed it in-house). By contrast, GGA's Japanese releases called their game "日本国内開発、日本人に向けた" (developed in Japan, for Japanese users) and "日本が企画・開発するゲームとしては唯一のNBA公式タイトル" (the only official NBA title planned and developed in Japan) [P].

**Shared design DNA** [P store and press text; I]: both versions use auto-simulated matches with player-triggered set plays and "super plays", scouting, card training and upgrades, a Season mode, and tower events (Japan added these in July 2025; global has "Tower Race"). The global version adds PvP Arena, Club (a guild with chat), RvR Club Conquest, a trading Market, a Season Pass and "3D player models". Genre labels differ: Japan called it an "オンラインシミュレーションゲーム" (online simulation game); global is marketed as a "strategy card game".

**The regional plan dates back years** [P]: from May to Nov 2023, Gravity's IR decks listed "NBA RISE TO STARDOM – Additional Launching – Southeast Asia, Korea, Australia, New Zealand". That is exactly the 2026 eight-region set.

**Sequence** [P; reason for the link is I]:
- 2025: Gravity extended the NBA/NBPA license.
- January 2026: Japanese live-ops effectively stopped.
- July 2026: the global CBT ran.
- 2026-07-30, about a week later: Japan announced its shutdown, citing "現在の開発・運営体制を考慮したうえで…今後お客様にご満足いただけるサービスの提供が困難" (given the current development and operations setup, it would be hard to keep providing a satisfying service).

**Conclusion [I]:** the global NBA RISE is the long-planned APAC expansion of the NBA RISE franchise under the same Gravity NBA/NBPA agreement. It was re-released and operated by Gravity HQ as a new app with new branding. No primary source says whether it is a port or localisation of GGA's 2025 renewal client or a fresh build.

### 3. Developer and entity facts
- **Global version.**
  - Provider: GRAVITY Co., Ltd., 15F Nuritkum Square R&D Tower, 396 World Cup buk-ro, Mapo-gu, Seoul [P, store listing].
  - Listing names CEOs Park Hyun-chul and Kitamura Yoshinori; customer service +82-2-1588-9897 [P].
  - Spokesperson is Noh Geon-seok (노건석), Global Mobile Business Team Lead [S]. He also fronted Gravity's Hero's Gambit card-game CBT in Dec 2024 [S].
  - Privacy and terms pages are hosted on terms.withhive.com and support on customer.withhive.com/gravity [P]. That suggests Com2uS's Hive backend platform, but no partnership is confirmed [U].
- **Japanese version.** Gravity Game Arise Co., Ltd., a wholly owned Japanese subsidiary founded 2019-07-01 [P].
  - Staff: 60 in 2025, 55 in 2024, 47 in 2023 [P, 20-F].
  - Revenue ₩14,995M with a net loss of ₩2,513M in 2025; revenue ₩5,574M with a net loss of ₩6,237M in 2024 [P, 20-F]. These figures cover all GGA titles, not only NBA RISE.
  - The 2026 refund notice gives GGA's address as Marunouchi 1-11-1, Chiyoda, Tokyo. The 20-F gives Hacchobori [P].
- **Gravity Game Hub (Singapore):** I found no role for it in NBA RISE [U].
- **Engine and team size:** not found [U].

### 4. Licensing
- **Licensors:** NBA (NBA Properties) and the NBPA. Every Gravity/GGA copyright line names only these two [P].
- **Original agreement:** May 2020, covering "the right to develop and publish an NBA licensed game". Payments were "license fees and guaranteed minimum royalties in installments" [P].
- **Extension:** "in 2025… extended and additional license fees were committed" [P]. Interestingly, the FY2024 20-F omitted the NBA from purchase obligations and the FY2025 20-F re-added it [P].
- **Amounts:** Not disclosed. Purchase obligations are reported only in aggregate (FY2025: ₩2,186M due within 12 months and ₩527M in 1–3 years) [P].
- **Territory:** The NBA press release says "first in Japan, then across Asia-Pacific" [P]. The 6-K refers to "contract regions" [P]. The exact territory list is [U].
- **Legends:** Retired legends appeared in Japan (for example Bird, Magic, Iverson, Nowitzki) [P]. I found no NBRPA or other legends-licensing disclosure [U]. Global store copy mentions players and coaches from current rosters, not legends [P].

### 5. Store presence and platforms (checked 2026-11-08)
- **Google Play:**
  - Package: `com.gravity.nbarisegv.aos` [P].
  - Store title: "NBA RISE: Basketball Strategy"; developer page id 6262333202706287552.
  - 100K+ downloads, about 1.12K reviews; the star rating varies by storefront (AU 4.2, KR 4.7, ID/MY 4.8).
  - Shows "Available on Android, Windows*" with "Powered by Intel", i.e. Google Play Games on PC.
  - Chart position at the time of the check: #9 Top Free Sports in SG and #7 in TH.
- **App Store:**
  - Listing: id6762187862 (https://apps.apple.com/ph/app/nba-rise-basketball-cards/id6762187862) [P].
  - Title: "NBA RISE: Basketball Cards" in English and "NBA RISE: 농구 카드 전략" in Korean.
  - Released 2026-10-20; requires iOS 15.0; 265 MB.
  - Languages: EN, ID, KO, TH and ZH.
  - Rated 17+ with a "Loot Boxes" advisory.
  - Ratings: TH 4.89 (63), KR 4.81 (48), PH 4.80 (41).
- **Age ratings by region:**
  - Google Play: AU Mature (Violence, Sexualised Imagery, Online Interactivity and Chat); KR 15+ (Sexuality); PH, ID, MY, SG, TH and NZ "Rated for 16+" (Strong Violence).
  - Unlaunched storefronts still carry ratings: US/CA Teen, GB PEGI 16, DE USK 16, JP 16+, TW PG15, BR 12+.
  - Korea's GRAC rating is 15+, per the App Store advisory [P].
- **Official site:** https://nbarise.gnjoy.com/ (redirects to /ko/official; locales KO, EN, TH, TL, ID, ZH-CN, ZH-TW). Probability disclosures at probability.gnjoy.com [P].
- **Social:**
  - Discord: discord.gg/Sz4Za6ZrMy
  - Facebook: facebook.com/profile.php?id=61590508838426
  - Instagram: @playnbarise
  - YouTube: @PLAYNBARISE
  - No X account is linked from the global site.
  - Japan's X account was @NBA_RISE [P].
- **Steam:** none (no Steam search results) [P].
- **Japan app (still listed):** Google Play `com.gravityga.nbarisetostardom` with 50K+ downloads and rated 3+; App Store id1574474570 rated 3.40 from 1,858 ratings, last version 2.0.14 [P].
  - Warning: the old Japanese domain nbarisetostardom.com has lapsed and now serves a gambling-spam page.

### 6. Investor materials and financial context
- **No dollar or won figures:** Gravity has never disclosed NBA RISE revenue or expectations in its 6-Ks, 20-Fs or IR decks [P].
- **What does appear:**
  - **FY2021 20-F:** the NBA RISE TO STARDOM launch helped raise advertising spend to ₩35,948M.
  - **Q1 2022 6-K:** lower QoQ advertising spend for NBA RISE TO STARDOM in Japan.
  - **FY2022 20-F:** R&D fell "following the launch of… NBA Rise to Stardom in 2021".
  - **IR pipeline entries 2021–2025:** as in the timeline above.
- **The global launch is missing from the Q1 and Q2 2026 business updates** and from the Aug 2026 pipeline slide [P]. Q3 2026 results had not been published as of Nov 8 [P].
- **Gravity scale:**
  - FY2025 preliminary revenue about ₩560bn, operating profit about ₩77bn, cash plus short-term instruments ₩618.6bn [P].
  - Q2 2026 revenue ₩161,884M, with mobile at ₩128,611M [P].
  - Ragnarok Online is offered in 91 markets [P].
- **Sports titles in the portfolio:** CPBL Pro-baseball 2021 (Taiwan), JLPGA Heroine Collection (Japan, 2025-03-25), and NBA RISE. Everything else is overwhelmingly Ragnarok IP [P].

### 7. Japanese version: ambassadors, collaborations and events
- **Ambassadors:** Yuta Watanabe (2021), Yuki Kawamura (2025-07-10), Rui Hachimura (2025-08-12).
- **TV and celebrity tie-ins:** a 10-episode show with Cocorico Tanaka, Ami Tokito and Chris Sasaki (2021); a Tabuse × Watanabe talk (Jan 2022).
- **NBA Rakuten:** co-produced programme (May 2022) and the RISE TO NIGHT viewing event (Oct 2022).
- **Anniversaries:** half-anniversary and first anniversary.
- **Themed events (2025):** THE GENIUS, Greatest Rivalry, Playoffs 2025, HISTORY OF HACHIMURA, THE TAG and others [all P].
- **Why the renewal happened:** the stated aims were "より直感的な操作、よりスピーディーな試合展開、快適なプレイ体験" (more intuitive controls, faster matches, a more comfortable play experience) [P]. No business reason was stated.

### Sources
**Primary:**
- https://pr.nba.com/nba-nbpa-gravity-mobile-gaming-experience-asia-pacific
- GGA press PDFs at gravityga.jp/wp-content/uploads/:
  - 2021/02/20210217press-release.pdf, 2021/08/2021-08-13-press-release.pdf, 2021/09/20210928_press-release.pdf
  - 2021/11/press-release_20211101.pdf, _20211102.pdf, _20211110.pdf, _20211115_nba.pdf, _20211116.pdf, _20211125.pdf, _20211126.pdf
  - 2021/12/press-release_20211201_nba.pdf
  - 2022/01/press-release_20220106.pdf, 2022/04/press-release_20220401_nba.pdf, 2022/05/press-release_20220524.pdf, 2022/07/press-release_20220707_nba.pdf, 2022/09/press-release_20220929_1.pdf, 2022/11/press-release_20221124_nba.pdf
  - 2023/02/press-release_20230209.pdf
  - 2024/11/press-release_20241126_nba.pdf
  - 2025/02/press-release_20250218.pdf, 2025/02/press-release_20250220.pdf, 2025/03/press-release_20250327.pdf, 2025/04/press-release_20250424.pdf, 2025/07/press-release_20250710_NBA_RISE.pdf, 2025/08/press-release_20250731.pdf, 2025/09/press-release_20250904.pdf, 2025/10/press-release_20251021.pdf, 2025/11/press-release_20251106.pdf, 2025/11/press-release_20251127.pdf, 2025/12/press-release_20251223.pdf
- GGA press index: https://gravityga.jp/category/press/
- nbarise.com notices:
  - https://nbarise.com/gupqoq/
  - https://nbarise.com/vjuaka/
  - https://nbarise.com/mgvjuf/
  - https://nbarise.com/kcodks/
  - https://nbarise.com/mjvyyd/
  - https://nbarise.com/vbmaqo/
  - https://nbarise.com/dfopsd/
  - https://nbarise.com/uyjuig/
  - https://nbarise.com/dsrwl/
  - https://nbarise.com/reinsde/
  - https://nbarise.com/yqfdhz/
  - https://nbarise.com/lastupk/
  - https://nbarise.com/ypgreqa/
  - https://nbarise.com/bnjgkf/
  - https://nbarise.com/yhdrjk/
  - https://nbarise.com/ct/news/
- PR TIMES notice on the early iOS download: https://prtimes.jp/main/html/rd/p/000000081.000071574.html
- SEC filings:
  - FY2025 20-F: https://www.sec.gov/Archives/edgar/data/1313310/000162828026026985/grvy-20251231.htm
  - Earlier 20-Fs: FY2020 (000156459021021574), FY2021 (000162828022010914), FY2022 (000162828023013345), FY2023 (000162828024018421), FY2024 (000162828025019782)
  - 6-Ks: 2021-02-16, 2021-08-13, 2021-11-12, 2022-05-13, 2026-02-13, 2026-05-08, 2026-08-07
  - EDGAR submissions API: https://data.sec.gov/submissions/CIK0001313310.json
- Gravity IR decks: API at https://www.gravity.co.kr/Api/IrPds; PDFs on img.gravity.co.kr (2021 Q1–2026 2Q)
- Google Play:
  - https://play.google.com/store/apps/details?id=com.gravity.nbarisegv.aos
  - https://play.google.com/store/apps/details?id=com.gravityga.nbarisetostardom
- iTunes API: https://itunes.apple.com/lookup?id=6762187862 and https://apps.apple.com/jp/app/nba-rise/id1574474570
- Official sites: https://nbarise.gnjoy.com/ and https://nbarise.com/

**Secondary:**
- https://www.invenglobal.com/articles/27412/gravity-officially-launches-nba-rise-across-8-regions
- https://www.invenglobal.com/articles/24039/gravity-launches-cbt-for-nba-rise-an-officially-licensed-nba-card-game
- https://www.inven.co.kr/webzine/news/?news=322325
- https://www.khgames.co.kr/news/articleView.html?idxno=309489
- https://www.ddaily.co.kr/page/view/2026102017023664548
- https://news.bizwatch.co.kr/article/mobile/2026/07/22/0026
- https://news.bizwatch.co.kr/article/mobile/2024/12/20/0014
- https://www.inews24.com/view/2021080
- https://gamebiz.jp/news/401032
- https://gamebiz.jp/news/396511
- https://gamebiz.jp/news/380432
- https://gamebiz.jp/news/430264
- https://dengekionline.com/article/202608/83074
- https://vegcale.com/?p=4677
- https://ascii.jp/elem/000/004/312/4312277/
- https://nz.finance.yahoo.com/news/nba-rise-stardom-official-launch-110000137.html
- https://www.mumuplayer.com/id/games/nba-rise-basketball-strategy-on-pc.html

**Could not fetch:** thisisgame.com/articles/428056 and kukinews (403), gamer.ne.jp (403), web.archive.org (blocked).

### Still unresolved
- Exact CBT start date (July 21 or 22) and pre-registration dates for the global version.
- Engine and team size.
- License term length, fee amounts and territory list.
- Legends licensing (NBRPA or otherwise).
- Month of the 2025 license extension.
- Whether the global client is derived from GGA's code.
- Any plans for markets beyond the 8 regions.
- Global revenue (first possible disclosure is the Q3 2026 results, due around mid-Nov 2026).
