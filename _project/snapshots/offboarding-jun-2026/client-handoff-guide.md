# Your Website — Owner's Guide

**Prepared for Dr. Imran Qureshi · drimranqureshi.com · June 2026**

This guide covers three things: the one-time setup to take ownership (about 30 minutes), how to make changes to your website without knowing how to code, and what (little) it costs to run. Keep this document — it answers most questions you'll have later.

---

## What you now own

Your web presence is four pieces. After the handoff, every one of them is in accounts you control:

| Piece | What it does | Where it lives |
|---|---|---|
| **Your domain** — drimranqureshi.com | Your address on the internet | Your domain registrar (already yours) |
| **Your website files** | The pages themselves — 50+ pages of content | GitHub (transferring to you) |
| **Your hosting** | Puts the pages on the internet, fast | Vercel (you'll set up below) |
| **Your analytics** | Shows visitors, calls, and bookings | Google Analytics (I'll add you as admin) |

Your website is hand-built for speed. There is no software to update, no plugins to break, and no security patches to install — one reason it loads fast and ranks well. The trade-off: it's not a drag-and-drop editor. Section 3 covers how changes get made.

---

## 1. One-time setup (about 30 minutes)

### Step 1 — Create a GitHub account and accept the website transfer

GitHub is where your website's files live. Think of it as a Dropbox for websites, with a full history of every change.

1. Go to **github.com** and click **Sign up**. Use an email you check regularly. It's free.
2. Send me your GitHub username.
3. I'll transfer the website to you. You'll get an email from GitHub — **click Accept transfer** within 24 hours.
4. Done. The website's files now belong to your account.

### Step 2 — Create a Vercel account and connect your website

Vercel is the hosting service — it takes the files from GitHub and serves them to the world.

1. Go to **vercel.com** and click **Sign up**. Choose **"Continue with GitHub"** and log in with the account from Step 1. This links the two automatically.
2. On your Vercel dashboard, click **Add New → Project**.
3. You'll see your website repository (the files from Step 1) in the list. Click **Import**.
4. On the settings screen, change nothing — the site configures itself. Click **Deploy**.
5. In about a minute you'll see your website live at a temporary address ending in `.vercel.app`. That confirms it works.

**One honest note on cost:** Vercel's free plan is meant for personal projects. For a business website, the right plan is **Vercel Pro at about $20/month** — that's your entire hosting bill. (For comparison, typical medical-website hosting runs $50–150/month.)

### Step 3 — Point your domain at your new hosting

This is the moment your domain switches from my hosting account to yours. Best done in the evening; any interruption is brief.

1. In your Vercel project, go to **Settings → Domains** and add both `drimranqureshi.com` and `www.drimranqureshi.com`.
2. Vercel will show you one or two settings (called DNS records) to enter at your domain registrar — the company where you bought drimranqureshi.com. Log in there, find DNS settings, and enter exactly what Vercel shows.
3. Within an hour (usually minutes), Vercel shows a green checkmark and your website is being served entirely from your own accounts.
4. Tell me when this is done — I'll shut down my copy and add you as admin on Google Analytics.

If you'd rather do this step together on a 15-minute call, just say so. It's the only step with any real fiddliness.

---

## 2. How to make changes without coding

You have three good options, from smallest to biggest change.

### Option A — Small text changes: do them yourself on GitHub

Changing a phone number, correcting a sentence, updating office hours — you can do this in your browser in five minutes.

1. Log in at github.com and open your website repository.
2. Click the page you want to edit — for example, `contact.html`. (The homepage is `index.html`; treatment pages are in the `treatments` folder.)
3. Click the **pencil icon** (top right of the file view).
4. Find the text you want to change. **Press Ctrl+F (Cmd+F on Mac) and search for the exact words** as they appear on the website — this drops you right where you need to be.
5. Change only the words. **Two safety rules:**
   - Never change anything inside angle brackets — everything that looks like `<this>` is machinery, not content.
   - If the same text appears several times in the file, it may be intentional (some text appears once for Google and once for visitors). Change all matching copies of the sentence you're editing.
6. Click **Commit changes** (the green button), then **Commit changes** again on the pop-up.
7. That's it. Your live website updates itself within about a minute.

**If something looks wrong afterwards:** don't panic — nothing is ever lost. GitHub keeps every previous version. Any developer (or I) can restore the page in two minutes.

### Option B — Bigger text changes: use an AI assistant

For rewriting a paragraph or adding a new FAQ, tools like ChatGPT or Claude handle the machinery for you:

1. On GitHub, open the page file, click the pencil, and **copy the entire file**.
2. Paste it into ChatGPT or Claude and say what you want in plain English — *"Change the second paragraph to say … Keep everything else exactly the same, and give me back the complete file."*
3. Paste the result back over the file's contents and commit, as in Option A.
4. Check the live page a minute later. If anything looks off, restore the previous version.

### Option C — Anything structural: use a developer

New pages, design changes, new photos, layout work — that's developer work, and this website is deliberately easy for any developer to work on (they will recognize the setup immediately; there's nothing exotic here). Expect small jobs to take an hour or two. I'm also happy to remain your on-call option for occasional changes — just email me.

### If you ever want full self-service

If you someday want a drag-and-drop editor (like Squarespace), that's a rebuild — a one-time project that trades away some of the site's speed. There's no urgency; it's just an option to know about. Ask me or any web professional and they can quote it.

---

## 3. The address change (one open item)

Your website still shows the Cinco Ranch address. CLS is handling your Google Business Profile for the move — but **the address printed on the website itself is separate**, and it appears on every page.

My offer stands: send me the exact suite number and ZIP for 1400 Ravello (I believe it's 77450 — worth confirming with CLS), and I'll update the entire website as a final courtesy before we finish the handoff. Otherwise, hand this guide to whoever manages the site next — it's a routine job for a developer.

---

## 4. Running costs and upkeep

| Item | Cost | When |
|---|---|---|
| Domain renewal (drimranqureshi.com) | ~$15–20/year | Yearly, at your registrar — **keep this renewed; it's your address** |
| Vercel Pro hosting | ~$20/month | Monthly |
| GitHub | Free | — |
| Google Analytics | Free | — |
| Software updates, security patches | **None needed** | The site has no software to maintain |

**Total: roughly $20/month plus the yearly domain fee.** Nothing else expires or needs attention.

---

## 5. Keep these safe

- GitHub login (website files)
- Vercel login (hosting)
- Domain registrar login (your domain — the most important one)
- Google account with Analytics access

If a future marketing person or developer needs access, **add them to your accounts** rather than sharing your passwords — GitHub, Vercel, and Analytics all support inviting collaborators.

---

## Questions?

Email me any time — happy to point you or whoever helps you next in the right direction. It's been a genuine pleasure building this with you.

— Rameel
