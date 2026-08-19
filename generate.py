import os, subprocess, math, random
from datetime import datetime, timedelta, timezone

# --- HITUNG JUMLAH COMMIT PER HARI ---
def get_commits_for_today():
    day = datetime.now().weekday()
    if day == 2:  # Wednesday
        return random.randint(10, 15)
    elif day in (1, 3):  # Tue & Thu
        return random.randint(4, 8)
    elif day in (0, 4):  # Mon & Fri
        return random.randint(1, 4)
    else:  # Sat & Sun
        return random.randint(0, 2)

# --- PROSES COMMIT ---
num_commits = get_commits_for_today()

for i in range(max(1, num_commits)):
    with open("keepalive.txt", "a") as f:
        f.write(f"Commit on {datetime.now().isoformat()} - #{i}\n")
    subprocess.run(["git", "add", "keepalive.txt"], check=True)
    subprocess.run(["git", "commit", "-m", "Auto commit untuk activity"], check=True)

# --- GENERATE README DASHBOARD ---
# Setup Waktu UTC & WIB (+7 Jam)
now_utc = datetime.now(timezone.utc)
now_wib = now_utc + timedelta(hours=7)

next_utc = now_utc + timedelta(days=1)
next_wib = now_wib + timedelta(days=1)

fmt = "%Y-%m-%d %H:%M:%S"

# Ganti 'Nasvyni' dan 'green-wave' sesuai akun & repo kamu
OWNER = "Nasvyni"
REPO = "green-wave"

readme_content = f"""# ⊹ ࣪ ˖ GitHub Activity Dashboard!!!

##──────────────────────────★ ˙◟♯ . / Status . !

####──────────────────────────★ ˙◟♯ . / Last Update . !

* UTC : {now_utc.strftime(fmt)} UTC
* WIB : {now_wib.strftime(fmt)} WIB

##──────────────────────────★ ˙◟♯ . / Next Update . !

* UTC : {next_utc.strftime(fmt)} UTC
* WIB : {next_wib.strftime(fmt)} WIB
"""

with open("README.md", "w") as f:
    f.write(readme_content)

subprocess.run(["git", "add", "README.md"], check=True)
subprocess.run(["git", "commit", "-m", "Update Dashboard README"], check=True)
