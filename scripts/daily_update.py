"""
Daily Update Script
Appends a lightweight, genuine-looking engineering log entry with IST date/time.
Ensures idempotency (skips if today's entry already exists).
"""

import os
import sys
import random
from datetime import datetime, timezone, timedelta

# Ensure UTF-8 stdout/stderr across platforms
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Define Indian Standard Time (UTC +5:30)
IST = timezone(timedelta(hours=5, minutes=30))

# Rotating genuine micro-log messages
LOG_MESSAGES = [
    "Reviewing documentation and library updates 📖",
    "Daily check-in & environment maintenance ✅",
    "Explored performance benchmarks and optimization techniques ⚡",
    "Code cleanup, dependency checks, and routine refactoring 🧹",
    "Studying design patterns and architecture best practices 📐",
    "Experimenting with automation scripts and workflow enhancements ⚙️",
    "Reading technical articles and release notes 🔍",
    "Algorithm practice and system design notes update 💡",
    "Checking CI/CD pipeline metrics and build logs 📊",
    "Writing notes on debugging techniques and tooling 🛠️",
    "Routine repository housekeeping and index update 📦",
    "Exploring cloud-native tooling and developer experience improvements 🚀"
]

def get_log_file_path() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    return os.path.join(repo_root, "daily-log", "log.md")

def update_daily_log(force: bool = False) -> bool:
    log_file_path = get_log_file_path()
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    now_ist = datetime.now(IST)
    date_str = now_ist.strftime("%Y-%m-%d")
    time_str = now_ist.strftime("%H:%M")

    # If log file exists, check if today's date already has an entry (unless force is True)
    if not force and os.path.exists(log_file_path):
        with open(log_file_path, "r", encoding="utf-8") as f:
            content = f.read()
            if f"- **{date_str}" in content or f"[{date_str}]" in content:
                print(f"[SKIP] Log entry for {date_str} (IST) already exists.")
                return False
    elif not os.path.exists(log_file_path):
        # Create file with initial header if missing
        with open(log_file_path, "w", encoding="utf-8") as f:
            f.write("# Daily Activity Log\n\nA lightweight automated check-in and developer log.\n\n---\n\n")

    # Pick a pseudo-random message using day-of-year + seed for consistent rotation or random selection
    selected_message = random.choice(LOG_MESSAGES)
    new_entry = f"- **{date_str} {time_str} IST** — {selected_message}\n"

    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(new_entry)

    print(f"[SUCCESS] Appended entry for {date_str} {time_str} IST: {selected_message}")
    return True

if __name__ == "__main__":
    force_run = "--force" in sys.argv or os.environ.get("FORCE_UPDATE", "").lower() == "true"
    updated = update_daily_log(force=force_run)
    if not updated:
        # Exit code 0 so GitHub Actions doesn't fail, but script signals no change
        sys.exit(0)
