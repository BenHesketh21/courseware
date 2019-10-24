# Introduction



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Installation](#installation)
	- [Windows](#windows)
	- [Linux](#linux)
	- [MacOS](#macos)
- [Tasks](#tasks)
	- [Open PowerShell](#open-powershell)
	- [Make a Variable](#make-a-variable)
	- [Show the Contents of a Variable](#show-the-contents-of-a-variable)
	- [Test a Connection to a Remote Host](#test-a-connection-to-a-remote-host)
	- [Conditionals](#conditionals)
		- [Connection Test to a Host that doesn't exist](#connection-test-to-a-host-that-doesnt-exist)
		- [Connection Test to a Host that does exist](#connection-test-to-a-host-that-does-exist)
	- [Exit PowerShell](#exit-powershell)

<!--TOC_END-->
## Overview
PowerShell is a tool that allows us to manage machines from the command-line, as well as create scripts to automate tasks on Windows, Linux and MacOS operating systems.
Below are some notable characteristics about PowerShell:
- **Command-line shell**
    - Single commands can be run in an interactive shell
- **Scripting language**
    - Multiple commands, logic and control flow can be implemented in scripts to automate complex tasks
- **Open Source**
    - The source code for the application is open to the public, meaning everyone can view the code and everyone can request to make contributions to the code
- **Available on Windows, Linux and MacOS**
    - Pre-installed and configured on Windows 
    - Built on the .NET Framework
    - Object oriented scripting is available through the .NET framework that PowerShell has been developed on

## Installation

### Windows
PowerShell is compatible with all of the popular operating systems. PowerShell is already pre-installed on Windows, so there is no need for initial installation or further configuration to get started with it.

### Linux
PowerShell is available through most popular package managers for Linux. However, you must configure the relevant package manager to work with PowerShell, which is entirely dependent on your Linux version.
Please refer to the [Microsoft documentation](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux?view=powershell-6) to configure and install PowerShell correctly for your operating system.

### MacOS
PowerShell can be installed on Mac by using the brew package manager:
```bash
brew cask install powershell
```

## Tasks
Here are some basic commands and concepts to try out in PowerShell.

### Open PowerShell
On Windows you can simply search for `powershell` in the start menu.
With MacOS and Linux, open a terminal and execute `pwsh`.

### Make a Variable
Variables have all sorts of uses within programming, and will be important for most PowerShell scripts:
```powershell
$myVariable = “Hello World”
```

### Show the Contents of a Variable
Logging output is a good way for debugging and understanding where the scripts you create are at. You can use `Write-Output` or `Echo` for this.
```powershell
Write-Output $myVariable
```

### Test a Connection to a Remote Host
We can see if a connection can be made to a remote machine by using the Test-Connection command.
```powershell
Test-Connection google.co.uk
```

### Conditionals
All commands that are executed either succeed or fail; we can use this to change how scripts behave or react to failed commands.
If you run the examples below, they will print out a different message to the console depending on whether the `Test-Connection` commands succeeds.

#### Connection Test to a Host that doesn't exist
```powershell
if (Test-Connection goasd1le.co2.rq.r.q2r) {
   Write-Output "Connection Successful"
} else {
   Write-Output "Could not connect"
}
```

#### Connection Test to a Host that does exist
```powershell
if (Test-Connection google.co.uk) {
   Write-Output "Connection Successful"
} else {
   Write-Output "Could not connect"
}
```

### Exit PowerShell
You can run the `exit` command to quit PowerShell:
```powershell
exit
```
