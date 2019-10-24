# Error Handling



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Terminating vs Non-Terminating Errors](#terminating-vs-nonterminating-errors)
- [The $error Variable](#the-error-variable)
- [ErrorAction](#erroraction)
- [Try/Catch/Finally Block](#trycatchfinally-block)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview

Error handling refers to the anticipation, detection, and resolution of programming, application, and communications errors.

This process can be seen in most programming languages, but this module will focus on Error Handling in PowerShell.

## Terminating vs Non-Terminating Errors

It is important to firstly understand the types of errors that can occur during execution:

* **Terminating Error**: A serious error during execution that halts the command (or script execution) completely. Examples can include non-existent cmdlets, syntax errors that would prevent a cmdlet from running, or other fatal errors.
* **Non-Terminating Error**: A non-serious error that allows execution to continue despite the failure. Examples include operational errors such file not found, permissions problems, etc.

## The $error Variable

When either type of error occurs during execution, it is logged to a global variable named **$error**.

On a new PowerShell instance, where no errors have occured yet, the **$error** variable is ready and waiting. At this point it will be empty, and you can check this by running the following:

```powershell
$error.Count
```

## ErrorAction

We can use `ErrorAction` to handle non-terminating errors in PowerShell.

When running a script, you can add a command line option of `-ErrorAction` followed by:

* **SilentlyContinue**: error messages are suppressed and execution continues.
* **Stop**: forces execution to stop, behaving like a terminating error.
* **Continue**: the default option. Errors will display and execution will continue.
* **Inquire**: prompt the user for input to see if we should proceed.
* **Ignore**: the error is ignored and not logged to the error stream. Has very restricted usage scenarios.

An example of this would be if we wanted to zap processes on our pc (providing we are comfortable we know what we are doing!). You could do the following:

```powershell
Stop-Process 5132, 5076, 5072 -ErrorAction SilentlyContinue
```

If process `5132` didn't exist and we didn't have an `-ErrorAction`, the script would come to a halt prematurely and throw an error message (`Cannot find process with the process identifier 5132`)

## Try/Catch/Finally Block

A terminating error stops a script from running, so we need to make sure we handle the error in some way.

To handle terminating errors in scripts, we use `Try`, `Catch` and `Finally` blocks.

Use the `Try` block to define a section of a script in which you want PowerShell to monitor for errors.

PowerShell then searches for a `Catch` block to handle the error.

After a `Catch` block is completed, the `Finally` block is run.

If the error cannot be handled, the error is written to the error stream.

```powershell
try { NonsenseString }
catch { "An error occured." }
finally { "Exiting." }
```

PowerShell does not recognise `NonsenseString` as a cmdlet or other item. Running this script returns the following result:

```powershell
An error occured.
Exiting.
```

When the script encounters `NonsenseString`, it causes a terminating error. The `Catch` block handles the error by running what is inside that block.

The `Finally` block runs every time the script is run, even if the `Try` statement ran without error or an error was caught in a `Catch` block.

## Tasks

1. Open a new Powershell Instance
2. Check the `$error` variable, to see if there is anything inside it
3. Write the following to the console:

```powershell
function Hello{
    [CmdletBinding()]
    param($Name)

    Write-Error -Message "Nothing to write to console"
}
```

4. Type `Hello` in the console - you should see an error message saying `Nothing to write to console`
5. Check the count of the `$error` variable (it should now be `1`)
6. Use `$error[0]` to see the error that is stored inside the variable. What do you notice about it?
7. Type `Hello` again, but this time try to not have an error message shown (hint: `SilentlyContinue`)
8. Create a `Try`, `Catch`, `Finally` Block to catch an error (use `ThisCmdlet-DoesnotExist`), and give some feedback to the user about what kind of error has been encountered.
