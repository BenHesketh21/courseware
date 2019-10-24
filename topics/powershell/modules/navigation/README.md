# Navigation



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Working Directory](#working-directory)
- [Showing Directory Contents](#showing-directory-contents)
	- [`ls` command](#ls-command)
		- [Output](#output)
	- [`dir` command](#dir-command)
		- [Output](#output-1)
- [Changing the Current Working Directory](#changing-the-current-working-directory)
- [Path Names](#path-names)
	- [Path Ending with a Folder](#path-ending-with-a-folder)
	- [Path Ending with a File](#path-ending-with-a-file)
	- [Absolute Path](#absolute-path)
		- [Windows](#windows)
		- [Linux](#linux)
	- [Relative Paths](#relative-paths)
- [Tasks](#tasks)
	- [Change to Your Home Directory](#change-to-your-home-directory)
	- [Make Some Folders](#make-some-folders)
	- [Change into Folder `2`](#change-into-folder-2)
	- [Change into Folder `b`](#change-into-folder-b)
	- [Clean Up](#clean-up)

<!--TOC_END-->
## Overview
Knowing how to navigate a file system with PowerShell, Command Prompt or Bash is important for being able to automate tasks with their respective scripting languages.
Fortunately the commands are very similar for all of these applications when it comes to navigation.
Using an interactive console is the easiest way to start learning navigation in PowerShell.

## Working Directory
Whenever you are in an interactive console or running a script with PowerShell, each session has something called a working directory.

Knowing what the working directory can be very important, especially when accessing files.
The current working directory is usually shown before the cursor in a console. If you cannot see this and you aren't running a script, you may view your current working directory by running the Print Working Directory command:
```powershell
pwd
```

## Showing Directory Contents
To view the contents of a directory you can use either of these commands:

### `ls` command
`ls` will provide you with a simple list of the files and folders in your current working directory:
```powershell
ls
```

#### Output
```text
PS /home/bob/projects/github.com/bob-crutchley/notes> ls
automation   courses			  pip_dependencies  state.json	venv
_config.yml  packages-microsoft-prod.deb  README.md	    topics
```

### `dir` command
`dir` can be executed to show the current contents of your working directory with some information about the files:
```powershell
dir
```

#### Output
```text
PS /home/bob/projects/github.com/bob-crutchley/notes> ls -al
total 76
drwxr-xr-x  9 bob bob  4096 Sep 16 14:44 .
drwxr-xr-x 11 bob bob  4096 Sep 13 11:45 ..
drwxr-xr-x  3 bob bob  4096 Sep  2 10:44 automation
drwxr-xr-x  2 bob bob  4096 Sep  2 09:24 .circleci
-rw-r--r--  1 bob bob    25 Sep  2 09:24 _config.yml
drwxr-xr-x  3 bob bob  4096 Sep  2 09:24 courses
drwxr-xr-x  8 bob bob  4096 Sep 16 14:43 .git
drwxr-xr-x  3 bob bob  4096 Aug 30 09:21 .github
-rw-r--r--  1 bob bob    34 Aug 30 09:21 .gitignore
-rw-r--r--  1 bob bob  2452 Nov 27  2017 packages-microsoft-prod.deb
-rw-r--r--  1 bob bob    15 Aug 30 09:21 pip_dependencies
-rw-r--r--  1 bob bob  3658 Aug 30 09:21 README.md
-rw-r--r--  1 bob bob 19762 Sep 16 14:39 state.json
drwxr-xr-x 16 bob bob  4096 Sep 16 14:39 topics
drwxr-xr-x  5 bob bob  4096 Aug 30 14:42 venv
```

## Changing the Current Working Directory
The working directory can be changed by using the Change Directory (`cd`) command:
```powershell
cd folder_name
```

## Path Names
A path is an ordered list of directories on on a file system which describe the location of a file or folder. This list of directories is delimited with a backslash (`\`) on Windows and a forward slash (`/`) on Linux.

### Path Ending with a Folder
```text
C:\Users\bob
```

### Path Ending with a File
```text
C:\Users\bob\readme.txt
```

### Absolute Path
An absolute path specifies the location of a file or folder by providing the **full path** i.e. every directory from the top of the filesystem down to the object in question.
On Windows, you must specify the drive letter (Default primary drive is `C:`) at the start of the path.
Linux has a very different file system to Windows - you only need to start the path with a forward slash (`/`) to get to the root of the file system.
Below are examples of absolute paths to the hosts file on both Windows and Linux.

#### Windows
```text
C:\Windows\System32\drivers\etc\hosts
```

#### Linux
```text
/etc/hosts
```

### Relative Paths
Accessing the absolute path for all files can be tedious work. Relative paths make it possible to access files and folders that are relative to your current location in the file system (your working directory).
For example, if you were in the `C:\Windows\System32\drivers` folder on Windows, we would only need to execute the following command to get into the `C:\Windows\System32\drivers\etc folder`:
```powershell
cd etc
```
The current working directory that you are in and the relative path that is specified in the command are added together; resolving to the absolute path of the file or folder.

Relative paths are especially useful if you are needing to reference a directory that is “backwards” in the filesystem.
You can accomplish this by using `..` as the relative path:
```powershell
cd ..
```

`..` just means “one directory up”, and we can use it alongside other folders as well.
For instance if there were two folders:
- `C:\Users\bob\folder_1`
- `C:\Users\bob\folder_2`
And the current working directory was in the first folder (`C:\Users\bob\folder_1`)
We can change into the second folder by using a relative path:
```powershell
cd ..\folder_2
```

## Tasks

### Change to Your Home Directory
Make sure that you are in your home directory by running the following command:
```powershell
cd $home
```

### Make Some Folders
We'll be using a new command here to create some folders for us to navigate through:
```powershell
New-Item -ItemType Directory -Path $home/powershell-navigation/1/2
New-Item -ItemType Directory -Path $home/powershell-navigation/a/b
```
After running those commands we will have the following directory structure:
```text
powershell-navigation/
├── 1
│   └── 2
└── a
    └── b
```

### Change into Folder `2`
The `cd` command can be used to change the directory into folder 2:
```powershell
cd powershell-navigation/1/2
```
Our current working directory can now be confirmed by running `pwd`.

### Change into Folder `b`
One of the better ways to change to folder `b` from our current working directory is by using mor relative paths:
```powershell
cd ../../a/b
```
We can check out working directory again now with `pwd`.

### Clean Up
Let's change back to our home directory and delete the folders that were created to clean up.
```powershell
cd $home
Remove-Item -Recurse $home/powershell-navigation
```
