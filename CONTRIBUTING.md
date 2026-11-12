# CONTRIBUTING.md

# Contribution and Collaboration Report

## 1. Project Setup

The project was initiated collaboratively by Tanishqa Chahal (Roll No. 60) and Jahnavi (Roll No. 32). Tanishqa created the GitHub repository and invited Jahnavi as a collaborator, who accepted the invitation and cloned the repository to establish the shared development environment.

**GitHub Repository:** https://github.com/Tanishqa444/Inventory-Management-System


## 2. Individual Contributions

The eight application features were divided equally between the two members, with each independently implementing and testing four features.

### Tanishqa Chahal — Roll No. 60

**Branch:** `feature-member1`

**A. Feature Commits (`products.py`)**

| No. | Commit Message                            |
| --- | ----------------------------------------- |
| 1   | Implement add product functionality       |
| 2   | Implement update product functionality    |
| 3   | Implement product sorting functionality   |
| 4   | Implement view all products functionality |

**B. Additional Commits**

| No. | Commit Message / Contribution                                                                                                                   |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Created the shared project foundation on `main`, including `main.py`, `storage.py`, `inventory.json` and the application menu                   |
| 2   | Added `__pycache__/` and `*.pyc` exclusions to `.gitignore`  and pushed the changes                                                                                   |
| 3   | Removed temporary feature-testing code and pushed the cleanup                                                                                   |
| 4   | Created `conflict-demo.txt` and the `conflict-member1` branch                                                                                   |
| 5   | Updated the conflict demonstration file as Member 1                                                                                             |
| 6   | Fetched Jahnavi’s branch and merged it into conflict-member1, triggering a merge conflict and resolved it by combining both members' changes, then committed and pushed the resolution               |
| 7   | Created and pushed `CONTRIBUTING.md` documentation, including individual contributions, commits, branching, pull requests, reviews and conflict resolution |

### Jahnavi — Roll No. 32

**Branch:** `feature-member2`

**A. Feature Commits (`inventory.py`)**

| No. | Commit Message        |
| --- | --------------------- |
| 1   | Delete Product        |
| 2   | Search Product        |
| 3   | Low Stock Alert       |
| 4   | Total Inventory Value |

**B. Additional Commits**

| No. | Commit Message / Contribution                                                                                                                                                             |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Added Python cache exclusions to `.gitignore` on her branch and pushed the changes                                                                                                                           |
| 2   | Updated conflict demo as Member 2                                                                                                                                                         |
| 3   | Documented collaborative conflict resolution                                                                                                                                              |
| 4   | Created and committed README documentation                                                                                                                                                |
| 5   | Created `conflict-member2` and independently modified the shared conflict demonstration file                                                                                              |
| 6   | Committed and pushed conflicting changes                                                                                                                                                  |
| 7   | Merged Tanishqa's resolved branch, verified combined changes and added a separate documentation contribution to `conflict-demo.txt`                                                       |
| 8   | Authored and pushed `README.md`, covering project objectives, features, technologies, team contributions, project structure, execution instructions, sample output and repository details |

## 3. Branching and Commit Workflow

Our team followed a feature-branch workflow to enable independent development, testing and integration.

| Branch             | Purpose                                      |
| ------------------ | -------------------------------------------- |
| `main`             | Shared foundation and integrated application |
| `feature-member1`  | Tanishqa's product management features       |
| `feature-member2`  | Jahnavi's inventory management features      |
| `conflict-member1` | Tanishqa's conflict demonstration changes    |
| `conflict-member2` | Jahnavi's conflict demonstration changes     |

Both members maintained meaningful commits and pushed their work to the shared GitHub repository.

## 4. Pull Requests and Code Reviews

Both members submitted pull requests targeting `main` and conducted reciprocal code reviews.

| PR | Feature Contribution               | Submitted By | Reviewed and Approved By |
| -- | ---------------------------------- | ------------ | ------------------------ |
| #1 | Four product management features   | Tanishqa     | Jahnavi                  |
| #2 | Four inventory management features | Jahnavi      | Tanishqa                 |

Each examined the other's implementation and changed files on GitHub. Both members also tested the other member's assigned features before approving the pull requests. Both approved PRs were subsequently merged into `main`.

## 5. Deliberate Merge Conflict and Resolution

A deliberate content conflict was introduced in `conflict-demo.txt`.

| Step | Activity                                                                                                                                                         |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Tanishqa created `conflict-demo.txt` on `main` with the original project description.                                                                            |
| 2    | Both members independently created `conflict-member1` and `conflict-member2` from the original `main` branch.                                                    |
| 3    | Tanishqa changed the description to "Inventory project description updated by member 1."                                                                         |
| 4    | Jahnavi independently changed the same line to "Inventory project description updated by Member 2."                                                              |
| 5    | Both committed and pushed their respective changes.                                                                                                              |
| 6    | Tanishqa fetched Jahnavi's branch and merged it into `conflict-member1`, triggering a Git content conflict.                                                      |
| 7    | Tanishqa resolved the conflict in Visual Studio Code by retaining both contributions, then committed and pushed the resolution.                                  |
| 8    | Jahnavi merged the resolved branch into `conflict-member2`, verified the combined changes and added a separate documentation line before committing and pushing. |


## 6. Documentation Contributions

| Member   | Documentation     | Scope                                                                                                                                                  |
| -------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Jahnavi  | `README.md`       | Project overview, objectives, features, technologies, team contributions, project structure, execution instructions, sample output and repository link |
| Tanishqa | `CONTRIBUTING.md` | Individual contributions, commit history, branching workflow, pull requests, code reviews and conflict resolution                                      |

Both documentation files were authored and pushed to the shared GitHub repository.

## 7. Integration and Testing

After both feature branches were merged into `main`, both members synchronized their local repositories using `git pull origin main`.

**Application execution:**

```bash
python main.py
```

Both members jointly executed and tested all eight integrated application features, verifying their functionality after merging into `main`. The integrated application was verified, and temporary test data was cleared to restore `inventory.json` to its initial empty state.

## 8. Conclusion

Both members made substantial and complementary contributions across application development, shared architecture, testing, documentation and Git-based collaboration. The project demonstrates independent feature ownership, meaningful commit practices, branching, remote pushes, pull requests, reciprocal code reviews, application integration and deliberate merge-conflict resolution.
