# Address Migration Runbook — Cinco Ranch → Energy Corridor

**Move:** 23501 Cinco Ranch Blvd, Suite G205, Katy TX 77494 → 1400 Ravello Dr, [Suite TBD], Katy TX [77450 TBD]
**Deadline:** by Aug 1, 2026 (firm — signage ordered). Exact date TBD from Dr. Q.
**Strategy:** prep on `address-migration` branch now; cut over the day the practice physically moves.
**Full plan:** `~/.claude/plans/joyful-noodling-quiche.md`

---

## Status tracker

### Phase 0 — Confirm NAP (BLOCKING)
- [ ] Email sent to Dr. Q (`email-to-dr-q-nap-confirmation.md`)
- [ ] Suite / unit number confirmed: __________
- [ ] ZIP confirmed (77450 vs 77449): __________
- [ ] Shared CLS Health building? Y/N + implications: __________
- [ ] Firm move date + last day at old office: __________
- [ ] New geo coordinates obtained (lat/lng): __________

### Phase 1 — Prep on `address-migration` branch (after NAP confirmed)
- [ ] Fill CONFIRMED_* constants in `swap_address.py`
- [ ] Run `swap_address.py` (address + geo swap, scripted)
- [ ] Reposition `pain-management-cinco-ranch-tx.html` (we serve it, not in it)
- [ ] Rewrite proximity copy: "minutes from Cinco Ranch Blvd & Grand Pkwy" → I-10 + Grand Pkwy
- [ ] Rewrite building copy: second floor / medical plaza / parking (confirm new details)
- [ ] Update map embeds (~10 pages)
- [ ] Build new Energy Corridor / I-10 location page (template: `pain-management-fulshear-tx.html`)
- [ ] Add new page to footer Service Areas + sitemap
- [ ] Validate all JSON-LD
- [ ] Commit to branch (NOT main)

### Phase 2 — Cutover (the day the practice physically moves)
- [ ] Merge `address-migration` → `main`, push (Vercel deploys)
- [ ] GBP: MOVE the existing listing (Edit → Address) — do NOT recreate
- [ ] GBP: update service area + "from the business" description
- [ ] Citations: update all 10 directories (checklist below)
- [ ] GSC: resubmit sitemap + request re-indexing on homepage/contact/about/both location pages/top treatments
- [ ] Grid tracker: re-center `config.json` to new coords, run post-move baseline scan

### Phase 3 — Post-move monitoring
- [ ] Re-warn client about the expected re-evaluation dip
- [ ] NAP consistency audit (Google the practice, check aggregator listings)
- [ ] Bi-weekly scans from new center; compare to pre-move baseline
- [ ] Clean up any stale old-address listings

---

## Citation update checklist (Phase 2 — all must show the NEW address)

NAP consistency across the web is essential. Update every one:

| # | Directory | URL | Updated? |
|---|---|---|---|
| 1 | GBP (Google Business Profile) | business.google.com | [ ] MOVE listing |
| 2 | Healthgrades | healthgrades.com/physician/dr-imran-qureshi-do-18z251yi70 | [ ] |
| 3 | Vitals | vitals.com/.../DoctorsOfOsteopathy_Imran_Mohammed_Qureshi.html | [ ] |
| 4 | Doximity | doximity.com/pub/imran-qureshi-do | [ ] |
| 5 | WebMD | doctor.webmd.com/doctor/imran-qureshi-... | [ ] |
| 6 | Healthline FindCare | care.healthline.com/.../dr-imran-qureshi-1467080622 | [ ] |
| 7 | Medical News Today | connect.medicalnewstoday.com/.../dr-imran-qureshi-1467080622 | [ ] |
| 8 | LinkedIn | linkedin.com/in/imran-qureshi-d-o-685420107 | [ ] |
| 9 | Zocdoc | zocdoc.com/doctor/imran-qureshi-do-651654 | [ ] |
| 10 | Memorial Hermann | memorialhermann.org/.../dr-imran-qureshi-do-1467080622 | [ ] (was already stale Webster TX — fix to new address) |
| 11 | CLS Health | providers.cls.health/provider/imran-qureshi/4850969 | [ ] (employer — likely auto-updates, verify) |
| 12 | Bing Places (added Jun 2026, growth program) | bingplaces.com | [ ] |
| (auto) | NPI Registry | NPI 1467080622 | [ ] update practice location |

**Note:** sameAs schema URLs themselves don't change (the profile URLs stay the same) — what changes is the *address shown on each profile*, which Rameel updates in each directory's dashboard. The website schema `PostalAddress` IS updated by the swap script.

---

## Key reminders

- **Phone number does NOT change** — `(281) 982-2144` stays. No `tel:` edits.
- **"Cinco Ranch" stays as a service-area city** — only the `23501 Cinco Ranch Blvd` street token changes.
- **Never recreate the GBP listing** — moving it preserves the 58 reviews + ranking history.
- **Hold `main`** — nothing live until the confirmed physical move date.
