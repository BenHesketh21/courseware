# Syntax



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Commenting](#commenting)
	- [Single Line Comments](#single-line-comments)
	- [Multi-Line Comments](#multiline-comments)
	- [Inline Commenting](#inline-commenting)
	- [Shebang Line](#shebang-line)
- [String Interpolation (GStrings)](#string-interpolation-gstrings)
- [Optional Parenthesis](#optional-parenthesis)
	- [Overview](#overview-1)
	- [When you need parenthesis](#when-you-need-parenthesis)
	- [Omitting Parenthesis with Named Parameters](#omitting-parenthesis-with-named-parameters)
- [Tasks](#tasks)
	- [Commenting](#commenting-1)

<!--TOC_END-->
## Overview
This document aims to cover the basics of the Groovy programming language's syntax.
Many of the concepts will be easier to pick up if you have used a programming language like Java before, but don't worry if you haven't!

## Commenting
Comments in Groovy are just like Java:

### Single Line Comments
```groovy
// single line comment
```

### Multi-Line Comments
Multi-line comments start with `/*` and end with `*/`; this saves you having to put `//` on every commented line:
```groovy
/* 
    multi line comment
*/
```

### Inline Commenting
The same syntax for multi-line comments can be used for commenting inline:
```groovy
println 1 /* one */ + 2 /* two */
```

### Shebang Line
If the `groovy` command is available on your `PATH`, you can add a shebang line to your Groovy scripts so that you can execute your script directly. Here's an example:
```groovy
#!/usr/bin/env groovy
println "Hello"
```
If the script above was in a file called `test.groovy`, you would be able to execute it by running `./test.groovy`.

## String Interpolation (GStrings)
String interpolation can be used to easily get the value of a variable into a string; in Groovy, these are known as GStrings.
To do this, you need to include the variable reference within `${}`, inside of a literal string:
```groovy
def name = "bob"
println "Hello, my name is ${name}"
```
This doesn't stop at variables; you can also make function calls that return a string to interpolate into the literal string:
```groovy
def getName() {
    "Bob"
}
println "Hello, ${getName()}"
```

## Optional Parenthesis

### Overview
In an attempt to make code more readable, Groovy allows you the choice of omitting parenthesis.
For example, you can omit parenthesis on function calls:
```groovy
// calling a function like in java
System.out.println("Hello")
// and the "groovy" way...
println "Hello"
```

### When you need parenthesis
However, sometimes you will still need to use parenthesis. One example is when you are calling a function with no parameters;
we need to include parenthesis here so that Groovy doesn't think that you are trying to access a property:
```groovy
// accessing a property
println person.name
// accessing a function
println person.getName()
```

### Omitting Parenthesis with Named Parameters
Named parameters can be used whilst omitting parenthesis:
```groovy
myObject.myFunction param1: "First Parameter", param2: "Second Parameter"
```

## Tasks
Here are some tasks to try out some of the syntax discussed above.
For any of the tasks where you are writing code, please add them to a `groovy-syntax.groovy` file in this folder, and create a single line comment to separate each task, using the task name, like this:
```groovy
// First Task
println "code for first task"

// String Interpolation
def codeForSecondTask() {
    return ""
}
```

### Commenting
Create a comment at the top of the file that contains the following:
```text
  ___  ____   __    __   _  _  _  _    ____  _  _  __ _  ____  __   _  _
 / __)(  _ \ /  \  /  \ / )( \( \/ )  / ___)( \/ )(  ( \(_  _)/ _\ ( \/ )
( (_ \ )   /(  O )(  O )\ \/ / )  /   \___ \ )  / /    /  )( /    \ )  (
 \___/(__\_) \__/  \__/  \__/ (__/    (____/(__/  \_)__) (__)\_/\_/(_/\_)
 ```
<details>
<summary>Show Solution</summary>
The easiest way to implement this is by using a multi-line comment:

```groovy
/*
  ___  ____   __    __   _  _  _  _    ____  _  _  __ _  ____  __   _  _
 / __)(  _ \ /  \  /  \ / )( \( \/ )  / ___)( \/ )(  ( \(_  _)/ _\ ( \/ )
( (_ \ )   /(  O )(  O )\ \/ / )  /   \___ \ )  / /    /  )( /    \ )  (
 \___/(__\_) \__/  \__/  \__/ (__/    (____/(__/  \_)__) (__)\_/\_/(_/\_)
 */
```

</details>

### String Interpolation
The following example interpolates the `name` variable into a string and uses the `println` function to print it to the console:
```groovy
String name = "bob"
println "Hello ${name}"
```
We can use `System.getenv("USER")` to get the current user running the application.
Using only the `println` function, try to print the same string, but for the current user who is running the application.
<details>
<summary>Show Solution</summary>

Function calls can be interpolated into strings, just like variables:

```groovy
println "Hello, ${System.getenv("USER")}"
```

</details>

### Omitting Parenthesis
Here is a block of groovy code that looks very similar to Java; try making it more "Groovy" by omitting unnecessary parenthesis.
Why not use string interpolation, instead of the string concatenation that is already there:
```groovy
def user = System.console().readLine("What's your name?\n")
def age = System.console().readLine("Hi " + user + ", what is your age?\n")
println("Your name is " + user + " and you are " + age + " years old.")
```

<details>
<summary>Show Solution</summary>

We can remove the parenthesis for the function calls and interpolate the `user` and `age` variables, like this:

```groovy
def user = System.console().readLine "What's your name?\n"
def age = System.console().readLine "Hi ${user}, what is your age?\n"
println "Your name is ${user} and you are ${age} years old."
```

</details>
