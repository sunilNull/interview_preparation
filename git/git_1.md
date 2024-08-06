Certainly! Here are 100 questions and answers related to Git, covering basic, intermediate, and advanced concepts, as well as best practices and common scenarios.

### Basic Git Concepts

1. **What is Git?**
    - Git is a distributed version control system that tracks changes to files and coordinates work on those files among multiple people. It was created by Linus Torvalds in 2005.

2. **What is a repository in Git?**
    - A repository (or repo) is a directory that contains all the project files and the entire revision history. It can be local to your computer or a remote repository hosted on a service like GitHub.

3. **What is a commit in Git?**
    - A commit is a snapshot of your repository at a specific point in time. It records changes made to the files and includes a unique ID, a message describing the changes, and metadata like the author and timestamp.

4. **How do you create a new Git repository?**
    - Use the `git init` command to initialize a new repository.
      ```sh
      git init
      ```

5. **How do you clone an existing Git repository?**
    - Use the `git clone` command followed by the repository URL.
      ```sh
      git clone https://github.com/user/repo.git
      ```

6. **What is a branch in Git?**
    - A branch is a parallel version of a repository. It allows you to work on different features or bug fixes separately from the main codebase (usually the `main` or `master` branch).

7. **How do you create a new branch?**
    - Use the `git branch` command followed by the branch name.
      ```sh
      git branch my-branch
      ```

8. **How do you switch to a different branch?**
    - Use the `git checkout` command followed by the branch name.
      ```sh
      git checkout my-branch
      ```

9. **How do you create and switch to a new branch in one command?**
    - Use the `git checkout -b` command followed by the branch name.
      ```sh
      git checkout -b my-branch
      ```

10. **What is a merge in Git?**
    - A merge is an operation that integrates changes from one branch into another. It combines the changes from the source branch into the target branch.

11. **How do you merge a branch into another branch?**
    - First, switch to the target branch using `git checkout`, then use the `git merge` command followed by the source branch name.
      ```sh
      git checkout main
      git merge my-branch
      ```

12. **What is a conflict in Git?**
    - A conflict occurs when changes in two branches being merged conflict with each other, meaning Git cannot automatically merge the changes.

13. **How do you resolve conflicts in Git?**
    - Edit the conflicting files to resolve the conflicts, then stage the resolved files with `git add` and commit the changes.

14. **How do you check the status of your Git repository?**
    - Use the `git status` command to see the state of your working directory and the staging area.
      ```sh
      git status
      ```

15. **How do you view the commit history in Git?**
    - Use the `git log` command to view the commit history.
      ```sh
      git log
      ```

16. **How do you add changes to the staging area?**
    - Use the `git add` command followed by the file name or `.` to add all changes.
      ```sh
      git add myfile.txt
      git add .
      ```

17. **How do you commit changes?**
    - Use the `git commit` command with the `-m` flag followed by a commit message.
      ```sh
      git commit -m "My commit message"
      ```

18. **What is a remote repository in Git?**
    - A remote repository is a version of your project hosted on the internet or network, allowing you to collaborate with others. Examples include repositories on GitHub, GitLab, or Bitbucket.

19. **How do you add a remote repository?**
    - Use the `git remote add` command followed by a name for the remote and the repository URL.
      ```sh
      git remote add origin https://github.com/user/repo.git
      ```

20. **How do you push changes to a remote repository?**
    - Use the `git push` command followed by the remote name and branch name.
      ```sh
      git push origin main
      ```

21. **How do you pull changes from a remote repository?**
    - Use the `git pull` command followed by the remote name and branch name.
      ```sh
      git pull origin main
      ```

22. **What is the difference between `git fetch` and `git pull`?**
    - `git fetch` downloads changes from the remote repository but does not merge them into your working directory. `git pull` is a combination of `git fetch` and `git merge`, meaning it downloads and merges changes.

23. **How do you delete a branch in Git?**
    - Use the `git branch -d` command followed by the branch name to delete a local branch.
      ```sh
      git branch -d my-branch
      ```

24. **How do you delete a remote branch?**
    - Use the `git push` command with the `--delete` option followed by the remote name and branch name.
      ```sh
      git push origin --delete my-branch
      ```

25. **What is a tag in Git?**
    - A tag is a reference that points to a specific commit, often used to mark release points (e.g., v1.0, v2.0).

26. **How do you create a tag?**
    - Use the `git tag` command followed by the tag name.
      ```sh
      git tag v1.0
      ```

27. **How do you push tags to a remote repository?**
    - Use the `git push` command with the `--tags` option.
      ```sh
      git push origin --tags
      ```

28. **What is the `.gitignore` file?**
    - The `.gitignore` file specifies intentionally untracked files that Git should ignore. It typically contains patterns for files or directories to ignore.

29. **How do you create a `.gitignore` file?**
    - Create a file named `.gitignore` in the root of your repository and add the files or directories you want to ignore.
      ```sh
      touch .gitignore
      echo "node_modules/" >> .gitignore
      ```

30. **What is a fork in GitHub?**
    - A fork is a copy of a repository that allows you to make changes without affecting the original repository. It's often used to contribute to other people's projects.

### Intermediate Git Concepts

31. **What is a rebase in Git?**
    - Rebase is a process that moves or combines a sequence of commits to a new base commit. It's often used to keep a clean and linear project history.

32. **How do you perform a rebase?**
    - Use the `git rebase` command followed by the branch name.
      ```sh
      git checkout my-branch
      git rebase main
      ```

33. **What is the difference between `merge` and `rebase`?**
    - `merge` creates a new commit that combines the changes from two branches, preserving the history of both. `rebase` moves the entire branch to a new base, resulting in a linear history without merge commits.

34. **How do you abort a rebase?**
    - Use the `git rebase --abort` command to stop the rebase process and return to the original branch state.
      ```sh
      git rebase --abort
      ```

35. **How do you continue a rebase after resolving conflicts?**
    - After resolving conflicts, use the `git rebase --continue` command.
      ```sh
      git add myfile.txt
      git rebase --continue
      ```

36. **What is a cherry-pick in Git?**
    - Cherry-pick is a Git command that allows you to apply changes from a specific commit to another branch, picking individual commits from one branch and applying them to another.

37. **How do you cherry-pick a commit?**
    - Use the `git cherry-pick` command followed by the commit hash.
      ```sh
      git cherry-pick <commit-hash>
      ```

38. **What is a detached HEAD in Git?**
    - A detached HEAD state occurs when you are not on a branch but are instead directly referencing a specific commit. Changes made in this state can be lost if not properly saved.

39. **How do you return to a previous commit without creating a new branch?**
    - Use the `git checkout` command followed by the commit hash.
      ```sh
      git checkout <commit-hash>
      ```

40. **What is the `git stash` command used for?**
    - `git stash` temporarily saves your changes that are not ready to be committed so you can work on something else and later apply the stashed changes.

41. **How do you stash your changes?**
    - Use the `git stash` command.
      ```sh
      git stash
      ```

42. **How do you apply stashed changes?**
    - Use the `git stash apply` command.
      ```sh
        git stash apply
    ```

43. **How do you list stashes?**
    - Use the `git stash list` command.
      ```sh
      git stash list
      ```

44. **How do you drop a stash?**
    - Use the `git stash drop` command followed by the stash reference (e.g., `stash@{0}`).
      ```sh
      git stash drop stash@{0}
      ```

45. **What is a submodule in Git?**
    - A submodule is a repository embedded inside another repository. Submodules allow you to keep a Git repository as a subdirectory of another Git repository.

46. **How do you add a submodule?**
    - Use the `git submodule add` command followed by the repository URL and the directory where you want to add it.
      ```sh
      git submodule add https://github.com/user/repo.git subdir
      ```

47. **How do you update submodules?**
    - Use the `git submodule update` command.
      ```sh
      git submodule update --init --recursive
      ```

48. **What is Git flow?**
    - Git flow is a branching model for Git, designed by Vincent Driessen, that defines a strict branching model for projects and offers a standard way of managing releases, hotfixes, and feature branches.

49. **How do you initialize Git flow in a repository?**
    - Use the `git flow init` command.
      ```sh
      git flow init
      ```

50. **What is `git bisect`?**
    - `git bisect` is a command that uses binary search to find the commit that introduced a bug by checking out different commits and running tests.

51. **How do you start a bisect session?**
    - Use the `git bisect start` command followed by the `bad` and `good` commit references.
      ```sh
      git bisect start
      git bisect bad <bad-commit>
      git bisect good <good-commit>
      ```

52. **How do you mark a commit as good or bad during a bisect session?**
    - Use the `git bisect good` or `git bisect bad` command.
      ```sh
      git bisect good
      git bisect bad
      ```

53. **How do you end a bisect session?**
    - Use the `git bisect reset` command.
      ```sh
      git bisect reset
      ```

54. **What is `git blame`?**
    - `git blame` shows what revision and author last modified each line of a file. It's useful for identifying who made changes and when.

55. **How do you use `git blame`?**
    - Use the `git blame` command followed by the file name.
      ```sh
      git blame myfile.txt
      ```

56. **What is `git diff`?**
    - `git diff` shows the differences between commits, commit and working tree, etc. It helps you see changes between different states of your repository.

57. **How do you use `git diff`?**
    - Use the `git diff` command to see changes between the working directory and the index, or specify commit references.
      ```sh
      git diff
      git diff <commit1> <commit2>
      ```

58. **What is `git rm`?**
    - `git rm` removes files from the working directory and the index. It's used to delete tracked files.

59. **How do you use `git rm`?**
    - Use the `git rm` command followed by the file name.
      ```sh
      git rm myfile.txt
      ```

60. **What is `git mv`?**
    - `git mv` moves or renames a file, directory, or symlink. It stages the move or rename for the next commit.

61. **How do you use `git mv`?**
    - Use the `git mv` command followed by the source and destination.
      ```sh
      git mv oldfile.txt newfile.txt
      ```

62. **What is `git reset`?**
    - `git reset` is used to undo changes. It can modify the index, working directory, and commit history depending on the options used.

63. **How do you reset the index and working directory to a previous commit?**
    - Use the `git reset --hard` command followed by the commit reference.
      ```sh
      git reset --hard <commit>
      ```

64. **What is the difference between `git reset --soft`, `--mixed`, and `--hard`?**
    - `--soft`: Moves the HEAD to the specified commit and keeps the changes in the index and working directory.
    - `--mixed`: Moves the HEAD to the specified commit, resets the index but not the working directory.
    - `--hard`: Moves the HEAD to the specified commit and resets both the index and working directory.

65. **What is `git revert`?**
    - `git revert` creates a new commit that undoes the changes from a previous commit. It's used to safely undo changes without altering the commit history.

66. **How do you revert a commit?**
    - Use the `git revert` command followed by the commit hash.
      ```sh
      git revert <commit-hash>
      ```

67. **What is `git show`?**
    - `git show` displays information about a commit, including the changes introduced by the commit.

68. **How do you use `git show`?**
    - Use the `git show` command followed by the commit hash.
      ```sh
      git show <commit-hash>
      ```

69. **What is `git tag -a`?**
    - `git tag -a` creates an annotated tag, which includes a message and is stored as a full object in the Git database.

70. **How do you create an annotated tag?**
    - Use the `git tag -a` command followed by the tag name and `-m` for the message.
      ```sh
      git tag -a v1.0 -m "Version 1.0"
      ```

### Advanced Git Concepts

71. **What is a Git hook?**
    - Git hooks are scripts that run automatically in response to specific Git events (e.g., committing, merging). They can be used to enforce policies, run tests, or automate tasks.

72. **How do you create a Git hook?**
    - Place an executable script in the `.git/hooks` directory with the appropriate hook name (e.g., `pre-commit`, `post-merge`).

73. **What is a bare repository?**
    - A bare repository is a repository without a working directory. It contains only the Git database and is used for sharing a repository, typically on a server.

74. **How do you create a bare repository?**
    - Use the `git init --bare` command.
      ```sh
      git init --bare
      ```

75. **What is a Git worktree?**
    - Git worktree allows you to have multiple working directories associated with a single Git repository, enabling you to work on different branches simultaneously.

76. **How do you create a new worktree?**
    - Use the `git worktree add` command followed by the directory and branch name.
      ```sh
      git worktree add ../new-worktree my-branch
      ```

77. **What is `git filter-branch`?**
    - `git filter-branch` is a powerful tool for rewriting Git history, allowing you to modify commits, remove sensitive data, or change the structure of the repository.

78. **How do you use `git filter-branch`?**
    - Use the `git filter-branch` command with various options to specify the desired changes.
      ```sh
      git filter-branch --tree-filter 'rm -rf secrets.txt' HEAD
      ```

79. **What is `git fsck`?**
    - `git fsck` verifies the integrity of the Git database, checking for corrupted objects and other issues.

80. **How do you use `git fsck`?**
    - Use the `git fsck` command.
      ```sh
      git fsck
      ```

81. **What is `git gc`?**
    - `git gc` (garbage collection) cleans up unnecessary files and optimizes the local repository.

82. **How do you use `git gc`?**
    - Use the `git gc` command.
      ```sh
      git gc
      ```

83. **What is `git archive`?**
    - `git archive` creates an archive of files from a specific commit or branch. It's used to package a repository's contents for distribution.

84. **How do you use `git archive`?**
    - Use the `git archive` command followed by the commit or branch and the output format.
      ```sh
      git archive --format=zip HEAD > archive.zip
      ```

85. **What is `git bundle`?**
    - `git bundle` creates a single file containing the contents of a repository. It's useful for transferring repositories without a network connection.

86. **How do you create a Git bundle?**
    - Use the `git bundle` command followed by the file name and the reference(s) to include.
      ```sh
      git bundle create repo.bundle main
      ```

87. **What is the `refs` directory in Git?**
    - The `refs` directory stores references to commit objects, including branches,

 tags, and other pointers to specific commits.

88. **What is the `objects` directory in Git?**
    - The `objects` directory contains all the Git objects, including commits, trees, blobs, and tags. These objects form the Git database.

89. **What is `git reflog`?**
    - `git reflog` records changes to the references (e.g., branch heads) in your repository. It's useful for recovering lost commits and understanding changes.

90. **How do you use `git reflog`?**
    - Use the `git reflog` command to view the reference log.
      ```sh
      git reflog
      ```

91. **What is `git blame -e`?**
    - `git blame -e` shows the email of the author along with the commit information for each line of a file.

92. **How do you use `git blame -e`?**
    - Use the `git blame -e` command followed by the file name.
      ```sh
      git blame -e myfile.txt
      ```

93. **What is `git sparse-checkout`?**
    - `git sparse-checkout` allows you to checkout only a subset of the files in a repository, useful for large repositories where you don't need all the files.

94. **How do you set up sparse checkout?**
    - Use the following commands:
      ```sh
      git sparse-checkout init --cone
      git sparse-checkout set <directory>
      ```

95. **What is a `git hook`?**
    - A Git hook is a script that runs automatically in response to specific Git events like commits, merges, and pushes.

96. **How do you enable a Git hook?**
    - Place an executable script with the hook's name (e.g., `pre-commit`, `post-merge`) in the `.git/hooks` directory.

97. **What is `git rerere`?**
    - `git rerere` stands for "reuse recorded resolution." It helps to remember how you resolved conflicts, so if the same conflict arises again, Git can automatically resolve it using the recorded resolution.

98. **How do you enable `git rerere`?**
    - Use the `git config` command to enable rerere.
      ```sh
      git config --global rerere.enabled true
      ```

99. **What is `git mergetool`?**
    - `git mergetool` is a command that launches a merge resolution program to help resolve conflicts in your working directory.

100. **How do you use `git mergetool`?**
    - Use the `git mergetool` command after a conflict has occurred.
      ```sh
      git mergetool
      ```

These questions and answers cover a broad range of Git topics and should help you prepare for interviews, as well as deepen your understanding of Git.
