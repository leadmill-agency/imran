# Dr. Imran Qureshi — Project Status

## Client Info
- **Client:** Dr. Imran Qureshi, D.O.
- **Practice:** Interventional Spine & Sports Medicine
- **Location:** 23501 Cinco Ranch Blvd, Suite G205, Katy, TX 77494
- **Phone:** (281) 982-2144
- **Live site:** https://www.drimranqureshi.com
- **Hosting:** Vercel (auto-deploys from GitHub `main` branch)
- **Repo:** https://github.com/leadmill-agency/imran
- **GA4:** G-SHWLFXVMMF
- **Booking:** LumaHealth portal

---

## Current Site Inventory (44 pages)

### Core Pages (5)
| Page | URL |
|------|-----|
| Homepage | / |
| About | /about |
| Contact | /contact |
| Insurance | /insurance |
| 404 | /404 |

### Condition Pages (11)
| Page | URL |
|------|-----|
| Low Back Pain | /low-back-pain |
| Herniated & Bulging Discs | /bulging/herniated-discs |
| Nerve Pain & Neuropathy | /nerve-pain/neuropathy |
| Neck Pain & Arm Numbness | /neck-pain-and-arm-numbness |
| Knee Pain & Arthritis | /knee-pain/arthritis |
| Hip Pain & Arthritis | /hip-pain/arthritis |
| Shoulder Injuries & Pain | /shoulder-injuries/pain |
| Sacroiliac (SI) Joint Pain | /sacroiliac-si-joint-pain |
| Sports Injuries | /sports-injuries |
| Regenerative Medicine | /regenerative-medicine |
| Imaging | /imaging |

### Treatment Pages (9)
| Page | URL |
|------|-----|
| Epidural Steroid Injections | /treatments/epidural-steroid-injections |
| Radiofrequency Ablation | /treatments/radiofrequency-ablation |
| Nerve Blocks | /treatments/nerve-blocks |
| PRP Therapy | /treatments/prp-therapy |
| Spinal Cord Stimulation | /treatments/spinal-cord-stimulation |
| Joint Injections | /treatments/joint-injections |
| Trigger Point Injections | /treatments/trigger-point-injections |
| Kyphoplasty | /treatments/kyphoplasty |
| Discography | /treatments/discography |

### Hub Pages (2)
| Page | URL |
|------|-----|
| Treatments Hub | /treatments |
| Conditions Hub | /conditions |

### Blog Posts (10)
| Post | URL |
|------|-----|
| Blog Hub | /blog |
| When Should You See a Pain Specialist? | /blog/when-to-see-a-pain-specialist |
| What Is Radiofrequency Ablation? | /blog/what-is-radiofrequency-ablation |
| PRP Therapy for Joint Pain | /blog/prp-therapy-for-joint-pain |
| Epidural Steroid Injections: What to Expect | /blog/epidural-steroid-injection-what-to-expect |
| Back Pain Red Flags | /blog/back-pain-red-flags |
| Back Pain: Surgery vs. Injection | /blog/back-pain-surgery-vs-injection |
| Is My Back Pain Serious? | /blog/is-my-back-pain-serious |
| RFA Guide | /blog/radiofrequency-ablation-guide |
| ESI Side Effects | /blog/epidural-steroid-injection-side-effects |
| Nonsurgical Treatment for Herniated Disc | /blog/nonsurgical-treatment-herniated-disc |

### City/Geo Pages (5)
| Page | URL |
|------|-----|
| Cinco Ranch | /pain-management-cinco-ranch-tx |
| Cypress | /pain-management-cypress-tx |
| Fulshear | /pain-management-fulshear-tx |
| Richmond | /pain-management-richmond-tx |
| Sugar Land | /pain-management-sugar-land-tx |

---

## Work Log

### Month 1 (Feb 2026) — Site Build & Foundation
**Status: Complete**

- Built full website from scratch (static HTML, inline CSS, Vercel hosting)
- 32 pages at launch: homepage, about, contact, insurance, 11 condition pages, 6 treatment pages, 5 city pages, 7 blog posts, blog hub, 404
- Schema markup on all pages (MedicalCondition, MedicalProcedure, Physician, FAQPage)
- GA4 tracking installed site-wide
- Mobile responsive design with hamburger nav
- Zocdoc/One Medical inspired design system (teal + gold palette, Playfair Display + DM Sans)
- Favicons, OG tags, canonical tags, robots.txt, sitemap.xml
- 5 geo/city landing pages for local SEO
- Connected to Google Search Console, submitted sitemap

### Month 2 (Mar 2026) — Content Expansion
**Status: Complete**

Deliverables from content pack (files in `_project/archive/month-2-content-pack/`):

- [x] **3 new procedure pages** — trigger point injections, kyphoplasty, discography
  - Full body copy (~1,500 words each), MedicalProcedure + Physician + FAQPage schema, 5-6 FAQs each, CTAs, internal link maps
- [x] **2 hub/pillar pages** — /treatments and /conditions
  - Card-based layouts linking to all treatment and condition pages, MedicalBusiness + Physician schema
- [x] **2 blog posts** — "Epidural Steroid Injection Side Effects" (800/mo target) and "Nonsurgical Treatment for Herniated Disc" (200/mo target)
  - ~2,000 words each, Article + Physician + FAQPage schema, 4 FAQs each, comprehensive internal linking
- [x] **Blog hub updated** with 2 new post cards
- [x] **11 condition pages optimized** — added contextual internal links to new treatment pages, blog posts, and hub pages per optimization-specs.md
- [x] **Navigation updated site-wide** — Conditions and Treatments nav links now point to hub pages instead of homepage anchors
- [x] **Footer updated site-wide** — 3 new treatment links added (trigger point injections, kyphoplasty, discography)
- [x] **Sitemap updated** — 7 new URLs added (44 total), lastmod dates updated on all modified pages
- [x] **GSC indexing requested** for all 7 new URLs (Mar 24, 2026)

Commit: `86f5b1d` — 42 files changed, 6,465 insertions

**Client feedback round (Apr 2, 2026):**

- [x] **ESI treatment page updated** — Dr. Qureshi revised fluoroscopy description ("in office fluoroscopic guidance... proper needle placement... accurately delivers medication to your problem area") and injection frequency (limited to 3-4/year, every 3 months if needed)
- [x] **Imaging/MRI claims corrected** — Removed "MRI on-site" from homepage feature card (now "X-Ray & Ultrasound Guided Procedures"), updated imaging.html title/meta/H1/hero, clarified MRI is coordinated with local centers not performed on-site, updated insurance page
- [x] **Years of experience corrected** — Changed "10+ years" to "6+ years" on about page (meta, OG, badge, body)
- [x] **4 new Google reviews added** — Vivian S., Gene M., Nancy B., Paula B. Review count updated to 52 site-wide
- [x] **Repo organized** — Non-website files moved to `_project/` folder

Commits: `048337c` (repo org), `df5843e` (reviews), `ee0bb33` (client feedback)

**Remaining (non-code):**
- [ ] Monitor GSC indexing for 7 new URLs (check ~Apr 5-7)
- [ ] Track keyword rankings: "epidural steroid injection side effects" (800/mo) and "non surgical treatment for herniated disc" (200/mo)

### Month 3 (Apr 2026) — Local SEO & Technical Fixes
**Status: In Progress**

**SEO audit fixes (Apr 11, 2026):**
- [x] Fixed og:url www mismatch on 22 pages
- [x] Added missing og:url, og:description, geo.placename to blog posts
- [x] Added missing 6th FAQ to insurance page schema
- [x] Added FAQPage schema to 4 blog posts (back-pain-surgery-vs-injection, radiofrequency-ablation-guide, epidural-steroid-injection-what-to-expect, is-my-back-pain-serious)
- [x] Added Physician schema to ESI treatment page + 5 city pages
- [x] Removed duplicate areaServed entries on 5 city pages

Commit: `481f49a` — 40 files changed

**Local SEO schema expansion (Apr 11, 2026):**
- [x] Added MedicalBusiness + LocalBusiness schema to 21 pages (9 treatment + 11 condition + insurance) that previously had no location schema

**Local SEO action plan created:**
- [x] GBP optimization checklist with business description, categories, services, Q&A, photos
- [x] Citation building checklist (25+ directories with exact NAP)
- [x] Review acceleration strategy (target: 100+ reviews by month 6)
- [x] 8 weeks of GBP post content
- [x] Local backlink opportunity list
- See `_project/reference/local-seo-action-plan.md` for full details

**Client call prep (Apr 16, 2026):**
- [x] GBP side-by-side comparison: Dr. Qureshi vs Silky Patel, MD
- [x] Month 3 scope proposal (adds GLP-1 weight loss, PRP emphasis, 5 new priority pages)
- [x] SEO progress report for client call
- [x] Call agenda with talking points and timing
- See `_project/archive/call-prep-apr-2026/` for all 4 docs

**Month 3 scope revision (incorporating client feedback from Apr 14 email):**
- New P1 pages to build: GLP-1 Weight Loss, Lumbar ESI, Cervical ESI, Knee Injection, Shoulder Injection
- PRP therapy page rewrite + site-wide emphasis
- 2 new blog posts (GLP-1 education, PRP vs Cortisone)
- Citation building + review acceleration execution

**GSC / GA4 analysis (Apr 17, 2026):**

Reviewed GSC indexing + GA4 organic query data. Key findings:

**Indexing crisis discovered:**
- Only 18 of 55 pages indexed (44 site pages + old URLs). 37 not indexed.
- 24 pages "Discovered — currently not indexed" (Google found them but chose not to index yet)
- 9 pages returning 404 errors (old Squarespace URLs + pages from keyword plan that were never built)
- 3 pages with redirect issues
- 1 page excluded by noindex (this is 404.html — correct/expected)

**Traffic trending up (slowly):**
- Mar 1-17: 9 clicks / 352 impressions / 2.56% CTR / position 10.98
- Apr 1-17: 11 clicks / 361 impressions / 3.05% CTR / position 13.46
- Clicks +22% MoM, CTR +19% MoM
- New non-brand queries surfacing ("pain specialist near me", "pmr doctor", "dr qureshi pain management")
- Brand queries ranking positions 2-4
- 68 total web search clicks since launch
- FAQ rich results valid on 12 pages
- HTTPS: 14 valid, 0 issues

**Fixes applied (Apr 17, 2026):**
- [x] Added 9 redirects to vercel.json for 404 URLs
  - `/carpal-tunnel/hand-numbness` → `/nerve-pain/neuropathy`
  - `/failed-back-surgery/spinal-cord-stimulator` → `/treatments/spinal-cord-stimulation`
  - `/spine-compression-fractures` → `/treatments/kyphoplasty`
  - `/faq` → `/`
  - `/elbowpain` → `/sports-injuries`
  - `/physical-therapy` → `/treatments`
  - `/home` → `/`
  - `/new-dropdown` → `/`
  - `/appointments` → `/contact`
- [x] Verified noindex tag only on 404.html (correct behavior)

**GBP dashboard audit (Apr 17, 2026):**

Client shared GBP dashboard screenshots. Findings:

**What's been done on GBP:**
- 4 categories set: Pain management physician (primary), Medical clinic, Pain control clinic, Sports medicine physician
- Full business description with keyword coverage (procedures, weight loss meds, parking instructions)
- Accessibility attributes completed
- Payment attributes completed (NFC, credit, debit, not cash-only)
- Service options (Hindi, English)
- Planning: Appointment required
- 3 named services under primary category: Sports Medicine, Interventional Spine Medicine, Physical Medicine and Rehabilitation
- CLS Health affiliation visible (cls.health linked)
- Posting weekly (most recent 4 days ago)

**GBP issues still open:**
- 🚨 **Website URL points to `cls.health/locations/pain-management-cinco-ranch`, NOT `drimranqureshi.com`** — highest-impact fix, traffic from GBP is going to CLS Health's site
- No services listed under 3 of 4 categories (Medical clinic, Pain control clinic, Sports medicine physician)
- Products section is empty
- All social profiles link to CLS Health's socials, not Dr. Qureshi's own
- Opening date not set
- "From the business" section empty (separate from description)

**Client call outcomes (Apr 21, 2026):**

Call went well. Client engaged with all recommendations. Key outcomes:
- ✅ Client updated all pages to be indexed (requested indexing via GSC)
- ✅ Client switched GBP website URL from cls.health to drimranqureshi.com (biggest single fix)
- ✅ Month 3 scope confirmed: new pages, review velocity, GBP posting cadence, citations, GBP products
- ✅ We now have direct GBP access
- ✅ Client pointed us to https://silkypatelmd.com as reference for homepage FAQ section
- ✅ Approved us writing + publishing page content; he will review after it's live (faster iteration)

**Directory / citation audit (Apr 21, 2026):**

Researched current citation coverage via Google search. Findings:

**Already listed (confirmed):**
- Healthgrades ✅
- Vitals ✅ — but our schema had WRONG URL pointing to a different doctor. Fixed.
- Doximity ✅
- CLS Health ✅
- WebMD ✅ (was not in our schema — added)
- Healthline FindCare ✅ (was not in our schema — added)
- Medical News Today Connect ✅ (was not in our schema — added)
- NPI Database ✅ (automatic via NPI #1467080622)
- Zocdoc ✅ (per client)

**Not listed yet (priority to claim):**
- Yelp, RateMDs, CareDash, Sharecare, U.S. News Health, Yellow Pages, Manta, BBB, Angi, Katy Area Chamber of Commerce

**Fixes applied (Apr 21, 2026):**
- [x] Fixed Vitals sameAs URL across all 41 pages — was pointing to a different doctor (Imran Qureshi, MD, Vascular & Interventional Radiology, Chicago, IL). Now correctly points to DoctorsOfOsteopathy_Imran_Mohammed_Qureshi.html
- [x] Added WebMD, Healthline FindCare, and Medical News Today Connect URLs to sameAs schema across all 41 pages
- [x] Built homepage FAQ section with 8 FAQs (patterned after Silky Patel's structure) + FAQPage JSON-LD schema
- [x] FAQs cover: what pain management doctors do, when to see one, conditions treated, treatments offered, pain management vs surgery, choosing the right doctor, chronic pain help, referrals

**Apr 23 progress:**
- [x] GBP services across all 4 categories ✅
- [x] 8 GBP Products live ✅
- [x] GSC sitemap resubmitted, all "Discovered – not indexed" pages submitted for indexing ✅
- [x] Yelp, Manta, RateMDs claimed ✅ (12 citations now live)
- [x] GLP-1 + PRP clinical questions sent to Dr. Qureshi (async)

**Apr 23 — AI Overview / E-E-A-T retrofit (FULLY SHIPPED, all 5 sub-workstreams complete)**

Client provided ChatGPT deep research report (`_project/reference/medical_ai_overview_seo_playbook.md`) on Google AI Overview ranking for medical sites. We did a content audit (`_project/snapshots/eeat-content-audit-apr-23.md`) — site scored 5.2/10 baseline, below AI Overview eligibility threshold.

**All 5 sub-workstreams completed Apr 23 (commits `9b6e7bf` → `f4ec3a2`):**

| Sub-workstream | Status | Pages affected |
|---|---|---|
| 1. Trust pages (`/medical-disclaimer`, `/editorial-policy`) | ✅ | 2 new + footer link on all 43 pages |
| 2. "Medically reviewed by Dr. Imran Qureshi, D.O." byline | ✅ | 20 main pages |
| 3. External authority citations (Mayo, Cleveland Clinic, MedlinePlus, NIH NIAMS, NINDS) | ✅ | 20 pages, 51 inline citations |
| 4. Answer-first opening blocks (75-125 word direct query answers) | ✅ | 20 main pages |
| 5. H2 question-based refactor (clinical labels → patient questions) | ✅ | 20 pages, 71 H2s converted |

**Estimated E-E-A-T score: 5.2/10 → ~8.5/10** (above AI Overview eligibility threshold).

Comprehensive technical SEO audit also run on all 43 pages — 100% clean on titles, metas, canonicals, OG tags, robots, geo, schema, GA4, favicons. Sitemap perfectly mirrors HTML files. Zero broken internal links.

**Apr 23 — Technical SEO fixes shipped:**
- Fixed 2 broken internal links (phantom `/blog/back-pain-red-flags` removed; plural `/epidural-steroid-injections-what-to-expect` typo corrected)
- Added 2 redirects in vercel.json as safety nets for those URLs
- Trimmed 5 city page meta descriptions from 220+ chars to under 150
- Created `_project/snapshots/post-deploy-checklist-apr-23.md` for post-deploy verification

**Apr 23 — Post-deploy actions completed by client:**
- ✅ Vercel deploy verified (all green)
- ✅ Live pages spot-checked
- ✅ GSC: sitemap resubmitted
- ✅ GSC: 2 new trust pages requested for indexing
- ✅ GSC: Re-requested indexing on retrofitted pages
- ✅ Schema validated via Google Rich Results Test

**Removed from scope:**
- ~~Review acceleration system~~ (CLS Health has one)
- ~~Q&A seeding on GBP~~ (client opted out)
- ~~CareDash citation~~ (defunct directory)
- ~~LocalRank subscription~~ (May 2 — replaced with in-house DIY tool, saving $297/mo)
- ~~Katy Chamber of Commerce~~ (May 6 — verified $1,000/yr Bronze tier minimum, no free option; client decision pending; my rec: skip)

---

## ✅ May 1 Push — Month 3 Content + Internal Linking

- [x] Built `/treatments/glp-1-weight-loss` (GLP-1 weight loss treatment page using clinical answers from Dr. Qureshi)
- [x] Rewrote `/treatments/prp-therapy` with practice-specific pricing ($750/site, $1,200 two-site), single-injection protocol, exclusion criteria, >90% success rate citation
- [x] Built blog post: `/blog/glp-1-medications-for-weight-loss` (2,198 words, 8 min read, 5 FAQs, NIDDK + Cleveland Clinic citations)
- [x] Built blog post: `/blog/prp-vs-cortisone-injections` (2,154 words, 9 min read, 5 FAQs, NIH NIAMS + Cleveland Clinic citations)
- [x] Internal linking audit + 13 contextual cross-links added (no orphans, no broken links)
- [x] Built `/treatments/lumbar-epidural-injection`, `/treatments/cervical-epidural-injection`, `/treatments/shoulder-injection`
- [x] April progress report + email draft for client (`_project/snapshots/april-progress-report-2026-05-01.md`)

---

## ✅ May 2 Push — Maps Baseline + DIY Rank Tracker

- [x] Built in-house Maps grid rank tracker at `/Users/rameel/Desktop/Manual Library/Leadmill/tools/grid-rank-tracker/` — Python tool using Google Places API at $7/scan vs LocalRank's $297/mo
- [x] First baseline grid scan: 18 keywords × 81 grid points around Katy. Results in `_project/snapshots/maps-baseline-may-02.md`
- [x] April progress report finalized with real GA4 + GSC + GBP April-vs-March numbers
  - GBP calls 48 vs 40 (+20%), directions 51 vs 45 (+13%), website clicks 39 vs 36 (+8%)
  - Organic clicks 18 vs 15 (+20%), 21 new queries appearing
  - GA4 active users 83 vs 60 (+38%)
  - Indexed pages 41 vs 18 in early April (+128%)
- [x] Reports + Maps baseline pushed to imran 2 repo

---

## ✅ May 6-7 Push — Site-Wide Polish + Mid-Month Validation

This was the heaviest single-session day after April 23. **Six commits to `main`** in one block:

### Content & schema
- [x] **5 city pages differentiated** — each got 2 new H2 sections (~400 unique words/page) covering city-specific geography, demographics, and pain patterns. Eliminates duplicate-content risk (pages were ~95% identical before).
- [x] **GA4 conversion tracking shipped site-wide** — 4 events firing on 49 HTML pages: `phone_call_click`, `book_appointment_click`, `directions_click`, `form_submit`. Each event includes `page_path` for attribution.
- [x] **sameAs schema verified + expanded** — audited all 6 existing URLs via WebFetch + WebSearch. Found Healthgrades was a placeholder (`dr-imran-qureshi` returned homepage). Replaced with verified canonical (`dr-imran-qureshi-do-18z251yi70`). Added 4 new verified URLs: LinkedIn, Zocdoc, Memorial Hermann, CLS Health employer page. Schema now has **10 verified URLs** across all 49 pages (was 6 with 1 broken).
- [x] **Entity language fixes** — added "knee doctor" + "sports injury doctor" phrasing to homepage title/meta/FAQ, about page meta/body, knee-pain/arthritis answer block, and sports-injuries answer block. Targets 2 of 5 zero-coverage keywords from May 2 baseline.

### Measurement
- [x] **Mid-month grid scan** — May 7. Comparison vs May 2 baseline at `_project/snapshots/maps-mid-month-may-7.md`.
  - **8 of 13 actively-ranking keywords improved in 5 days**
  - "pain management katy tx" doubled top-10 coverage (23 → 47 grid points)
  - "pain management doctor near me" hit map pack for the first time (0 → 2 top-3 points)
  - "neck doctor katy" jumped 6 rank positions (avg 19.0 → 12.8)
  - "epidural steroid injection katy" now ranks top-10 on **81/81 grid points** (was 79)
  - 5 zero-coverage keywords still at 0% — but expected (entity fixes too fresh / authority signals still aging in)

### Status & comms
- [x] Week-of-May-5 status doc + GBP Post #4 drafts at `_project/snapshots/week-of-may-5-status.md`

**Open items still on Rameel/client:**
- [ ] Mark GA4 events as Key Events in GA4 admin (24–48 hrs after first events appear)
- [ ] Publish GBP Post #4 (drafts ready in week-of-may-5-status.md)
- [ ] Claim Sharecare, Doctor.com, Wellness.com (free directories, ~15 min each)
- [ ] Yellow Pages re-attempt
- [ ] Memorial Hermann directory has stale Webster TX address — Dr. Qureshi should request MHMD update

**Open items for end-of-month (May 30):**
- [ ] End-of-May full Maps grid scan + comparison vs May 2 baseline (will become Month 3 client report data)
- [ ] Month 3 wrap-up report (start drafting May 12)
- [ ] Verify the 4 zero-coverage keywords have moved off 0% by May 30
- [ ] Trim remaining 27 meta descriptions over 160 chars (low priority, cosmetic)

---

## 📚 Lessons Learned (Apr–May 2026)

Durable principles surfaced from the engagement so far. Cross-reference these when planning future client work:

1. **The "GBP optimization takes 4–8 weeks" rule is real, not hopium.** May 2 → May 7 mid-month scan validated it: 5 days after the April retrofit shipped, 8 of 13 actively-ranking keywords moved up. Don't promise faster than 4–8 weeks for Maps movement.

2. **0%-coverage keywords are not all the same problem.** Always diagnose first:
   - If the phrase IS already on the site (e.g. 5+ mentions), it's an **authority signal** issue → add citations + sameAs + reviews. Wait for aging.
   - If the phrase is **NOT on the site**, it's an entity-language issue → add the literal phrase to title, meta, H2, and answer block. Wait 7–14 days.
   - Generic phrases ("muscle pain") → skip, not worth chasing.

3. **Average position is misleading.** Going from avg 10.98 → 13.46 looks like decline, but it's usually "more keywords ranking at deeper positions" dragging the average. Always pair avg position with **unique-queries-appearing** (better) or **top-10-coverage** (best) before reporting movement to client.

4. **Authority lifts the entity broadly.** When pain-management-family keywords moved May 2→7, they ALL moved together (5 different "pain management katy" variations, avg ranks 9–12 → 7–10). Authority signals don't help one query at a time.

5. **Always verify URLs in sameAs before adding to schema.** Healthgrades placeholder URL returned homepage for 2+ weeks before catching it. Pattern-matching slugs (e.g. `dr-imran-qureshi`) are not enough — WebFetch every URL once before adding.

6. **City pages are duplicate-content traps.** ~95% of body copy was identical across our 5 city pages — auditors miss this because each page LOOKS unique (different city in title/H1). Always diff `cinco-ranch.html` against `cypress.html` and require 300+ unique words per page.

7. **Local SEO heatmaps need verification, not the API output as-is.** The Places API gives "directionally correct" rankings but doesn't apply user personalization (search history, time of day, device). Useful for trend tracking; not pixel-perfect to what a patient sees on their phone.

8. **Run long Python scripts with `python -u`.** Default stdout buffering hides progress and can mask hangs. The `scan.py` first attempt hung at 35 minutes; second attempt with `-u` ran fine in 11 min.

9. **Check duplicate-vs-stale data in directories.** Memorial Hermann had Dr. Qureshi listed at his old residency address (Webster TX, 500 N Kobayashi) — NPI was correct, address was 4+ years stale. Always check directory listings against current practice address; flag updates back to client.

10. **GA4 loaded ≠ GA4 measuring.** GA4 was on every page from day 1, but with **zero key events configured**. The tag fired pageviews but couldn't tell us anything about conversions. Whenever you adopt GA4 on a new client, audit the events configured BEFORE assuming you can measure ROI.

11. **Building tools beats subscribing.** LocalRank: $297/mo for one feature (scanner) we used. DIY equivalent: $0/mo (within Google's $200 free credit) + ~6 hrs to build. At Leadmill's scale (4 clients), the math always favors building.

12. **The "right" sameAs count is 8–12, all verified.** Less = weak entity signal. More = noise. Each URL should be a profile that materially mentions the practice — not generic specialty directories with auto-populated stub pages.

13. **Track everything in `_project/` and exclude from indexing.** robots.txt `Disallow: /_project/` means we can keep working notes in the same git repo without worrying about Google indexing them. Standardize this on every client.

14. **Most "broken" or "missing" SEO problems are actually consistency problems.** All 49 pages had the same broken Healthgrades URL. All 5 city pages had the same duplicate copy. Site-wide fixes (one regex script over all files) beats per-page editing every time.

15. **Average position is a vanity metric for the dashboard. Top-10 coverage on the geo grid is the real KPI.** This drove the May 2 baseline doc and the comparison framework — stick with it.

---

## Headline metric for Month 3 client report (compare May vs April baseline):
- April baseline: 48 GBP calls, 51 directions, 39 site clicks, 138 profile interactions
- May target: 65+ calls, 65+ directions, 50+ site clicks, 175+ interactions
- May leading indicator (mid-month): Maps grid coverage on "pain management katy" family — top-10 went from 56-60 grid points (May 2) to 75-77 (May 7), with no top-3 yet. End-of-month target: 5+ top-3 grid points across at least one "pain management" variant.

---

## Technical Notes

- **Stack:** Static HTML + inline CSS. No build tools, no templating. Each page is self-contained.
- **Fonts:** Playfair Display (headings) + DM Sans (body) via Google Fonts
- **CSS:** Inline in every file. Two `<style>` blocks — global styles + inner page styles.
- **Vercel config:** `cleanUrls: true` strips .html extensions. `trailingSlash: false`.
- **Templates:** Use `treatments/nerve-blocks.html` for new treatment pages. Use `blog/what-is-radiofrequency-ablation.html` for new blog posts.
- **Schema pattern:** JSON-LD in `<head>`. Treatment pages get MedicalProcedure + Physician + FAQPage. Blog posts get Article + Physician + FAQPage. Hub pages get MedicalBusiness + Physician.
- **Header/footer** are duplicated in every file (no includes/partials). Nav, footer, and mobile nav must be updated in all files when changed.

---

## Project Files Structure
All non-website working files live in `_project/`. Reorganized Apr 29, 2026 for clarity:

```
_project/
├── PROJECT-STATUS.md                   ← this file (active)
├── month-3-detailed-execution-plan.md  ← active sprint plan
├── citations-tracker.md                ← active, updated as we claim listings
│
├── reference/                          ← evergreen reference docs
│   ├── citation-library.md             ← verified medical authority URLs
│   ├── local-seo-action-plan.md        ← GBP, citations, reviews strategy
│   ├── medical_ai_overview_seo_playbook.md  ← E-E-A-T playbook
│   ├── keyword-research/               ← 4 CSVs: page plan, keywords, competitors
│   └── doctor-photos/                  ← Dr. Qureshi photos
│
├── snapshots/                          ← point-in-time docs
│   ├── baselines-apr-22.md             ← April GBP/GA4 baseline metrics
│   ├── eeat-content-audit-apr-23.md    ← E-E-A-T audit (5.2/10 → 8.5/10)
│   └── post-deploy-checklist-apr-23.md ← Apr 23 push verification
│
└── archive/                            ← completed work, kept for reference
    ├── call-prep-apr-2026/             ← Apr 21 client call materials
    └── month-2-content-pack/           ← Mar 2026 content pack source markdowns
```

The `_project/` folder is excluded from search engine indexing via `robots.txt` (`Disallow: /_project/`).

Keyword research files in `_project/reference/keyword-research/`:
- `Page Build Plan-Table 1.csv` — full page-level keyword targeting plan
- `Keyword Priority Matrix-Table 1.csv`
- `Competitor Analysis-Table 1.csv`
- `Negative Keywords-Table 1.csv`
