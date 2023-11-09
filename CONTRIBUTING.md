# contributing
:tada: Thanks for taking the time to contribute! :tada:

You can make this project better by contributing to it. You can report mistakes and errors, create more content, or help with project planning. Whatever your background, there's a way to contribute: through the github website or desktop app, via the command-line, or even without
dealing with github.

## code of conduct
This project and everyone participating in it is governed by our [code of conduct](CODE_OF_CONDUCT.md). By participating you are expected to uphold this code, so please make yourself familiar with it.

## how to contribute

### 🌱 easy
If you don't have a github account but wanted to share feedback or ask questions about the project:
* email Lucy at l.killoran.1@research.gla.ac.uk

If you do have a github account:
* introduce yourself to the community by posting a message on our [community introductions issue](https://github.com/lakillo/archaeology-machine-learning/issues/7)
* report a mistake or error in the repository contents by [creating an issue](https://github.com/lakillo/archaeology-machine-learning/issues/new)

### 🪴 intermediate
* add examples to the main repository README file following the [repo style guide](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#repo-style-guide)
* check out the current [milestones](https://github.com/lakillo/archaeology-machine-learning/milestones) we're working towards and help us resolve one of the open issues

*both of the above options will involve making a pull request to ask for your changes to be merged into the main project, see [making a pull request](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#making-a-pull-request) below for details on how to do this.

### 🌴 advanced
* suggest improvements for the project or help us plan our next milestones by [creating an issue](https://github.com/lakillo/archaeology-machine-learning/issues/new)

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
