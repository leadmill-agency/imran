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

## Current Site Inventory (42 pages)

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

### Blog Posts (8)
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

Deliverables from content pack (files in `_project/content-packs/month-2/`):

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

### Month 3 (Apr 2026) — Planned
*Pending — content pack not yet delivered*

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
All non-website working files live in `_project/`:
```
_project/
  PROJECT-STATUS.md          ← this file
  content-packs/
    month-2/                 ← Mar 2026 content pack (markdowns, specs)
  keyword-research/          ← CSVs: page build plan, keyword matrix, competitor analysis
  reference/
    doctor-photos/           ← Dr. Qureshi headshots and office photos
    old-site-snapshot/       ← saved copy of original Squarespace site (gitignored)
```

Keyword research files in `_project/keyword-research/`:
- `Page Build Plan-Table 1.csv` — full page-level keyword targeting plan
- `Keyword Priority Matrix-Table 1.csv`
- `Competitor Analysis-Table 1.csv`
- `Negative Keywords-Table 1.csv`
