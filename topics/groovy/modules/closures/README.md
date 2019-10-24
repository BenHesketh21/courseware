# Closures



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Basic Usage](#basic-usage)
	- [Create](#create)
	- [Execute](#execute)
	- [Parameters](#parameters)
	- [Implicit `it` Parameter](#implicit-it-parameter)
- [Using a Closure as a Parameter](#using-a-closure-as-a-parameter)
	- [`each` Function Example](#each-function-example)
	- [`find` Function Example](#find-function-example)

<!--TOC_END-->
## Overview
A closure in Groovy is an open, anonymous, block of code that can take arguments, return a value and be assigned to a variable.  A closure may reference variables declared in its surrounding scope.  In opposition to the formal definition of a closure, a closure in the Groovy language can also contain free variables that are defined outside of its surrounding scope.
Although it breaks the formal concept of a closure, a Groovy closure does offer many advantages.

## Basic Usage

### Create
Here is a very simple example of a Closure:
```groovy
def simpleClosure = {
    println "Hi"
}
```

### Execute
We can execute a closure either just like we would a function, by using `()`, or by using the `call()` function:
```bash
def simpleClosure = {
    println "Hi"
}
// using ()
simpleClosure()
// using the call() function
simpleClosure.call()
```

### Parameters
Closures can be configured to have parameters very easily:
```groovy
// one parameter
def singleParamClosure = {param ->
    println "${param}"
}
// two parameters
def multiParamClosure = {param1, param2, param3 ->
    println "${param1}, ${param2}, ${param3}" 
}
```

### Implicit `it` Parameter
If you define a closure without parameters, it can still take a single parameter; this parameter will be stored in a variable called `it`:
```groovy
def justAnotherClosure = {
    println "Value of it: ${it}"
}
justAnotherClosure "test"
```

## Using a Closure as a Parameter
Because closures are just stored as variables, they can be passed to other functions and closures:
```groovy
def myClosure = {
    println "Hello from myClosure"
}

void myFunction(exec) {
    exec()
}

myFunction myClosure

// Hello from myClosure
```

### `each` Function Example
We can pass a closure to the `each` function, which will execute the closure for each element in an array:
```groovy
def students = ["bob", "jay", "shafeeq", "dev"]

students.each {
    println it
}
```

### `find` Function Example
The `find` function can be used to select an element from an array; all we have to do is pass it a closure that returns a boolean value. If the boolean value is true, the element will be returned:
```groovy
def students = ["bob", "jay", "shafeeq", "dev"]

def numberOne = students.find {
    it.equals "shafeeq"
}

println numberOne
```
