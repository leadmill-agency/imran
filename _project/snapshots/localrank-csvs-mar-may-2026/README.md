# LocalRank CSV Archive — Mar–May 2026

Raw scan exports from LocalRank's DataForSEO backend, covering the engagement window pre- and post-major changes. Saved here on May 11, 2026 from client's downloads.

## Files

| File | Scan Date | Grid | Keywords | Rows |
|---|---|---|---|---|
| `localrank-2026-03-04-95b84a65.csv` | 2026-03-04 | 5×5 = 25 pts | 10 (procedure-focused) | 250 |
| `localrank-2026-04-09-25b2e6a8.csv` | 2026-04-09 | 5×5 = 25 pts | 10 (procedure-focused) | 250 |
| `localrank-2026-04-20-30e9929b.csv` | 2026-04-20 | 7×7 = 49 pts | 10 (doctor-focused) | 490 |
| `localrank-2026-05-03-b81ba385.csv` | 2026-05-03 | 7×7 = 49 pts | 10 (doctor-focused) | 490 |
| `localrank-2026-05-11-4d3dfc9a.csv` | 2026-05-11 | 7×7 = 49 pts | 10 (doctor-focused) | 490 |

## CSV schema

```
Scan UUID, Business Name, Business URL, Scan Date, Status, Keyword, Pin Latitude, Pin Longitude, Rank, Found
```

- `Rank` = position 1–20 if found, `99` if not in top-20 results
- `Found` = "Yes" / "No" (Yes when Rank ≤ 20)
- `Status` = "completed" for all rows in these scans

## Important notes

- **Grid changed between Apr 9 and Apr 20** — earlier scans use a 25-point grid; later scans use a 49-point grid. Direct point-count comparisons across this boundary are not 1:1.
- **Keyword set changed between Apr 9 and Apr 20** — early scans tracked procedure/condition keywords ("epidural steroid injection katy", "lumbar epidural steroid injection katy"). Later scans pivoted to doctor-style keywords ("back doctor near me", "knee doctor near me"). Cross-set comparisons need care.
- **Source provider is DataForSEO** (per LocalRank's scan report PDF). Our in-house grid scanner uses Google Places API (New) directly. The two backends report slightly different rank universes — DataForSEO tends to count broader local results, Places API is tighter to the Local Pack.

## How to read this with the rest of the project

- See `_project/snapshots/maps-baseline-may-02.md` for our DIY tool's first scan
- See `_project/snapshots/maps-mid-month-may-7.md` for the May 2 → May 7 comparison
- See `_project/snapshots/maps-longitudinal-mar-may-2026.md` for the unified narrative across LocalRank + DIY tool data

## When to re-pull

Client can run a fresh LocalRank scan from their dashboard at any time. We're not paying for LocalRank anymore (canceled May 2 in favor of our DIY tool), but if the client renews or runs ad-hoc scans, drop the CSVs here.

For our own data, the in-house grid scanner at `/Users/rameel/Desktop/Manual Library/Leadmill/tools/grid-rank-tracker/` runs at $7/scan and stores results in `scans/`.
