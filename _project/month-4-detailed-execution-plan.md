# Month 4 (Jun 2026) — Detailed Day-by-Day Execution Plan

**Scope:** May 26 → Jun 30, 2026 (Month 3 wrap + Month 4 full)
**Client posture:** Async (per Dr. Qureshi's May 19 preference)
**Total time commitment:** ~30–45 min/day weekdays, weekends mostly off
**Primary focus:** Drive more SEO + AI Overview (AIO) results

---

## Strategic priorities for Month 4

In priority order:

1. **Review velocity** — biggest unlock for breaking into the "pain management katy" 3-pack
2. **AI Overview citation expansion** — make Dr. Q's site one of the cited sources in Google's AI answers for medical queries
3. **2 new procedure pages** — Knee Gel Injections + Genicular Nerve Block
4. **Conversion optimization** — testimonials + CTA test (GA4 Key Events now have a month of data to analyze)
5. **Bing/AEO** — submit to Bing Webmaster Tools so ChatGPT/Perplexity can index the site
6. **PAA mining** — convert "People Also Ask" boxes into on-page FAQs

---

## Phase 1: Wrap Month 3 (May 26–30)

### Mon May 26 — Reset day (today)

- [x] **Budget alert set on GCP** ($30/mo cap)
- [x] **Photos from Dr. Qureshi located** at `_project/reference/Imran Photos May 26/`
- [x] **Attribution note added to PROJECT-STATUS** (neighborhood group share documented)
- [ ] **Convert the 1 HEIC photo to JPG** (Mac Preview → File → Export → JPEG). Save back to the same folder.
- [ ] **Review the 8 photos.** Note which are: exterior office / interior office / Dr. Q at work / equipment / team. Tag mentally — we'll caption them tomorrow.

**Time: 15 min**

---

### Tue May 27 — Upload photos + run final May scan

**Morning (45 min):**
- [ ] **Upload all 8 photos to GBP:**
  1. Go to GBP dashboard → Photos
  2. For each photo: click "Add photo" → upload → categorize (Exterior, Interior, Team, At work, Identity)
  3. Add a 1-line caption per photo (e.g., "Dr. Imran Qureshi at the Cinco Ranch office," "Office exterior on Cinco Ranch Blvd")
  4. Photos should now be 18+ total (up from ~10)

**Afternoon (15 min active, ~12 min scan wait):**
- [ ] **Run final May DIY scan:**
  ```
  cd /Users/rameel/Desktop/Manual\ Library/Leadmill/tools/grid-rank-tracker
  python3 -u scan.py imran
  ```
  Will take ~12 min. Cost: ~$7. This is your end-of-May data point for the final report.

**Time: 60 min total**

---

### Wed May 28 — Pull final May numbers

**One sitting (30 min):**

- [ ] **GBP screenshots** for the full month of May (May 2026 only):
  - Overview tab
  - Calls tab
  - Directions tab
  - Website clicks tab
- [ ] **GSC screenshots** — last 30 days (May 1–31 ideally):
  - Main Performance view (clicks/impressions/CTR/position)
  - Queries tab (top 30)
- [ ] **GA4 screenshot** — Last 28 days:
  - Reports → Acquisition → Traffic acquisition (the same view as last time)
  - Also: Reports → Engagement → Conversions (now that Key Events are live ~10 days)
- [ ] **Indexed pages screenshot** from GSC → Indexing → Pages
- [ ] **Drop all screenshots in chat** — I'll do the comparison + write the final May numbers

**Time: 30 min**

---

### Thu May 29 — Final Month 3 report sent

- [ ] **Wait for me to regenerate the final Month 3 PDF** with end-of-May actuals + the External Attribution section
- [ ] **Review the PDF** (10 min)
- [ ] **Email Dr. Qureshi:**
  - Subject: `Month 3 final results — May numbers + Month 4 kickoff`
  - Attach the updated PDF
  - 3-line note: "Final May numbers in. SEO contribution explained alongside the neighborhood share you mentioned. Starting Month 4 with X/Y/Z focus. Let me know if any thoughts."

**Time: 20 min**

---

### Fri May 30 — Wrap

- [ ] **Update PROJECT-STATUS** with final Month 3 numbers + lessons (I'll do this; just confirm I have the data)
- [ ] **Tag git commit** so we have a clean "end of Month 3" snapshot to reference later

**Time: 5 min (Rameel) — most done by me**

---

### Sat May 31 + Sun Jun 1 — Off

Hard rest. Month 4 begins Monday.

---

## Phase 2: Month 4 Week 1 (Jun 2–6) — AIO baseline + first new procedure page

### Mon Jun 2 — AI Overview baseline check

**The single highest-leverage AIO activity:** manually search 15 target queries on Google, screenshot the AI Overview responses, document which sources are cited. This becomes your AIO baseline. Without it, we can't measure AIO progress.

**Step-by-step (60 min):**

1. **Open a fresh incognito Chrome window** (so personalization doesn't skew results). Set location to Katy, TX if Google asks.
2. **For each of these 15 queries, do the following:**
   - Type the query, search
   - If an AI Overview appears at the top: screenshot it (full panel)
   - Note: did Dr. Qureshi's site appear in the cited sources? Yes/No.
   - If yes: which sentence is it cited for?
   - If no: which sites ARE cited? (Mayo, Cleveland Clinic, Healthline, WebMD, etc.)
3. **Save screenshots** to `_project/snapshots/aio-baseline-jun-2/`

**Target query list:**
1. what is an epidural steroid injection
2. epidural steroid injection side effects
3. how long does epidural steroid injection last
4. is epidural steroid injection safe
5. what is radiofrequency ablation
6. how long does radiofrequency ablation last
7. what is PRP therapy
8. is PRP therapy effective for knee arthritis
9. PRP vs cortisone injections
10. how to treat sciatica
11. what causes low back pain
12. when should I see a pain management doctor
13. how do spinal injections compare to surgery
14. peripheral neuropathy treatment
15. cervical epidural injection what to expect

**Output:** A document at `_project/snapshots/aio-baseline-jun-2.md` with:
- Which queries trigger AIO (% of total)
- Which queries cite drimranqureshi.com (current baseline = probably 0)
- For each query that doesn't cite us: what does cite, and what's structurally different about the cited content

**Time: 60 min**

---

### Tue Jun 3 — AIO content priorities

**Analyze what you found yesterday. Draft response:**

- [ ] **Pick the 5 highest-priority queries to target** (highest combination of: high impressions in GSC + Dr. Q has matching content + AIO is currently citing a generic source)
- [ ] **For each, identify the structural fix:**
  - Is our answer-first block in the first 100 words? Direct answer in 1–2 sentences?
  - Do we have FAQPage schema? Does it include the exact question Google asks?
  - Are our H2s in question form (matching the way patients/AI Overview phrase the question)?
- [ ] **Save findings to `_project/snapshots/aio-action-list-jun-3.md`**

This is the playbook for what we'll fix throughout Month 4.

**Time: 45 min**

---

### Wed Jun 4 — Start knee gel injection page

The new procedure page sprint begins. Knee Hyaluronic Acid (Gel) Injections is the target — it's an underserved keyword with clear buyer intent, and we already have related infrastructure (joint-injections, knee-pain/arthritis pages).

**Side note:** ask Dr. Qureshi async at the start of the day:
- What's the typical hyaluronic acid (gel) injection protocol? (single shot or series? branded? Synvisc / Euflexxa / Supartz?)
- What's the cash-pay price?
- Typical patient profile?
- Expected duration of relief?

While waiting for his answer:

- [ ] **Draft page outline using the template at `treatments/joint-injections.html`** as base
- [ ] **Sections to include** (matches our AI-Overview-eligible template):
  - Quick answer block (75–125 words)
  - "What is hyaluronic acid (gel) injection for knee arthritis?"
  - "Who is a good candidate?"
  - "How is the procedure done?"
  - "What's the recovery and outcomes?"
  - "How does it compare to PRP and cortisone?"
  - 5 FAQs with FAQPage schema
  - 3+ external authority citations (NIAMS, Cleveland Clinic, AAOS)

**Time: 60 min (drafting only; ship Friday)**

---

### Thu Jun 5 — Continue knee gel injection page

**Apply yesterday's clinical answers (if Dr. Q replied), or use placeholders for cost/protocol that he can correct after publish:**

- [ ] **Finish the page**
- [ ] **Add schema:** MedicalProcedure, Physician, FAQPage
- [ ] **Internal linking:**
  - From `/knee-pain/arthritis` → link to new page (replace generic "joint injections" mention)
  - From `/treatments/joint-injections` → cross-link to gel injection page
  - From `/treatments/prp-therapy` → mention as comparison option in PRP vs other treatments section
  - From homepage → add to "Treatments" list
  - From `/treatments` hub → add card

**Time: 75 min**

---

### Fri Jun 6 — Ship knee gel injection page + GBP post

- [ ] **Final review:**
  - Run through the post-deploy checklist at `_project/snapshots/post-deploy-checklist-apr-23.md`
  - Validate JSON-LD at https://search.google.com/test/rich-results
- [ ] **Deploy** (git commit + push; Vercel auto-deploys)
- [ ] **Add to sitemap.xml** with lastmod date
- [ ] **Submit URL to GSC** for indexing
- [ ] **Publish GBP Post (Week 1):**
  ```
  🦵 Knee pain from arthritis? Hyaluronic acid (gel) injections offer up to 6 months of relief
  for many patients — no surgery, performed in-office under ultrasound guidance.
  Same-week appointments available. (281) 982-2144.
  ```
  CTA: "Learn more" → link to new knee gel injection page
  Use one of Dr. Q's recent photos (interior/at-work)

**Time: 45 min**

---

### Sat Jun 7 + Sun Jun 8 — Off

---

## Phase 3: Month 4 Week 2 (Jun 9–15) — Second new page + review push

### Mon Jun 9 — Genicular nerve block page draft

The second procedure page. Genicular nerve blocks bridge the gap between RFA and PRP — and explicitly target `knee doctor near me` and `knee pain doctor katy` (two of the keywords we want to recover).

**Step-by-step (75 min):**

- [ ] **Async ask Dr. Qureshi:** genicular nerve block protocol, typical pricing, patient candidates
- [ ] **Draft the page** using same template structure as knee gel injection
- [ ] **Cross-link with `/treatments/radiofrequency-ablation`** (RFA is the long-term version of the nerve block)

**Time: 75 min**

---

### Tue Jun 10 — Ship genicular nerve block page

- [ ] **Final review + deploy**
- [ ] **Add to sitemap**
- [ ] **Submit URL for indexing in GSC**
- [ ] **Internal linking** (same pattern as last week)

**Time: 30 min**

---

### Wed Jun 11 — People Also Ask (PAA) audit

**The single highest-leverage on-page SEO activity we haven't yet done.**

**Step-by-step (60 min):**

1. **Open Chrome incognito, location Katy TX**
2. **Search each of the top 10 organic queries from May's GSC report:**
   - imran qureshi do, dr imran qureshi, regenerative therapy katy tx, peripheral neuropathy treatment in katy, kyphoplasty houston, shoulder pain treatment in katy, knee pain relief in katy, etc.
3. **For each search, find the "People also ask" box** — typically right below the first 2–3 organic results
4. **Click each PAA question to expand it** — when you do, Google loads more PAA questions
5. **Document the PAA questions** in `_project/snapshots/paa-audit-jun-11.md`
6. **For each PAA question, identify which page on Dr. Q's site should answer it**

**Output:** A table mapping PAA questions to pages that need new H2s/FAQs.

**Time: 60 min**

---

### Thu Jun 12 — Add PAA-derived FAQs to top 5 pages

Based on yesterday's audit:

- [ ] **For each of the 5 highest-traffic pages, add 2–3 new FAQs** that match PAA questions
- [ ] **Update the page's FAQPage schema** to include the new FAQs
- [ ] **Deploy**

Pages to prioritize (highest traffic from May GSC):
1. `/treatments/epidural-steroid-injections`
2. `/treatments/radiofrequency-ablation`
3. `/treatments/prp-therapy`
4. `/low-back-pain`
5. `/knee-pain/arthritis`

**Time: 75 min**

---

### Fri Jun 13 — Review velocity push

The single highest-leverage action for breaking into the local 3-pack on "pain management katy."

- [ ] **Create a 1-click review template** (15 min):
  - Get the Google review URL for Dr. Qureshi's GBP (format: `https://search.google.com/local/writereview?placeid=ChIJHT05uVshQYYRFM2xWG_wWps`)
  - Generate a QR code linking to it (free at qr-code-generator.com)
  - Generate a short URL via bit.ly: e.g., `bit.ly/review-dr-qureshi`
- [ ] **Print 50 copies of a small "Review us" card** for the front desk:
  - Front: QR code + "Loved your visit? Leave us a review!"
  - Back: short URL + thank you message
  - Have Dr. Q approve before printing — async email with the design
- [ ] **GBP Post (Week 2):**
  ```
  Thank you to the 58+ patients who've shared their experience with us on Google Reviews.
  Your feedback helps other patients find the right care. If we've helped you, a quick
  review would mean the world.
  ```
  Add a link to the review URL.

**Time: 45 min**

---

### Sat Jun 14 — Run bi-weekly DIY scan

**12 min wait, ~$7 cost.** This is the mid-month measurement against the May 30 final scan.

```
cd /Users/rameel/Desktop/Manual\ Library/Leadmill/tools/grid-rank-tracker
python3 -u scan.py imran
```

While it runs:
- [ ] Send the scan results to me in chat when complete — I'll do the comparison

**Time: 15 min Rameel time**

---

### Sun Jun 15 — Off

---

## Phase 4: Month 4 Week 3 (Jun 16–22) — Conversion + Bing/AEO

### Mon Jun 16 — Submit to Bing Webmaster Tools

**Why this matters for AEO (Answer Engine Optimization):** ChatGPT, Perplexity, and Microsoft Copilot all use Bing search results to ground their answers. Without being in Bing's index, Dr. Q is invisible to those LLMs even when patients ask them about pain management.

**Step-by-step (30 min):**

1. **Go to https://www.bing.com/webmasters** — sign in with the same Google account (Bing accepts Google sign-in)
2. **Add the site:** drimranqureshi.com
3. **Verify ownership:** Bing accepts a Google Search Console verification (1-click) — pick that option
4. **Submit the sitemap:** https://www.drimranqureshi.com/sitemap.xml
5. **In Bing Webmaster Tools, go to URL Inspection** and request indexing on the 5 most important pages:
   - `/`
   - `/about`
   - `/treatments/epidural-steroid-injections`
   - `/treatments/radiofrequency-ablation`
   - `/treatments/prp-therapy`
6. **Wait 1–2 weeks for Bing to crawl** — recheck Jun 30

**Time: 30 min**

---

### Tue Jun 17 — GA4 conversion data analysis

GA4 Key Events have been live since May 18 — by Jun 17, that's a full month of conversion data.

- [ ] **GA4 → Reports → Engagement → Conversions** — note the daily conversion count by event:
  - `phone_call_click` (the most important)
  - `book_appointment_click`
  - `form_submit`
- [ ] **GA4 → Reports → Acquisition → Traffic acquisition** — sort by Conversions descending. Identify:
  - Which traffic source converts best (organic vs direct vs referral)?
  - What's the conversion rate?
- [ ] **GA4 → Reports → Engagement → Landing page** — which landing pages drive the most conversions?
- [ ] **Document findings** in `_project/snapshots/ga4-conversion-analysis-jun-17.md`

This is the first time we can measure actual conversion behavior, not just traffic.

**Time: 45 min**

---

### Wed Jun 18 — Testimonial blocks (Page 1: PRP)

Based on the May metrics, PRP is a high-value page that needs more conversion signals.

- [ ] **Ask Dr. Qureshi async** for 2–3 patient testimonials specific to PRP therapy. Suggest he pull from existing Google reviews that mention PRP.
- [ ] **While waiting, design a testimonial block** (HTML + CSS — should match the existing site design):
  - Patient first name + last initial
  - 2–3 sentence quote
  - Condition treated
  - Date (optional)
- [ ] **Add to `/treatments/prp-therapy`** below the existing "How effective is PRP?" section

**Time: 60 min**

---

### Thu Jun 19 — Testimonial blocks (Pages 2 + 3)

Repeat the testimonial block pattern on:
- [ ] `/treatments/epidural-steroid-injections`
- [ ] `/treatments/radiofrequency-ablation`

Use additional testimonials Dr. Q provides, or pull from public Google reviews that mention these procedures (with patient first-name-only attribution).

**Time: 60 min**

---

### Fri Jun 20 — GBP post + mid-month internal status

- [ ] **GBP Post (Week 3):**
  ```
  Genicular nerve blocks — a same-day procedure that can provide 6+ months of knee pain relief
  for patients who aren't yet ready for knee replacement. Image-guided, in-office.
  ```
  CTA: "Learn more" → /treatments/genicular-nerve-block (or whatever URL we used)
- [ ] **Write an internal mid-month status note** (no client email — internal only):
  - What's shipped Jun 1–20
  - What's pending
  - Are the new pages indexing? Showing in search?
  - Are conversion events tracking?

**Time: 45 min**

---

### Sat Jun 21 + Sun Jun 22 — Off

---

## Phase 5: Month 4 Week 4 (Jun 23–29) — A/B test + AIO recheck

### Mon Jun 23 — Homepage CTA copy test

Not a true A/B test (we don't have the traffic for statistical significance) — but a copy test on the homepage hero CTA. Try a different angle for 1 week and see if click-through to phone/book changes.

**Current homepage hero CTA:**
- Primary: "📞 Call (281) 982-2144"
- Secondary: "Book a Consultation ›"

**Test variations to try (pick one for this week):**
- Option A: Lead with availability: "Same-Week Appointments Available — Call (281) 982-2144"
- Option B: Lead with offer: "Free Insurance Verification — Call (281) 982-2144"
- Option C: Lead with reassurance: "Most Insurance Accepted — Same-Week Care — (281) 982-2144"

**Step-by-step:**
- [ ] Pick a variant (recommend A — directly addresses the biggest patient objection: "Can I get in soon?")
- [ ] Update homepage hero CTA copy
- [ ] Deploy
- [ ] Track GA4 `phone_call_click` events for the week to compare vs prior weeks

**Time: 30 min**

---

### Tue Jun 24 — AIO recheck (vs Jun 2 baseline)

**Same 15 queries as Jun 2. Same incognito setup.**

- [ ] **For each query, screenshot the AI Overview** as it appears today
- [ ] **Compare against the Jun 2 baseline:**
  - Did Dr. Qureshi's site get cited on any new queries?
  - Did the cited sources change for any queries?
  - For queries we made content fixes to (the 5 priorities from Jun 3): did our content show up?
- [ ] **Document at `_project/snapshots/aio-recheck-jun-24.md`**

**Time: 60 min**

---

### Wed Jun 25 — AIO follow-up fixes

Based on yesterday's AIO recheck, identify the 2–3 queries where we're closest to being cited but not quite. Make targeted content fixes:

- [ ] **For each near-miss query:**
  - Is the answer in the first 100 words? Make it more direct.
  - Does the FAQ schema include the exact question? Add it.
  - Are there enough external citations to authoritative sources? Add more if needed.
  - Is the H2 phrased exactly as the patient/AIO would ask? Convert.
- [ ] **Deploy fixes**

**Time: 75 min**

---

### Thu Jun 26 — GBP post + housekeeping

- [ ] **GBP Post (Week 4):**
  ```
  📍 Now accepting patients across Katy, Cinco Ranch, Fulshear, Sugar Land, Richmond, and Cypress.
  Specialized interventional treatments for back, neck, knee, shoulder, and nerve pain.
  Most insurance accepted. (281) 982-2144.
  ```
- [ ] **Housekeeping check:**
  - GBP photos: still showing the new 8 from May 27? Confirm.
  - Memorial Hermann directory address: has Dr. Q's correction landed? Re-check the directory URL.
  - Reviews count: where are we vs the 65+ June goal?

**Time: 30 min**

---

### Fri Jun 27 — Preliminary June numbers

- [ ] **Pull preliminary June numbers** (GBP/GSC/GA4 — same screenshot batch as May 28):
  - Will be ~26 days of June data
  - Send to me — I'll draft the Month 4 final report skeleton this weekend

**Time: 20 min**

---

### Sat Jun 28 + Sun Jun 29 — Off

---

## Phase 6: Month 4 Wrap (Jun 30)

### Mon Jun 30 — Final June scan + report

- [ ] **Run final June DIY scan** (~$7, 12 min wait)
- [ ] **Send the scan results to me** — I'll do the full Month 4 comparison + write the final report
- [ ] **Final June PDF** for client (I'll regenerate based on the May template)
- [ ] **Send to Dr. Qureshi async** with a 3-line note

**Time: 30 min**

---

## Cadence summary (after Month 4 wraps)

Once you're past Month 4, the steady-state cadence:

| Frequency | Task | Time |
|---|---|---|
| Mon + Thu | Publish a GBP post | 5 min each |
| Mon morning | Glance at GBP Performance dashboard | 5 min |
| Fri afternoon | Glance at GSC + GA4 | 10 min |
| Bi-weekly Sat | Run DIY grid scan | 15 min (mostly waiting) |
| Monthly end-of-month | Send client status PDF (async) | 30 min |

**Steady-state time: ~30 min/week + 30 min/month = ~2 hr 30 min per month per client.** That's the floor — pace yourself accordingly.

---

## Sanity-check totals

| Phase | Days | Rameel hours |
|---|---|---|
| Phase 1 (May 26–30 wrap) | 5 | ~2.5 hr |
| Phase 2 (Jun 2–6 AIO + page 1) | 5 | ~4.5 hr |
| Phase 3 (Jun 9–15 page 2 + PAA + reviews) | 7 | ~5 hr |
| Phase 4 (Jun 16–22 conversion + Bing) | 7 | ~4 hr |
| Phase 5 (Jun 23–29 A/B + AIO recheck) | 7 | ~3.5 hr |
| Phase 6 (Jun 30 wrap) | 1 | ~0.5 hr |
| **Total** | **32 work days** | **~20 hours over 5 weeks** |

That's **~4 hours per week average.** Roughly half of a typical "I have time for SEO" budget. Doable.

---

## What I (Leadmill agency-side) am responsible for during this window

In parallel with the Rameel-side tasks above, I'll be doing:

- All content writing for the 2 new procedure pages (drafts + final)
- All schema additions for new pages and PAA-derived FAQs
- All scan comparisons + reports (mid-month + final)
- All PDF report generation
- The AIO baseline + recheck analysis (you do the screenshotting; I do the analysis)
- The GA4 conversion data analysis (you screenshot; I synthesize)
- Updating PROJECT-STATUS at each phase boundary

---

## What's intentionally NOT in this plan (out of scope for Month 4)

- New city pages (we have 5 — that's enough for now)
- More directory citations (we're at 10 — playbook's right count)
- Schema redesigns (current schema is solid)
- Major homepage redesign (only the CTA copy test)
- Yelp / Manta / RateMDs URL collection (those are post-claim, lower priority than the conversion + AIO work)
- Katy Chamber of Commerce ($1k/yr; skipped per May decision)
- Anything client-side that requires Dr. Q to do extra work (he's busy + happy; don't burden him)

---

## When to deviate from this plan

This plan is a default. Deviate if:

- **The mid-month scan (Jun 14) shows the recovery has stalled or reversed** — pause new content; investigate (could be a Google algo update, schema rejection, or competitor activity)
- **GA4 conversion data shows specific high-converting pages need urgent work** — prioritize those over new procedure pages
- **Dr. Qureshi sends new direction** — client preference rules
- **Maps Platform credit gets activated** — can run more scans for free

---

## How to use this document

1. **Each morning,** check what's scheduled for today
2. **Block the time on your calendar** the night before
3. **If you miss a day, do the catch-up next morning** — don't compound the delay
4. **At the end of each phase,** ping me with status so I can spin into my parallel work

That's it. Now go win Month 4.
