import subprocess, random
from datetime import datetime

def get_commits_for_today():
    day = datetime.now().weekday()  # Mon=0, Tue=1, Wed=2, Thu=3, Fri=4, Sat=5, Sun=6
    
    if day == 2:
        return random.randint(10, 15)
    elif day in (1, 3):
        return random.randint(4, 8)
    elif day in (0, 4):
        return random.randint(1, 4)
    else:
        return random.randint(0, 2)

num_commits = get_commits_for_today()

if num_commits > 0:
    for i in range(num_commits):
        with open("activity.txt", "a") as f:
            f.write(f"Commit on {datetime.now().isoformat()} - #{i}\n")
        
        subprocess.run(["git", "add", "activity.txt"], check=True)
        subprocess.run(["git", "commit", "-m", f"daily update #{i}"], check=True)
else:
    print("No commits scheduled for today.")
