# Loops and Iteration

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [For Loop](#for-loop)
	- [Iterating an Array](#iterating-an-array)
- [While Loop](#while-loop)
	- [Iterating an Array](#iterating-an-array-1)
	- [Waiting for a File to be Deleted](#waiting-for-a-file-to-be-deleted)
	- [Infinite Loops](#infinite-loops)
		- [Avoiding Infinite Loops Example](#avoiding-infinite-loops-example)
- [Do While Loops](#do-while-loops)
	- [Do While Loops for User Input](#do-while-loops-for-user-input)
- [Do Until Loops](#do-until-loops)
	- [Waiting for a File to Exist](#waiting-for-a-file-to-exist)
- [Tasks](#tasks)
	- [File Contents](#file-contents)
	- [For Loop](#for-loop-1)
	- [While Loop](#while-loop-1)
	- [Do While Loop](#do-while-loop)
	- [Do Until Loop](#do-until-loop)

<!--TOC_END-->
## Overview
Arrays and iteration can be used in PowerShell for solving extensive, repetitive, procedural tasks.
One of PowerShells main purpose is to automate tasks on Windows, often for multiple machines.

The way that arrays can be iterated is by using loops.
There are a few different types of loops which can be utilised depending on the situation.

## For Loop
The For loop is a very basic type of loop which can be used in most situations.

There are a few main parts to a For loop:
- Value of a variable
- Condition for whether the next iteration of the loop should run
- An action to be perfomed against the variable on each iteration, such as just adding `1` to it
```powershell
For([VARIABLE];[CONDITION];[VARIABLE_ACTION]) {
    # commands
}
```

### Iterating an Array
For loops are commonly used to step through arrays, here's the logic used and an example to follow:
- Variable `i` equals `0` at the start
- For the condiiton, if the value of `i` is less than the value of the array's length then continue, otherwise exit the loop
- Execute the code block in the loop which just prints an element at the index for the value of `i`, so this would be `$colours[0]` the first time round
- Add `1` to `i` and start again, so on the second time it would start with `i` being equal to `1`
```powershell
$colours = @("Red", "Blue", "Green", "Orange", "Purple")
For ($i=0;$i -lt $colours.length; $i++) {
    $colours[$i]
}
```

## While Loop
While loops work by providing a single condition, the loop will continue to execute so long as that condition is met:
```powershell
While([CONDITION]) {
    # commands
}
```

### Iterating an Array
It would be slightly better to use a For loop to iterate arrays but it can still be done with a While loop:
```powershell
$colours = @("Red", "Blue", "Green", "Orange", "Purple")
While ($i -ne $colours.length) {
    $colours[$i]
}
```

### Waiting for a File to be Deleted
A more appropriate implementation of a while loop would be to use it on something that needs to wait until a condition is met, such as a file being deleted.

In the example shown below the following is evaluated:
- Set a `filePath` variable for a file called `file.txt` in the user's home directory
- For the loop condition check the file exists with `Test-Path`, this will return as **True** when the file exists
```powershell
$filePath = "$HOME\file.txt"
While (Test-Path "$filePath") {
    "Waiting for $filePath to be deleted exist..."
    Start-Sleep 2
}
```

### Infinite Loops
Something to be very cautious of when using While loops (and any type of loop for that matter) is to not get into an infinite loop.
If the condition for the loop is always met, then it will never stop running.

#### Avoiding Infinite Loops Example
Taking the waiting for a file example, we can add a counter which is incremented by `1` every time the loop executes and second condition to check if the counter has a value less than `10`.
For the example here, the conditions for the loop to continue running are:
- The file exists
- The counter has a value less that 10
```powershell
$counter = 0
$filePath = "$HOME\file.txt"
While (Test-Path "$filePath" -and ($counter -lt 10)) {
    "Waiting for $filePath to be deleted..."
    Start-Sleep 1
    $counter++
}
```

## Do While Loops
These are very similar to the while loop with one exception, the loops command block is executed before the condition is evaluated.
So this is a great option if you are needing the command to execute at least once, even if the condition is never met.
```powershell
Do {
    # commands
} While ([CONDITION])
```

### Do While Loops for User Input
One example use case for a Do While loop could be for taking user input.
This example here will use a normal While loop to take numbers from user input until the number is less than or equal to 10:
```powershell
$number = Read-Host "Please enter a number less than or equal to 10"
While([Int]$number -gt 10) {
    $number = Read-Host "Please enter a number less than or equal to 10"
}
```
Notice that we are having to run this line twice:
```powershell
$number = Read-Host "Please enter a number less than or equal to 10"
```
We can completely avoid this by using a `Do-While` loop:
```powershell
Do {
    $number = Read-Host "Please enter a number less than or equal to 10"
} While([Int]$number -gt 10) 
```

## Do Until Loops
Do until loops are almost identical to the Do While loops except for the condition is effectively inverted.
So as long as the condition **is not met**, the loop will continue to  execute **until** the condition is met.

The syntax of a Do Until loop is strucured the same as a Do While loop:
```powershell
Do {
    # commands
} Until([CONDITION])
```

### Waiting for a File to Exist
Because the condition for this type of loop is flipped, we can take the example from before to wait for file to be deleted and use this to wait for a file to be created:
```powershell
Do {
    "Waiting for $filePath to be deleted..."
    Start-Sleep 1
} Until (Test-Path "$filePath") 
```

## Tasks
We are going to use the different types of loops explained above to iterate over a log file (`log.txt`) and extract the errors, which can be found in this folder.
While working through this set of tasks make sure that you are creating and running the scripts in this directory.

### File Contents
Before we can try this out with any type of loop we will need to get the file content to iterate through.
So for each of the following steps you will need this at the top of your script:
```powershell
$content = Get-Content "log.txt"
```

### For Loop
With the for loop we can iterate over the file content just like an array, checking if the element contains an error message, printing it out to the console if it does. 
Create a file in this folder called `error-check-for-loop.ps1` and enter the following:
```powershell
$content = Get-Content "log.txt"
For ($i=0; $i -lt $content.Length; $i++) {
    if ($content[$i].Contains("[error]")) {
        "Line: $($i+1): $($content[$i])"
    }
}
```
Now try executing the script:
```powershell
./error-check-for-loop.ps1
```

### While Loop
The For loop example can be converted to the following to allow it work as a While loop.
Create a file called `error-check-while-loop.ps1` and enter the following:
```powershell
$content = Get-Content "log.txt"
While ($line -lt $content.Length) {
    if ($content[$line].Contains("[error]")) {
        "Line: $($line+1): $($content[$line])"
    }
    $line++
}
```
Give the script a go:
```powershell
./error-check-while-loop.ps1
```

### Do While Loop
Converting to a Do While loop from the While loop example above is very simple, just the condition needs to be moved.
Try creating a file called `error-check-do-while-loop.ps1` and enter the following:
```powershell
$content = Get-Content "log.txt"
Do {
    if ($content[$line].Contains("[error]")) {
        "Line: $($line+1): $($content[$line])"
    }
    $line++
} While ($line -lt $content.Length) 
```
Give the script a go:
```powershell
./error-check-do-while-loop.ps1
```

### Do Until Loop
The Do Until loop can be based off the Do While loop however the condition must be changed to check if the line number is equal to the length of the content instead.
Try creating a file called `error-check-do-until-loop.ps1` and enter the following:
```powershell
$content = Get-Content "log.txt"
Do {
    if ($content[$line].Contains("[error]")) {
        "Line: $($line+1): $($content[$line])"
    }
    $line++
} While ($line -eq $content.Length) 
```
Give the script a go:
```powershell
./error-check-do-until-loop.ps1
```
