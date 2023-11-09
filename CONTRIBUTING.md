# contributing
:tada: thanks so much for considering contributing to this project! :tada:

A quick note before we get started: this project and everyone participating in it is governed by our [code of conduct](CODE_OF_CONDUCT.md). By participating you are expected to uphold this code, so please make yourself familiar with it.

## 🚨 TL;DR
Since this project is about collecting resources, the most simple and helpful contribution you could make is to add one (or more) example(s) to the main repository README file, i.e. one of these:

![Screenshot 2023-11-09 at 15 56 16](https://github.com/lakillo/archaeology-machine-learning/assets/81825476/4c7de836-36a3-4f9b-92f0-88c0da963e5d)

To contribute an example by inserting a row into an existing table, please use the following formatting (for why this format, see [here](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#repo-style-guide)):

```
|<!-- -->title | year | data | technique | paper | code<!-- -->|
```

Simple contributions of this kind are hugely appreciated and make all the difference ✨

If the section you want to contribute to doesn't exist yet, please read on for more info on how to expand the existing repository structure.

## how to contribute

### 🌱 easy
If you don't have a github account but wanted to share feedback or ask questions about the project:
* email Lucy at l.killoran.1@research.gla.ac.uk

If you do have a github account:
* introduce yourself to the community by posting a message on our [👋 community introductions issue](https://github.com/lakillo/archaeology-machine-learning/issues/7)
* what do you think about the project's overall vision? leave a comment on our [🗺️ roadmap](https://github.com/lakillo/archaeology-machine-learning/issues/3) and let us know!
* report a mistake, error, or missing section in the repository contents by [📝 creating an issue](https://github.com/lakillo/archaeology-machine-learning/issues/new)

### 🪴 intermediate
* add examples to the main repository README file following the [repo style guide](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#repo-style-guide)
* check out the current [🐢 milestones](https://github.com/lakillo/archaeology-machine-learning/milestones) we're working towards and help us resolve one of the open issues

*both of the above options will involve making a pull request to ask for your changes to be merged into the main project, see [making a pull request](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#making-a-pull-request) below for details on how to do this.

### 🌴 advanced
* suggest improvements for the project or help us plan our next milestones by [📝 creating an issue](https://github.com/lakillo/archaeology-machine-learning/issues/new)

## repo style guide
Before making a contribution to the main repository contents (the README), please familiarise yourself with the information recorded for each example:
* title: the title of the project / tool / academic paper
* year: the year of publication / release
* data: the data type used (e.g. aerial imagery, lidar, satellite)
* technique: the machine learning technique used (e.g. classification, segmentation)

We use specific formatting when documenting examples in the README. This formatting enables us to easily turn the README contents into a spreadsheet, which will be available for download with each archived release of the repository.

To contribute an individual example to a section, please us the following formatting:

```
|<!-- -->title | year | data | technique | paper | code<!-- -->|
```

To contribute a whole new section or subsection, please use the following formatting:

```
## high-level application area name (e.g. remote sensing, which includes data types aerial, lidar, satellite, etc)
### first machine learning technique name
| title | year | data | technique | paper | code |
| ---- | ---- | ---- | ---- | ---- | ---- |
|<!-- -->title | year | data | technique | paper | code<!-- -->|

### second machine learning technique name
| title | year | data | technique | paper | code |
| ---- | ---- | ---- | ---- | ---- | ---- |
|<!-- -->title | year | data | technique | paper | code<!-- -->|

### third machine learning technique name ...
```

## making a pull request
This repository's contents is written in [github flavored markdown](https://guides.github.com/features/mastering-markdown/). To manage changes to the project's content we use [github's standard workflow](https://guides.github.com/introduction/flow/), which is based on contributors making requests for their changes to be pulled into the main project content (or, a pull request!).

To make a pull request:
1. [create a fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) of this
   repository on GitHub
2. [clone your fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository) of this repository to create a local copy on your computer
3. [create a new branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository) in your local copy for each significant change
4. [commit the changes](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits) in that branch
5. push that branch to your fork on github
6. [submit a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) from that branch to the master repository
7. if you receive feedback, make changes in your local clone and push them to your branch on github (the pull request will update automatically)
8. pull requests will be merged  after at least one other person has reviewed the pull request and approved it

For lots more heplful info, check out github's guidance on [collaborating with pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests).

## attribution
This document is adapted from the contributor guidelines for Open Life Science.
