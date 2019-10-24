<!--PROPS
{
    "estTime": 10
}
-->

# Cloning



<!--TOC_START-->
## Contents
- [Overview](#overview)
	- [Cloning a repository](#cloning-a-repository)
- [Tasks](#tasks)
	- [Cloning a Repository](#cloning-a-repository-1)

<!--TOC_END-->
## Overview
`git clone` allows the cloning of a repository to a newly created directory. Additionally, the command creates remote
tracking branches for the ones in the repository and checks out the initial branch (which becomes the current active branch).

Once the clone is created, `git fetch` can be executed, without additional arguments, to get updates for the remote 
branches. Similarly, a `git pull`, without arguments, would merge the remote branch into the current branch.

### Cloning a repository
In order to clone a repository, there are a couple of things you need to do first:
* Install Git on your machine
* Find the URL of the repository you want to clone

To get the URL of the repository you want to clone, you need to go to that repository in the VCS you are using (such as GitHub). 
Once there, you can click on the *Clone or Download* and copy the URL. </br>
![Fork >](https://imgur.com/hkzKOvt.png)
![Fork >](https://imgur.com/hOQZaFu.png)

Open a terminal and navigate to the directory where you want to have the project saved. You can create a directory named
*projects* or use an existing one. In the example below, a new directory is created. </br>
![Fork >](https://imgur.com/3b4KMCR.png)

After the cloning has been completed, change to the project directory and run `git branch` to check that the active branch has been 
checked out. </br>
![Fork >](https://imgur.com/UEAW1EN.png)

## Tasks

### Cloning a Repository

* Create a new repository
    * Initialise the repository with a README.md file
* Clone the repository to the desired location
* Check that an active branch has been checked out
