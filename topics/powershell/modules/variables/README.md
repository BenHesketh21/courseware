# Variables



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Assignment and Access](#assignment-and-access)
- [Data Types](#data-types)
	- [Implicitly Applied Data Types](#implicitly-applied-data-types)
	- [Explicitly Applied Data Types](#explicitly-applied-data-types)
- [Tasks](#tasks)
	- [Create a Simple String Variable](#create-a-simple-string-variable)
	- [Access the `name` Variable](#access-the-name-variable)
	- [Create an Integer Variable](#create-an-integer-variable)
	- [Access both the `name` and `age` Variables](#access-both-the-name-and-age-variables)

<!--TOC_END-->
## Overview
Variables are a programming concept that has remained consistent across many different programming languages and PowerShell isn’t an exception; a variable is like a container that holds information.
Variables are a great way of storing information that allows us to develop programs that are far more flexible.

## Assignment and Access
In PowerShell, variables are set and accessed by using the dollar character `$`, which is then followed by the name of the variable.

Variables can be assigned by using the `=` character:
```powershell
$myVariable = "test"
```

Below is an example of the variable contents being accessed by using the echo command:
```powershell
echo $myVariable
```

## Data Types
PowerShell variables use data types, similar to programming languages like C#, Java and Python.
Data types can be explicitly applied to variables. In the event that you don't give a variable a data type, PowerShell will implicitly apply one for you.

### Implicitly Applied Data Types
PowerShell being able to understand a variable's data type implicitly provides the value of less code. For example, if we want a variable of type `String`, then it could be accomplished by surrounding the value with quotes `“”`:
```powershell
$myStringVariable = "powershell will understand that this is a string"
```
Variables of type `Integer` can be applied by omitting the quotes and setting the value as a number:
```powershell
$myIntegerVariable = 2
```

### Explicitly Applied Data Types
There are often times where we should set the data type for a variable as it allows for functionality which only a specific type has. It also improves the readability of the code.
For example, a variable with a type of `DateTime` will have more functionality built-in to work with dates as opposed to using a `String`.
Take this string `“February 26, 2015”` for instance - we can see it is a date but PowerShell doesn’t know that you want it to be of type `DateTime`, so for an occasion where we want to compare two dates, PowerShell won't be able to do it:
```text
PS C:\Users\bob> $differenceBetweenTwoDates = (“February 26, 2015” - “February 15, 2015”)
Cannot convert value "February 26, 2015" to type "System.Int32". Error: "Input string was not in a correct format."
At line:1 char:1
+ $differenceBetweenTwoDates = (“February 26, 2015” - “February 15, 201 ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : InvalidCastFromStringToInteger
```
As shown above in the error message, PowerShell has made the assumption that we want to convert both of the `String` values to be an `Integer`, except this is quite far from what we want.

So if we explicitly tell PowerShell to consider those Strings as `DateTime` objects, then PowerShell will attempt to parse them as such:
```text
PS C:\Users\bob> $time = ([DateTime]“February 26, 2015” - [DateTime]“February 15, 2015”)

PS C:\Users\bob> echo $time
Days              : 11
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 0
Ticks             : 9504000000000
TotalDays         : 11
TotalHours        : 264
TotalMinutes      : 15840
TotalSeconds      : 950400
TotalMilliseconds : 950400000
```

## Tasks

### Create a Simple String Variable
Create a simple variable which contains your name, for the example below you can replace `bob` with your name:
```powershell
$name = "bob"
```

### Access the `name` Variable
The `name` variable that has just been created can be accessed like this:
```powershell
echo "Hi, my name is $name"
```
You should then see an output like this but with your name:
```text
Hi, my name is bob
```

### Create an Integer Variable
We can create another variable for your age, you can replace `23` here with your age:
```powershell
$age = 23
```

### Access both the `name` and `age` Variables
Both variables that have been created can be accessed in an `echo` command at the same time:
```powershell
echo "Hi, my name is $name and I am $age years old"
```
You should then see an output like this with your name and age:
```text
Hi, my name is bob and I am 23 years old
```
