# 🧭 CCN UST - Dev Board Contribution Guide

Welcome to the dev board project! This doc covers **how we work**, from branching and committing to issue creation and pull requests.

---

## 🧱 Branching Strategy

### Permanent Branches:

* **`main`**: Stable production-ready code. Only maintainers (Mamun) push here.
* **`dev`**: Main development branch. All work merges into this.

### Working Branches (Short-Lived):

Create from `dev`, and name them like:

| Purpose | Prefix     | Example                    |
| ------- | ---------- | -------------------------- |
| Feature | `feature/` | feature/user-auth          |
| Bug Fix | `bugfix/`  | bugfix/fix-login           |
| Chore   | `chore/`   | chore/pep8-accounts        |
| Docs    | `docs/`    | docs/update-readme         |
| Hotfix  | `hotfix/`  | hotfix/db-connection-error |

### Workflow:

1. Checkout `dev` → `git checkout dev && git pull`
2. Create new branch → `git checkout -b feature/task-name`
3. Do your work
4. Commit and push → `git push origin feature/task-name`
5. Open a Pull Request to merge into `dev`

### Read this for better understanding:[git-branch-cheatsheet.md](/docs/git-branch-cheatsheet.md)
---

## ✅ Commit Message Guidelines

Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

```
<type>: <short summary> (#issue_number)
```

**Types:** `feature`, `bugfix`, `docs`, `chore`, `hotfix`

### Examples:

* `feature: add login API with JWT (#3)`
* `bugfix: fix user session timeout (#5)`
* `chore: apply PEP8 to accounts app (#2)`

---

## 🔄 Pull Requests (PR)

* Target branch: `dev` only (never `main`)
* Title: Clear and relevant
* Description:

  * What you did
  * Why you did it
  * How to test it (if needed)
* Link the issue like: `Closes #2`

PRs are reviewed before being merged. Only lead (Mamun) merges to `main`.

---

## 🐛 Issue Creation

Every task, bug, or improvement starts as an **Issue**.

### Issue Template:

```
## 📝 Task
Brief explanation of the task.

## 📂 Affected Areas
List of files/modules.

## 🔧 Tools
(Optional) What tools to use (e.g. black, isort).

## ✅ Done When
- Clear completion criteria

Tag: (feature, bug, chore, docs)
```

Example Issue:

```
#2 Apply PEP8 to accounts app

## 📝 Task
Format code in `accounts/` to follow PEP8.

## 📂 Affected Files
- accounts/views.py
- accounts/forms.py

## 🔧 Tools
- black
- isort

## ✅ Done When
- All files formatted with black
- No functional change
- PR raised and linked to this issue
```

---

Let’s keep it clean, consistent, and collaborative.

> Need help? Ask Mamun or open an issue tagged `question`.
