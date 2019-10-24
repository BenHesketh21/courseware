# Functions



<!--TOC_START-->
## Contents
- [Basic Usage](#basic-usage)
	- [Creating a Function](#creating-a-function)
	- [Calling a Function](#calling-a-function)
	- [Creating Functions with Parameters](#creating-functions-with-parameters)
	- [Calling Functions with Parameters](#calling-functions-with-parameters)
- [Return Values](#return-values)
	- [No value (void)](#no-value-void)
	- [Returning a Type](#returning-a-type)
	- [Return Keyword](#return-keyword)
- [Tasks](#tasks)
	- [Create Some Basic Functions](#create-some-basic-functions)
		- [Current User Message Function](#current-user-message-function)
		- [Addition Function](#addition-function)

<!--TOC_END-->
## Basic Usage

### Creating a Function
Functions can be defined by declaring a type to return, like `String` or specifying `void`, meaning that the function wont return anything and then including `() {}` after the function name:
```groovy
void myFunction() {
    // does lots of cool stuff
}
```

### Calling a Function
Stating the function name with `()` afterwards will call (execute) the function:
```groovy
void testFunction() {
    println "I've been called!"
}
testFunction()
```
Note: parenthesis cannot be omitted if the function does not take any parameters.

### Creating Functions with Parameters
We can provide parameters to functions with or without types:
```groovy
def functionWithoutTypes(param1, param2) {
    println "${param1}, ${param2}"
}
def functionWithTypes(String param1, String param2) {
    println "${param1}, ${param2}"
}
```

### Calling Functions with Parameters
Parameters must be passed in order to the function:
```groovy
void logItem(String item, int amount) {
    println "Item: ${item}, Amount: ${amount}"
}
logItem("Apple", 5)
```

## Return Values

### No value (void)
To create a function that isn't going to return a value, the void keyword must be used:
```groovy
void myFunction() {
    // Do not return any values
}
```

### Returning a Type
You can specify a return types for functions as well:
```groovy
String myStringFunction() {
    // returning a string value
    return "Some String"
}
Account myAccountFunction() {
    // returning a new account project
    return new Account()
}
```

### Return Keyword
The return keyword is commonly used for specifying values to be returned from a function however this keyword can be omitted if you choose to do so:
```groovy
String withReturnKeyword() {
    return "String Example"
}
String withoutReturnKeyword() {
    "String Example"
}
```

## Tasks
Please create any files for these tasks in this folder.

### Create Some Basic Functions

#### Current User Message Function
Create a file called `current-user-message.groovy`.
The following function can take a string parameter, a message, and then add the current user's name to the message provided, this string will then be returned.
Add the function and function call to `current-user-message.groovy` and execute the file to see it working.
```groovy
String formatMessageForCurrentUser(String message) {
    "Hi ${System.getenv("USER")}, ${message}"
}
println formatMessageForCurrentUser("how are you?")
```

#### Addition Function
Try to create another function that can add two numbers together and return the value as an `int` type.
Create this in a file called `addition-function.groovy`
<details>
<summary>Show Solution</summary>

```groovy
int sumOf(int firstNumber, int secondNumber) {
    firstNumber + secondNumber
}
println sumOf(1, 2)
```

</details>
