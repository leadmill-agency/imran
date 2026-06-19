# CLAUDE.md — Dr. Imran Qureshi SEO Engagement

Memory anchor for this repo. Read this first on any new session. Last updated: end of Month 3 (June 2026).

## 🚨 ACTIVE: PRACTICE ADDRESS MOVE (as of May 26, 2026)

The practice is **relocating by Aug 1, 2026**:
- **From:** 23501 Cinco Ranch Blvd, Suite G205, Katy TX 77494 (current — still live)
- **To:** 1400 Ravello Dr, [Suite TBD], Katy TX 77450 (Energy Corridor / I-10 & TX-99 — a CLS Health facility, ~5–7 mi north)

**Migration is prepped on the `address-migration` git branch — DO NOT merge to `main` until the practice physically moves** (Vercel auto-deploys main; changing the address early sends patients/Google to an empty office and risks GBP suspension). Full runbook: `_project/snapshots/address-move-may-2026/RUNBOOK.md`. Plan: `~/.claude/plans/joyful-noodling-quiche.md`.

**Blocking step:** Dr. Q must confirm exact suite # + ZIP (77450 vs 77449) — email drafted at `_project/snapshots/address-move-may-2026/email-to-dr-q-nap-confirmation.md`.

**Gotchas:** (1) "Cinco Ranch" stays as a service-area city — only the `23501 Cinco Ranch Blvd` street token changes. (2) Phone number does NOT change. (3) MOVE the GBP listing, never recreate (preserves 58 reviews). (4) Expect a re-evaluation ranking dip post-move (4–8 wks, like April).

## What this is

SEO + AI Overview engagement for **Dr. Imran Qureshi, D.O.** — interventional pain management physician in Katy, TX. Agency: **Leadmill** (operator: Rameel). Static HTML site on Vercel, auto-deploys from GitHub `main`.

- **Live site:** https://www.drimranqureshi.com
- **Repo:** https://github.com/leadmill-agency/imran
- **GA4:** G-SHWLFXVMMF
- **GBP place_id:** ChIJHT05uVshQYYRFM2xWG_wWps
- **Address:** 23501 Cinco Ranch Blvd, Suite G205, Katy, TX 77494 · (281) 982-2144
- **Booking:** LumaHealth portal

## Where everything lives

| What | Path |
|---|---|
| **Project status (READ FIRST)** | `_project/PROJECT-STATUS.md` — full engagement state, what's shipped/pending |
| **Agency master playbook** | `/Users/rameel/Desktop/Manual Library/Leadmill/playbooks/local-seo-ai-overview-playbook.md` — the canonical SEO/AIO methodology + 20 Field Notes lessons. Read the Field Notes section before doing anything non-trivial. |
| **Month-by-month plans** | `_project/month-3-detailed-execution-plan.md`, `_project/month-4-detailed-execution-plan.md` |
| **Snapshots (point-in-time)** | `_project/snapshots/` — reports, scan analyses, audits, client call agendas |
| **Reference docs** | `_project/reference/` — keyword research, citation library, client photos |
| **Grid rank tracker tool** | `/Users/rameel/Desktop/Manual Library/Leadmill/tools/grid-rank-tracker/` — local-only git repo, NOT pushed to GitHub |

## Critical operational gotchas (learned the hard way — DON'T repeat these)

1. **Grid scan billing:** Run scans with `python3 -u scan.py imran` (the `-u` prevents buffering hangs). The `FIELD_MASK` in `scan.py` MUST stay `places.id` only — adding `displayName` or other fields bumps Google Places API from $5/1000 (Essentials) to $40/1000 (Pro), an 8x cost spike. This already cost ~$120 once. Each scan now costs ~$7.
2. **GCP Free Trial credit is EXPIRED.** Scans are real cash now (~$7 each). A $30/mo budget alert is set. Run bi-weekly, not more.
3. **Every URL in `sameAs` schema must be WebFetch-verified before adding.** Healthgrades placeholder URL returned the homepage for 2+ weeks before we caught it. We're at 10 verified URLs (the playbook's right count of 8–12) — done with directory hunting.
4. **Don't celebrate single-scan ranking spikes.** May 11 showed a keyword in the map pack; May 18 it reversed; June 3 it settled. Rankings are noisy — wait for 2+ consecutive scans before calling a trend (Field Note #17).
5. **Don't project month-end from a front-loaded partial month.** Mid-May projection said +52% calls; actual was +20%. Report actuals with date ranges, not forecasts (Field Note #20).
6. **Always ask the client about non-SEO marketing.** Dr. Q shared his site in a 300+ member neighborhood group in late April — inflated early-May GBP numbers. Organic search metrics are pure SEO; GBP calls/clicks are a mix (Field Note #19).

## Engagement state at end of Month 3 (June 2026)

**Final May results (actuals, not projections):**
- GBP calls: 60 (+20% vs April) — the durable SEO baseline
- GBP website clicks: 52 (+33%)
- GBP total interactions: 170 (+21%)
- Organic search clicks: 56 (+211%) — cleanest pure-SEO win
- Organic impressions: 2,460 (+237%)

**Maps coverage settled at a HIGHER baseline than May 2 (the validating win):**
- pain management doctor katy: 81/81 grid points in top-10 (entire service area)
- pain management katy: 80/81
- pain management katy tx: 74/81 (tripled from 23)

**Scan history (DIY tool):** May 2, May 7, May 11, May 18, Jun 3, Jun 17. Plus 5 LocalRank CSVs (Mar 4–May 11) in `_project/snapshots/localrank-csvs-mar-may-2026/`. Latest analysis: `_project/snapshots/ga4-conversion-analysis-jun-17.md` (Jun 17 scan + GA4 + the first AEO/AI-assistant traffic signal).

## What's done / removed from scope

- ✅ April E-E-A-T retrofit (51 citations, bylines, answer-blocks, 71 H2 conversions)
- ✅ GBP URL fixed (was cls.health → now drimranqureshi.com)
- ✅ GA4 conversion tracking live (Key Events marked May 18)
- ✅ 5 city pages differentiated
- ✅ sameAs verified (10 URLs)
- ✅ LocalRank cancelled → DIY tracker ($297/mo → ~$7/scan)
- ❌ Paid directories (Sharecare, Wellness.com, Castle Connolly, BBB, Doctor.com, Katy Chamber) — skipped
- ❌ Q&A seeding, review-acceleration system — client opted out / CLS Health has one

## Current focus: Month 4 (June)

Per `_project/month-4-detailed-execution-plan.md`. Priorities: (1) review velocity, (2) **AI Overview citation expansion**, (3) 2 new procedure pages (knee gel injection, genicular nerve block), (4) conversion optimization, (5) Bing/AEO indexing, (6) PAA-derived FAQs.

## Conventions

- Static HTML, inline CSS, no build step. Each page self-contained. Header/footer duplicated across all files (update everywhere when changing).
- Templates: `treatments/nerve-blocks.html` for treatment pages, `blog/what-is-radiofrequency-ablation.html` for blog posts.
- Schema: JSON-LD in `<head>`. Treatment pages = MedicalProcedure + Physician + FAQPage. Validate at search.google.com/test/rich-results.
  - `MedicalProcedure.procedureType` must be a `MedicalProcedureType` enum IRI (e.g. `https://schema.org/PercutaneousProcedure`), NOT free text like "Injection" — free text is a schema.org validation error (fixed Jun 2026).
  - Blog `Article` schema needs `image` + `publisher.logo` (ImageObject) for Google rich-results eligibility. Currently both point at the headshot/favicon-192 as a baseline — swap `image` to per-post hero images when those exist.
  - Known un-fixed inconsistency: schema `@id`/`url` use non-www `drimranqureshi.com` while the site canonicalizes to `www` (non-www 307s to www). Not a validation error; left for a deliberate pass.
- Page-depth standard: location/city + procedure + condition pages must be **1,000+ visible words AND genuinely differentiated** from sibling pages — not just long. Measure both: word count, and cross-page boilerplate ratio (sentence overlap with city/distinguishing tokens normalized out) — keep boilerplate well under 50%. Procedure/condition pages already clear this; the 5 `pain-management-*-tx` city pages were brought from ~870–935 words / ~50% boilerplate to 1,000+ / ~38–42% in Jun 2026 by adding verified per-city local content (named master-planned communities + population-specific clinical angle + localized FAQ). Differentiate with web-verified local facts (a fabricated neighborhood backfires), and keep city-page additions move-durable — no drive-time/route/office copy (the address migration handles those). See playbook Field Note #28.
- Commit messages end with the Co-Authored-By trailer. Branch off `main` only when asked; commit/push only when asked.
- `_project/` is gitignored from search engines via robots.txt `Disallow: /_project/`.
- Site-wide changes: write a Python/regex script over all files, don't hand-edit page-by-page (Field Note #8). AFTER running it, validate the output — parse every `application/ld+json` block and confirm injected code landed in the right tag (a May 2026 GA4-injection script pasted JS inside an `ld+json` tag on blog/index.html, breaking the schema AND silently killing tracking; Field Note #21).
