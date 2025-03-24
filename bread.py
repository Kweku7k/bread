import os
import datetime
import subprocess

# GitHub repository details
REPO_OWNER = "kweku7k"
REPO_NAME = "bread"

# Get the current time
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Update README.md
readme_path = "README.md"
with open(readme_path, "a") as file:
    file.write(f"\nLast updated: {timestamp}")

# Git commands to commit and push
subprocess.run(["git", "config", "--global", "user.name", "GitHub Actions Bot"])
subprocess.run(["git", "config", "--global", "user.email", "actions@github.com"])
subprocess.run(["git", "add", readme_path])
subprocess.run(["git", "commit", "-m", f"Updated README at {timestamp}"])
subprocess.run(["git", "push"])