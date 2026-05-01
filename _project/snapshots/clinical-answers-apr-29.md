# Clinical Q&A from Dr. Qureshi — Apr 29, 2026

*Async response to questions sent Apr 23. Unblocks Month 3 page builds for GLP-1 and PRP.*

---

## GLP-1 Weight Loss

| Question | Answer |
|----------|--------|
| **Medications offered** | Semaglutide and Tirzepatide — only generic versions (compounded, not brand-name Wegovy/Ozempic/Zepbound/Mounjaro) |
| **Pricing** | Cash pay starting as low as $100/month |
| **Intake process** | Office consultation, blood work, vitals, BMI/weight check, medical history. **Virtual appointments available** for follow-ups. |
| **Eligibility** | Open to most patients **EXCEPT those with personal or family history of thyroid cancer** (absolute contraindication). Further eligibility discussed at visit. |
| **Lifestyle/nutrition coaching** | **No** — practice does not provide nutrition or lifestyle coaching alongside the medication. |
| **Contraindications to highlight** | Thyroid cancer (personal or family history) |
| **Typical results** | - Weight loss visible as early as **1 month**<br>- Up to **25% weight loss after 72 weeks**<br>- Most patients lose **5-10+ pounds per month** |
| **In-office marketing** | Has a tirzepatide poster up in office — claims "Lose Weight and Lose it Fast" with stats: **22% weight loss, 48 lbs, 9 in 10** patients |

### Implications for the page

✅ **Use:** Generic Semaglutide and Tirzepatide (cheaper than brand names — this is a positioning advantage to highlight)
✅ **Use:** $100/month starting price is a strong differentiator vs Wegovy/Ozempic/Zepbound retail
✅ **Use:** Virtual follow-ups available
✅ **Use:** Results timeline (1 month → 5-10 lbs/month → up to 25% at 72 weeks)
⚠️ **Handle carefully:** Thyroid cancer contraindication must be prominently displayed (FDA black box warning territory — required disclosure)
⚠️ **Handle carefully:** "No lifestyle coaching" — frame as "Dr. Qureshi prescribes the medication; nutrition counseling is not part of the program" rather than "we don't help with lifestyle." Patients who need structured coaching should know to seek it elsewhere.
⚠️ **Verify before publishing:** The poster's "22% / 48 lbs / 9 in 10" claims need source citations (likely the SURMOUNT-1 trial for tirzepatide). Either cite the trial or use Dr. Qureshi's softer "up to 25% at 72 weeks" framing on the website.

---

## PRP Therapy

| Question | Answer |
|----------|--------|
| **Conditions treated most** | Knee osteoarthritis, tendon injuries, shoulder pain |
| **Typical protocol** | Single injection (not a series) |
| **Pricing** | $750 per site, or $1,200 for two sites |
| **Success rate in his practice** | >90% success rate, improved long-term effect compared to steroids |
| **Who is NOT a candidate** | - Patients with various blood disorders<br>- Active infections<br>- Cancer<br>- Patients on blood thinners |

### Implications for the page

✅ **Use:** Knee osteoarthritis is the lead condition (most common indication)
✅ **Use:** Single-injection protocol is a differentiator vs practices that push 2-3 injection series
✅ **Use:** Pricing is concrete ($750 single, $1,200 two-site bundle)
✅ **Use:** "Improved long-term effect vs steroids" is a strong positioning claim
⚠️ **Handle carefully:** ">90% success rate" is a strong claim — should be framed as Dr. Qureshi's clinical experience, not a published statistic. Soften to "the majority of patients in our practice see meaningful improvement" or cite a peer-reviewed study with similar results.
⚠️ **Required content:** Contraindications (blood disorders, infection, cancer, blood thinners) must be clearly listed — patient safety + medical disclaimer requirement

---

## Recommended Citations for Each Page

### GLP-1 page
- FDA: GLP-1 medications (mechanism, approved uses)
- NIH: obesity treatment guidelines
- SURMOUNT-1 trial (tirzepatide, NEJM) — for the 22% weight loss claim
- STEP trials (semaglutide, NEJM) — for semaglutide outcomes
- Cleveland Clinic: thyroid cancer contraindication explainer (for the warning section)

### PRP page (already enhanced — see existing /treatments/prp-therapy)
- Cleveland Clinic PRP: https://my.clevelandclinic.org/health/treatments/platelet-rich-plasma-prp-injection
- NIH NIAMS: osteoarthritis page (for knee OA section)
- Cleveland Clinic PRP risks/benefits: existing citation

---

## Page-build status

**Now unblocked:**
- [x] `/treatments/glp-1-weight-loss` — all clinical info available, can build immediately
- [x] `/treatments/knee-injection` — uses PRP info above plus general joint injection content (steroid + HA + nerve blocks for genicular nerve)
- [x] `/treatments/prp-therapy` rewrite — can incorporate practice-specific success rate and pricing

**Use the master playbook structure:**
- Answer-first block (75-125 word direct query response) at top
- "Medically reviewed by Dr. Imran Qureshi, D.O. | Last reviewed: May 2026" byline
- 2-3 external authority citations
- Question-based H2s
- Visible warning box for contraindications (esp. thyroid cancer for GLP-1)
- FAQ section with FAQPage schema
- Internal links to related pages (about, contact, insurance, regenerative-medicine)
- Add to sitemap.xml + footer treatments list

---

## Open question for Rameel

**Tirzepatide poster claims (22% / 48 lbs / 9 in 10):** the in-office poster cites these. Do you want them on the website page as well, or stick with Dr. Qureshi's softer "up to 25% at 72 weeks / 5-10 lbs/month" framing?

The poster numbers come from the SURMOUNT-1 trial (peer-reviewed, NEJM) so they're cite-able. But the website is more conservative ground than an in-office poster. Recommend the softer framing on the website with one citation to SURMOUNT-1.
