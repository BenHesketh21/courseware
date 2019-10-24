# Links and Images



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Links](#links)
	- [Inline Link](#inline-link)
	- [Reference Link](#reference-link)
- [Images](#images)
	- [Inline Image Link](#inline-image-link)
	- [Reference Image Link](#reference-image-link)

<!--TOC_END-->
## Overview
This module explains how to integrate links and images into your Markdown files. Links and images make your Markdown more interactive and interesting, so it's really useful to learn how to use them.

## Links
There are two different link types in Markdown, but both of them render the exact same way.

### Inline Link
An inline link occurs within the text body, and is a really quick way of creating a link in your Markdown file. To do an inline link, you wrap the text you want to use as the link in square brackets `[]`, and then put the link in normal brackets `()`:
```markdown
[Search for it](http://www.google.com)
```

[Search for it](http://www.google.com)

### Reference Link
These links, as the name implies, reference another place on your document, where the link is defined. The syntax for these is similar to, but not the same as, inline links:
```markdown
Here's a link to [Google][google-link]
And one to [GitHub][github-link]

[google-link]: http://www.google.com
[github-link]: http://www.github.com
```

Here's a link to [Google][google-link]  
And one to [GitHub][github-link]

[google-link]: http://www.google.com
[github-link]: http://www.github.com

The advantage of a reference link is that if you had multiple links to the same place in your document, and the link changed, you'd only need to update the link in one place (think variable in programming!)

You can add other Markdown elements to links, such as **bold** and _italics_, by simply using the syntax you saw in the last module.

## Images
Once you know how to create links in Markdown, you can work with images! The main difference is that images are prefaced with an exclamation mark `!`.

Just like links, images have two styles that render in exactly the same way:

### Inline Image Link
To create an inline image link, enter an exclamation mark `!`, wrap the alt text in square brackets `[]`, and then wrap the link in normal brackets `()`:
```markdown
My favourite food:  
![egg](https://static-s.aa-cdn.net/img/ios/454956113/395fdfd6a701d37e111c1ff20b993aed)
```

My favourite food:

![egg](https://static-s.aa-cdn.net/img/ios/454956113/395fdfd6a701d37e111c1ff20b993aed)

You don't necessarily need to add the alt text (in this case `egg`), but it makes the content asccesible to a wider audience (such as visually impaired), which is always a good thing.

### Reference Image Link
For this, you follow the same pattern as the reference link in the previous section, but use the `!` as well:
```markdown
![Manchester City][blue]
![Manchester United][red]

[blue]: https://cdn.images.express.co.uk/img/dynamic/footballteams/x256/20.png
[red]: https://icons.iconseeker.com/png/fullsize/soccer-teams/manchester-united-fc-logo.png
```

![Manchester City][blue]

![Manchester United][red]

[blue]: https://cdn.images.express.co.uk/img/dynamic/footballteams/x256/20.png
[red]: https://icons.iconseeker.com/png/fullsize/soccer-teams/manchester-united-fc-logo.png

And that's it, for now, for links and images!
