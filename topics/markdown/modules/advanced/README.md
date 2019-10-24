# Advanced



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Image Align](#image-align)
	- [Left Alignment](#left-alignment)
	- [Right Alignment](#right-alignment)
	- [Centre Alignment](#centre-alignment)
- [Collapse Sections](#collapse-sections)
- [Tables](#tables)
	- [Table Alignment](#table-alignment)
- [Closing](#closing)
- [Task](#task)

<!--TOC_END-->
## Overview
This topic will go over some of the more advanced Markdown syntax and formatting. There's lots you can do with Markdown, so experiment beyond this brief introduction to it!

## Image Align
As you saw in the last topic, we didn't dictate where we wanted our images to be displayed on the page. You'll be glad to hear that we are able to do this: 

### Left Alignment

<img align="left" width="100" height="100" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">

To left align your images, you need to do the following:
```html
<img align="left" width="100" height="100" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">
```

___

### Right Alignment

<img align="right" width="100" height="100" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">

To right align your images, use:
```html
<img align="right" width="100" height="100" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">
```

___

### Centre Alignment
To align your images in the centre of a page, simply use:
```html
<p align="center">
  <img width="460" height="300" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">
</p>
```

<p align="center">
  <img width="460" height="300" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">
</p>

As you can see, you can also dictate the width and height of an image at the same time!

___

## Collapse Sections
<details>
<summary>Click to learn!</summary>

Collapsing large blocks of text can make your Markdown easier to read. It is also really useful for solutions or hints to exercises.

To add a collapsing section, you need to do:
```html
<details>
<summary>"Click to expand"</summary>
this is hidden
</details>
```
</details>

___

## Tables
To add a table, use three or more hyphens (---) to create each column’s header, and use pipes (|) to separate each column. You can optionally add pipes on either end of the table:
```markdown
| Column1     | Column2     |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
```

| Column1     | Column2     |
| ----------- | ----------- |
| Row1        | Row1        |
| Row2        | Row2        |

### Table Alignment
You can align text in the columns to the left, right, or center by adding a colon (:) to the left, right, or on both side of the hyphens within the header row:
```markdown
| Left Align  | Centre Align | Right Align   |
| :---        |    :----:    |          ---: |
| Row1        | Row1         | Row1          |
| Row2        | Row2         | Row2          |
```

| Left Align  | Centre Align | Right Align   |
| :---        |    :----:    |          ---: |
| Row1        | Row1         | Row1          |
| Row2        | Row2         | Row2          |

## Closing
By no means is this an extensive Markdown module, but it should give you the tools to create Markdown README.md files to a relatively good standard. Make sure to give the task below a go!

## Task
* Go to the [projects folder](./project)
* Create a README.md to explain how to get the simple python application up and running
* The formatting is for you to be creative with, but you must highlight to the user that they need to:
  * Install python3 (including a link to the website)
  * Install `pip3` - `sudo apt install python-pip`
  * Pip install virtualenv with `pip3 install virtualenv`
  * Create their virtual environment - `virtualenv venv`
    * And make sure they are working inside of it - `source venv/bin/activate`
  * Install the pip dependencies file, using `pip3 install -r pip_dependencies.txt`
  * Run the python program - `python3 pass_gen.py`
