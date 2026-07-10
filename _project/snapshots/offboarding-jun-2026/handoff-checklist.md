# Website Handoff Checklist — Dr. Imran Qureshi

Clean transfer of every asset to accounts Dr. Q controls. Goal: he leaves owning everything, with no Leadmill credentials or dependencies left embedded. Work top to bottom.

## 0. Security — do this FIRST (before any transfer)

- [x] **Local remote cleaned (done by Claude, Jun 2026).** The embedded PAT was removed from `.git/config`; remote is now `https://github.com/leadmill-agency/imran.git` with no token. Verified the token was NOT in any committed file or git history — it lived only in the local config. ⚠️ Side effect: `git push`/`fetch` from this folder now needs fresh auth (GitHub login prompt, `gh auth login`, a credential helper, or SSH) — the token was previously doing that silently.
- [x] **Old token killed (done by Rameel, Jun 2026).** Regenerated the PAT on GitHub, which invalidates the exposed `ghp_0Rz…` value — the leaked credential is now dead server-side. New token is scoped `repo`, expires Jul 22 2026.
- [x] **Secure auth confirmed.** Git credential helper is `osxkeychain` and the remote is token-free, so the new token gets stored in macOS Keychain on first push (enter GitHub username + paste new token as the password at the prompt) — never re-embedded in `.git/config`. **Do not paste the new token into the remote URL or share it.**

**✅ Security section complete.**

## Quick transfer sequence (GitHub + Vercel) — the remaining work

Domain is his and the refund is done, so this is all that's left. Order matters; do it in one sitting.

**Prereqs (Rameel collects from Dr. Q):** his **GitHub username** (free account; create one if needed), and a **Vercel account** (he should sign up at vercel.com *with his GitHub login* — links them automatically). Pick a low-traffic window for the domain swap (brief downtime possible).

1. **Publish + transfer the CLEAN repo** (never the original — see §1) → Rameel pushes `imran-website-handoff/website` to a new `drimranqureshi-website` repo, then transfers it; Dr. Q accepts the email.
2. **Dr. Q stands up his own Vercel project** from the transferred repo → §2 below. It deploys to a temporary `*.vercel.app` URL first — confirm that loads. (His fresh Vercel project contains nothing of Leadmill's — no env vars, no history.)
3. **Move the domain** to his Vercel project: remove `drimranqureshi.com` + `www` from Leadmill's old Vercel project, add them to his new project, then he updates/confirms the DNS records Vercel shows at his registrar. Verify both `www` and non-www load.
4. **Rameel cleanup:** once his site is live on the domain, delete the old Leadmill Vercel project and grant GA4 admin (§4). Done.

> Lower-downtime alternative: instead of steps 2–3, transfer the *existing* Vercel project to his account (Vercel "Transfer Project" flow, if your plan supports it) — keeps the domain attached, then just reconnect the Git integration to his repo. Use whichever your Vercel plan allows.

---

## 1. GitHub — the website code  🔁 REVISED: transfer the CLEAN repo, never the original

- ⚠️ **Do NOT transfer `leadmill-agency/imran`.** Its git history permanently contains `_project/` (all internal reports, the offboarding notes, refund reasoning) and commit messages that narrate the whole engagement. Deleting files now would NOT remove them from history.
- [x] **Clean handoff repo built (done by Claude, Jun 2026)** at `/Users/rameel/Desktop/Manual Library/Leadmill/imran-website-handoff/website` — 73 site files, ONE anonymous commit ("Dr. Imran Qureshi website — initial version"). Scrubbed: `_project/`, `CLAUDE.md`, `AGENTS.md`, `.claude/`, `.vercel/`, the robots.txt `/_project/` line, and **author-name metadata found inside 6 PNG icons** (all images re-encoded, verified rendering). Full-tree sweep for internal terms: clean, including binaries. Client-friendly `README.md` added.
- [ ] **Rameel: publish the clean repo (5 min).** On github.com → New repository → name it `drimranqureshi-website` (private, empty — no README). Then:
  ```
  cd "/Users/rameel/Desktop/Manual Library/Leadmill/imran-website-handoff/website"
  git remote add origin https://github.com/YOUR-USERNAME/drimranqureshi-website.git
  git push -u origin main
  ```
- [ ] **Get Dr. Q's GitHub username** (guide walks him through creating the account).
- [ ] **Transfer the clean repo to him:** repo → Settings → Danger Zone → Transfer ownership → his username. He accepts the email.
- The original `leadmill-agency/imran` repo stays private under Leadmill as the engagement archive. Do not delete it; do not share it.

## 2. Vercel — the hosting

- **What it is:** the Vercel project that auto-deploys from the GitHub repo on every push. `vercel.json` in the repo holds the config (static, clean URLs).
- [ ] **Transfer the Vercel project** to a Vercel account Dr. Q controls (Vercel → Project → Settings → transfer to another team/account), **or** have him create a free Vercel account and "Import" the transferred GitHub repo fresh.
- [ ] **Reconnect the Git integration** so his Vercel deploys from his repo.
- [ ] **Confirm the production domain** (`www.drimranqureshi.com`) is attached in his Vercel project's Domains tab.
- [ ] Verify a test deploy works from his side (push a trivial change or trigger a redeploy → site stays up).

## 3. Domain + DNS — `drimranqureshi.com`  ✅ RESOLVED

- [x] **Dr. Q owns the domain/registrar** (confirmed Jun 2026). No domain transfer needed. He controls DNS, so when the site moves to his Vercel project he'll point/confirm the DNS records Vercel gives him (see the transfer sequence below). After cutover, re-verify non-www 307 → www and both load.

## 4. Google Analytics — GA4 `G-SHWLFXVMMF`

- [ ] **Grant Dr. Q Admin** on the GA4 property (Admin → Property Access Management → add his Google account as Administrator), or move the property under an account he owns.
- [ ] Confirm the tracking tag (`G-SHWLFXVMMF`) stays in the site — it's hardcoded across the pages, so it keeps working as long as the GA4 property stays live under his control.

## 5. Already his / NOT transferring

- **Google Business Profile** — CLS Health is handling the move + ongoing management. Leadmill does not touch it.
- **LumaHealth booking portal** — already his (the "Book Online" links point to his Luma form).
- **Bing Webmaster / Bing Places** — he set these up; his to keep. (Note: the Bing Places listing still shows the old `cls.health` URL — worth fixing to `drimranqureshi.com`, but it's now his call.)

## 6. How to actually manage the site going forward (set honest expectations)

This is a hand-built static site optimized for speed and SEO — **not** a drag-and-drop editor he logs into. Three realistic paths, by budget/comfort:

| Path | What it means | Best if |
|---|---|---|
| **(a) Keep a developer on call** | Pay someone (Rameel ad-hoc, or a freelancer) for occasional edits via the GitHub→Vercel flow | He wants edits rare and the site fast — *recommended for most physicians* |
| **(b) Migrate to an editable platform** | Rebuild on Squarespace/Wix/WordPress so he self-edits | He wants full self-service and will accept slower load + a rebuild cost + likely a temporary SEO dip |
| **(c) Learn the GitHub→Vercel workflow** | He edits HTML + commits himself | Only if he's technically inclined — steep for a non-dev |

Recommend (a) or (b). Do **not** imply he can easily self-edit raw HTML.

## 7. Final courtesy (optional — only if he asks + confirms NAP)

- [ ] If Dr. Q wants the website address updated to 1400 Ravello before handoff: confirm suite # + ZIP (likely 77450, to match CLS), then run `_project/snapshots/address-move-may-2026/swap_address.py` on `main`, do the manual proximity/Cinco-Ranch rewrites per the RUNBOOK, validate JSON-LD, deploy. Hand off a finished, accurate site.
- [ ] If not: hand off as-is and tell him (or his next manager) the website address still needs updating at the move — point them at the RUNBOOK as the recipe.
- [ ] Do **not** silently merge the `address-migration` branch — fold it into the above or leave it documented.

## Sign-off

- [x] Domain controlled by Dr. Q (he owns the registrar)
- [x] Old Leadmill PAT revoked (regenerated) + scrubbed from local config
- [x] Billing: latest charge refunded
- [ ] Recurring subscription cancelled (confirm no future charges)
- [ ] Repo owned by Dr. Q · Vercel owned by Dr. Q · GA4 admin = Dr. Q
- [ ] Site live and deployable end-to-end from his accounts
