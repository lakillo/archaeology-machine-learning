[![license: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![GitHub issues](https://img.shields.io/github/issues/lakillo/archaeology-machine-learning)
<!-- [![visits](https://hits.sh/github.com/lakillo/archaeology-machine-learning.svg?label=visits&color=11cc9a)](https://hits.sh/github.com/lakillo/archaeology-machine-learning/) -->

# 👋 welcome to the archaeology machine learning repository

## 📖 introduction to the project
Machine learning (ML) techniques present new ways of approaching archaeological research questions and interest in applying these methods continues to grow. 
This repository documents the application of ML techniques to archaeological data, aiming to assist those working in the field by:

* providing an overview of the ways ML is being applied in archaeology
* sparking new ideas whilst reducing duplication of work
* encouraging the sharing of code, data, and other resources
* making resources more [FAIR](https://www.nature.com/articles/sdata201618) (Findable, Accessible, Interoperable, and Reuseable)

By doing this, we hope to support practitioners to **learn about, critically apply, or contribute to conversations about, machine learning techniques for archaeology**.

## ✅ how to contribute
This project is open for contributions! 

Check out our [🗺️ roadmap](https://github.com/lakillo/archaeology-machine-learning/issues/3) to get an overview of the current milestones we're working towards and find out how to participate.

## 🗞️ releases
Archived releases of this repository with a citeable DOI will be made at regular intervals.

## 🙏 acknowledgements
This project was kicked off as part of [Open Seeds cohort 8](https://openlifesci.org/openseeds/ols-8/), and was inspired by these great projects: [satellite-image-deep-learning](https://github.com/satellite-image-deep-learning/), [Rchaeology](https://rchaeology.github.io/about/), [open-phytoliths](https://github.com/open-phytoliths), [AncientMetagenomeDir](https://github.com/SPAAM-community/AncientMetagenomeDir), and [open-archaeo](https://github.com/zackbatist/open-archaeo).

## 📁 repository contents
Machine learning techniques can be described and categorised in a number of different ways, which can make the field confusing to navigate. The data structure of this repository aims to simplify things. It's based on a hierarchy of information which goes from the most general way of describing a technique to the most specific, e.g.:

> **application area** —> **task** —> **model/algorithm**

For contributors, guidance on how to use this hierarchy to structure your contributions can be found in the [💅 repo style guide](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md#-repo-style-guide).

# ⚙️ machine learning techniques for archaeology
<!-- START DATA -->

## ⚛️ chemical analysis

| task                                   | authors            |   year | data type       | technique      | paper                                                 | code                                                                            | data                                                                             |
|:---------------------------------------|:-------------------|-------:|:----------------|:---------------|:------------------------------------------------------|:--------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| regression for stable isotope analysis | Bataille et al     |   2020 | strontium       | RF             | [paper](https://doi.org/10.1016/j.palaeo.2020.109849) | [code](https://ars.els-cdn.com/content/image/1-s2.0-S0031018220302947-mmc4.zip) | [data](https://ars.els-cdn.com/content/image/1-s2.0-S0031018220302947-mmc1.xlsx) |
| regression for stable isotope analysis | Funck et al        |   2020 | strontium       | RF             | [paper](https://doi.org/10.1002/jqs.3262)             | nan                                                                             | [data](https://onlinelibrary.wiley.com/doi/10.1002/jqs.3262)                     |
| regression for stable isotope analysis | Bataille et al     |   2018 | strontium       | RF             | [paper](https://doi.org/10.1371/journal.pone.0197386) | [code](https://doi.org/10.1371/journal.pone.0197386.s001)                       | nan                                                                              |
| classification for elemental analysis  | Charalambous et al |   2016 | ceramics ED-XRF | kNN, C4.5, LVQ | [paper](https://doi.org/10.1016/j.jasrep.2015.08.010) | nan                                                                             | nan                                                                              |

## 📚️ natural language processing

| task                                              | authors        |   year | data type        | technique                          | paper                                             | code                                                                            | data                                           |
|:--------------------------------------------------|:---------------|-------:|:-----------------|:-----------------------------------|:--------------------------------------------------|:--------------------------------------------------------------------------------|:-----------------------------------------------|
| masked language modelling for archaeological text | Brandsen       |   2023 | english language | ArchaeoBERT                        | [paper](https://doi.org/10.5281/zenodo.8300777)   | [model](https://huggingface.co/alexbrandsen/ArchaeoBERT)                        | nan                                            |
| named entity recognition for archaeological text  | Brandsen       |   2023 | english language | ArchaeoBERT-NER                    | [paper](https://doi.org/10.5281/zenodo.8300777)   | [model](https://huggingface.co/alexbrandsen/ArchaeoBERT-NER)                    | nan                                            |
| masked language modelling for archaeological text | Brandsen       |   2023 | dutch language   | ArcheoBERTje                       | [paper](https://doi.org/10.5281/zenodo.8300777)   | [model](https://huggingface.co/alexbrandsen/ArcheoBERTje)                       | nan                                            |
| named entity recognition for archaeological text  | Brandsen       |   2023 | dutch language   | ArcheoBERTje-NER                   | [paper](https://doi.org/10.5281/zenodo.8300777)   | [model](https://huggingface.co/alexbrandsen/ArcheoBERTje-NER)                   | [data](https://doi.org/10.5281/zenodo.3544544) |
| masked language modelling for archaeological text | Brandsen       |   2023 | german language  | bert-base-german-cased-archaeo     | [paper](https://doi.org/10.5281/zenodo.8300777)   | [model](https://huggingface.co/alexbrandsen/bert-base-german-cased-archaeo)     | nan                                            |
| named entity recognition for archaeological text  | Brandsen       |   2023 | german language  | bert-base-german-cased-archaeo-NER | [paper](https://doi.org/10.5281/zenodo.8300777)   | [model](https://huggingface.co/alexbrandsen/bert-base-german-cased-archaeo-NER) | nan                                            |
| dataset for named entity recognition              | Brandsen et al |   2020 | dutch language   | CoNNL                              | [paper](https://aclanthology.org/2020.lrec-1.562) | nan                                                                             | [data](https://doi.org/10.5281/zenodo.3544544) |

## 🛰️ site detection

| task                                  | authors                              |   year | data type                                                        | technique                                                   | paper                                                              | code                                                  | data                                                 |
|:--------------------------------------|:-------------------------------------|-------:|:-----------------------------------------------------------------|:------------------------------------------------------------|:-------------------------------------------------------------------|:------------------------------------------------------|:-----------------------------------------------------|
| dataset for maya archaeology          | Kokalj et al                         |   2023 | lidar visualisation, lidar canopy height, SAR, optical satellite | object recognition, object detection, semantic segmentation | [paper](https://doi.org/10.1038/s41597-023-02455-x)                | nan                                                   | [data](https://doi.org/10.6084/m9.figshare.22202395) |
| segmentation for field systems        | Küçükdemirci et al                   |   2022 | lidar DTMs                                                       | U-Net                                                       | [paper](https://onlinelibrary.wiley.com/doi/full/10.1002/arp.1886) | nan                                                   | nan                                                  |
| image classification for hollow roads | Verschoof-van der Vaart and Landauer |   2021 | lidar visualisation                                              | Resnet-34 CNN                                               | [paper](https://doi.org/10.1016/j.culher.2020.10.009)              | nan                                                   | nan                                                  |
| object detection for mining pits      | Gallwey et al                        |   2019 | lidar DSM                                                        | U-Net                                                       | [paper](https://doi.org/10.3390/rs11171994)                        | [model](https://www.mdpi.com/2072-4292/11/17/1994/s1) | nan                                                  |
| object detection for multiple classes | Verschoof-van der Vaart and Lambers  |   2019 | lidar visualisation                                              | Faster R-CNN                                                | [paper](https://doi.org/10.5334/jcaa.32)                           | nan                                                   | nan                                                  |

## 🌏 spatial predictive modelling

| task                                   | authors              |   year | data type                 | technique    | paper                                                 | code                                                      | data                                                      |
|:---------------------------------------|:---------------------|-------:|:--------------------------|:-------------|:------------------------------------------------------|:----------------------------------------------------------|:----------------------------------------------------------|
| regression for roman sites             | Castiello and Tonini |   2021 | soil, topography          | RF           | [paper](https://doi.org/10.5334/jcaa.71)              | nan                                                       | nan                                                       |
| regression for formative period sites  | Yaworsky et al       |   2020 | environmental, topography | MaxEnt, RF   | [paper](https://doi.org/10.1371/journal.pone.0239424) | [code](https://doi.org/10.1371/journal.pone.0239424.s001) | [data](https://doi.org/10.1371/journal.pone.0239424.s002) |
| classification for habitat suitability | Jones et al          |   2019 | climate, topography       | RF           | [paper](https://doi.org/10.1111/jbi.13684)            | nan                                                       | nan                                                       |
| classification for soil geochemistry   | Oonk and Spijker     |   2015 | soil geochemistry         | kNN, SVM, NN | [paper](https://doi.org/10.1016/j.jas.2015.04.002)    | nan                                                       | nan                                                       |

<!-- END DATA -->

---
