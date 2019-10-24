# Arrays

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Create](#create)
	- [One or Less Elements](#one-or-less-elements)
	- [Multi Dimentional Arrays](#multi-dimentional-arrays)
- [Access Array Elements](#access-array-elements)
	- [By Index](#by-index)
	- [Multiple Elements](#multiple-elements)
		- [Ranges](#ranges)
	- [Last Element](#last-element)
	- [Multi Dimensional](#multi-dimensional)
- [Add Array Elements](#add-array-elements)
	- [Append to An Array](#append-to-an-array)
- [Change Array Elements](#change-array-elements)
- [Tasks](#tasks)
	- [Log Files](#log-files)
		- [Getting the Log Files](#getting-the-log-files)
		- [Last 3 Log File Paths](#last-3-log-file-paths)
		- [Compress the Log Files](#compress-the-log-files)
	- [CSV Table](#csv-table)
		- [Read in the CSV File](#read-in-the-csv-file)
		- [Create a Multi Dimensional Array from the CSV](#create-a-multi-dimensional-array-from-the-csv)
		- [Iterate the Multi Dimentional Array](#iterate-the-multi-dimentional-array)

<!--TOC_END-->
## Overview
Arrays hold a list of data, in PowerShell they don't need to be the same type of data.
Arrays can come in useful whenever we need to store lots of information to process one at a time, for instance:
- Servers to connect to and configure
- Application folders to build and upload
- Log files to analyse

## Create
To create an array the easiest way to do it is just list the data, seperated by commas:
```powershell
$myArray = 1,"two",3,"four",5
```

### One or Less Elements
Sometimes you will need to explicitly cast to array, for instance if there is only 1 or no elements in the array to start with:
```powershell
# array with 1 element
$myArray = @(1)
# an empty array
$myArray = @()
```

### Multi Dimentional Arrays
A multi dimentional array is basically just storing arrays within an array, this comes in useful when processing grid or table information such as CSV files.
The multi dimentional arrays can be created by nesting brackets `()` in the assignment:
```powershell
$multiDimentionalArray = @((1,2,3),(1,2,3))
# same assignment but over multiple lines
$multiDimentionalArray = @(
    (1,2,3),
    (1,2,3)
)
```

## Access Array Elements
There wouldn't be much point storing data in arrays unless we can access them later, so that's what we'll be looking at here in this section.

### By Index
A very common way to access some data in an array is by its index.
Just like many other languages index start at `0`, so the first element in the list is at index `0`.
```powershell
# access the 1st element in an array
$myArray[0]
## access the 3rd element in an array
$myArray[2]
```

### Multiple Elements
A comma seperated list of indexes can be provided to access multiple elements in an array:
```powershell
$myArray = @(1,2,3)
# access the 1st and 3rd elements 
$myArray[0,2]
```

#### Ranges
Multiple elements can be accessed from an array as a range.
For example you can access elements 1 to 3 (0,1,2):
```powershell
$myArray = @(1,2,3)
$myArray[0..2]
```
A range and specific indexes can be access by adding `+`:
```powershell
$myArray = @(1,2,3,4,5,6,7,8)
# access the 1st and 3rd elements, also access elements at index 4 to 7
$myArray[0,2+4..7]
```

### Last Element
The last element of an array can be accessed by using `-1` as the index:
```powershell
$myArray = @(1,2,3,4,5,6,7,8)
# show only the last element (8)
$myArray[-1]
```
You can think of `-1` as a "special" index for getting the last element - all other indexes must be a postive number, for instance `-5` wouldn't work.

### Multi Dimensional
Access to elements in multi dimentional arrays work pretty much the same as when you are accessing regular arrays.
We can use two sets of brackets `[][]` for specifying which elements we would like:
```powershell
$people = @(
    ("Bob",23,"Manchester"),
    ("Jay",27,"San Francisco")
)
# Bob
$people[0][0]
# 23
$people[0][1]
# Manchester
$people[0][2]
# Jay
$people[1][0]
# 27
$people[1][1]
# San Franciso
$people[1][2]
```
The easiest way to think of this is like you are accessing an array inside of another array.
You specify which array with the first index and then which element inside of that sub array that you want.
Based on the example above here is a table showing which indexes get which elements in the array:

| |0|1|
|-|-|-|
|0|Bob (`[0][0]`)|Jay (`[1][0]`)|
|1|23 (`[0][1]`)|27 (`[1][1]`)|
|2|Manchester (`[0][2]`)|San Francisco (`[1][2]`)|

## Add Array Elements
There are of scenarios where the array has been created but we still intend to added more elements.

### Append to An Array
Elements can be appended to an array using the `+=` operator:
```powershell
$myArray = 1,2,3
$myArray += 4
```

## Change Array Elements
Once an array has been created we are still able to amend any of the elements in the list by specifying the index:
```powershell
$myArray = 1,2,3
# change the value of the 1st element in the array
$myArray[0] = 10
```

## Tasks
This set of tasks is split up into a couple of sections, managing log files with arrays and the second task is to read in a comma seperated values CSV file and display it as a table using multi dimentional arrays.

### Log Files
In this section we are going to be making a script that can:
- Read a folder full of log files
- Compress the 3 latest log files into a zip archive

Start by creating a file in this module folder called `last-3-log-files.ps1`.

#### Getting the Log Files
The log files are stored in the `logs` folder on this module, for purpose of this exercise they are actually empty but named with a date.

We will need a list of the log file names before we can start figuring out which are the 3 latest:
```powershell
$logFiles = Get-ChildItem "logs" -Filter *.log
```
The log file names will actually be in ascending order by default, we can reverse this to make it easier for us to get the latest 3:
```powershell
$logFiles = Get-ChildItem "logs" -Filter *.log
[Array]::Reverse($logFiles)
```

#### Last 3 Log File Paths
The paths for the log files that we want to compress need to be aquired.
We can iterate over the log files, only selecting the first three using a ranged selection.
When we are iterating over this list, we can collect the `FullName` property which is the full path to the log file, and store it in another list:
```powershell
$logFiles = Get-ChildItem "logs" -Filter *.log
[Array]::Reverse($logFiles)
$logFilePaths = @()
ForEach ($logFile in $logFiles[0..2]) {
    $logFilePaths += $logFile.FullName
}
```

#### Compress the Log Files
Now we know which files to compress we can compress them into an archive using the `Compress-Archive` command.
A zip file called `logs.zip` will now be created:
```powershell
$logFiles = Get-ChildItem "logs" -Filter *.log
[Array]::Reverse($logFiles)
$logFilePaths = @()
ForEach ($logFile in $logFiles[0..2]) {
    $logFilePaths += $logFile.FullName
}
$compress = @{
    Path=$logFilePaths
    CompressionLevel = "Optimal"
    DestinationPath = "logs.zip"
}
Compress-Archive @compress
```

### CSV Table
There is a file called `scores.csv` which contains some results for test takers.
This section includes some heavy use of loops in PowerShell, don't worry if you don't quite understand these at this point, just know that we are using loops to traverse through the arrays, processing each element one at a time.

Start this section by creating a file in this module folder called `csv-scores-table.ps1`.

#### Read in the CSV File
The contents of the CSV can be obtained by using the `Get-Content` command:
```powershell
$contents = Get-Content scores.csv
```

#### Create a Multi Dimensional Array from the CSV
To create a multi dimensional array from the contents we can read the contents line by line and seperate them into columns and rows:
```powershell
$contents = Get-Content scores.csv
$rows = @()
ForEach ($line in $contents) {
    $columns = $line -split ","
    $rows += , $columns
}
```
Notice the way that `$columns` is being appended to `$rows`; a comma has been included to say explicity that we want to append the `columns` variable to `$rows` as an array:
```powershell
$rows += , $columns
```

#### Iterate the Multi Dimentional Array
Now the information is sorted in a multi dimensional array, a loop can be used to iterate through it and print out the values in a basic format for a table:
```powershell
$contents = Get-Content scores.csv
$rows = @()
ForEach ($line in $contents) {
    $columns = $line -split ","
    $rows += , $columns
}
For ($row=0;$row -lt $rows.Length;$row++) {
    "=============="
    $output = ""
    For ($column=0; $column -lt $rows[0].Length;$column++) {
        $output += "$($rows[$row][$column]) | "
    }
    $output
}
```
The ouput should look something like this:
```text
==============
Name | Score |
==============
Bob | 80% |
==============
Jay | 85% |
==============
John | 80% |
==============
Tadas | 85% |
```
