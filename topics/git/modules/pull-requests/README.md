# Pull Requests



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Collaborative Tool](#collaborative-tool)
- [Creating a Pull Request](#creating-a-pull-request)
	- [1) PR From a Branch Within a Repository](#1-pr-from-a-branch-within-a-repository)
		- [Create a feature branch and push it to VCS](#create-a-feature-branch-and-push-it-to-vcs)
		- [Create a Pull Request](#create-a-pull-request)
	- [2) PR from a Forked Repository](#2-pr-from-a-forked-repository)
		- [Create a Pull Request](#create-a-pull-request-1)
- [Closing a Pull Request](#closing-a-pull-request)
- [After a Pull Request](#after-a-pull-request)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview
Pull requests let you tell others about changes you've pushed to a GitHub repository.  

Once a pull request is sent, interested parties can review the set of changes, discuss potential modifications, and even push follow-up commits if necessary.

## Collaborative Tool
Pull Requests are commonly used by teams and organisations collaborating using the **Shared Repository Model**.

This is where everyone shares a single repository, and seperate (topic) branches are used to develop features and isolate changes.

Many open-source projects on Github use pull requests to manage changes from contributors, as they are useful in providing a way to notify project maintainers about any changes made.

Once the project maintainer has been notified of a change via a pull requests, it opens the door for code review and general discussion about a set of changes.
This is really great, as it can be done before any changes are merged into the master branch.

## Creating a Pull Request
There are 2 main flows when dealing with pull requests:

### 1) PR From a Branch Within a Repository

#### Create a feature branch and push it to VCS
1. Clone a repository down using `git clone [URL to repository]` and `cd` into it
2. Create and switch to a new (feature) branch using `git checkout -b [new branch name]`
3. Make changes on your feature branch, and then use `git add` and `git commit` to stage your changes. You will need to configure your VCS email and username at this point, using `git config` (if you haven't already) 
4. Push the feature branch up to git using `git push origin [new branch name]`
5. You new branch should now be reflected in your VCS

#### Create a Pull Request
This is done on your VCS GUI (in this example, we are using GitHub):

1. Go to the repository you're working with and click on the 'Compare and pull request' button:

![](https://i.imgur.com/4C9qMiD.png?1)

2. You will need to choose which branch you want the changes to eventualy be implemented on (`base`), and which branch the proposed changes are currently on (`compare`):

![](https://i.imgur.com/lWX58HA.png?1)

3. At this point, you can give your pull request a title and add some comments, for context:

![](https://i.imgur.com/geCW0mU.png?1)

4. You can configure additional options on the right hand side, such as assigning a reviewer, adding a label, etc:

![](https://i.imgur.com/i0zyMAG.png?2)

5. Click 'Create pull request':

![](https://i.imgur.com/xwRCTyk.png?3)

### 2) PR from a Forked Repository

#### Create a Pull Request
This is also done on your VCS GUI:

1. Ensure you have a forked repository, and have made some changes to it
2. Navigate to the repository from which you created your fork
3. Click on 'New pull request':

![](https://help.github.com/assets/images/help/pull_requests/pull-request-start-review-button.png)

4. Amend your `base` and `compare` to reflect to correct branches
5. Click on 'compare accross forks':

![](https://help.github.com/assets/images/help/pull_requests/compare-across-forks-link.png)

6. Confirm that the base fork is the repository you'd like to merge changes into. Use the `base` drop-down menu to select the branch of the repository you'd like to merge changes into:

![](https://help.github.com/assets/images/help/pull_requests/choose-base-fork-and-branch.png)

7. Use the head fork drop-down menu to select your forked repository, then use the compare branch drop-down menu to select the branch you made your changes in:

![](https://help.github.com/assets/images/help/pull_requests/choose-head-fork-compare-branch.png)

8. Insert a title and description for your pull request
9. Configure any other options you want on the right hand side
10. Click 'Create Pull Request'

## Closing a Pull Request
You can simply click on the "Close" button on the pull request page to close it:

![](https://i.imgur.com/fsFyzqL.png?1)

You will be given the option to delete the branch directly at this point, should you wish to do so. 

## After a Pull Request
Once a pull request has been opened, it can be reviewed by other collaborators and merged into the base branch you dictated earlier.

## Tasks
- Try to create a new feature branch from an existing GitHub project (or create a new project)
- Create a pull request to have the new feature merged into the project
- Fork a repository from GitHub - this can be any repository you feel like
- Make some changes in the forked repository
- Create a pull request to have your feature merged into the original project
