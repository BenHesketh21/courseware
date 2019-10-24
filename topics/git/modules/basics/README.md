<!--PROPS
{
    "name": "Basics",
    "est_time": 15
}
-->

# Basics



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Basic Workflow](#basic-workflow)
- [Common Commands and Concepts](#common-commands-and-concepts)
	- [Cloning a Repository (`git clone`)](#cloning-a-repository-git-clone)
	- [Staging a Change (`git add`)](#staging-a-change-git-add)
	- [Username and Email in Git Config (`git config`)](#username-and-email-in-git-config-git-config)
		- [Setting Config Globally](#setting-config-globally)
		- [Setting Config Locally](#setting-config-locally)
	- [Local Repository Status (`git status`)](#local-repository-status-git-status)
	- [Commiting a Change (`git commit`)](#commiting-a-change-git-commit)
	- [Pushing Changes (`git push`)](#pushing-changes-git-push)
	- [Retrieving Remote Changes](#retrieving-remote-changes)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview
Git is used for tracking changes in source code during software development.
It is designed for coordinating work amongst programmers, but it can be used to track changes in any set of files.

## Basic Workflow
The basic workflow for using Git includes staging, committing and pushing changes.
Before a change can be committed it must be staged and to apply your changes for everyone else on the team, the changes must be pushed to the remote repository.

## Common Commands and Concepts
As we know, Git is an incredibly popular tool and there are some commands that are likely to be encountered most days when using it in a basic project workflow.

### Cloning a Repository (`git clone`)
To download a remote repository you can use the `git clone` command and provide the URL of the remote repository.
The clone command is very useful because it configures the local repository for you, the remote repository is automatically configured for when you need to push your new changes to it.
```bash
# git clone [REPOSITORY_URL]
git clone https://github.com/bob-crutchley/vim
```

### Staging a Change (`git add`)
Staging is the step that you must take before commiting a change.
Staging is a feature in Git that enables the developer to choose what changes are actually going to get committed to the repository when the commit is made. There is a few ways you stage files:
```bash
# stage all files
git add --all

# stage all files (only if you are at the root of your project)
git add .

# stage selected files: git add [FILES]
git add file_1.txt file_2.txt
git add *.txt
```

### Username and Email in Git Config (`git config`)
Before you can commit changes to the repository you need to have your username and email configured.
This can either be set in the scope of the repository you downloaded or set globally, so that it does not need to be configured for any other repository that you clone.
The information that  you enter will get tied to the commit and this task doesn’t need to be repeated every time you want to make a commit.

#### Setting Config Globally
```bash
# git config --global user.name "[USERNAME]"
git config --global user.name "bob-crutchley"
# git config --global user.email "[EMAIL]"
git config --global user.email "bob@email.com"
```

#### Setting Config Locally
```bash
# git config user.name "[USERNAME]"
git config user.name "bob-crutchley"
# git config user.email "[EMAIL]"
git config user.email "bob@email.com"
```

### Local Repository Status (`git status`)
Knowing the current state of your local repository is very useful so that you can understand what commands to run.
For instance, how can you know what files have been staged and not staged?
```bash
git status
```

### Commiting a Change (`git commit`)
When you make a commit to a Git repository, you are effectively “saving” the changes that you have staged to the repository.
Unlike saving files in most other programs, Git also requires a message to be saved against the commit along with some basic information about the user from the Git config shown above.
What you put in this message is important, so that you understand what it is that you changed on that particular commit.
Commits can be reverted, so it helps when there is a concise message about what was implemented or removed.
```bash
# git commit -m "[COMMIT_MESSAGE]"
git commit -m "initial commit"
```

### Pushing Changes (`git push`)
To apply the changes that you have made in a remote repository you must push them to that remote repository.
Only changes that have been committed will be pushed to the remote repository.
We can use `git push` and provide the remote repository (default is origin) and remote branch to push our changes.
```bash
# git push -u [REMOTE] [REMOTE_BRANCH]
git push -u origin master
```

### Retrieving Remote Changes
Because Git is a collaborative tool, other people could have made changes to code in the remote repository, these changes will need to be pulled down to avoid conflicts in the code.
```bash
# git pull [REMOTE] [REMOTE_BRANCH]
git pull origin master
```

## Tasks
- Create a new Git repository
- Clone the repository to your [USER_HOME]/projects/
- Configure the user.name and user.email properties globally
- Add the following files to the repository folder, it doesn’t matter what these files contain
    - file.java
    - file.cs
    - file1.txt
    - File2.txt
- Stage the java file and commit it
- Stage all text files and commit them
- Push the changes to your remote repository
- Add a new file called file.py
- Stage all files and commit them
- Push the changes to your remote repository
