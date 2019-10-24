# Environment Variables

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Access Types](#access-types)
	- [Which Access Type and When?](#which-access-type-and-when)
		- [Example Scenario](#example-scenario)
- [Accessing an Environment Variable](#accessing-an-environment-variable)
- [Assigning Environment Variables](#assigning-environment-variables)
	- [Process Level Assignment](#process-level-assignment)
	- [User & System Level Assignment](#user--system-level-assignment)
		- [User Level Example](#user-level-example)
		- [System Level Example](#system-level-example)
- [Unassign Environment Variables](#unassign-environment-variables)
	- [Unassign Process Level Environment Variable](#unassign-process-level-environment-variable)
	- [Unassign User Level Environment Variable](#unassign-user-level-environment-variable)
	- [Unassign System Level Environment Variable](#unassign-system-level-environment-variable)
- [Tasks](#tasks)
	- [Process Level Assignment](#process-level-assignment-1)
	- [User & System Level Assignment](#user--system-level-assignment-1)
		- [User Level](#user-level)
		- [System Level](#system-level)
	- [Viewing System & User Level Environment Variables on Windows](#viewing-system--user-level-environment-variables-on-windows)
	- [Unassign the Environment Variables](#unassign-the-environment-variables)

<!--TOC_END-->
## Overview
PowerShell has the ability to set and access system environment variables.
Environment variables are just like normal variables, except they are configured outside of applications.
This gives us the ability to program applications more generically, as opposed to hard-coding the values that we want into the program itself.

## Access Types
Environment variables differ from regular variables, because they are not subjected to scope like regular variables are.
However, there are different access types that you can set on an environment variable, which affects access to it.

|Access Type|Description|
|-----------|-----------|
|Process|The current PowerShell session and any applications started within it will be able to access the variable. Environment variables at this level can be thought of as temporary; when the process stops or the system restarts, the variable will no longer exist.|
|User|Any applications being run by the same system user will be able to access the variable. The variable is persisted and will still be accessible after a reboot.|
|System|Access is allowed across the entire system, and the variable will remain after a restart. Only administrators can modify these variables.|

### Which Access Type and When?
Deciding on which access type to use can get fairly subjective; however, if you consider the scopes for the variables, it isn't too hard to figure out. Try answering the following question in order to decide what scope to use: does it need to be accessible at this scope?

#### Example Scenario
Let's consider the following scenario as an example:
- Deploying an application server that needs a database connection passed in as an environment variable
- Application server executable is run by the `app` user
- The application is executed as a service (a background process that is not started by a PowerShell session)

From this information, we can see that a System environment variable is not a good option here. This is because only the `app` user needs access to the value stored in that environment variable.
A better scenario to have the envinronment variable as a System access type would be if every user on the system needed to be able to access the same variable. 

We can't really use a Process level environment variable because the application is executed as a service, so not executed by a PowerShell session.

This leaves us with the User level, which will mean that any process running as the `app` user will have access to this variable.
This will work with the application being executed as a service.

## Accessing an Environment Variable
Environment variables can be accessed in PowerShell by using `$env:` and the name of the environment variable:
```powershell
echo $env:HOMEPATH
```
All the types of environment variables we have discussed are accessed in the same way.
The access level will only change whether they are accessible or not.

When setting an environment variable that is either for `User` or `System` level, you will need to restart the PowerShell session before you will be able to access it.

## Assigning Environment Variables
There are a couple of ways to assign an environment variable, depending on what access type is going to be needed.

### Process Level Assignment
You can use `$env` to assign a process level environment variable:
```powershell
$env:TEST_VARIABLE = “test variable value”
```

### User & System Level Assignment
User and System level environment variable assigment will need to be configured by leveraging the .NET framework that PowerShell has access to.
This works by accessing the `SetEnvironmentVariable` method from the `System.Environment` class.
We can pass this method the variable `name`, `value` and the `type`.

#### User Level Example
```powershell
[System.Environment]::SetEnvironmentVariable("TEST_VARIABLE", "test variable", "User")
```

#### System Level Example
System-wide environment variables can be provided by using the `Machine` type, which seems a bit ambiguous considering it's for a System environment variable.
Remember, when you are setting a System environment variable, you will need have a PowerShell session opened as an administrator on Windows.
You could try running the example shown here in a non-administritive PowerShell session first to see the error, then try running it in an administrivtive PowerShell window:
```powershell
[System.Environment]::SetEnvironmentVariable("TEST_VARIABLE", "test variable", "Machine")
```

## Unassign Environment Variables
Variables can be unassigned by setting them to be `$null`.
So, to unassign a variable, you just assign `$null` to it.
Some examples have been included in this section for extra clarification.

### Unassign Process Level Environment Variable
```powershell
$env:TEST_VARIABLE = $null
```

### Unassign User Level Environment Variable
```powershell
[System.Environment]::SetEnvironmentVariable("TEST_VARIABLE", $null, "User")
```

### Unassign System Level Environment Variable
```powershell
[System.Environment]::SetEnvironmentVariable("TEST_VARIABLE", $null, "Machine")
```

## Tasks
Although PowerShell can be used on other systems like Linux, these exercises are best suited on a Windows machine. This is so that you can see the the different access types working correctly.
You will find that only process environment variables seem to work correctly on Linux.

### Process Level Assignment
Let's set a process level environment variable called `TEST_PROCESS_VARIABLE`, with a value of `test process variable`:
```powershell
$env:TEST_PROCESS_VARIABLE = “test process variable”
```
We can now check that the variable has been assigned correctly by accessing it:
```powershell
echo $env:TEST_PROCESS_VARIABLE
```

### User & System Level Assignment
Now we can assign simliar variables, but on a `User` and `System` level, by using PowerShell's .NET capabilities.

#### User Level
```powershell
[System.Environment]::SetEnvironmentVariable("TEST_USER_VARIABLE", "test user variable", "User")
# restart your powershell session
echo $env:TEST_USER_VARIABLE
```

#### System Level
```powershell
[System.Environment]::SetEnvironmentVariable("TEST_SYSTEM_VARIABLE", "test system variable", "Machine")
# restart your powershell session
echo $env:TEST_SYSTEM_VARIABLE
```

### Viewing System & User Level Environment Variables on Windows
Specifically for Windows, we are able to view the System and User environment variables that have been assigned.

A common way to open the Environment Variables window is by navigating through these steps:
- Right click on the Start Menu 
- Select Control Panel
- Select System
- Select Advanced System Settings
- Select Environment Variables

The fastest way we can get to the Environment Variables open, for the purpose of this exercise, is by using the Window Run application to open it:
- Press `Windows key` and `R` on you keyboard to open the run window
- Enter the following and select ok: `rundll32.exe sysdm.cpl,EditEnvironmentVariables`:

![Windows Run Environment Variables](https://lh3.googleusercontent.com/McdTfOGpJ8oPdFGQqcXbIrwo7EpatdsRPeSHFQkGOgeAlzjZ7GR_sl4JtO3_cHNPwUdmxIirbDVc4Zumy8Bcy5ofaz6nlKtGjKZZVujecS203-GlDrkBNBzDaMg38zo0zxxCYP7DgvM6SOyUsg97zjK5aosQMV1hWCIS5ZRBnooQaF6f2o3RGade-p36wUjCI9i_Ghk6fQ0ICa55HilYcHagIHWtmpj7dzmc23lvtWtr2Wib7RPdsGho-omxeP7gVUyAGcJBxuL1iHusAxN1zTg9HPdHdaYkhcnPJM_URDGBHq97AWhsDWqv0Be3oQCs9P4B17-dGHbxjpY-6n-fjilnuNWC-4zh5Tsc8PlINsg-r4lUC6DIRhwA5EQa-aikrCJGuZLlevVEWdo6CUupfHdbxI8ug12rdicr9Bjv6GjvxHFTtyBz-Vhx-klYfPGSc50riuNkE1kZngvfvMoa2Wuo3uCJlA4Lj13d4sydfJKv8EpXuPwtZowocbLik_ZmOzfE6RKd0yKw1SCEskai19_KvT-T-v7WMmqQ1ieFc4UyshYY2meuhBLDc2G_QYWgqvTq_ZB6I12bxNSQSVgJFxge3rYAG7iASJzDHl0T2ETGw5HRi_hxrb4o84ahDbhxUG1olnmuRPJbXbW3tbSqNdMF247AVsiTvwI8xbrxodlPhZUZSb9CURHpuiKRBYX9TKaMnZxL7xqwpfWKHVFQaexKFLDUBdSE8vCZ5LlvgAC4sFpP=w408-h223-no)

You should now have the Environment Variables window open.
The `TEST_USER_VARIABLE` and `TEST_SYSTEM_VARIABLE` environment variables should also be visible:

![Windows Environment Variable Window](https://lh3.googleusercontent.com/CZcMmNjbj8P8GPe0yzmhSQJ_0Q4fJzxeWnURhMWiEe-oFHuJ12B9Pm3j84Y4qnToWqdFmVoFVKp0V9M0bema3xtWkYEBepbUoxRErf_hKYuXYEmZ3r-o_1Y6HiXyfoIE5yQZ0SO5gwQ4AscZpuHJBe7iWXFHSo8WfS7zNPi4dkpj_KFDIRSqxfgzUfn7vyC_W2af0vrMstPJlrmn91ynSCUZNJRQM0ebAhR569dh4qEIaOJU5FawdDf90ZaYtSdhoHvnJ5MNJEtkW4G3AGEoDUEZX5d0Ikl5g9ZOqWGNBiKmSiEADR309w6ZFoZXx-CHfsau-NvyhRTRCjC12KYy3-_HIigYJRM7cDP_vOnnldydTySRV8rQn7UpEB0gZBwDaLqUi4T1crbQuCBdtPOy0dgcFVyASx9M_ZnTg6wLpqLDHzm1lOv7OGtdLXGfmj5srnbgf_6X1oPxMNw3yJPJQvarZKm0KzA7i4pexZ3ghO7q_bAbtqSBcyGHbYnktwDYo-ubLmNaUzJSa0gG9k-NBqfavosnOICC82ME9OGod6TeC5HcqIva-A203x4Yl9eyfvWk2fNG-fkZjV2M6ogt-XFGQ4yZkAARfgDhx3Uxrvunxo13vn1T366f0MhRzru3f4T8XdngZ954b5huXYTFGT2bSZ6OIOm-rGipej9WSRHcITKdBFEyR9RFdmhElJxkt6nbzN0lTxBSX1aD8JCimWomLi4MLJtWGM-uudy1ZYp7AgDY=w376-h427-no)

### Unassign the Environment Variables
The variables created in this task can be unassignd by setting their values to `$null`:
```powershell
[System.Environment]::SetEnvironmentVariable("TEST_USER_VARIABLE", $null, "User")
[System.Environment]::SetEnvironmentVariable("TEST_SYSTEM_VARIABLE", $null, "Machine")
```
