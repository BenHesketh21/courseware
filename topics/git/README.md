# Git
<!--TOC_START-->
## Contents
- [Overview](#overview)
	- [Software and Version Control](#software-and-version-control)
	- [Online Services That Use Git](#online-services-that-use-git)
- [Installation](#installation)
	- [Windows](#windows)
	- [Linux](#linux)
		- [RHEL/CentOs](#rhelcentos)
		- [Debian/Ubuntu](#debianubuntu)
	- [Mac OS X](#mac-os-x)
		- [DMG File](#dmg-file)
- [Modules](#modules)

<!--TOC_END-->
## Overview
Git is a distributed version-control system for tracking changes in source code during software development.
It is designed for coordinating work among programmers, but it can be used to track changes in any set of files.
Its goals include speed, data integrity, and support for distributed, non-linear workflows.
### Software and Version Control
When developing software, especially in an enterprise environment when the software is going to be a product for a client, it is almost unthinkable to not have the source code in some form of Version Control System.
Version Control Systems keep track of every single change that has been made to the code base, usually also with an indication of the time that change was made or “committed” and a comment from the developer who had made that change.
### Online Services That Use Git
Git is the underlying tool for quite a few very popular services such as GitHub, GitLab and BitBucket.
These services add more features for managing project source code such as security, access control, pull requests and other project documentation and planning tools depending on the service.
## Installation
### Windows
1. Navigate to the Git download for Windows in your preferred web browser (the download should automatically start when you go to the link below):

https://git-scm.com/download/win

2. Click on next for every option and finally click install
3. The installer adds the Git program to your PATH environment variable, so it can be accessed either in the Windows command prompt or by using the Git Bash terminal that was also installed.
### Linux
Because of how popular the Git tool is, it can be installed by using almost any package manager that is included with the operating system, below are examples for RHEL/CentOS and Ubuntu.
#### RHEL/CentOs
```bash
sudo yum install -y git
```
#### Debian/Ubuntu
```bash
sudo apt install -y git
```
### Mac OS X
Git can easily  be installed on Mac OS by downloading and running a DMG file or by using the brew package manager if you have it installed.
#### DMG File
Similar to Windows, you can navigate to the Git download page for Mac OS and run the installer (DMG file): https://git-scm.com/download/mac
```bash
brew install git
```
<!--MODULES_START-->
## Modules
- [Basics](./modules/basics)
- [Branching](./modules/branching)
- [Cloning](./modules/cloning)
- [Forking](./modules/forking)
- [GitHub Project Boards](./modules/github-project-boards)
- [GitHub Reviews](./modules/github-reviews)
- [Merging](./modules/merging)
- [Pull Requests](./modules/pull-requests)
- [Reverting](./modules/reverting)
<!--MODULES_END-->
