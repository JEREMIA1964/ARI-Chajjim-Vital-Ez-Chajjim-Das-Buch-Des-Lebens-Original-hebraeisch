#!/usr/bin/env python3
import os
import subprocess
import yaml
from pathlib import Path
from datetime import datetime

# Pfade
REPO_PATH = "/Users/_QQ-SYSTEM/ezchajjim_hns_json"
DATA_PATH = os.path.join(REPO_PATH, "data/ez")
LOG_FILE = os.path.join(REPO_PATH, "branch_log.yaml")
MAX_TOKENS = 3000

branch_log = {"branches": []}

def count_tokens(text: str) -> int:
    return len(text.split())

def git(cmd, ignore_error=False):
    """Git-Befehl ausführen"""
    try:
        subprocess.run(["git"] + cmd, cwd=REPO_PATH, check=True)
    except subprocess.CalledProcessError as e:
        if not ignore_error:
            raise
        else:
            print(f"⚠️ Git-Befehl übersprungen: {cmd}")

def log_branch(section, branch_name, tokens, teile, commit_msg, status):
    branch_log["branches"].append({
        "zeit": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "section": section,
        "branch": branch_name,
        "tokens": tokens,
        "teile": teile,
        "commit_msg": commit_msg,
        "status": status
    })

def save_log():
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        yaml.dump(branch_log, f, allow_unicode=True, sort_keys=False)

def create_branch_and_push(filepath, branch_name, commit_msg, section):
    # Prüfen ob Branch existiert
    result = subprocess.run(
        ["git", "rev-parse", "--verify", branch_name],
        cwd=REPO_PATH,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if result.returncode == 0:
        print(f"⚠️ Branch {branch_name} existiert bereits – wechsle hinein.")
        git(["checkout", branch_name])
    else:
        git(["checkout", "-b", branch_name])

    # Datei ins Staging holen
    git(["add", filepath], ignore_error=True)

    # Commit versuchen
    commit_ok = subprocess.run(
        ["git", "commit", "-m", commit_msg],
        cwd=REPO_PATH
    ).returncode == 0

    if commit_ok:
        status = "committed"
    else:
        status = "no_changes"
        print(f"ℹ️ Keine Änderungen in {filepath}, überspringe Commit.")

    # Push immer machen (auch wenn kein Commit)
    git(["push", "-u", "origin", branch_name], ignore_error=True)

    # Zurück nach main
    git(["checkout", "main"], ignore_error=True)

    log_branch(section, branch_name, 0, 1, commit_msg, status)

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read()
    tokens = count_tokens(data)

    fname = Path(filepath).name
    base, _ = os.path.splitext(fname)

    branch_name = f"{base}"
    commit_msg = f"WWAQ-Upload: {base} (≤{MAX_TOKENS} Tokens)"

    create_branch_and_push(filepath, branch_name, commit_msg, base)

def main():
    files = sorted(Path(DATA_PATH).glob("section_*.json"))
    for f in files:
        process_file(str(f))
    save_log()

if __name__ == "__main__":
    main()
