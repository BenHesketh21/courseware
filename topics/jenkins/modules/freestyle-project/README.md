# Freestyle Project



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Create a Freestyle Project](#create-a-freestyle-project)
- [Source Code Management](#source-code-management)
- [Build Triggers](#build-triggers)
	- [Build Periodically](#build-periodically)
	- [GitHub Hook](#github-hook)
	- [Poll SCM](#poll-scm)
- [Build Environment](#build-environment)
	- [Delete Workspace Before Build Starts](#delete-workspace-before-build-starts)
	- [Secret Texts & Files](#secret-texts--files)
- [Build](#build)
- [Post-build Actions](#postbuild-actions)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview
Freestyle projects in Jenkins are a type of job you can create for almost any automated task.
These are the best place to start for building any sort of general purpose automation in Jenkins.

## Create a Freestyle Project
Go ahead and select `New Item` from the Jenkins dashboard, and then create a new Freestyle Project called `freestyle-project`:
![Freestyle Project](https://i.imgur.com/qGGXAKX.png)

## Source Code Management
This section is used for configuring a source code repository to download.
The job will download the repository you provide into the jobs workspace.

## Build Triggers
The most simple way to run a Jenkins job is by pressing the build button for the job.
However, jobs can be triggered in many ways (we usually try to avoid doing this manually).

### Build Periodically
You can create a schedule here for the job; for example, having it build every hour or at 6:15 PM every Thursday.

### GitHub Hook
This is where GitHub can send a HTTP POST request; for example, a webhook to your Jenkins server to trigger a build of the job.
This must be configured in GitHub and your Jenkins instance must be accessable from the internet for this to work.

### Poll SCM
This feature can be used if your Jenkins instance is not accessible on the internet.
Jenkins will check, using a schedule that you define, whether a change has been made on the configured SCM repository.
As soon as a change has been detected, the job will be executed.
The minimum polling interval is every 1 minute.

## Build Environment

### Delete Workspace Before Build Starts
You will likely want this option checked.
The folder where the job runs on the host machine's file system will be deleted before building again.

### Secret Texts & Files
You may securely use secret texts and files that you have configured in the Credentials section here in the job.
These secrets will also be hidden in the Jenkins logs as well.

## Build
This is likely where you will spend most of your time on a Jenkins job.
The most common build step here is `Execute shell`; other options are available, depending on what plugins you have installed.
Exactly what your job accomplishes is configured here.

## Post-build Actions
You may want to configure your job to react depending on how the build went.
For instance, you could be notified by email if the job failed.
You could also publish a report if the job completed successfully.
Like with most of the options, the sky is the limit; it all depends on what plugins are installed.

## Tasks
These tasks will take you through configuring a very simple Freestyle Project, which will download this repository and execute the `run.sh` script that is in this directory.
1. If you haven't created a Freestyle Project already, go ahead and create one now
2. Lets configure it to download this project and checkout to this subdirectory:
    - Under `Source Code Management` select `Git`
    - Enter `https://github.com/bob-crutchley/notes` into the `Repository URL` field
3. Now add an `Execute shell` build step and enter the following into it:
    ```bash
    cd topics/jenkins/modules/freestyle-project
    sh run.sh
    ```
4. Run the job
5. Navigate to the jobs logs; you should see the contents of this `README.md` file displayed in the logs
