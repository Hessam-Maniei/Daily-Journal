from datetime import datetime
import os

def create_journal():
    today = datetime.now().strftime("%Y-%m-%d")
    folder = "journal"
    os.makedirs(folder, exist_ok=True)

    filename = os.path.join(folder, f"{today}.md")
    with open(filename, "a") as f:
        f.write(f"\nUpdate at {datetime.now().strftime('%H:%M:%S')}\n")

    print(f"Updated journal entry: {filename}")

if __name__ == "__main__":
    create_journal()

