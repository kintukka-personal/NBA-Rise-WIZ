<!-- Research report compiled 2026-11-09. The official pack data it mentions is preserved in ../data/. -->

# NBA RISE (GRAVITY, global 2026): companion-resource landscape, checked 2026-11-08/09

## Summary
- **Nobody offers a database, tier list, team builder, synergy calculator, market price tracker or bot for NBA RISE.** I found none in any of the 7 languages. What exists: the official channels, five code pages, a few emulator vendor guides (mostly marketing), sponsored-style launch blog posts, and about 18 small YouTube gameplay videos.
- **There is an official public card list.** Gravity's legally required probability pages (Korean only) list every card in every pack by name, series, grade and drop rate. I parsed all 55 pack pages: **878 unique cards** across 403 player names and 7 series (25-26 SEASON 390, Starter 385, The Core 60, LOCKDOWN 11, HALLOWEEN 11, FLAME 11, The Edition 10). By grade: COMMON 238, UNCOMMON 182, RARE 176, ULTRA RARE 124, EPIC 145, LEGEND 13. Higher grade labels (Elite, Prime, IConic, GOAT) appear but contain no cards yet. These pages do **not** include card stats; they say stats are only visible in the in-game collection screen. The pages also describe a pity rule (an EPIC is guaranteed after 100 cards) and a wishlist for EPIC pulls.
- **The game has an in-game Market where all items, including player cards, can be traded** (Inven Global launch article). That is the futbin-style price-tracking opportunity, and nobody covers it.
- **All 12 candidate domains return NXDOMAIN, and registry lookups say 10 are not registered.** The two .gg names could not be confirmed.

## 1. NBA RISE resources found

### Official
| Name | URL | Type | Lang | What it offers | Depth / activity | Official? |
|---|---|---|---|---|---|---|
| Official site | nbarise.gnjoy.com (redirects to /ko/official, /en/official) | site | KO, EN, TH, TL, ID, ZH-CN, ZH-TW | One landing page: features, a "Card Collection" carousel of 19 card images, store links, social links, support, odds | Single page. Other paths (/en/news, /notice, /guide, /players, /collection) return 404 | Official |
| Odds disclosure | probability.gnjoy.com/NBA/NBARISE/NBARISE/NBA-NOTIFY → LIST1 (54 packs) and LIST3 (Diamond Box), with detail pages at prd-clutch-api.gnjoy.com/ext/news/offerrate?offerGroupId=… | data | KO | Every card in each pack, with grade and drop % | 55 pages. Note dated 2026-10-22. Packs live now include LOCKDOWN (ended), HALLOWEEN, FLAME | Official |
| Discord | discord.gg/Sz4Za6ZrMy | community | EN (multi) | Announcements, codes, events | 2,745 members, 85 online (invite API, 2026-11-09). Community server with onboarding | Official |
| Facebook page | facebook.com/profile.php?id=61590508838426 | social | ? | Coupon codes are announced here | Blocked (HTTP 400 / login wall). Stats not verified | Official (linked from the site) |
| Instagram @playnbarise | instagram.com/playnbarise | social | ? | – | Blocked (429). Not verified | Official |
| YouTube @PLAYNBARISE | youtube.com/@PLAYNBARISE | video | EN, KO | Trailers and promos | 92 subscribers, 29 videos. CBT trailer 2.38M views, animation teaser 1.98M, "The Dream" EP.1 579K, launch trailer 436K. Views far above subscribers, which suggests paid promotion (my inference) | Official |
| Gravity YouTube Brand Channel | youtube.com (video scyJRAUHptA) | video | KO | KR CBT announcement | 233 views | Official (corporate) |
| TikTok @playnbarise | tiktok.com/@playnbarise | social | – | – | Name "NBA RISE", 0 followers, 0 videos. ID decodes to creation around 2026-06-08. **Not verified as official** | Unclear |
| Hive support / Game FAQ | customer.withhive.com/gravity/faq/game/3422 | FAQ | KO/EN | Official FAQ and ticket form | Rendered by JavaScript, so I could not read the content | Official |
| Google Play listing | play.google.com/…id=com.gravity.nbarisegv.aos | store | EN | – | PH store: 4.6★, 1.14K reviews, 100K+ downloads, updated Oct 28 2026. **Also installs on Windows via Google Play Games on PC** | Official |
| App Store listing | apps.apple.com/…/id6762187862 | store | – | – | v1.1.1 (2026-11-05). PH 4.82★ (44 ratings), KR 4.82★ (49), AU 4.30★ (23). Rated 17+ | Official |
| JP predecessor site | nbarise.com | site | JA | Service-end and refund notices | Last post Aug 31 2026. Game is dead | Official (old game) |
| NBA press release | pr.nba.com/nba-nbpa-gravity-mobile-gaming-experience-asia-pacific | news | EN | 2021 licence announcement | 2021-02-15 | Official |

### Third-party
| Name | URL | Type | Lang | What it offers | Depth / activity | |
|---|---|---|---|---|---|---|
| UCNGame codes | ucngame.com/codes/nba-rise-codes/ | codes | EN | 7 codes with exact rewards and expiry dates (3 expire Nov 18, 4 expire Nov 30), redeem steps | Dated Oct 24 2026, title says "NOV 2026". Best of the code pages | 3rd party |
| MrGuider codes | mrguider.org/codes/nba-rise-codes/ | codes | EN | Same codes, redeem steps | Updated Oct 24 2026 (from search snippet). **Direct fetch blocked (403)** | 3rd party |
| 9to5gaming codes | 9to5gaming.com/nba-rise-basketball-codes/ | codes | EN | Same 7 codes, rewards listed only as "free rewards" | Dated Oct 23, "updated Nov 2026". Content is template-like | 3rd party (new) |
| Clashiverse codes | clashiverse.com/nba-rise-basketball-codes/ | codes | EN | Same 7 codes | Nov 2 2026, author Oman Bilal | 3rd party (new) |
| MuMuPlayer guides | mumuplayer.com/th/blog/nba-rise-basketball-strategy-beginner-guide.html and …-release-date.html | guide | TH | Short beginner tips ("two-core" build, resource and content priority, fatigue rotation). Release date and pre-registration rewards | Oct 1 2026. No tier list or player picks. Promotes the emulator | 3rd party (vendor) |
| MuMuPlayer PC pages | mumuplayer.com/games/nba-rise-basketball-strategy-on-pc.html (+ /kr /th /jp /id /vi /tw /ru /pt /es) | PC emulator page | ~10 languages | Install instructions, marketing | – | 3rd party (vendor) |
| MEmu Play | memuplay.com/how-to-play-nba-rise-basketball-strategy-on-pc.html (+ /zh, /id) | PC emulator page | EN/ZH/ID | Install instructions | Shows v1.0.3, Oct 28 2026 | 3rd party (new) |
| Naver blog launch reviews | blog.naver.com/12512512/224449341627 (includes a coupon list), blog.naver.com/ngga32472/224449909504, blog.naver.com/dekiruho123/224451027691 | review / codes | KO | Launch overviews | Oct 21–23 2026. Look like publisher-seeded reviews (my inference) | 3rd party (new) |
| inews24 "[겜별사]" review | inews24.com/view/2021080 | review | KO | Mechanics: player condition, rotation, set-play timing, rerolls at start | One article | Press |
| Lapakgaming top-up | lapakgaming.com/id-id/nba-rise | commerce | ID | Gold and bundle prices (2,000 Gold Rp17,000 up to Hall of Fame Package Rp248,700). Uses NBA Rise ID | Prices updated Nov 8 2026 | 3rd party (new) |
| AppGoblin | appgoblin.info/apps/com.gravity.nbarisegv.aos | app intelligence | EN | Estimates: about 218K installs and MAU, $10K+/month revenue (Android only) | Crawled 2026-10-21 to 2026-11-08 | 3rd party |
| DCInside "Nba rise" minor gallery | gall.dcinside.com/mgallery/board/lists/?id=ris1017e | community | KO | – | Created 2026-07-24. **2 junk posts in total**, last one Aug 18. Manager absent. Dead | 3rd party (new) |
| Inven game DB | inven.co.kr/webzine/news/?game=13857 | news hub | KO | News only. Still marked "테스트" (test). No board | 1 news article | Press |
| Gamerch wiki (JP game) | gamerch.com/nba-rise/ | wiki | JA | Top page, reroll ranking, 3 boards | 1 editor, last edit 2026-01-23, 8 comments. Game is dead | 3rd party |
| TapTap / QooApp (JP game) | taptap.io/app/226680, apps.qoo-app.com/en/app/16792 | listing | – | – | TapTap 2.2/10 (10 ratings), 3.8K followers. QooApp 2.4 (3 ratings). I found no listing for the global game | 3rd party |
| BlueStacks (JP game only) | bluestacks.com/apps/sports/nba-rise-to-stardom-on-pc.html | PC emulator page | multi | – | No page for the global game found | 3rd party |
| YouTube creators | DAQ1bqHZq_4 Gachaman (1,290 views), TXHgQuEib8A and AyDuOGx0V08 AetherFyre (2,393 / 1,776), Jw_GGvam1R0 Adeptless (1,792), FpyljTDbIhw 불닭방송국 (1,375), WRXB9B5iLbI IrpanXGame (667), idhk_2RGWb8 Gamer쿠그너즈 (462), C4Osin6kUmU anonzlive TH (462), 45o2OA4-IIA ijavi (409), uN6ALpZuWZg 게임달고나 (389), bo6CBp9TuR4 산타PD (311), 9bhXehWL8rM 겜딘 (256), SUokdcKDBYI iroGames (230), HGG8_t5ZKVE Lenzy Games (163), _Z0OEHnVzRQ 킷싱 (59), 9zy8nl1ksc0 MDO ID (30), others under 40 views | video | EN, KO, TH, ID | Gameplay, first impressions, streams | Mostly 2 weeks to 3 months old. **No guide, tier-list or pack-opening analysis videos** | 3rd party |
| News | invenglobal.com/articles/27412 (launch, 2026-10-19), invenglobal.com/articles/24039 (CBT), gamingonphone.com (CBT 2026-07-23, pre-registration 2026-09-16), thisisgame.com/articles/428056, news.bizwatch.co.kr, thisisgamethailand.com (blocked 403) | news | EN, KO, TH | Facts. Launch article lists modes: PvP Arena, Popularity Battle, Tower Race, PvE Season, Daily Division, RvR Club Conquest, Clubs, Market | – | Press |

### Searched, nothing found (or blocked, marked)
- **Tier lists, card databases, deck or lineup builders, synergy or pack calculators, market price trackers:** none in any language.
- **Reddit:** login wall (www returns 403, old.reddit redirects to login). Web search found no subreddit or threads. *Unverified.*
- **Fandom:** all *.fandom.com pages and the community API sit behind a Cloudflare challenge. *Unverified.* Web search found no NBA RISE Fandom.
- **Namu Wiki:** 403, no search hit, no Wayback snapshot. *Unverified.*
- **Arca.live:** Cloudflare challenge, no search hit. *Unverified.*
- **Other Korean boards:** no Naver Cafe or Naver Game Lounge, nothing on Ruliweb, no Inven board.
- **Japanese guide sites:** Game8, GameWith and AppMedia return 404. Altema, wikiwiki and atwiki return 403 (*unverified*).
- **Big code sites:** PocketTactics, PocketGamer, GameRant, Destructoid, Beebom, LootBar and GamingonPhone have no codes page.
- **PC emulators:** BlueStacks has no page for the global game. LDPlayer returns 403 (*unverified*).
- **Discord listings:** Disboard and top.gg are blocked (403). discords.com has no result. No unofficial servers or bots found.
- **Telegram:** handles nbarise, nbariseofficial, playnbarise, nbarisegame, nbarise_th, nbarise_id, nbariseph and similar do not exist.
- **Facebook groups and X:** login walls; web search found none. No companion apps on Google Play or the App Store. GitHub has only your own repo.
- **TikTok @nbarise** ("Nba Rise242", 47 followers, created 2021) is probably unrelated.
- **Warning:** nbarisetostardom.com, the old JP domain still linked from Gamerch, has lapsed and now hosts an Indonesian gambling spam site.

## 2. Domain checks
I used DNS-over-HTTPS (dns.google) plus registry RDAP. `dig` was not installed and WHOIS port 43 is blocked here.

| Domain | DNS | Registration (RDAP) | Verdict |
|---|---|---|---|
| nbarisedb.com, nbarisehub.com, nbarisebin.com, nbarise.net, nbarisetracker.com | NXDOMAIN | Verisign 404 | Not registered |
| nbarise.wiki, nbarise.tools, nbarise.info, nbarise.app, nbarise.io | NXDOMAIN | Registry 404 | Not registered |
| nbarise.gg, risedb.gg | NXDOMAIN at the .gg registry | No RDAP for .gg; WHOIS blocked | Very likely unregistered (not confirmed) |

None serve an NBA RISE site and none are parked. Positive control: nbarise.com is registered (2024-02-20 to 2027-02-20) and resolves. Premium pricing on available names was not checked.

## 3. Gaps a fut.gg-style tool could fill
1. **Searchable card database** with stats, position, grade, series and coach cards. The card list exists in the official odds pages but stats are only in-game, so they need manual entry, screenshot contributions (fhcwiz's model) or OCR.
2. **Market price tracking:** price history, alerts, sell/flip calculators.
3. **Lineup builder** with chemistry and synergy rating, position balance, bench rotation and coach selection.
4. **Pack odds and pity calculator:** expected cost to an EPIC (100-card pity), wishlist odds, which pack is best value.
5. **Card upgrade / promotion cost planner** for training manuals, gold and silver, including the unused higher grades.
6. **Tier lists** (meta, per position, per mode) and counter-tactic guides for set plays.
7. **Code tracker** with expiry dates in EN, KO, TH, ID and TL. Only English aggregators exist now.
8. **Event, season pass and promo calendar,** and tracking of new series such as FLAME and HALLOWEEN.
9. **Mode guides** (Tower Race, Popularity Battle, Club Conquest), club recruitment, leaderboards.
10. **Localised content** for TH, ID, TL and KO, and a Discord bot (card lookup, codes).

## 4. Benchmark feature lists
**fhcwiz.com** (Football Head Coach 27, free, no accounts, data stays in the browser)
- PTC Solver: shows the remaining average, positions and rarities needed, with closest-card suggestions. A cheapest-completion optimizer is "coming soon".
- List of all PTCs (permanent, limited, progressive, tiered, event).
- Player database filtered by OVR, position, card type, set, team and stat. Grid or list view. CSV/JSON import and CSV export.
- Compare 2–4 cards, with the best stat highlighted.
- Team Builder: captains, weakest-link finder, roster rating, saved builds.
- Game Plan (beta): suggests offensive and defensive tactics from your depth chart and opponent scouting.
- Pack odds lookup, plus a Best Cards page and a PTC guide.
- Personal tools: price history with notes, claimed-challenge tracker, backup export/import.
- Community leaderboard: users send screenshots by email, 10 ranks. Also a blog, and it installs as an offline app.

**fut.gg**
- Player database, compare, "Past & Present", gallery and holographic card pages.
- Evolutions: all evos, Evo Lab, evolved players, best PlayStyles by role, evo leaderboards.
- GG Club: links your EA account and syncs your squads, evolutions and players; "Hidden Gems".
- SBCs: all SBCs, streamlined SBC solver, rating combinations, cheapest by rating.
- Objectives tracker, Season Pass, live events, token store.
- Squad Builder, Gauntlet builder, saved squads, popular tactics.
- Market: momentum trends and price ranges. Campaign hubs (in packs, live, upgrades).
- Community tools: tier lists, card creator, collections, player pools, Rush, FUT Grid daily game.
- Reference pages (clubs, nations, leagues, rarities, roles, chemistry styles), news, iOS and Android apps, sister sites.

**futbin.com** (the website was behind a Cloudflare challenge; this list comes from its Play listing and secondary sources)
- Player pages: 3 lowest Buy Now prices, hourly and daily price graphs, price range, automatic tax calculator, stats, traits.
- Notifications: player, market, squad and SBC alerts.
- SBC details, user-contributed solutions, solution cost, best-value SBC ranking.
- Squad Builder with chemistry-based suggestions and total squad price. Squads sync between web and app.
- Evolutions hub and builder, popular evos.
- Pack Scan, Team of the Week list, consumable prices, player comparison, draft simulator, news.
- Premium in-app tiers (Bronze to Platinum, $1.99–6.99) that remove ads. App: 10M+ downloads, 4.6★ (326K reviews), updated Nov 6 2026.

## 5. Sources
nbarise.gnjoy.com/ko/official · probability.gnjoy.com/NBA/NBARISE/NBARISE/NBA-NOTIFY · probability.gnjoy.com/NBA/LIST1 · probability.gnjoy.com/NBA/LIST3 · prd-clutch-api.gnjoy.com/ext/news/offerrate?offerGroupId=10020 (and 54 others) · discord.com/api/v10/invites/Sz4Za6ZrMy?with_counts=true · youtube.com/@PLAYNBARISE · tiktok.com/@playnbarise · customer.withhive.com/gravity/faq/game/3422 · play.google.com/store/apps/details?id=com.gravity.nbarisegv.aos · itunes.apple.com/lookup?id=6762187862 · nbarise.com · nbarisetostardom.com · pr.nba.com/nba-nbpa-gravity-mobile-gaming-experience-asia-pacific · ucngame.com/codes/nba-rise-codes/ · mrguider.org/codes/nba-rise-codes/ · 9to5gaming.com/nba-rise-basketball-codes/ · clashiverse.com/nba-rise-basketball-codes/ · mumuplayer.com/th/blog/nba-rise-basketball-strategy-beginner-guide.html · mumuplayer.com/th/blog/nba-rise-basketball-strategy-release-date.html · mumuplayer.com/games/nba-rise-basketball-strategy-on-pc.html · memuplay.com/how-to-play-nba-rise-basketball-strategy-on-pc.html · blog.naver.com/12512512/224449341627 · blog.naver.com/ngga32472/224449909504 · blog.naver.com/dekiruho123/224451027691 · inews24.com/view/2021080 · lapakgaming.com/id-id/nba-rise · appgoblin.info/apps/com.gravity.nbarisegv.aos · gall.dcinside.com/mgallery/board/lists/?id=ris1017e · inven.co.kr/search/webzine/top/NBA 라이즈 · gamerch.com/nba-rise/ · taptap.io/app/226680 · apps.qoo-app.com/en/app/16792 · bluestacks.com/apps/sports/nba-rise-to-stardom-on-pc.html · kamigame.jp/game/70392/ · invenglobal.com/articles/27412/gravity-officially-launches-nba-rise-across-8-regions · invenglobal.com/articles/24039 · gamingonphone.com/news/nba-rise-opens-pre-registration-on-mobile-as-the-basketball-card-strategy-game-prepares-for-launch/ · gamingonphone.com/news/nba-rise-hits-the-court-with-its-basketball-action-now-live-with-its-first-closed-beta-test-on-android/ · thisisgamethailand.com/games/mobile/nba-rise-dl-th/ · thisisgame.com/articles/428056 · news.bizwatch.co.kr/article/mobile/2026/07/22/0026 · fhcwiz.com · fut.gg · fut.gg/about · play.google.com/store/apps/details?id=com.futbin · rdap.verisign.com and rdap.org lookups · dns.google/resolve

The 55 raw odds pages are saved in (session scratchpad, not preserved)/offers/ if you want to build a card list from them.
