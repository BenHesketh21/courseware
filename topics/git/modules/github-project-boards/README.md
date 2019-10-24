# GitHub Project Boards
<!--Props
{
    "prerequisites":[
        "git/pull-requests"
    ]
}
-->

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Project Board Make-up](#project-board-makeup)
- [Cards](#cards)
- [Types of Project Boards](#types-of-project-boards)
- [Templates for Project Boards](#templates-for-project-boards)
- [Creating a User-Owned Project Board](#creating-a-userowned-project-board)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview

Project boards on **GitHub** help you organize and prioritise your work.

You can create project boards for specific feature work, comprehensive roadmaps, or even release checklists.

With project boards, you have the flexibility to create customised workflows that suit your needs.

## Project Board Make-up

Project Boards are made up of **issues**, **pull requests** and **notes**, that are categorised as **_cards_** in columns that you have pre-defined. These can be as basic or advanced as you like.

You can drag and drop, or use keyboard shortcuts, to re-order cards within a column, move cards from column to column, and change the order of columns.

## Cards

Project board cards contain relevant metadata for issues and pull requests.

You can view and make lightweight edits to issues and pull requests within your project board by clicking on the issue or pull request's title.

## Types of Project Boards

Types of project boards:

* User-owned project boards: can contain issues and pull requests from any personal repository.
* Organisation-wide project boards: can contain issues and pull requests from any repository that belongs to an organisation.
* Repository project boards: scoped to issues and pull requests within a single repository.

## Templates for Project Boards

You can use templates to quickly set up a new project board.

When you use a template to create a project board, your new board will include columns, as well as cards with tips for using project boards (you can delete these using the `...` on each card).

You can also choose a template with automation already configured.

The options are:

* Basic kanban: Track your tasks with `To do`, `In progress`, and `Done` columns
* Automated kanban: Cards automatically move between `To do`, `In progress`, and `Done` columns
* Automated kanban with review: Cards automatically move between `To do`, `In progress`, and `Done` columns, with additional triggers for pull request review status
* Bug triage: Triage and prioritise bugs with `To do`, `High priority`, `Low priority`, and `Closed` columns

## Creating a User-Owned Project Board

The first step is to go to GitHub, click `Projects` and then `New Project`:

![Start](https://i.imgur.com/0Lzpd1t.png?1)

Fill in the form, including name of the board, the template you want to use, and which reository to link to. For this example, we will use a `Basic kanban` and link it to a repository called `scripts`:

![form1](https://i.imgur.com/b3Yfyjz.png?1)
![form2](https://i.imgur.com/esBvG7A.png?1)

The Project Board will now show up under `Projects`:

![PB](https://i.imgur.com/xWOJL1A.png?1)

From here, you can close or edit the board using the `...`:

![edit](https://i.imgur.com/nSOwSHV.png?1)

When you click on the Project Board, you will see the columns defined by the template you chose (in this, we have `To Do`, `In Progress` and `Done`). On the right hand side, you can see the **open issues** and any **Pull Requests** from the linked reository.

As this is a User-Owned Project Board, we could uncheck the box that says `Only show results from linked repositories`, and we would be able to see the issues and Pull Requests from all owned repositories:

![add](https://i.imgur.com/VzWZ33p.png?1)

From here you can drag cards to the columns, with the `To Do` column being a good starting point:

![ToDo](https://i.imgur.com/fMHh54a.png?1)

The process of moving the cards between columns in this example is manual, but it could all be automated if we wished to do so!

Project Boards are a great colaborative tool for tracking the different projects that you, or your team, are working on.

## Tasks

1. Create a new repository, or use an existing one
2. Go into your repository, and click `issues`:

![issues](https://i.imgur.com/x8uYejW.png?1)

3. Submit 3 issues for your repository. For now, these just need a title
4. Create a User Owned project board and link your respoitory to it
5. Add the issues you made to the `To Do` column
6. Create a Repository scoped project board for your repository and add the issues you submitted to the `To Do` column.

You can do lots with GitHub Project Boards and it is a very broad topic. Make sure to experiment with different templates and also with automating your boards!
