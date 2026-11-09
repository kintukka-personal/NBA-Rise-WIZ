# RiseWiz brand

The visual system and brand for **RiseWiz**, a fan companion for GRAVITY's NBA RISE. It is the third sibling of FHCWiz and UFMWiz.

## Files

| Path | What it is |
|---|---|
| [`RiseWiz_Visual_System.html`](RiseWiz_Visual_System.html) | The full system: identity, voice, foundation, colour, type, texture, live components, rarities, the clipboard, rules, build and limits. Open it in a browser. Published copy: https://claude.ai/artifact/HQYr5ho3buzBmXzckeeSbf |
| [`tokens.css`](tokens.css) | 198 drop-in custom properties (`--rw-*`), the same values the document uses |
| [`measurements/samples.md`](measurements/samples.md) | Where every measured value came from: image, region and method |
| [`measurements/font_fit.json`](measurements/font_fit.json) | Typeface identification for words: 32 faces scored against in-game text (Open Sans) |
| [`measurements/font_fit_numerals.json`](measurements/font_fit_numerals.json) | Typeface identification for numbers: Team Power, scores and OVR scored against 35 condensed faces (Anton) |
| [`measurements/hue_occupancy.json`](measurements/hue_occupancy.json) | Hue distribution of the game's saturated UI pixels |
| [`screenshots/catalog.csv`](screenshots/catalog.csv) | All 424 screenshots in the corpus: source page and image URL, size, sha1, the screen shown, and whether it is full in-game UI. 142 are; 51 of those are from the July 2026 closed beta |
| [`tools/`](tools/) | `sample.py` (region median and clusters, vertical profiles), `palette.py` (median-cut palette and dark-pixel bias), `huegap.py` (hue occupancy), `absent.py` (OKLab + colour-vision absent-colour search), `font_fit_render.js` + `font_fit.html` and `font_fit_numerals_render.js` + `font_fit_numerals.html` (render candidate faces for overlap scoring) |

## The short version

- **The game's half is measured.**
  - Cool slate grounds, centred on `#2A2E32`. 89% of dark pixels lean blue.
  - Flat fills with no gloss anywhere. Elevation comes from glow.
  - Cyan `#00AEEF` commits. Home is blue `#158EFD` and away is red `#DF263D`.
  - Gold is Team Power and synergy. Bronze chips are offensive tactics and mint chips are defensive tactics.
  - A five-step condition scale, and six rarity metals.
- **Two typefaces, both identified by glyph overlap.** Words are Open Sans: Bold for interface text, ExtraBold for titles. Big numbers are Anton: Team Power, scores and OVR.
- **Every hue is the game's.** An OKLab search with colour-vision simulation found no colour more than 6.3 ΔE from all 34 game accents. So RiseWiz owns a material, not a colour: **black marker on a white clipboard**.
- **The mark** is a W run off two screens, in basketball's own notation.
- **The wordmark** is RISEWIZ in Big Shoulders Display Black. RISE is in the game's inactive grey `#8B94A2`, WIZ is white, and a white marker rule sits beneath.
- **Name.** "NBA" never appears in brand type; the family pattern takes the game's own word, RISE. `risewiz.gg` is unregistered (`risewiz.com` is taken).

## Re-measuring

When GRAVITY ships a new screen or rarity:
1. Add its screenshot to `screenshots/catalog.csv`.
2. Sample it with `tools/sample.py IMG name:x0,y0,x1,y1`.
3. Log the value in `measurements/samples.md`.
4. Add the token to both `tokens.css` and the Build section of the HTML.

The Legend frame and the four reserved grades above it (Elite, Prime, Iconic, GOAT) are still unmeasured. No public screenshot shows them yet.

`tools/font_fit.html` expects the candidate fonts to be loadable. Google Fonts load directly. The official site's fonts (Nexon Football Gothic, Pretendard, S-Core Dream) are not committed here; fetch them from nbarise.gnjoy.com's own stylesheet to re-run that comparison.

Screenshots themselves are not committed, because they are GRAVITY's and the NBA's copyrighted material. The catalogue records every source URL instead.
