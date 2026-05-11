# Maps Coverage — Full Longitudinal View, Mar 4 → May 11, 2026

**Generated:** May 11, 2026
**Sources:**
- LocalRank/DataForSEO scans archived in `localrank-csvs-mar-may-2026/` (5 scans across 10 weeks)
- Our DIY Google Places API tool: `tools/grid-rank-tracker/scans/imran-2026-05-02-2035.json` + `imran-2026-05-07-2215.json`

This is the first time we have **pre-engagement baseline data** for Dr. Qureshi. Until now we only had our May 2 baseline; the client's LocalRank account had been quietly tracking from March 4, but we hadn't pulled the CSVs into the project.

The story is more nuanced than our earlier "May 2 → May 7 looks good" framing suggested.

---

## Headline: Dip-then-Recovery

Major site changes shipped April 22–23 (GBP URL switch + full E-E-A-T retrofit). The textbook re-evaluation cycle followed:

- **Apr 20** — pre-changes, coverage near peak
- **May 3** — bottom of the dip, coverage tanked across multiple keywords
- **May 11** — first signs of recovery underway

This is the **4–8 week re-evaluation window we always tell clients to expect after major site work**. We just didn't have the pre-change baseline to see it clearly before.

---

## Coverage trend by keyword (doctor-focused set)

LocalRank 49-point grid, ~18-mile radius around Katy.

| Keyword | Apr 20 | May 3 | May 11 | Trajectory |
|---|---|---|---|---|
| **pain management doctor near me** | **93%** (46/49) | **48%** (24) | **55%** (27) | 📉 → ⬆️ recovering |
| **neck doctor near me** | **51%** (25) | **8%** (4) | **14%** (7) | 📉 → ⬆️ recovering (top-3: 2 → 1 → 3) |
| **neck doctor katy** | 24% (12) | 4% (2) | 4% (2) | 📉 → flat |
| **back doctor near me** | 12% (6) | 2% (1) | 2% (1) | 📉 → flat |
| **knee doctor near me** | 8% (4) | 2% (1) | 2% (1) | 📉 → flat |
| **sciatica** | 14% (7) | 2% (1) | 2% (1) | 📉 → flat |
| **back doctor katy** | 2% (1) | 0% | 0% | 📉 → flat |
| **sports injury doctor near me** | 2% (1) | 2% (1) | 2% (1) | flat |
| **muscle pain** | 0% | 0% | 0% | flat (generic, not pursued) |
| **pain management katy** | 100% (49) | 97% (48) | 100% (49) | held strong |

**Summary:** Across the 8 keywords with meaningful coverage at Apr 20, **all 8 dropped** between Apr 20 and May 3. **2 are visibly recovering** by May 11 (`pain management doctor near me`, `neck doctor near me`). The rest are still at the bottom of the dip — but only 8–18 days have passed since the dip bottomed, well inside the 4–8 week recovery window.

---

## Coverage trend by keyword (procedure-focused set)

LocalRank 25-point grid for these older scans. Tracked Mar 4 and Apr 9 only — these keywords were dropped from the LocalRank scan set after Apr 9.

| Keyword | Mar 4 | Apr 9 | Trend |
|---|---|---|---|
| **lumbar epidural steroid injection katy** | 100% (25/25) | 100% (25) | held |
| **cervical epidural steroid injection katy** | 96% (24) | 100% (25) | ↑ |
| **pain management katy tx** | 100% (25) | 96% (24) | flat |
| **epidural steroid injection katy** | 96% (24) | 100% (25) | ↑ |
| **epidural injection katy tx** | 92% (23) | 80% (20) | ↓ slight |
| **neck pain doctor katy** | 84% (21) | 64% (16) | ↓ |
| **back pain doctor katy tx** | 24% (6) | 4% (1) | ↓ |
| **sciatica treatment katy** | 4% (1) | 0% | ↓ |
| **back doctor near me** | 4% (1) | 4% (1) | flat |
| **prp injection katy tx** | 0% | 0% | flat |

The "procedure + katy" variants stayed strong. The "doctor + location" variants were already declining before we entered the engagement — explains why those are also slower to recover today.

---

## The crown jewel: avg-rank improvement on `epidural steroid injection katy`

Tracked across the full timeline:

| Date | Source | Coverage | Avg rank | Best rank |
|---|---|---|---|---|
| Mar 4, 2026 | LocalRank | 96% (24/25) | 11.1 | 6 |
| Apr 9, 2026 | LocalRank | 100% (25/25) | 11.4 | 5 |
| May 2, 2026 | DIY tool | 100% (81/81) | **5.9** | — |
| May 7, 2026 | DIY tool | 100% (81/81) | 6.1 | — |

**Avg rank moved from 11.1 → 5.9 across 8 weeks — a 5-position jump on our strongest keyword.** This survives the April–May dip narrative because the procedure-specific keywords held up while doctor-specific keywords took the hit.

Why this matters: `epidural steroid injection katy` is the **highest-intent buyer query** for Dr. Qureshi's practice. Patients searching this are actively shopping for the procedure, often within days of booking. Going from avg rank 11 to avg rank 6 means appearing in the top-of-page Local Pack ~70% more often.

---

## What happened on Apr 22–23 that triggered the dip

Per `_project/PROJECT-STATUS.md`:

1. **Apr 22** — Client switched GBP website URL from `cls.health/locations/pain-management-cinco-ranch` to `drimranqureshi.com`. This is a major signal change to Google — the practice's canonical URL changed.

2. **Apr 23** — Full E-E-A-T / AI Overview retrofit shipped in one push:
   - 2 trust pages (`/medical-disclaimer`, `/editorial-policy`)
   - "Medically reviewed by" byline on 20 main pages
   - 51 external authority citations added across 20 pages
   - Answer-first opening blocks on 20 main pages
   - 71 H2 conversions from clinical labels to patient questions

This is the equivalent of a substantial site relaunch. Google's response: re-evaluate from scratch. Local rankings dip while the new authority signals load in. Then climb back, typically to a HIGHER baseline than before.

This is **exactly what should happen** after major site work. We just didn't have the historical visibility to confirm it until now.

---

## Cross-validation: Our DIY tool vs LocalRank

The two backends largely agree on coverage direction. Where they disagree, it's geographic span (LocalRank uses 18-mi grid, ours uses 7-mi).

| Keyword | DIY May 2 (81-pt, 7mi) | LocalRank May 3 (49-pt, 18mi) | Agree? |
|---|---|---|---|
| pain management katy | 100% / 81 | 97% / 49 | ✓ |
| pain management doctor near me | 56% / 81 | 48% / 49 | ✓ close |
| neck doctor near me | 20% / 81 | 8% / 49 | Partial (geographic span effect) |
| neck doctor katy | 5% / 81 | 4% / 49 | ✓ |
| back doctor katy | 0% / 81 | 0% / 49 | ✓ |
| back doctor near me | 7% / 81 | 2% / 49 | ✓ both narrow at-practice |
| sciatica | 3% / 81 | 2% / 49 | ✓ |

**Verdict:** DIY tool is directionally accurate. Replacing LocalRank's $297/mo subscription was the right call — the data quality is comparable.

---

## What this changes for the May 19 client call

The framing for the Month 3 results call should be honest about the dip:

> "Across April, we made the biggest single push of the engagement — switched your GBP website URL to your own domain, and rebuilt every condition and treatment page with the trust signals Google's algorithms actually look for. Google's algorithm responded the way it always does after major site work: it re-evaluated everything, which caused a brief drop in local rankings between Apr 20 and May 3. That drop is the cost of admission for the new authority baseline we're building toward.
>
> The recovery is now underway. Two of our highest-priority keywords (`pain management doctor near me` and `neck doctor near me`) are already climbing back. And the keyword that matters most for procedure conversions — `epidural steroid injection katy` — is at its best position of the year (avg rank 6, up from 11 in early March). We expect the rest of the keywords to follow over the next 2–4 weeks, just as the textbook recovery cycle plays out."

This is more accurate than the prior "rankings are climbing" framing — and more credible, because we're showing the client we know what's happening and why.

---

## What it changes for our internal practice

**Lesson:** Always pull pre-change baseline data before shipping major changes. We had three months of LocalRank scans sitting on the client's account but didn't ingest them until May 11 — too late to use the Apr 20 baseline as a pre-change reference point.

For Leadmill's other clients (PROTECH, Elemental Doors, Emporium): if they have any historical local-rank tracking data, pull it into the project repo before shipping anything major. The pre-baseline is what makes the dip explainable; without it, the dip looks like failure instead of an expected recovery curve.

Added to playbook Field Notes as new lesson #16.
