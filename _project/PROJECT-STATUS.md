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

**Remaining (next focus):**
- [ ] Client to send missing GBP photos
- [ ] Client to provide GLP-1 + PRP async clinical answers
- [ ] Build citations on remaining 6-8 directories (Sharecare, US News, Doctor.com, Castle Connolly, Wellness.com, BBB, Angi, Katy Chamber)
- [ ] Yellow Pages retry (couldn't claim Apr 23)
- [ ] Differentiate city page content (need client input for local testimonials)
- [ ] Update sameAs schema with new directory listings
- [ ] Re-run LocalRank scan in 4-6 weeks (target: ~May 7)
- [ ] Month 3 priority pages: GLP-1, Lumbar ESI, Cervical ESI, Knee Injection, Shoulder Injection (using new E-E-A-T template)
- [ ] Month 3 blog posts: "GLP-1 Medications" + "PRP vs Cortisone" (using new template)
- [ ] PRP page rewrite + site-wide emphasis
- [ ] GA4 conversion tracking setup (currently 0 key events — critical for Month 3 measurement)
- [ ] Trim remaining 27 meta descriptions over 160 chars (low priority, cosmetic)
- [ ] Monitor GSC indexing rate over next 1-2 weeks

**Headline metric for Month 3 client report (compare May vs April baseline):**
- April baseline: 42 GBP calls, 45 directions, 31 site clicks, 118 profile interactions
- May target: 60+ calls, 65+ directions, 50+ site clicks, 175+ interactions

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
