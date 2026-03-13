#!/usr/bin/env python3
import sys
import subprocess
import os

WORKSPACE_DIR = "/Users/bornforthis/.openclaw/workspace/skills"
GITHUB_REPO_DIR = "/Users/bornforthis/OpenClaw-Skills"

def run_cmd(cmd, cwd=None):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, shell=True, cwd=cwd, text=True, capture_output=True)
    if res.returncode != 0:
        print(f"Error: {res.stderr}")
        sys.exit(1)
    return res.stdout

def sync_skill(skill_name, message):
    source = os.path.join(WORKSPACE_DIR, skill_name) + "/"
    target = os.path.join(GITHUB_REPO_DIR, skill_name) + "/"
    
    if not os.path.exists(source):
        print(f"Source {source} does not exist.")
        sys.exit(1)
        
    if not os.path.exists(target):
        print(f"Target {target} does not exist. Creating...")
        os.makedirs(target, exist_ok=True)
        
    print(f"Syncing {skill_name}...")
    run_cmd(f"rsync -av --delete --exclude='.git' '{source}' '{target}'")
    
    print("Committing and pushing...")
    run_cmd("git add .", cwd=GITHUB_REPO_DIR)
    
    # Check if there are changes
    status = run_cmd("git status --porcelain", cwd=GITHUB_REPO_DIR)
    if not status.strip():
        print("No changes to commit.")
        return

    commit_msg = message if message else f"chore({skill_name}): sync from workspace"
    run_cmd(f'git commit -m "{commit_msg}"', cwd=GITHUB_REPO_DIR)
    run_cmd("git push origin main", cwd=GITHUB_REPO_DIR)
    print(f"Successfully pushed {skill_name} to GitHub!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 sync.py <skill_name> [commit_message]")
        sys.exit(1)
    
    skill_name = sys.argv[1]
    msg = sys.argv[2] if len(sys.argv) > 2 else None
    sync_skill(skill_name, msg)
