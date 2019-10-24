<!--PROPS
{
	"estTime": 10
}
-->

# Forking



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Proposing a change](#proposing-a-change)
- [Your idea](#your-idea)
- [Tasks](#tasks)
	- [Forking a repository](#forking-a-repository)
	- [Updating forked repository from original](#updating-forked-repository-from-original)

<!--TOC_END-->
# Overview

In layman's terms, forking is creating a copy of an existing repository under your account. 

Forking a repository allows you to freely experiment with the existing code base, without the fear of breaking the project.
Forking also gives you the ability to contribute to a project, by adding additional functionality. 

## Proposing a change

Imagine you are using someone's project and you find a bug. Usually, you would raise an issue for this; however, forking means you would be able to attempt a fix yourself. 
The steps would be:
1. Fork the repository
2. Create a new branch
3. Fix the issue
4. Submit a pull request to the owner of the original project

If the owner approves your fix, your work should then be merged into the original repository.

## Your idea 

If a project is under public license that allows you to freely use it, you could use the project as a starting point for
your own project. For example, if you found a web application that you liked, and it was under the public license,
you could fork the project and add any additional functionality. This would then be yours to freely use or distribute.

## Tasks

### Forking a repository

You will now: fork a remote repository, configure upstream (to get updates from the original repository) and propose a change to the owner

1. Make sure you're logged into your GitHub account
2. Click on "Fork", in the top right of this page, for the `notes` project. This will create a copy of the repository under your account <br />
![Fork >](https://imgur.com/X0bNG7K.png)
3. You will be redirected to your account's version of the repository
4. Click on the green "Clone or download" button, and copy the URL <br />
![Fork >](https://imgur.com/hkzKOvt.png)
5. Open a Bash terminal in the location you want to clone your project
6. Run the command `git clone [URL]`, but replace [URL] with the repository URL you copied in the previous step
7. Change directory to the project you just cloned
8. Run the following command, to confirm that you have cloned the correct repository: `git remote -v`. You should get a 
similar output for `fetch` and `push`, but the URL will be pointing to your repository <br />
![Fork >](https://imgur.com/FOASYQ2.png)

### Updating forked repository from original

Now you will set up your local project to receive updates from the original repository. This is required, so that when
the owner of the original repository adds new functionality, bug fixes etc., you will be able to get these changes as well.

1. Open your Bash terminal, in the root directory of your project. You should be able to see that you're on the master 
branch. Next, you want to execute `git remote -v` to make sure that the upstream to the original repository is not set up yet.
You should see a similar output to this. <br />
![Fork >](https://imgur.com/lqS0EUr.png)
2. In your browser, go to the original git repository and copy the repository URL. You can do this by clicking on the
green "Clone or download" button and copying the URL <br />
![Fork >](https://imgur.com/hkzKOvt.png)
3. Execute the following command in your Bash terminal, but replace the [URL] with the one you just copied:
`git remote add upstream [URL]` 
4. Next, you want to check that this has worked, which you can do by executing the `git remote -v` command.
The output should look similar to this: <br />
![Fork >](https://imgur.com/KpAfGaP.png)
5. Now you will pull the changes from the original repository into yours, which you can do by executing the `git fetch upstream` command in your
Bash terminal. The output will depend on whether there are new changes or not: <br />
![Fork >](https://imgur.com/L7S2JB1.png)
6. You will want to update the master branch, so we will merge the *upstream/master* into the *local origin/master*. You can do this
by executing the `git merge upstream/master` command. Keep in mind that there may be merge conflicts that you will
 need to resolve. If you have resolved the merge conflicts, or if there were none, you should *push* to update your 
 *origin/master* branch. <br />
![Fork >](https://imgur.com/OYejtWC.png)
