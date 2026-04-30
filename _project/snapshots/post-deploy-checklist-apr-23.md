# Post-Deploy Indexing & Verification Checklist
*After Apr 23 push of E-E-A-T retrofit + technical fixes*

## What just shipped (8 commits today)

| Commit | What it did |
|--------|-------------|
| `9b6e7bf` | Built `/medical-disclaimer` + `/editorial-policy`; added "Medically reviewed by" byline to 20 pages |
| `9841b52` | Added 51 external authority citations to 20 pages |
| `1e55a65` | Added "Quick answer" first-block to 20 pages |
| `9ad84ee` | H2 question-based refactor on top 5 pages (22 H2s) |
| `846fa76` | H2 refactor on remaining 15 pages (49 H2s) |
| (next push) | Fixed broken internal links + trimmed 5 city page meta descriptions + 2 new redirects |

**Total today:** 71 H2 conversions, 51 citations, 20 answer blocks, 20 bylines, 2 new trust pages, 2 new redirects, 5 trimmed metas.

---

## Verify Vercel Deploy (do first)

1. [ ] Open https://vercel.com → drimranqureshi project → Deployments tab
2. [ ] Confirm latest commit (`846fa76` and the upcoming fix commit) shows "Ready" / green
3. [ ] If any deployments show "Error", click them and review the build log
4. [ ] Spot-check 3 pages live in browser:
   - https://www.drimranqureshi.com/medical-disclaimer (should render with red emergency box)
   - https://www.drimranqureshi.com/editorial-policy (should render policy sections)
   - https://www.drimranqureshi.com/low-back-pain (should show byline + "Quick answer" block + question-based H2s)

## GSC Actions (Google Search Console)

### 1. Resubmit sitemap
- [ ] Go to GSC → drimranqureshi.com → Sitemaps
- [ ] Click "Submit" again on `sitemap.xml` to trigger a fresh crawl
- [ ] Confirm sitemap shows "Success" with 43 URLs detected

### 2. Submit the 2 new trust pages for indexing
- [ ] URL Inspection: `https://www.drimranqureshi.com/medical-disclaimer` → click "Request Indexing"
- [ ] URL Inspection: `https://www.drimranqureshi.com/editorial-policy` → click "Request Indexing"

### 3. Validate fix on the 404 report
- [ ] Pages → Not indexed → Not found (404)
- [ ] If still showing the 9 old 404s plus the 2 new redirects, click "Validate Fix" again
- [ ] The redirects should clear these from the report within 1-2 weeks

### 4. Re-request indexing on retrofitted pages (high-impact)
The 20 main pages have been substantially updated (new answer blocks, citations, bylines, refactored H2s). Worth requesting fresh indexing on the highest-priority ones:

- [ ] /low-back-pain
- [ ] /bulging/herniated-discs
- [ ] /nerve-pain/neuropathy
- [ ] /neck-pain-and-arm-numbness
- [ ] /knee-pain/arthritis
- [ ] /hip-pain/arthritis
- [ ] /shoulder-injuries/pain
- [ ] /sacroiliac-si-joint-pain
- [ ] /sports-injuries
- [ ] /regenerative-medicine
- [ ] /imaging
- [ ] /treatments/epidural-steroid-injections
- [ ] /treatments/radiofrequency-ablation
- [ ] /treatments/nerve-blocks
- [ ] /treatments/prp-therapy
- [ ] /treatments/spinal-cord-stimulation
- [ ] /treatments/joint-injections
- [ ] /treatments/trigger-point-injections
- [ ] /treatments/kyphoplasty
- [ ] /treatments/discography

GSC limits to ~10-15 indexing requests per day per property. Spread these over 2 days.

### 5. Check Coverage report 7-10 days from now
- [ ] Indexed pages should be growing toward 43 (was 18 last check)
- [ ] "Discovered — currently not indexed" count should be shrinking
- [ ] Note: not all pages will get indexed even with requests; Google decides

## Schema Validation

### Use Google's Rich Results Test on these high-priority pages:

1. [ ] https://search.google.com/test/rich-results — paste in:
   - https://www.drimranqureshi.com/ (homepage — MedicalBusiness + Physician + FAQPage)
   - https://www.drimranqureshi.com/low-back-pain (MedicalCondition + FAQPage + MedicalBusiness)
   - https://www.drimranqureshi.com/treatments/epidural-steroid-injections (MedicalProcedure + FAQPage + MedicalBusiness)
   - https://www.drimranqureshi.com/medical-disclaimer (WebPage + Physician)
   - https://www.drimranqureshi.com/blog/nonsurgical-treatment-herniated-disc (Article + FAQPage)

2. [ ] All should show "Page is eligible for rich results" with no critical errors. Warnings are OK.

## What Was Verified Clean

✅ **All 43 indexable pages** have:
- Title tag (unique, present)
- Meta description (now all under 200 chars; 5 city pages trimmed to <150)
- Canonical URL (uses www, self-referencing)
- Open Graph tags complete
- Robots meta = "index, follow"
- Geo meta tags (US-TX / Katy, Texas)
- Inline CSS design system
- GA4 tracking (G-SHWLFXVMMF)
- Favicon links

✅ **Schema coverage:**
- All 9 treatment pages: MedicalProcedure + Physician + FAQPage + MedicalBusiness
- All 11 condition pages: MedicalCondition + Physician + FAQPage + MedicalBusiness
- All 9 blog posts: Article + Physician (FAQPage where applicable)
- 2 hub pages: MedicalBusiness + Physician
- 2 trust pages: WebPage + Physician + MedicalBusiness
- 5 city pages: MedicalBusiness + LocalBusiness + Physician + areaServed
- About: Physician with hasCredential array
- Insurance: FAQPage + Physician + MedicalBusiness

✅ **Internal links:** 0 broken (49 unique internal href targets, all resolve)

✅ **Sitemap parity:** 43 URLs in sitemap = 43 indexable HTML files

✅ **404 handling:** 11 redirects in vercel.json (covering old Squarespace URLs + planned-but-not-built pages + the 2 new fixes today)

✅ **robots.txt:** Allows all, points to sitemap

## Remaining Minor Issues (not urgent)

- **27 pages have meta descriptions 161-194 chars** — slightly over Google's display limit. Will be truncated on desktop SERPs but won't hurt rankings. Worth a separate trim pass when there's time.
- **32 pages have title tags 70-98 chars** — slightly over the recommended 60-65. Won't hurt rankings, just visual truncation on some devices.
- **404.html missing OG tags** — minor, only matters if a 404 URL gets shared on social.

These can be addressed in a future "polish" pass — none block indexing or hurt rankings.

## Schedule for Re-checking

| Date | Check |
|------|-------|
| **Apr 24-25** | Verify Vercel deploy clean, request indexing on 10 priority URLs |
| **Apr 26-27** | Request indexing on remaining 10 URLs |
| **May 1** | Check GSC indexed count (should be growing) |
| **May 7** | Run fresh LocalRank scan to compare to Apr 9 baseline |
| **May 14** | Mid-Month-3 GSC + GA4 pull for client report prep |
| **May 20** | Full Month 3 results report |
