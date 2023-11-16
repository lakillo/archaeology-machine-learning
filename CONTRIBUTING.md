# ✅ contributing
:tada: thanks so much for considering contributing to this project! :tada:

A quick note before we get started: this project and everyone participating in it is governed by our [code of conduct](CODE_OF_CONDUCT.md). By participating you are expected to uphold this code, so please make yourself familiar with it.

## ⏩ TL;DR
Since this project is about collecting resources, the most simple and helpful contribution you could make is to add one (or more) example(s) to the main repository README file, i.e. one of these:

<img width="854" alt="Screenshot 2023-11-16 at 10 57 59" src="https://github.com/lakillo/archaeology-machine-learning/assets/81825476/7dc06a90-8ef0-4605-aa5b-05e4763d8647">

To contribute an example by inserting a row into an existing section of the README, please copy and paste the below template, replacing the text with your contribution:

```
|<!-- -->title | authors (max 2 names, or first author and et al) | year | data type | technique | [paper](link) or paper:tbc | [code](link) or code:tbc | [data](link) or data:tbc<!-- -->|
```

Simple contributions of this kind are hugely appreciated and make all the difference ✨

For why we use this format, see [here](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#repo-style-guide).

If the section you want to contribute to doesn't exist yet, please read on for more info on how to expand the existing repository structure.

## ✅ how to contribute

### introduce yourself!
1. post a message on our [👋 community introductions issue](https://github.com/lakillo/archaeology-machine-learning/issues/7)

### fix typos or errors in existing content
1. report a mistake or error in the repository contents by [📝 creating an issue](https://github.com/lakillo/archaeology-machine-learning/issues/new)
2. help us resolve any open issues relating to errors by [making a pull request](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#making-a-pull-request)

### work on an open issue
1. check out the current [🐢 milestones](https://github.com/lakillo/archaeology-machine-learning/milestones) we're working towards
2. click into a milestone to see the open issues
3. help us resolve any open issues by [making a pull request](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#making-a-pull-request)

### add new examples to existing sections in the README
1. familiarise yourself with the [repo style guide](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#repo-style-guide)
2. to contribute by inserting a row into an existing section of the README, copy and paste the below template, replacing the text with your contribution:

```
|<!-- -->title | authors | year | data type | technique | [paper](link) or paper:tbc | [code](link) or code:tbc | [data](link) or data:tbc<!-- -->|
```

For why we use this format, see [here](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#repo-style-guide).

### add new sections to the README
1. familiarise yourself with the [repo style guide](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#repo-style-guide)
2. to contribute a new section or subsection, copy and paste the below template, replacing the text with your contribution:

```
## high-level application area name (e.g. remote sensing, which includes data types aerial, lidar, satellite, etc)
### first machine learning technique name
|title | authors | year | data type | technique | paper | code | data |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|<!-- -->title | authors | year | data type | technique | [paper](link) or paper:tbc | [code](link) or code:tbc | [data](link) or data:tbc<!-- -->|

### second machine learning technique name
|title | authors | year | data type | technique | paper | code | data |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|<!-- -->title | authors | year | data type | technique | [paper](link) or paper:tbc | [code](link) or code:tbc | [data](link) or data:tbc<!-- -->|

### third machine learning technique name ...
```

### help us plan the project vision and roadmap
1. familiarise yourself with our project [🗺️ roadmap](https://github.com/lakillo/archaeology-machine-learning/issues/3)
2. in the [🗺️ project vision and roadmap](https://github.com/lakillo/archaeology-machine-learning/milestone/2) milestone, comment on an open issue or [📝 create a new issue](https://github.com/lakillo/archaeology-machine-learning/issues/new) explaining your idea
3. help us resolve any open issues relating to project planning by [making a pull request](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#making-a-pull-request)

### contribute without a github account
1. get in touch via email at l.killoran.1@research.gla.ac.uk

## 💅 repo style guide
This repository's contents is written in [github flavored markdown](https://guides.github.com/features/mastering-markdown/). 

When making a contribution to the main repository contents in the README, please use the below structure and formatting:
* title: the title of the project / tool / academic paper
* authors: maximum 2 names, or first author and et al if there are more than two authors
* year: the year of publication / release
* data: the data type used (e.g. aerial imagery, lidar, satellite)
* technique: the machine learning technique used (e.g. classification, segmentation)
* paper: the link to the paper (if there is one) in markdown style [paper](link), or paper:tbc if no link available
* code : the link to the code in markdown style [code](link), or code:tbc if no link available
* dataset : the link to the data in markdown style [data](link), or datasest:tbc if no link available

We use this formatting because it:
* lets us to easily turn the README contents into a spreadsheet which will be available for download with each archived release of the repository
* helps everyone to keep the repo contents as clear to read and easy to contribute to as possible
* means that potential contributors can easily look for missing content (e.g. any 'tbc' links)

## 🎣 making a pull request
To manage changes to the project's content we use [github's standard workflow](https://guides.github.com/introduction/flow/), which is based on contributors making requests for their changes to be pulled into the main project content (or, a pull request!).

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

## 🙏 attribution
This document is adapted from the contributor guidelines for Open Life Science.
