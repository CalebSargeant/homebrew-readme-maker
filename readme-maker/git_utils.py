import os
import subprocess

def get_repo_name():
    if subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], capture_output=True).returncode != 0:
        print("Not in a Git repository. Exiting.")
        exit(1)

    repo_path = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
    return os.path.basename(repo_path)