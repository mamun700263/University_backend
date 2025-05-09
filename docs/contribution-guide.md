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

Here’s a refined and cleaner version of your workflow and commit guidelines:

---

## 🚀 Git Workflow

1. **Switch to `dev` branch**

   ```bash
   git checkout dev && git pull
   ```

2. **Create a new feature branch**

   ```bash
   git checkout -b feature/task-name
   ```

3. **Make your changes**

4. **Stage your work**

   ```bash
   git add .        # Or specify files: git add path/to/file
   ```

5. **Commit using Conventional Commits**

   ```bash
   <type>: <short summary> (#issue_number)
   ```

6. **Push your branch**

   ```bash
   git push origin feature/task-name
   ```

7. **Create a Pull Request**

   * Merge your feature branch into `dev`

---

## ✅ Commit Message Guidelines

Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format:

```
<type>: <short summary> (#issue_number)
```

**Types:**

* `feature` – New feature
* `bugfix` – Bug fix
* `docs` – Documentation changes
* `chore` – Maintenance or non-functional updates
* `hotfix` – Urgent fix for critical issues

### 💡 Examples

* `feature: add login API with JWT (#3)`
* `bugfix: fix user session timeout issue (#5)`
* `chore: apply PEP8 formatting to accounts app (#2)`

---

📖 **Helpful Resources:**

* [Git Branch Cheat Sheet](/docs/git-branch-cheatsheet.md)
* [Branch Management Guide](/docs/branch_management.md)



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
