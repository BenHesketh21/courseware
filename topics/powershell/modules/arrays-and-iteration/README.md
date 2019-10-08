# Arrays and Iteration
<!--TOC_START-->
### Contents
- [Overview](#overview)

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
- An action to be perfomed against the variable on each iteration
```powershell
For([VARIABLE];[CONDITION];[VARIABLE_ACTION]) {
    # loop statements
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
