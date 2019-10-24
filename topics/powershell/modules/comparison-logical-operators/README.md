# Comparison and Logical Operators

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Comparison Operators](#comparison-operators)
- [Logical Operators](#logical-operators)
- [Use with `if` and `while` Statements](#use-with-if-and-while-statements)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview
PowerShell operators play an important role in PowerShell scripting. Learning to use operators is essential if you want to take your scripting to the next level.

There are two types of operators we will discuss in this module, Comparison Operators and Logical Operators, and they are typically used in conjunction with `if` and `while` statements.

## Comparison Operators
These allow you to specify conditions for comparing values. This is a very common attribute of any programming or scripting language.

Some of the key comparison operators in PowerShell include:

* `-eq` : equals
* `-ne` : not equals
* `-gt` : greater than
* `-ge` : greater than or equal to
* `-lt` : less than
* `le` : less than or equal to

All comparison operators are case-insensitive by default. To make them case-sensitive, you would precede the operator with a `c` (for example, `-ceq` for equals).

These operators return a value of `True` when one or more of the input values is identical to the specified pattern, and `False` when this isn't the case.

Some examples are:

```powershell
PS > 2 -eq 2
True
```
```powershell
PS > 2 -gt 3
False
```
```powershell
PS > "abc" -ne "dfg"
True
```
```powershell
PS > 27 -le 27
True
```
```powershell
PS > "abc" -ne "abc"
False
```

## Logical Operators
Logical operators are great because they allow you to check for multiple conditions in one expression.

Some of the key logical operators in PowerShell include:

* `-and` : `True` when both statements are `True`
* `-or` : `True` when either statement is `True`
* `-xor` : `True` when only one statement is `True`
* `-not` or `!` : Negates the statement that follows

The general syntax for this would be:

```powershell
(condition) (operator) (condition)
```

Some examples of these in action are:

```powershell
PS > (1 -eq 1) -and (2 -gt 1)
True
```
```powershell
PS > (2 -eq 1) -or (5 -lt 4)
False
```
```powershell
PS > (1 -eq 1) -xor (2 -eq 2)
False
```
```powershell
PS > -not (8 -lt 10)
False
```
```powershell
PS > !(12 -gt 12)
True
```

## Use with `if` and `while` Statements
The general syntax for using operators with `if` and `while` statements is:

```powershell
(statement) (condition) {command_block}
```

For example:

```powershell
PS > if (12 -eq 12 -and 28 -lt 30){"This is most definitely True!"}
```
This will check to see if the condition, `(12 -eq 12 -and 28 -lt 30)` is `True`. If it is, the code inside the curly brackets will execute. 

In this example, the condition is `True` (12 is equal to 12 and 28 is less than 30), so `This is most definitely True!` was displayed on the console.

```powershell
PS > $val = 0
while ($val -lt 5){
    $val++
    Write-Host $val
}
```

In this example, we firstly set a variable called `$var` to the value of 0. We then use a `while` statement, so that the code inside the curly brackets will execute as long as the condition is `True`.

The condition in this case is `($val -lt 5)`. As long as whatever is inside the `$val` variable is less than 5, the code inside the curly brackets will execute.

Inside the curly brackets, we write what is stored in the `$var` variable to the console. Then, we increase the value of `$var` by 1 (using `$var++`). So, every time this code block executes, the value of `$var` will increase by 1.

Once the value of `$var` is no longer less than 5, the condition is false and the code inside the curly braces won't execute.

## Tasks
In the PowerShell console:

1. Create 3 conditions that evaluate to `True`.
2. Create 3 conditions that evaluate to `False`.
3. Use a logical operator to evaluate 2 conditions at the same time, and have the console display `True` 3 times and `False` 3 times.
4. Create a simple `if` statement that evaluates a condition and displays something to the console.
