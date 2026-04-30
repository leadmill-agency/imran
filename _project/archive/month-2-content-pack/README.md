# Month 2 Content Pack — Dr. Imran Qureshi

## What's In Here

### /procedure-pages/ (3 new pages)
- **trigger-point-injections.md** — full page content, SEO metadata, FAQ schema, CTAs
- **kyphoplasty.md** — full page content, SEO metadata, FAQ schema, CTAs
- **discography.md** — full page content, SEO metadata, FAQ schema, CTAs

Note: The 5-month plan called for 5 procedure pages (nerve blocks, trigger point injections, PRP, kyphoplasty, discography) but nerve blocks and PRP already exist on the site. Only 3 new pages needed.

### /blog-posts/ (2 new posts)
- **epidural-steroid-injection-side-effects.md** — targets "epidural steroid injection side effects" (800/mo, KD 49)
- **nonsurgical-treatment-herniated-disc.md** — targets "non surgical treatment for herniated disc" (200/mo, KD 12)

### /hub-pages/ (2 new pages)
- **treatments-hub.md** — pillar page linking to ALL treatment pages (URL: /treatments)
- **conditions-hub.md** — pillar page linking to ALL condition pages (URL: /conditions)

### /condition-optimization/ (11 pages)
- **optimization-specs.md** — per-page specs for internal linking updates across all 11 condition pages. Covers which new treatment links, blog links, and hub links to add to each page.

## Implementation Order
1. Build the 3 new procedure pages
2. Build the 2 hub pages
3. Build the 2 blog posts
4. Run the condition page optimization pass (add internal links per specs)
5. Update sitemap.xml with all new URLs
6. Push to GitHub, confirm Vercel deploys, request indexing in GSC

## URL Mapping
| Content | URL |
|---------|-----|
| Trigger Point Injections | /treatments/trigger-point-injections |
| Kyphoplasty | /treatments/kyphoplasty |
| Discography | /treatments/discography |
| Treatments Hub | /treatments (index) |
| Conditions Hub | /conditions |
| Blog: ESI Side Effects | /blog/epidural-steroid-injection-side-effects |
| Blog: Nonsurgical Herniated Disc | /blog/nonsurgical-treatment-herniated-disc |
