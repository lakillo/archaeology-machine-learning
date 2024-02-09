# ✅ contributor guidelines
:tada: thanks so much for considering contributing to this project! :tada:

A quick note before we get started: this project and everyone participating in it is governed by our [code of conduct](CODE_OF_CONDUCT.md). By participating you are expected to uphold this code, so please make yourself familiar with it.

There are many options for participating in this project; whether you're a seasoned github user and are ready to [📝 create an issue](https://github.com/lakillo/archaeology-machine-learning/issues/new) or [🎣 make a pull request](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#-making-a-pull-request), or you're new here and [don't have an account](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#contribute-without-a-github-account). Read on to find out more.

## ⏩ TL;DR: how to contribute
Since this project is about collecting resources, the most simple and helpful contribution you could make is to add one or more examples to the repository's main data file, which is the csv file in the data folder.

To contribute by adding an example to the csv:
1. take note of the [💅 repo style guide](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#-repo-style-guide)
2. fork and clone the repo, and make a new branch (see instructions in [🎣 make a pull request](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#-making-a-pull-request))
3. add your contributions to the csv file (data/archaeology-machine-learning-data.csv)

>> [!IMPORTANT] where should I add things in the csv?
> 
>Don't worry about the order you add things in! Just add your contributions to the next available row of the csv file. 
> 
> We have a github action which automatically sorts the csv after each commit and keeps it neat and tidy 🧹🤖.

3. [🎣 make a pull request](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#-making-a-pull-request)

Simple contributions of this kind are hugely appreciated and make all the difference ✨

## ✅ other ways to contribute

### introduce yourself!
1. post a message on our [👋 community introductions issue](https://github.com/lakillo/archaeology-machine-learning/issues/7)

### fix typos or errors in existing content
1. report a mistake or error in the repository contents by [📝 creating an issue](https://github.com/lakillo/archaeology-machine-learning/issues/new)
2. help us resolve any open issues relating to errors (you may need to [🎣 make a pull request](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#-making-a-pull-request))

### work on an open issue
1. check out the current [🐢 milestones](https://github.com/lakillo/archaeology-machine-learning/milestones) we're working towards
2. click into a milestone to see the open issues
3. help us resolve any open issues (you may need to [🎣 make a pull request](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#-making-a-pull-request))

### help us plan the project vision and roadmap
1. read our project [🗺️ roadmap](https://github.com/lakillo/archaeology-machine-learning/issues/3)
2. in the [🗺️ project vision and roadmap](https://github.com/lakillo/archaeology-machine-learning/milestone/2) milestone, comment on an open issue or [📝 create a new issue](https://github.com/lakillo/archaeology-machine-learning/issues/new) explaining your idea
3. help us resolve any open issues relating to project planning (you may need to [🎣 make a pull request](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#-making-a-pull-request))

### contribute without a github account
1. get in touch via email at l.killoran.1@research.gla.ac.uk

## 💅 repo style guide
This repository's contents is written in [github flavored markdown](https://guides.github.com/features/mastering-markdown/). 

As mentioned on the README, this repository aims to simplify the navigation of machine learning research and is based on a hierarchy of information which goes from the most general way of describing a technique to the most specific:

application area —> task —> model/algorithm

We recognise that this isn't going to cover all the details of every example, but it will provide enough information for the community to learn, explore, and build. When choosing how to add your example, think generally about the **main** aim, task and technique used.

This is what the csv structure looks like:

| task | author(s) | year | application area | data type | method | paper | code | data |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

And here's some specific guidelines for filling it in:

1. **task** = the [machine learning task] for [thing being analysed], e.g.:
	- [image classification] for [hollow roads]
	- [named entity recognition] for [archaeological text]
	- [classification] for [soil geochemistry]
	- [regression] for [stable isotope analysis]

1. **author(s)** = author(s) last name (+ et al if 3 or more authors)

2. **year** = year of publication/creation

3. **application area** = this column is important as it categorises all the data on the README. choose the overall domain of the example from the existing column values, e.g.:
	- chemical analysis
	- natural language processing
	- site prospection/monitoring
	- spatial predictive modelling
	- OR add new areas as needed (see next section)

4. **data type** = the kind of data that the example uses, e.g.:
	- lidar visualisations
	- DEM
	- english language text
	- strontium

5. **method** = the name of the main machine learning model/algorithm used. use acronyms if you can to keep it short, there will be a reference section to explain them, e.g.:
	- R-CNN
	- BERT
	- SVM

1. **paper** = link to paper if published (DOI preferred)

	- if not published, add a relevant link for information about the example
2. **code** = link to the code or model (DOI preferred)

3. **data** = link to the dataset (DOI preferred)

## 🌱 adding a new application area
If the example you're adding doesn't have its domain represented, simply enter a new value for the overall domain of the example in the application area column of the csv.

If you feel like it, you can also choose an emoji to represent the section on the README. Find the emoji mapping section in the file build/update-csv-and-readme.py and add your new area and emoji:

```
> emoji_mapping = {
    'chemical analysis': '⚛️',
    'natural language processing': '📚️',
    'site prospection/monitoring': '🛰️',
    'spatial predictive modelling': '🌏',
    'new area': '📊',
    # insert new areas in the list in alphabetical order
}
```

This file is is our tidy-up-and-README-making script which runs automatically after each change to the csv file 🧹🤖.

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
