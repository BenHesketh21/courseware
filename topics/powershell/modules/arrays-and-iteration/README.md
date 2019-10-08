# Arrays and Iteration
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Loops](#loops)
	- [For Loop](#for-loop)
		- [Iterating an Array](#iterating-an-array)
	- [While Loop](#while-loop)
	- [Iterating an Array](#iterating-an-array-1)
	- [Waiting for a File to Exist](#waiting-for-a-file-to-exist)
	- [Infinite Loops](#infinite-loops)

<!--TOC_END-->
## Overview
Arrays and iteration can be used in PowerShell for solving extensive, repetetive, procedural tasks.
One of PowerShells main purpose is to automate tasks on Windows, often for multiple machines.

## Loops
The way that arrays can be iterated is by using loops.
There are a few different types of loops which can utilise depending on the situation.

### For Loop
The For loop is a very bsaic type of loop which can be used in most situations.

There are a few main parts to a For loop:
- Value of a variable
- Condition for whether the next iteration of the loop should run
- An action to be perfomed against the variable on each iteration, such as just adding `1` to it
```powershell
For([VARIABLE];[CONDITION];[VARIABLE_ACTION]) {
    # commands
}
```
#### Iterating an Array
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
### While Loop
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
### Waiting for a File to Exist
A more appropriate implementation of a while loop would be to use on something that needs to wait until a condition is met, such as a file existing.

In the example shown below the following is evaluated:
- Set a `filePath` variable for a file called `file.txt` in the user's home directory
- For the loop condition check the file exists with `Test-Path`, the boolean result of this can be inverted to make it so the condition is **True** if the file **doesn't** exist
```powershell
$filePath = "$HOME\file.txt"
While (!(Test-Path "$filePath")) {
    "Waiting for $filePath to exist..."
    Start-Sleep 2
}
```
### Infinite Loops
Something to be very cautious of when using While loops (and any type of loop for that matter) is to not get into an infinite loop.
If the condition for the loop is always met, then it will never stop running.

Taking the waiting for a file example, we can add a counter and a second condition to the loop.
For example here, if the loop has executed 10 times, then it will exit because both conditions inside the loop condition need to be met:
```powershell
$counter = 0
$filePath = "$HOME\file.txt"
While (!(Test-Path "$filePath") -and ($counter -lt 10)) {
    "Waiting for $filePath to exist..."
    Start-Sleep 2
    $counter++
}
```
## Do-While Loops
These are very similar to the while loop with once exception, the loops command block is executed before the condition is evaluted.
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

