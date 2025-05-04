# 🧠 Branch Management Guidelines

When working in a team, it's easy for Git branches to pile up like junk drawers. To keep things clean, scalable, and sane, follow these branch management best practices.

---

## 🧩 Branch Types & Lifespan

| Branch Type      | Keep? | Notes                                         |
|------------------|-------|-----------------------------------------------|
| `main` / `master`  | ✅ Yes | Production-ready, stable code.                |
| `dev` / `develop`  | ✅ Yes | Integration branch for ongoing development.   |
| `feature/*`       | 🔁 Until Merged | Delete after PR is merged.             |
| `bugfix/*`        | 🔁 Until Merged | Same as feature branches.              |
| `hotfix/*`        | 🔁 Until Merged | Used for urgent fixes in `main`.       |
| `chore/*`         | ❌ Only if active | Clean up when done.               |
| `experiment/*`    | ⚠️ Maybe | Keep only if experimental work is valuable. |
| `backup/*`        | ❌ Temporary | Avoid long-term storage.                |

---

## 🧼 Branch Cleanup Rules

- ✅ **After merging a PR**, delete the feature/bugfix branch.
- ⚠️ **If a branch is stale** (>30 days inactive), review and archive or delete it.
- ❌ **Don’t keep dead WIP branches** with no future.

---

## 🛠 Useful Git Commands

```bash
# List branches already merged into current branch
git branch --merged

# Delete a local branch
git branch -d branch-name

# Delete a remote branch
git push origin --delete branch-name
