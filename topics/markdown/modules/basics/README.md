# Basics



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Italics & Bold](#italics--bold)
- [Headers](#headers)
- [Blockquotes](#blockquotes)
- [Lists](#lists)
- [Paragraphs](#paragraphs)
	- [Hard Breaks](#hard-breaks)
	- [Soft Breaks](#soft-breaks)

<!--TOC_END-->
## Overview

This module covers some of the fundamentals of Markdown. After this, you should be well on your way to creating your own Markdown files. 

## Italics & Bold
Making text _italic_ and/or **bold** is really useful. Thankfully, it's simple to do. To make text italic, surround it with `_`, and to make it bold, surround it with `**`, like so:
```markdown
_this would make text italic_
**this would make text bold**
```
You can make words **_both bold and italic_**:
```markdown
**_This would make the sentence bold and italic_**
```

## Headers
To make headers in Markdown, you preface the phrase with a `#` symbol. Headers come in different size, which can be dictated by the number of `#` symbols you use:
```markdown
# Header 1 = Largest
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6 - Smallest
```

## Blockquotes
If you need to call special attention to a quote from another source, or design a pull quote for a magazine article, then Markdown's blockquote syntax will be useful. A blockquote is a sentence or paragraph that's been specially formatted to draw attention to the reader:
> "Hard work beats talent, when talent doesn't work hard"

To do this, all you have to do is preface the line with a `>` symbol:
```markdown
> This would make this sentence a block quote
```
If your quote spans multiple lines, you will need to put a `>` before each line (even the empty lines):
```markdown
> Quote spanning
>
>
> multiple lines
```

## Lists
You can create a list with bullet points, by prefacing each list item with a `*`, or a list with numbers, by prefacing each list item with a number and full stop (`1.`):
```markdown
* Bullet
* Point
* List

1. Numbered
2. List
```
* Bullet
* Point
* List

1. Numbered
2. List

You can make nested lists by indenting each item **one space** more than the preceding item:
```markdown
* Indented
 * list
 * would look like
  * this
```
* Indented
  * list
  * would look like
    * this

## Paragraphs
If you want text to format your text to span a few lines (think poetry or a small paragraph under a list item), you won't be able to manually insert each new line:
```markdown
This poetry is very smart,
Each new line is a new start,
Or is it?
```
Eventhough this looks like a verse of (amazing) poetry, Markdown would render this as one long line - this isn't what we want!

### Hard Breaks
A hard break is where you would take the above verse and forcefully insert new lines:
```markdown
This poetry is very smart,

Each new line is a new start,

Or is it?
```
Doing this would affect the togetherness of the text, which also isn't what we want to do.

### Soft Breaks
We want to use a soft break for this. To do this, you would insert 2 spaces at the end of each line (below, each `.` denotes a space):
```markdown
This poetry is very smart,..
Each new lines is a new start,..
It is!
```

It's not as simple as making the text 'readable'...we have to make sure Markdown interprets the text how we want it to.
