# 🤖 Daily GitHub Contribution Bot

A fully automated, server-side GitHub Actions workflow that appends a lightweight, genuine-looking check-in entry to `daily-log/log.md` every day.

---

## 📌 What This Does and Why

- **Automated & Serverless**: Runs completely on GitHub Actions servers — no local cron jobs, VPS, or running laptop required.
- **Meaningful Diffs**: Appends genuine developer log entries with IST timestamps instead of empty or spammy commits.
- **Idempotent**: Prevents double-commits if triggered multiple times on the same date.
- **Humanized Jitter**: Automatically randomizes scheduled execution within a 0–2 hour window so commits don't happen at the exact same second each day.
- **Zero Secrets / PAT Management**: Uses the standard built-in `GITHUB_TOKEN` provided automatically by GitHub Actions.

---

## 🚀 Quick Setup

### 1. Enable GitHub Actions Write Permissions (Required)
By default, GitHub Actions workflows have read-only access. You must grant write access for the bot to push commits:

1. In your GitHub repository, navigate to **Settings** > **Actions** > **General**.
2. Scroll down to **Workflow permissions**.
3. Select **"Read and write permissions"**.
4. Click **Save**.

---

## 🧪 Testing the Bot Manually

You don't have to wait for the cron schedule to test the workflow:

1. Go to the **Actions** tab in your repository.
2. Select **Daily Contribution Bot** from the left sidebar.
3. Click the **Run workflow** dropdown button on the right, and choose **Run workflow**.
4. Manual runs will automatically skip the randomized sleep delay and execute immediately.

---

## ⏰ Changing the Schedule & Timezone

The schedule is configured in [`.github/workflows/daily-commit.yml`](.github/workflows/daily-commit.yml) using standard cron syntax (in **UTC**):

```yaml
on:
  schedule:
    # 04:30 UTC = 10:00 AM IST
    - cron: '30 4 * * *'
```

### Common Cron Examples:
| Schedule | UTC Cron Expression | Local Time (IST) |
|---|---|---|
| Morning (~9:30 AM IST) | `0 4 * * *` | 9:30 AM IST |
| Afternoon (~2:00 PM IST) | `30 8 * * *` | 2:00 PM IST |
| Evening (~8:00 PM IST) | `30 14 * * *` | 8:00 PM IST |
| Twice a day | `0 4,14 * * *` | 9:30 AM & 7:30 PM IST |

---

## 📂 Project Structure

```
├── .github/
│   └── workflows/
│       └── daily-commit.yml    # GitHub Actions workflow definition
├── daily-log/
│   └── log.md                 # Markdown log file updated daily
├── scripts/
│   └── daily_update.py        # Python script for updating log entries
└── BOT_README.md              # Bot documentation
```
