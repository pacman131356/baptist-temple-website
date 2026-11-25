# Baptist Temple: concept preview

Concept redesign of [baptist-temple.com](https://www.baptist-temple.com/) (Connersville Baptist Temple, Connersville, IN), prepared by Holden Creative. Not the church's official site; every page is marked as a preview and kept out of search engines.

## How it's built
- `build.py` writes every page from one shared header and footer. Edit it, then run `python3 build.py`.
- `styles.css` holds all styles; `site.js` runs the menu, scroll reveals, and preview-only forms.
- Static files, no build step on Netlify. Every push to `main` deploys.

## Pages (12)
Home, Plan a Visit, Our Story & Beliefs, Our Team, Kids, Students, Sunday School, Adults & Outreach, Watch, Connection Card, Prayer Requests, Contact. Old addresses (`/about-us`, `/beliefs`, `/plan`, `/other-ministries`) redirect.

Left out: Resources (its bulletin and study-sheet links point to Google Drive files we don't have yet), Sunday Sermon Notes (`/new-page` is a placeholder on the current site), and Cart.

## Content
All facts come from the current site (fetched Nov 24, 2026). Nothing is invented. Items to confirm with the church:
- Pastor's surname: the staff heading says "Ferriera"; his bio and the Sunday School page say "Ferreira". The preview uses Ferreira.
- Kids ages: the kids page says birth to 6th grade, its meta description says 5th. The preview uses 6th.
- Sunday School time: the Watch page says 9:00; every other page says 9:30. The preview uses 9:30.
- Staff bios are shortened.

## Images
Photos load from the church's own Squarespace image host, so nothing has been copied yet. Only the church's own photos are used; the stock and AI-generated images on the current site were left out. Sources are listed in `IMAGE-SOURCES.md`. Before launch, copy originals into the client's Google Drive folder and serve optimized copies from `/img`.
