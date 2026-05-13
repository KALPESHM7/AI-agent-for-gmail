import subprocess
import time
import sys

print("Starting OpenClaw AI Agent...")

while True:

    print("\nChecking emails...\n")

    subprocess.run(
        [sys.executable, "email_agent.py"]
    )

    print("\nWaiting 60 seconds...\n")

    time.sleep(60)
