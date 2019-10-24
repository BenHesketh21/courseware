# Installation Wizard
Configuring Jenkins using a graphical interface.

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Unlocking Jenkins](#unlocking-jenkins)
- [Customize Jenkins](#customize-jenkins)
- [Plugin Installation](#plugin-installation)
- [Create the First Admin User](#create-the-first-admin-user)
- [Instance Configuration](#instance-configuration)
- [Dashboard](#dashboard)
	- [Dashboard Links](#dashboard-links)

<!--TOC_END-->
## Overview
This document aims to guide you through the setup process of Jenkins, through the graphical (web) interface.

## Unlocking Jenkins
To make sure that it is you who is trying to configure Jenkins, the setup requires you to enter an initial admin password; this is stored on the file system of the machine that Jenkins is running on.
The page clearly states where this file is located - you just need to copy the contents of it into the text field and click `Continue`.

![Jenkins Initial Admin Password](https://i.imgur.com/Poqds4F.png)

## Customize Jenkins
Jenkins is highly configurable due to the amount of plugins that you can install.
This is fantastic, but, if you are new to Jenkins, you might not have much of an idea about what plugins you would want.
Fortunately, the setup gives you the option to install suggested plugins - select this option.

![Customize Jenkins](https://i.imgur.com/hg1BlXL.png)

## Plugin Installation
For this part, there isn't much to do but wait.
The suggested plugins, or plugins that you selected, will be installed; how fast they are installed depends on your internet speed.
If plugins are failing to install, make sure that you have the latest version on Jenkins installed.

![Plugin Installation](https://i.imgur.com/tNnEJVf.png)

## Create the First Admin User
At this point, you can either fill in the form, to have your details saved into the first admin account, or continue as admin; this will mean that the admin user account name is `admin` and the password will stay as the initial admin password that you entered.
Be careful not to enter actual passwords and information here, especially if you are connected to a Jenkins instance over the internet with no TLS or SSL configured (HTTPS secure connection).

![Create First Admin User](https://i.imgur.com/DIzyESa.png)

## Instance Configuration
All you will need to for this step is to select `Save and Finish`.

![Instance Configuration](https://i.imgur.com/SPPAiXG.png)

## Dashboard
You should now have Jenkins setup and have the following dashboard on your screen:

![Dashboard](https://i.imgur.com/JsVUo3x.png)

### Dashboard Links

|Link|Description|
|----|-----------|
|New Item| This is for creating new jobs in Jenkins. Jobs are essentially scripts that can be triggered.|
|People| The users that are registered to this instance of Jenkins.|
|Build History|A graph displaying the jobs that have been executed over time, through this instance of Jenkins.|
|Manage Jenkins|This is where to go for setting up plugins and other administrative settings for Jenkins.|
|My Views|You can customise how the jobs, and what jobs, are listed on the dashboard here.|
|Credentials|In the Jenkins jobs that you create, you may need to authenticate with external services, such as GitHub. Credentials for these external services can be stored securely here, and accessed by jobs and plugins when they need them.
|Lockable Resources|This plugin allows defining lockable resources (such as printers, phones, computers, etc.) that can be used by builds. If a build requires a resource that is already locked, it will wait for the resource to be free. You can define a lock-priority globally or on a per-job basis.|
