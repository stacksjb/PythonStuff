import os
import subprocess
import sys

def run_command(command, capture_output=False):
    """Run a shell command and optionally capture its output."""
    try:
        if capture_output:
            result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.strip()
        else:
            subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e.stderr if capture_output else e)
        return None

def get_dangling_commits():
    """Get a list of dangling commits."""
    output = run_command("git fsck --no-reflog | awk '/dangling commit/ {print $NF}'", capture_output=True)
    if output:
        return output.splitlines()
    return []

def evaluate_commit(commit_hash, lost_temp_branch):
    """Evaluate a single dangling commit."""
    print(f"\nEvaluating commit: {commit_hash}")

    # Create a temporary branch for the commit
    temp_branch = f"temp_{commit_hash[:8]}"
    print(f"Checking out commit {commit_hash} into temporary branch {temp_branch}...")
    run_command(f"git checkout -b {temp_branch} {commit_hash}")

    # Allow the user to inspect the commit
    print("\nYou are now on the temporary branch. Inspect the commit and decide what to do.")
    print("Options:")
    print("  [k] Keep: Merge this commit into the 'lost_temp' branch.")
    print("  [s] Skip: Skip this commit.")
    print("  [p] Purge: Permanently delete this commit.")
    print("  [q] Quit: Stop evaluating commits.")
    choice = input("Enter your choice (k/s/p/q): ").strip().lower()

    if choice == "k":
        # Switch back to the lost_temp branch and merge the commit
        print(f"Switching back to {lost_temp_branch} and merging {commit_hash}...")
        run_command(f"git checkout {lost_temp_branch}")
        merge_result = run_command(f"git merge --no-ff --allow-unrelated-histories -m 'Merging dangling commit {commit_hash}' {temp_branch}")
        if merge_result is None:
            print(f"Conflict encountered while merging {commit_hash}. Aborting merge.")
            run_command("git merge --abort")
        else:
            print(f"Successfully merged {commit_hash} into {lost_temp_branch}.")
    elif choice == "s":
        print(f"Skipping commit {commit_hash}.")
    elif choice == "p":
        # Purge the dangling commit
        print(f"Purging commit {commit_hash}...")
        run_command(f"git update-ref -d refs/original/{commit_hash}")
        print(f"Commit {commit_hash} has been permanently deleted.")
    elif choice == "q":
        print("Quitting evaluation.")
        sys.exit(0)
    else:
        print("Invalid choice. Skipping this commit.")

    # Delete the temporary branch
    print(f"Deleting temporary branch {temp_branch}...")
    run_command(f"git checkout {lost_temp_branch}")
    run_command(f"git branch -D {temp_branch}")

def main():
    # Ensure we're in a Git repository
    if not run_command("git rev-parse --is-inside-work-tree", capture_output=True):
        print("This script must be run inside a Git repository.")
        sys.exit(1)

    # Create or switch to the 'lost_temp' branch
    lost_temp_branch = "lost_temp"
    if run_command(f"git show-ref --verify --quiet refs/heads/{lost_temp_branch}"):
        print(f"Switching to existing branch '{lost_temp_branch}'...")
        run_command(f"git checkout {lost_temp_branch}")
    else:
        print(f"Creating and switching to branch '{lost_temp_branch}'...")
        run_command(f"git checkout -b {lost_temp_branch}")

    # Get all dangling commits
    dangling_commits = get_dangling_commits()
    if not dangling_commits:
        print("No dangling commits found.")
        sys.exit(0)

    print(f"Found {len(dangling_commits)} dangling commits.")
    for commit in dangling_commits:
        evaluate_commit(commit, lost_temp_branch)

    print("\nAll dangling commits have been evaluated.")

if __name__ == "__main__":
    main()
