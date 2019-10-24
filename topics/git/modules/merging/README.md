<!--PROPS
{
    "estTime": 30
}
-->

# Merging



<!--TOC_START-->
## Contents
- [Overview](#overview)
	- [Merge conflicts](#merge-conflicts)
- [Tasks](#tasks)
	- [Handling Merge Conflicts](#handling-merge-conflicts)
		- [Initialise a Repository for Testing Merge Conflicts](#initialise-a-repository-for-testing-merge-conflicts)
		- [Create a Branch with a Conflict](#create-a-branch-with-a-conflict)
		- [Attempt to Merge the New Branch](#attempt-to-merge-the-new-branch)
		- [Resolving the Conflict](#resolving-the-conflict)

<!--TOC_END-->
## Overview
Joining the history of two or more branches through `git merge` incorporates changes into the current branch. This command is 
used by `git pull` to incorporate changes from a different repository, as well as to merge changes from one branch into 
another.

If we assume that we have a history like this, and the current branch is **master** :
```
      E---F---G issue
     /
A---B---C---D master
```
Executing `git merge issue` would add changes E, F and G into master and result in a new commit.
This new commit would end up in the following history.
```
      E---F---G issue
     /         \  
A---B---C---D---H master
```

### Merge conflicts
Merge conflicts happen when more than one person has edited a file, and the line numbers that were edited are the same
. It can also happen if someone deleted a file that another person was working on.

This conflict only affects the person performing the merge, and the rest of the team wouldn't be affected by it.

If a merge conflict happens, *Git* will automatically halt the merge process and mark the file, or files, that are
 conflicting. It is then up to the developer to resolve them.

## Tasks

### Handling Merge Conflicts
You will now go through the steps required to cause a merge conflict.

#### Initialise a Repository for Testing Merge Conflicts
1. Open a terminal
2. Create a new directory by executing `mkdir git-merge-conflict`
3. Change directory by executing `cd git-merge-conflict`
4. Initialise this directory as a git repository by executing `git init .`
5. Create a new text file *hello.txt* in the directory
6. Add some text, such as "hello world", to the *hello.txt* file. Save and close the file
7. Now you need to make git track changes for the *hello.txt* file, which can be done by executing the `git add
 hello.txt` command
8. Now you need to create a save point, which is known as a commit. This will have the current state of the *hello.txt file in it. Execute the `git commit -m "initial commit"` command to achieve this </br>
![Fork >](https://imgur.com/cm8Oky3.png)

#### Create a Branch with a Conflict
Now that you have a repository and a master branch with a file on it, the next step is to create a new branch to
 use to cause the merge conflict.
 
1. Checkout a new branch by executing `git checkout -b new-branch`
2. Open the text file *hello.txt* and add a new line of text to it, such as "making a change to the file". Your text
 file should now look like this:
```
hello world
making a change to the file
```
3. Let's ensure Git keeps track of the hello.txt file that we made a change to. This can be done by executing the `git add hello.txt` command. Now you
 need to commit again, but this time with a message that reflects the change made - `git commit -m "made a change to
  hello.txt file"`. The change we made will now try to override the changes in master branch, for the text file *hello.txt*.
4. A change to the text file *hello.txt* is now required before we can cause a merge conflict. Let's go back to
 our *master* branch, by executing the `git checkout master` command
5. Open the text file *hello.txt* and add a new line of text to it, such as "making a bigger change". Your
 text file on master should now look like this:
```
hello world
making a bigger change
```
The *hello.txt* on the *new-branch* branch should look like this:
```
hello world
making a change to the file
```
Let's commit the change we made to the *hello.txt* file to the master branch, by executing `git add hello.txt` followed by
 `git commit -m "modified hello.txt file"`. </br>
![Fork >](https://imgur.com/y6GoKCn.png) 

#### Attempt to Merge the New Branch
Now, we want to merge changes from the *new-branch* branch to the *master* branch. However, Git won't be able to figure out which version of
 the second line to use - it will create a merge conflict, which the developer will be responsible for resolving.
1. Let's go ahead and actually cause the merge conflict, by executing the `git merge new-branch` command. You should get an output
 similar to this:</br>
![Fork >](https://imgur.com/yFzxuUD.png)
2. Let's take a look at the contents of the *hello.txt* file now, which should look similar to this:
```
hello world
<<<<<<< HEAD
making a bigger change
=======
making a change to the file
>>>>>>> new-branch
```
The main thing to recognise is that the first line (`hello world`) doesn't have a conflict, but there is a conflict between the
 second line of the *master* and *new-branch* branches.

#### Resolving the Conflict
To resolve the merge conflict, there are a couple of steps needed:
Firstly, decide which second line to keep out of `making a bigger change` or `making a change to the file`. You could also
 choose something entirely different, such as keeping or deleting both lines.
Secondly, delete the lines *Git* added, to show where the merge conflict is happening `<<<<<<< HEAD
`, `=======`, `>>>>>>> new-branch`. 
Let's say you decide to keep the second line that's currently in *master* branch. After cleaning up the file, it
 should look like this:
```
hello world
making a bigger change
```
Next, you need to save the changes made. This can be done by executing the `git add hello.txt` command, followed by
 the `git commit -m "resolved merge conflict"` command. </br>
![Fork >](https://imgur.com/IsF5LQK.png)
Running `git status` should now indicate that there are no longer any conflicts to resolve.
