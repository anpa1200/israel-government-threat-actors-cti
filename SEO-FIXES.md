# SEO fixes

Prepared locally on 2026-08-14. These changes are not committed, pushed, or deployed.

## Issue 4 — Docusaurus metadata

- `docusaurus.config.js` centralizes the browser-title suffix through the site title `1200km`, retains the project-specific 1200×630 social card, enables Git-backed update times, and emits the exact site name.
- `src/theme/DocItem/Metadata/index.js` supplies exact title, description, social, image, and modified-time parity for every route.
- `scripts/generate-seo-descriptions.mjs` combines reviewed route overrides with a grammar-safe tool-record template grounded in actor, type, confidence, source, behavior, IOC, mapping, and hunt fields; six-word phrase accounting prevents repetitive template tails.
- `scripts/seo-description-overrides.json` provides curated page-specific summaries for actor, methodology, report, navigation, and behavior-rich tool routes; no prose is clipped to fit.
- `src/generated/seo-descriptions.json` contains the 194 generated route descriptions.
- `scripts/check-seo.mjs` validates every built route and fails on metadata or tool-description diversity regressions.
- `package.json` regenerates descriptions before each build and includes `check:seo` in the existing validation workflow.

## Issue 7 — HexStrike destination labels

- `docusaurus.config.js` labels each `0x4m4/hexstrike-ai` navigation link as “HexStrike AI (upstream project).”
- `docs/ecosystem.md` gives the same explicit upstream label to both in-body links. No owner/fork destination occurs in this repository.

## Issue 8 — discovery and lastmod

- `.github/workflows/deploy-pages.yml` and `.github/workflows/validate.yml` check out full Git history so deployment and validation builds can derive real update dates.
- `docusaurus.config.js` enables Git-backed documentation dates and date-based sitemap entries.

## Issue 9 — structured data

- `src/theme/DocItem/Metadata/index.js` emits valid absolute-URL `BreadcrumbList` JSON-LD for every route.
- `scripts/check-seo.mjs` parses every JSON-LD block, validates breadcrumb order and absolute URLs, and rejects missing metadata.

## Validation

- `npm run build` — passed.
- `npm run check:seo` — passed: 194 routes, 194 unique descriptions, 194/194 sitemap `lastmod` values.
- The generated-description file is idempotent across repeated generation (SHA-256 `8b65b377e256c23410508fd065ac9179ac38349e6e24ec557d75c522b516cd58`).
- All 194 documentation descriptions were editorially reviewed after generation; actor summaries and tool records use complete page-grounded prose with normalized technical casing and no six- or seven-word phrase appears on more than two tool routes.
- Cross-site validation from the Field Manual checker passed across all four sites: 292 routes and 292 globally unique descriptions.
- `.github/workflows/validate.yml` and `.github/workflows/deploy-pages.yml` parse as valid YAML with full-history checkout enabled.
- Canonical URLs remain under `https://1200km.com/israel-government-threat-actors-cti/`.
- Every built title contains exactly one ` | 1200km` suffix; Open Graph and Twitter titles, descriptions, and images match.
- Every non-root documentation route exposes a Git-derived `article:modified_time`; the root is also a Git-backed documentation route.
- `git diff --check` — passed.

## Deploy and human follow-ups

- Commit and deploy this repository before treating the production metadata or sitemap as updated.
- After deployment, merge the sub-site sitemap into the main sitemap index and submit it to Google Search Console and Bing Webmaster Tools.
- Request indexing for the project landing page after the production build is live.
- No `article:published_time` was invented: the documentation framework exposes reliable last-update history but not a trustworthy creation date for every source page.

## Complete touched-file manifest

- `.github/workflows/deploy-pages.yml`
- `.github/workflows/validate.yml`
- `SEO-FIXES.md`
- `docs/ecosystem.md`
- `docusaurus.config.js`
- `package.json`
- `scripts/check-seo.mjs`
- `scripts/generate-seo-descriptions.mjs`
- `scripts/seo-description-overrides.json`
- `src/generated/seo-descriptions.json`
- `src/theme/DocItem/Metadata/index.js`
