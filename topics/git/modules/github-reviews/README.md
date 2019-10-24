# GitHub Reviews

<!--PROPS
{
    "prerequisites":[
        "git/pull-requests"
    ]
}
-->

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Requesting a Review](#requesting-a-review)
- [Reviewing a PR](#reviewing-a-pr)
	- [Making Comments](#making-comments)
		- [Making a Suggestion in Your Comment](#making-a-suggestion-in-your-comment)
	- [Editing and Deleting Comments](#editing-and-deleting-comments)
	- [Keeping Track of Reviewed Files](#keeping-track-of-reviewed-files)
	- [Finishing the Review](#finishing-the-review)
- [Good Practice](#good-practice)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview

When submitting a Pull Request (PR) on GitHub (or most Git Providers), you can request a review to take place.

In the review, other developers and/or members of your team can propose/request changes, ask for clarity in certain areas, discuss certain files, and eventually (hopefully!) approve the PR.

Once the PR has been approved, it is then able to be merged to another branch, usually `develop` or `master`.

## Requesting a Review

You request a review when submitting a PR. All you need to do is use the `Reviewers` section on the right hand side:

![PR](https://i.imgur.com/7WOX06T.png?1)

This will request a review from the person you choose from the dropdown.
Please note that the person you would like to review your PR must be a collaborator on the GitHub project.

## Reviewing a PR

If someone has requested a review from you, this will show up in the `Pull Requests` section, under the repository on GitHub:

![PR1](https://i.imgur.com/r1bU4Su.png?1)

Once you have clicked on the correct PR, you will see that your review has been requested. You can click the `Add your review` button to start:

![Review](https://i.imgur.com/8hIAoyo.png?1)

### Making Comments
If you want to make a comment on a line in a file, you just use the blue `+` sign on the left hand side (it will appear as you hover over the `+` sign):

![Plus](https://i.imgur.com/QRqqWZX.png?1)

#### Making a Suggestion in Your Comment
In the popup box, you can make a general comment if you wish or you can use the highlighted button to insert a suggestion:

![Suggestion](https://i.imgur.com/CkGL6e7.png?1)

This will paste the line you are commenting on into the comment box, so you can explicitly state any changes you think would be beneficial.

The first time you do this, you will have the option to click on `Start review`, which will begin tracking any changes you make (including the one you just made).

From then on, when you make a comment/suggestion, the `Start review` button will be replaced with a button saying `Add Review Comment`:

![ReviewStart](https://i.imgur.com/Znn9hPA.png?1)

### Editing and Deleting Comments
You can edit or delete any comments or suggestions you make:

![Edit](https://i.imgur.com/XWQIBWD.png?1)

### Keeping Track of Reviewed Files
And, following good practice, you should check `viewed` when you are done reviewing a file:

![Checked](https://i.imgur.com/fV8LJsU.png?1)

### Finishing the Review
When you have viewed all files, you can click on `Finish your review`:

![Finish](https://i.imgur.com/LkomHRf.png?1)

This will bring up a comment box where you can choose to:

* Make a comment without approval - this is usually asking for clarity around something
* Approve the review - the changes can then be merged into `develop` or `master`
* Request changes - this stops a merge from happening before the changes you've requested have been made

Once you have made your choice, you can go ahead and click `Submit review`, which will finish the review process and notify the person who requested the review that the review has been completed:

![Complete](https://i.imgur.com/NbuxasH.png?1)

## Good Practice

It is always good practice to not only look over any files in a review, but also to **test** any code in there.

If there is code in the file, try to run it on your machine and make sure that:

* It runs correctly
* It follows best practices
* It is efficient
* Any instructions given are clear.

## Tasks

NB. This task works much better with somebody else. If you really want to do it individually, you will need to make another GitHub account...

1. Create a Pull Request, similar to how you will have done in the `Pull Requests` module, to merge a feature change from a `feature` branch into the `master` branch (ideally, you will make something that requires changing - for example, some broken code)
2. Add a Reviewer to the PR
3. Have the other person/other account do the same thing on their GitHub (requesting a review from you)
4. Start the review, making sure to test the new feature(s)
5. Make some comments for the other person/account
6. Either approve the review, or request changes
7. Complete the review
8. Complete the merge once your own PR has ben reviewed and approved by the other person/account
