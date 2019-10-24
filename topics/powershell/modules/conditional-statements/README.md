# Conditional Statements



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [`if`, `else` & `elseif` Statements](#if-else--elseif-statements)
	- [`if`](#if)
	- [`else`](#else)
	- [`elseif`](#elseif)
	- [Nesting Statements](#nesting-statements)
- [`switch` Statement](#switch-statement)
	- [Example](#example)
- [Tasks](#tasks)
	- [Obtain the User Input](#obtain-the-user-input)
	- [Calculate the User's Input with `if`, `else` & `elseif`](#calculate-the-users-input-with-if-else--elseif)
	- [Calculate the User's Input with a `switch` Statment](#calculate-the-users-input-with-a-switch-statment)

<!--TOC_END-->
## Overview
Conditional statements in PowerShell enable scripts to make decisions based on provided conditions.
PowerShell is like many other languages; it uses `if`, `else`, `elseif` and `switch` statements.
Conditions are evaluated to a boolean value (True or False).

## `if`, `else` & `elseif` Statements

### `if`
The `if` statement can be used to execute statements based on whether the provided condition is true or not:
```powershell
if (true) {
    echo "this statement will execute because the condition is true"
}
if (false) {
    echo "this statement will not execute because the condition is not true"
}
```

### `else`
The `else` statement can be used in conjunction with the `if` statement, to provide a block of statements to run if the `if` condition is not met:
```powershell
if (false) {
    echo "this statement will not run"
} else {
    echo "this statement will run, because the 'if' condition was not met"
}
```

### `elseif`
Using `elseif` will help if there's more than one condition that you're going to need to check.
You can have as many `elseif` statements as you like, but if you start getting many more than 2 or 3, for instance, you should consider using a `switch` statement.
```powershell
if (false) {
    echo "this statement will not run"
} elseif (true) { echo "this statement will run" } else {
    echo "this statement will not run because the 'ifelse' condition was met"
}
```

### Nesting Statements
These statements can, of course, be nested. However, be cautious when doing this, as having lots of nested statements can be very detrimental to the readability of the code:
```powershell
if (true) {
    echo "this statement will run"
    if (false) {
        echo "this statement won't run"
    } else {
        echo "this statement will run"
    }
}
```

## `switch` Statement
The `switch` statement is more appropriate to use when you want to test equality; for instance, checking if a given value eqauls something specific.

### Example
The example shown below will ask the user for a number between 1 and 3. Once a number has been selected, `"You selected [NUMBER]"` will be printed to the terminal.
If a number between 1 and 3 isn't entered then `"You didn't select a number between 1 and 3"` will be displayed on the terminal.

```powershell
switch (Read-Host "Pick a number between 1 and 3") {
    1 {"You selected 1"; break}
    2 {"You selected 2"; break}
    3 {"You selected 3"; break}
    default {"You didn't select a number between 1 and 3"}
}
```

For each statement, the first number on the line is being checked against what was provided in the `Read-Host` statement.
If the number matches, the block between the brances `{}` will be executed.

If a match is found, the switch statement will still continue to check the other statements, unless a `break` statement is issued.

Should none of the statements match, the `default` block will be executed.

## Tasks
This set of tasks will show you how `if`, `else`, `elseif` and `switch` statements can be applied to a simple PowerShell script.

The PowerShell script will figure out how much someone weighs on another planet:
- User input for the weight
- User input for selecting which Planet
- Multiply the relative gravity by the weight and output it

### Obtain the User Input
Create a script called `space-weight.ps1` and enter the following to gain the user input for the `weight` and the `planetNumber` to change the weight to.
The unit of weight can be obtained as well, just to make the output at the end a little nicer:
```powershell
$unit = Read-Host "What is the unit of weight? (KG/lbs)"
$weight = Read-Host "Please enter a weight: "
$planetNumber = Read-Host "
Which planet would you like to know how much this weighs on?
   1. Venus   2. Mars    3. Jupiter
   4. Saturn  5. Uranus  6. Neptune
"
```

### Calculate the User's Input with `if`, `else` & `elseif`
Using the `weight` and `planetNumber` variables, we can now figure out what weight it is going to be.

Here, we are going to add `if` and `elseif` statements, to figure out which Planet the user selected, and then we will multiply the weight by the relative gravity for the Planet.
If the user selects a number from the list that doesn't exist then this can be caught in an `else` statement, to inform the user that they have made an  invalid selection:
```powershell
# user input
$unit = Read-Host "What is the unit of weight? (KG/lbs)"
$weight = Read-Host "Please enter a weight"
$planetNumber = Read-Host "
Which planet would you like to know how much this weighs on?
   1. Venus   2. Mars    3. Jupiter
   4. Saturn  5. Uranus  6. Neptune
"
# calculate the user's input
if ($planetNumber -eq 1) {
    $planetName = "Venus"
    $weightOnPlanet = [Int]$weight * 0.78
} elseif ($planetNumber -eq 2) {
    $planetName = "Mars"
    $weightOnPlanet = [Int]$weight * 0.39
} elseif ($planetNumber -eq 3) {
    $planetName = "Jupiter"
    $weightOnPlanet = [Int]$weight * 2.65
} elseif ($planetNumber -eq 4) {
    $planetName = "Saturn"
    $weightOnPlanet = [Int]$weight * 1.17
} elseif ($planetNumber -eq 5) {
    $planetName = "Uranus"
    $weightOnPlanet = [Int]$weight * 1.05
} elseif ($planetNumber -eq 6) {
    $planetName = "Neptune"
    $weightOnPlanet = [Int]$weight * 1.23
} else {
    echo "Sorry, the planet number: $planetNumber is not recognised"
    exit
}
echo "On planet $planetName, $weight $unit would weigh: $weightOnPlanet $unit"
```
Once you have created the script, try running it!
```powershell
./space-weight.ps1
```

### Calculate the User's Input with a `switch` Statment
The last script will work fine, but it can be cleaned up quite a bit by using a `switch` statement instead; this will utilise the same logic that was implemented in the `if`, `elseif`, `else` example:
```powershell
# user input
$unit = Read-Host "What is the unit of weight? (KG/lbs)"
$weight = Read-Host "Please enter your weight"
$planetNumber = Read-Host "
Which planet would you like to know how much this weighs on?
   1. Venus   2. Mars    3. Jupiter
   4. Saturn  5. Uranus  6. Neptune
"
# calculate the user's input
switch ($planetNumber) {
    1 {
        $planetName = "Venus"
        $weightOnPlanet = [Int]$weight * 0.78
        break
    }
    2 {
        $planetName = "Mars"
        $weightOnPlanet = [Int]$weight * 0.39
        break
    }
    3 {
        $planetName = "Jupiter"
        $weightOnPlanet = [Int]$weight * 2.65
        break
    }
    4 {
        $planetName = "Saturn"
        $weightOnPlanet = [Int]$weight * 1.17
        break
    }
    5 {
        $planetName = "Uranus"
        $weightOnPlanet = [Int]$weight * 1.05
        break
    }
    6 {
        $planetName = "Neptune"
        $weightOnPlanet = [Int]$weight * 1.23
        break
    }
    default {
        echo "Planet Number: $planetNumber is not recognised"
        exit
    }
}
echo "On planet $planetName, $weight $unit would weigh: $weightOnPlanet $unit"
```
Now try running the script again, but with the `switch` statement implented!
