# AI Overview (AIO) Baseline — June 2026

## Where to upload screenshots

**Drop all AIO screenshots in:** `_project/snapshots/aio-baseline-jun/screenshots/`

Name each file by the query number (so I can match them): `q01.png`, `q02.png`, ... `q15.png`. Or just dump them and tell me the order — I'll sort it out.

## How to capture (do this in ONE sitting, ~45–60 min)

1. **Open Chrome in Incognito** (Cmd+Shift+N) — avoids personalization skewing results
2. **Set location to Katy, TX** if Google prompts (or search "katy tx weather" first to anchor location)
3. **For each of the 15 queries below:**
   - Type it into Google, search
   - **If an AI Overview panel appears at the top** (it says "AI Overview" with a sparkle icon, often "Generative AI is experimental"): screenshot the whole panel **including the cited source links on the right/bottom**
   - **If NO AI Overview appears:** screenshot the top of the results anyway (so we know it didn't trigger), and note it
4. **Save each screenshot** to the `screenshots/` folder, named by query number

## What I'm looking for in each screenshot

- Did an AI Overview trigger at all? (Many medical queries do; some don't.)
- Which sources did Google cite? (Mayo Clinic, Cleveland Clinic, Healthline, WebMD, NIH, etc.)
- **Is drimranqureshi.com cited anywhere?** (Baseline expectation: almost certainly 0 right now — that's fine, that's the point of a baseline.)

## The 15 target queries

Capture these exactly:

1. what is an epidural steroid injection
2. epidural steroid injection side effects
3. how long does an epidural steroid injection last
4. is an epidural steroid injection safe
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

(These are chosen because they match content we already have on the site, and several already show up in Dr. Q's GSC impressions — meaning Google already associates the site with these topics, so we have a real shot at AIO citation.)

## After you upload

Tell me they're in, and I'll:
1. Analyze which queries trigger AIO and which sources get cited
2. Identify the 5 highest-priority queries to target (best combination of: triggers AIO + we have matching content + currently citing a generic source we can displace)
3. Write the action list of content fixes (answer-block tweaks, FAQ schema additions, H2 conversions) to make our content AIO-citable
4. Save the analysis to `aio-baseline-jun/analysis.md`

Then we execute the fixes, wait ~2 weeks for re-crawl, and recheck (the Jun 24 recheck in the Month 4 plan).
