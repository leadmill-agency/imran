# Week of May 5–9, 2026 — Status

**Generated:** May 6, 2026

## ✅ Done this week (Mon–Tue)

| Item | Where | Notes |
|---|---|---|
| sameAs schema audit + 4 new verified directory URLs | All 49 HTML pages | LinkedIn, Zocdoc, Memorial Hermann, CLS Health added. Also fixed broken Healthgrades placeholder URL → real canonical. Total now 10 verified URLs. |
| 5 city pages differentiated | 5 city HTML files | Each got 2 new H2 sections (~400 unique words/page) with city-specific geography, demographics, and pain patterns. Eliminates duplicate-content risk. |
| GA4 conversion tracking shipped | All 49 HTML pages | 4 events now fire: phone_call_click, book_appointment_click, directions_click, form_submit. **You still need to mark them as Key Events in GA4 admin (24–48 hrs after first events appear).** |
| Entity language fixes for "knee doctor" + "sports injury doctor" | index, about, knee-pain/arthritis, sports-injuries | Targets 2 of the 5 zero-coverage keywords from the May 2 Maps baseline. |
| Mid-month Maps grid scan | tools/grid-rank-tracker | Currently running — comparison vs May 2 baseline ready as soon as scan finishes. |

## 🔄 In progress (running now)

- **Mid-month Maps grid scan** — 18 keywords × 81 grid points. Will produce a `compare.py` diff vs May 2 baseline showing rank movement. Early signal so far: "pain management doctor katy" is at avg 8 (vs baseline 9.2) — directional improvement.

## ⏳ Pending this week

| Item | Owner | Notes |
|---|---|---|
| Mark GA4 events as Key Events | Rameel | GA4 → Admin → Events → toggle "Mark as key event" on phone_call_click, book_appointment_click, form_submit. Wait 24–48 hrs after deploy for events to show up. |
| Publish GBP Post #4 | Rameel | Draft below — paste into GBP. |
| 4 directory citations (Sharecare, US News, Doctor.com, Wellness.com) | Rameel or Leadmill | Manual claim work. Each is ~15 min. Note: US News did not return a Dr. Qureshi profile in our search — it auto-populates from NPI eventually but isn't there yet. |
| Yellow Pages re-attempt | Rameel | First attempt failed — retry with different verification path. |

## 💸 Decision needed from client

**Katy Chamber of Commerce membership.** No free directory listing — Bronze tier is **$1,000/yr** with basic listing (200-char description, 8 keywords, logo on chamber homepage). Decision: include in budget or skip?

My take: **skip for now.** $1,000/yr is steep for one citation when we still have free high-DA citations to claim (Sharecare, Wellness.com, Doctor.com, etc.). Revisit at end of Q2 if we need to push entity authority further.

## 🔍 What I noticed in the audit

While reviewing the Month 3 plan vs current state, a few things from earlier weeks that are still pending:

1. **GBP Post #2 (PRP-focused)** — Apr 23 plan called for this. Don't know if it shipped — flag to verify in GBP.
2. **Q&A seeding (10 questions)** — Apr 21 task. Client previously opted out. Confirmed not happening.
3. **Memorial Hermann directory has stale Webster TX address** — discovered while verifying sameAs. Dr. Qureshi should request a directory update via MHMD to fix.
4. **GBP photos request from Apr 22** — still pending from client. Photo count is below target.

---

# GBP Post #4 — Draft to publish

**Pick one of these two options. Both work — just paste into GBP → Posts → "Add update".**

## Option A: Capacity announcement (recommended)

> 🟢 **Now accepting new patients with same-week availability**
>
> Board-certified pain specialist Dr. Imran Qureshi serves Katy, Cinco Ranch, Fulshear, Sugar Land, Richmond, and Cypress with image-guided interventional treatments — epidural injections, PRP therapy, radiofrequency ablation, joint injections, and more. Most major insurance accepted.
>
> 📞 Call (281) 982-2144 to schedule.

**CTA button:** "Call now" → tel:2819822144
**Image:** Use existing exterior or interior office photo.

## Option B: Educational / condition-focused

> 🦵 **Knee pain limiting your activity? You may not need surgery.**
>
> Most knee osteoarthritis can be managed for years with image-guided injections — corticosteroid, hyaluronic acid (gel), PRP therapy, or genicular nerve blocks for severe pain. Dr. Qureshi performs all knee injections under ultrasound guidance for accuracy.
>
> 📞 Same-week appointments available — (281) 982-2144

**CTA button:** "Learn more" → https://drimranqureshi.com/knee-pain/arthritis
**Image:** Use a knee anatomy or treatment photo.

---

**My recommendation:** Use **Option A this week**. It directly reinforces the GBP signals Google rewards (capacity, service area). Save Option B for next week when the knee-doctor entity language has 7+ days to age into the index.
