# Git Setup Guide - Syncing Local Repository with Remote

## Problem Diagnosis

You're seeing this error:
```
There is no tracking information for the current branch.
Please specify which branch you want to merge with.

git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:
git branch --set-upstream-to=<remote>/<branch> master
```

**Root Cause**: Your local `master` branch is not configured to track the remote branch, so Git doesn't know which remote branch to pull from.

---

## Solution: Step-by-Step

### Option 1: Quick Fix (RECOMMENDED)

Run this command in your Git Bash terminal:

```bash
git branch --set-upstream-to=origin/main master
```

**OR if your remote branch is named `master`:**

```bash
git branch --set-upstream-to=origin/master master
```

Then pull normally:

```bash
git pull
```

---

### Option 2: Check Remote Configuration

First, verify your remote is set up correctly:

```bash
# View all remotes
git remote -v
```

You should see:
```
origin  https://github.com/omkarmimade9/python-project.git (fetch)
origin  https://github.com/omkarmimade9/python-project.git (push)
```

If remote is missing, add it:

```bash
git remote add origin https://github.com/omkarmimade9/python-project.git
```

---

### Option 3: Pull Specific Branch

If you want to pull without setting tracking, specify the branch:

```bash
git pull origin main
```

**OR:**

```bash
git pull origin master
```

---

### Option 4: Complete Setup (If Repository is Fresh)

If your local repo is out of sync, follow this complete workflow:

```bash
# 1. Add remote if missing
git remote add origin https://github.com/omkarmimade9/python-project.git

# 2. Fetch all remote branches
git fetch origin

# 3. List all branches to see what's available
git branch -a

# 4. Set tracking and pull
git branch --set-upstream-to=origin/main master
git pull

# OR if tracking to main:
git checkout main
git branch --set-upstream-to=origin/main
git pull
```

---

## Understanding Git Branches

### Your Local Setup
- **Current Branch**: `master` (local)
- **Remote URL**: https://github.com/omkarmimade9/python-project
- **Remote Branch**: `main` (on GitHub)

**Important**: GitHub uses `main` as the default branch, but your local is named `master`

### Solution Explanation

```bash
git branch --set-upstream-to=origin/main master
       ↑
       Sets tracking from local 'master' branch
                        ↑
                        to track remote 'origin/main' branch
```

---

## Step-by-Step Visual Guide

### Step 1: Check Current Status
```bash
$ git status
On branch master
No commits yet
```

### Step 2: Set Upstream Tracking
```bash
$ git branch --set-upstream-to=origin/main master
branch 'master' set up to track 'origin/main'.
```

### Step 3: Verify Configuration
```bash
$ git branch -vv
* master abc1234 [origin/main: gone] Initial commit
```

### Step 4: Pull Updates
```bash
$ git pull
Fetching latest from remote...
Updating abc1234..def5678
Fast-forward
 MAIN_EXECUTION_OUTPUT.md | 500 +++
 EXECUTION_GUIDE.md       | 400 +++
 PROJECT_ANALYSIS_REPORT.md | 300 +++
 ...
 18 files changed, 3200 insertions(+)

✓ Successfully synced with remote!
```

---

## Complete Sync Workflow

Use this workflow to fully sync your local repo with remote:

```bash
# Step 1: Navigate to project directory
cd /d/Project

# Step 2: Verify remote is configured
git remote -v

# Step 3: Fetch latest from remote (doesn't modify local)
git fetch origin

# Step 4: View remote branches
git branch -a
# Output should show:
# * master
#   remotes/origin/HEAD -> origin/main
#   remotes/origin/main

# Step 5: Set upstream tracking
git branch --set-upstream-to=origin/main master

# Step 6: Pull all changes
git pull

# Step 7: Verify you have all files
git log --oneline
```

---

## Files You Should Have After Sync

After successful pull, you should have these NEW files:

✅ **Execution & Setup Guides**:
- MAIN_EXECUTION_OUTPUT.md
- EXECUTION_GUIDE.md
- GIT_SETUP_GUIDE.md

✅ **Analysis Documentation**:
- PROJECT_ANALYSIS_REPORT.md
- COMPLETE_CHARTS_DOCUMENTATION.md
- VISUALIZATIONS_GUIDE.md
- CHARTS_SUMMARY.md
- PROJECT_INFO.md

✅ **Data Files**:
- charts_summary.csv
- sample_restaurants_data.csv

✅ **Code Files**:
- main.py
- restaurant_analysis.py
- visualizations.py
- generate_sample_data.py
- create_excel_charts_report.py
- show_visualizations.py
- requirements.txt

**Total Expected**: 17+ files

---

## Troubleshooting Common Issues

### Issue 1: "fatal: 'origin' does not appear to be a 'git' repository"

**Solution**:
```bash
git remote add origin https://github.com/omkarmimade9/python-project.git
git fetch origin
```

### Issue 2: "error: src refspec main does not match any"

**Cause**: Remote branch is named `master`, not `main`

**Solution**:
```bash
git branch --set-upstream-to=origin/master master
```

### Issue 3: "fatal: bad object type"

**Solution**:
```bash
git fetch origin
git fsck --full
git gc --aggressive
```

### Issue 4: Merge conflicts after pull

**Solution**:
```bash
# See conflicts
git status

# Edit conflicted files manually
# Then:
git add .
git commit -m "Resolved merge conflicts"
```

---

## After Successful Sync

### Verify Everything is Updated
```bash
# Check your current commit
git log --oneline -n 5

# Verify you have latest files
ls -la

# Check file count
ls -1 | wc -l
```

### Set Default Branch Globally (Optional)

To avoid this issue in future projects:

```bash
# Configure Git to use 'main' as default for new repos
git config --global init.defaultBranch main
```

### Update Local Master to Main (Advanced)

If you want to rename your local branch to match remote:

```bash
# This renames master to main locally
git branch -m master main
git branch --set-upstream-to=origin/main main
git pull
```

---

## Quick Reference Commands

```bash
# Set tracking
git branch --set-upstream-to=origin/main master

# Pull changes
git pull

# Pull from specific remote
git pull origin main

# View tracking status
git branch -vv

# Show remotes
git remote -v

# Add remote
git remote add origin <url>

# Change remote URL
git remote set-url origin <new-url>

# Fetch without pulling
git fetch origin

# See what will be pulled
git log --oneline master..origin/main
```

---

## GitHub Desktop Alternative

If command line is inconvenient, use GitHub Desktop:

1. Download: https://desktop.github.com
2. Sign in with GitHub account
3. Clone repository or open existing
4. "Fetch origin" button syncs automatically
5. "Pull origin" pulls changes

---

## Testing Your Setup

After syncing, verify with:

```bash
# Run the main Python script
python main.py

# This should output:
# ======================================================================
# ZOMATO/SWIGGY RESTAURANT ANALYSIS SYSTEM
# ======================================================================
# [Step 1] Generating sample restaurant data...
# ✓ Sample data generated successfully
# ...
# [ANALYSIS COMPLETE!]
```

---

## Next Steps

1. ✅ Set upstream tracking
2. ✅ Pull latest changes
3. ✅ Verify all files are present
4. ✅ Run `python main.py`
5. ✅ Review documentation files

---

## Documentation Reference

- **PROJECT_INFO.md** - Project overview
- **EXECUTION_GUIDE.md** - How to run each class
- **MAIN_EXECUTION_OUTPUT.md** - Expected output
- **PROJECT_ANALYSIS_REPORT.md** - Analysis details
- **README.md** - Quick start

---

**Last Updated**: December 26, 2025, 20:15 IST
**Version**: 1.0
**Status**: Ready to sync
