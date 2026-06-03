#!/usr/bin/env python3
"""
Address migration swap script — Cinco Ranch -> Energy Corridor.

DO NOT RUN until Dr. Qureshi confirms the exact NAP (suite # + ZIP + coords).
Fill in the CONFIRMED_* constants below first, then run from the repo root:

    cd "/Users/rameel/Desktop/Manual Library/Leadmill/imran 2"
    python3 _project/snapshots/address-move-may-2026/swap_address.py

Run on the `address-migration` branch ONLY. Do not merge to main until the
practice physically moves (Vercel auto-deploys main).

What it does:
  - Swaps the full old-address tokens -> new address (longest-first)
  - Swaps geo coordinates in all JSON-LD
  - Preserves "Cinco Ranch" as a service-area city (only touches the
    "23501 Cinco Ranch Blvd" street token)
  - Prints a verification summary

What it does NOT do (manual, page-specific — see runbook):
  - Reposition the Cinco Ranch city page narrative
  - Rewrite "minutes from Cinco Ranch Blvd & Grand Pkwy" proximity copy
  - Rewrite building-specific copy (second floor / medical plaza / parking)
  - Update map embeds
  - Build the new Energy Corridor location page
"""

import re
import sys
from pathlib import Path

# ---- CONFIRM THESE WITH DR. Q BEFORE RUNNING -------------------------------
CONFIRMED_SUITE = "Suite XXX"      # e.g. "Suite 200" — or "" if no suite
CONFIRMED_ZIP = "77450"            # confirm 77450 vs 77449
NEW_LAT = "29.XXXXX"               # geocode 1400 Ravello Dr after confirmation
NEW_LNG = "-95.XXXXX"
# ----------------------------------------------------------------------------

# Old address components
OLD_STREET = "23501 Cinco Ranch Blvd"
OLD_SUITE = "Suite G205"
OLD_ZIP = "77494"
OLD_LAT = "29.743"
OLD_LNG = "-95.775"

NEW_STREET = "1400 Ravello Dr"

# Build new address fragments
NEW_SUITE_PART = (", " + CONFIRMED_SUITE) if CONFIRMED_SUITE else ""

# Longest-first replacement pairs (order matters — do specific before general)
REPLACEMENTS = [
    (f"{OLD_STREET}, {OLD_SUITE}, Katy, TX {OLD_ZIP}",
     f"{NEW_STREET}{NEW_SUITE_PART}, Katy, TX {CONFIRMED_ZIP}"),
    (f"{OLD_STREET}, {OLD_SUITE}",
     f"{NEW_STREET}{NEW_SUITE_PART}"),
    (f"{OLD_STREET}, Katy, TX {OLD_ZIP}",
     f"{NEW_STREET}, Katy, TX {CONFIRMED_ZIP}"),
    (f"{OLD_STREET}",
     f"{NEW_STREET}"),
    # schema PostalAddress streetAddress field (may be "23501 Cinco Ranch Blvd, Suite G205")
    (f'"streetAddress": "{OLD_STREET}, {OLD_SUITE}"',
     f'"streetAddress": "{NEW_STREET}{NEW_SUITE_PART}"'),
    # ZIP in schema postalCode
    (f'"postalCode": "{OLD_ZIP}"', f'"postalCode": "{CONFIRMED_ZIP}"'),
    # Geo coords (schema)
    (f'"latitude":{OLD_LAT}', f'"latitude":{NEW_LAT}'),
    (f'"latitude": {OLD_LAT}', f'"latitude": {NEW_LAT}'),
    (f'"longitude":{OLD_LNG}', f'"longitude":{NEW_LNG}'),
    (f'"longitude": {OLD_LNG}', f'"longitude": {NEW_LNG}'),
    (f'"longitude":-95.7749334', f'"longitude":{NEW_LNG}'),
    (f'"latitude":29.7427630', f'"latitude":{NEW_LAT}'),
]


def main():
    if "XXX" in CONFIRMED_SUITE or "XXXXX" in NEW_LAT:
        sys.exit("ABORT: fill in CONFIRMED_SUITE / NEW_LAT / NEW_LNG (and verify ZIP) first.")

    root = Path(".")
    files = [p for p in root.rglob("*.html")
             if "_project" not in p.parts and "node_modules" not in p.parts]

    changed = 0
    for p in files:
        t = p.read_text()
        orig = t
        for old, new in REPLACEMENTS:
            t = t.replace(old, new)
        if t != orig:
            p.write_text(t)
            changed += 1

    print(f"Swapped address in {changed} files.\n")

    # Verification
    import subprocess
    def count(pattern):
        r = subprocess.run(["grep", "-rl", pattern, "--include=*.html", "."],
                           capture_output=True, text=True)
        return len([x for x in r.stdout.splitlines() if "_project" not in x])

    print("VERIFY:")
    print(f"  files still containing OLD street '{OLD_STREET}': {count(OLD_STREET)}  (target: 0)")
    print(f"  files containing NEW street '{NEW_STREET}': {count(NEW_STREET)}")
    print(f"  files containing 'serving' + Cinco Ranch (service area, should be UNCHANGED): "
          f"{count('Cinco Ranch')}")
    print("\nNEXT (manual, see runbook):")
    print("  - reposition pain-management-cinco-ranch-tx.html narrative")
    print("  - rewrite 'minutes from Cinco Ranch Blvd & Grand Pkwy' proximity copy")
    print("  - rewrite 'second floor / medical plaza / parking' building copy")
    print("  - update map embeds")
    print("  - build the new Energy Corridor location page")
    print("  - validate all JSON-LD")


if __name__ == "__main__":
    main()
