[![license: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![GitHub issues](https://img.shields.io/github/issues/lakillo/archaeology-machine-learning)
<!-- [![visits](https://hits.sh/github.com/lakillo/archaeology-machine-learning.svg?label=visits&color=11cc9a)](https://hits.sh/github.com/lakillo/archaeology-machine-learning/) -->

# 👋 welcome to the archaeology machine learning repository

## 📖 introduction to the project
Machine learning (ML) methods present new ways of approaching archaeological research questions and interest in applying these methods continues to grow. 

This repository collects resources relating to the application of ML methods to archaeological data, aiming to:

* provide an overview of the ways ML is being applied in archaeology
* spark new ideas whilst reducing duplication of work
* encourage the sharing of code, data, and other resources
* make resources more [FAIR](https://www.nature.com/articles/sdata201618) (Findable, Accessible, Interoperable, and Reuseable)

By doing this, we hope to support practitioners to **learn about, critically apply, or contribute to conversations about, ML in archaeology**.

## ✅ how to contribute
Check out our **[🗺️ roadmap](https://github.com/lakillo/archaeology-machine-learning/issues/3)** for an overview of what we're working on, or go straight to the **[✅ contributor guidelines](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md)**.

## 🗞️ releases
Archived releases of this repository with a citeable DOI will be made at regular intervals.

# ⚙️ resources

> 1. ML case studies (split by application area)
>    - [⚛️ chemical analysis](https://github.com/lakillo/archaeology-machine-learning?tab=readme-ov-file#%EF%B8%8F-chemical-analysis)
>    - [🪨 lithic analysis](https://github.com/lakillo/archaeology-machine-learning?tab=readme-ov-file#-lithic-analysis)
>    - [📚️ natural language processing](https://github.com/lakillo/archaeology-machine-learning?tab=readme-ov-file#%EF%B8%8F-natural-language-processing)
>    - [🛰️ site detection](https://github.com/lakillo/archaeology-machine-learning?tab=readme-ov-file#%EF%B8%8F-site-detection)
>    - [🌏 spatial predictive modelling](https://github.com/lakillo/archaeology-machine-learning?tab=readme-ov-file#-spatial-predictive-modelling)
> 2. [📊 datasets](https://github.com/lakillo/archaeology-machine-learning?tab=readme-ov-file#-datasets)
> 3. [📖 glossary of technique names](https://github.com/lakillo/archaeology-machine-learning?tab=readme-ov-file#-glossary)

---

<!-- START -->

## ⚛️ chemical analysis

| task                                              | authors            |   year | data type          | technique                          | paper                                                 | code                                                                            | data                                                                             |
|:--------------------------------------------------|:-------------------|-------:|:-------------------|:-----------------------------------|:------------------------------------------------------|:--------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| classification for elemental analysis of ceramics | Ruschioni et al    |   2023 | x-ray fluorescence | LR, LDA, MLP, SVM, DT, RF, NB, KNN | [paper](https://doi.org/10.1016/j.jasrep.2023.103995) | [code](https://github.com/dariomalchiodi/JAS-Tarquinia-classification)          | [data](https://github.com/dariomalchiodi/JAS-Tarquinia-classification)           |
| regression for stable isotope analysis            | Bataille et al     |   2020 | strontium          | RF                                 | [paper](https://doi.org/10.1016/j.palaeo.2020.109849) | [code](https://ars.els-cdn.com/content/image/1-s2.0-S0031018220302947-mmc4.zip) | [data](https://ars.els-cdn.com/content/image/1-s2.0-S0031018220302947-mmc1.xlsx) |
| regression for stable isotope analysis            | Funck et al        |   2020 | strontium          | RF                                 | [paper](https://doi.org/10.1002/jqs.3262)             | nan                                                                             | [data](https://onlinelibrary.wiley.com/doi/10.1002/jqs.3262)                     |
| regression for stable isotope analysis            | Bataille et al     |   2018 | strontium          | RF                                 | [paper](https://doi.org/10.1371/journal.pone.0197386) | [code](https://doi.org/10.1371/journal.pone.0197386.s001)                       | nan                                                                              |
| classification for elemental analysis (ceramics)  | Charalambous et al |   2016 | x-ray fluorescence | KNN, DT, LVQ                       | [paper](https://doi.org/10.1016/j.jasrep.2015.08.010) | nan                                                                             | nan                                                                              |

## 🪨 lithic analysis

| task                       | authors             |   year | data type                  | technique   | paper                                                 | code                                                                                     | data                                                                                     |
|:---------------------------|:--------------------|-------:|:---------------------------|:------------|:------------------------------------------------------|:-----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| classification for lithics | Grove and Blinkhorn |   2020 | tabular (presence/absence) | NN          | [paper](https://doi.org/10.1371/journal.pone.0237528) | [code](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0237528#sec026) | [data](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0237528#sec026) |

## 📚️ natural language processing

| task                                              | authors   |   year | data type        | technique   | paper                                           | code                                                                            | data                                           |
|:--------------------------------------------------|:----------|-------:|:-----------------|:------------|:------------------------------------------------|:--------------------------------------------------------------------------------|:-----------------------------------------------|
| masked language modelling for archaeological text | Brandsen  |   2023 | english language | BERT        | [paper](https://doi.org/10.5281/zenodo.8300777) | [model](https://huggingface.co/alexbrandsen/ArchaeoBERT)                        | nan                                            |
| named entity recognition for archaeological text  | Brandsen  |   2023 | english language | BERT        | [paper](https://doi.org/10.5281/zenodo.8300777) | [model](https://huggingface.co/alexbrandsen/ArchaeoBERT-NER)                    | nan                                            |
| masked language modelling for archaeological text | Brandsen  |   2023 | dutch language   | BERT        | [paper](https://doi.org/10.5281/zenodo.8300777) | [model](https://huggingface.co/alexbrandsen/ArcheoBERTje)                       | nan                                            |
| named entity recognition for archaeological text  | Brandsen  |   2023 | dutch language   | BERT        | [paper](https://doi.org/10.5281/zenodo.8300777) | [model](https://huggingface.co/alexbrandsen/ArcheoBERTje-NER)                   | [data](https://doi.org/10.5281/zenodo.3544544) |
| masked language modelling for archaeological text | Brandsen  |   2023 | german language  | BERT        | [paper](https://doi.org/10.5281/zenodo.8300777) | [model](https://huggingface.co/alexbrandsen/bert-base-german-cased-archaeo)     | nan                                            |
| named entity recognition for archaeological text  | Brandsen  |   2023 | german language  | BERT        | [paper](https://doi.org/10.5281/zenodo.8300777) | [model](https://huggingface.co/alexbrandsen/bert-base-german-cased-archaeo-NER) | nan                                            |

## 🛰️ site detection

| task                                  | authors                              |   year | data type            | technique    | paper                                                              | code                                                  |   data |
|:--------------------------------------|:-------------------------------------|-------:|:---------------------|:-------------|:-------------------------------------------------------------------|:------------------------------------------------------|-------:|
| segmentation for field systems        | Küçükdemirci et al                   |   2022 | lidar DTMs           | U-Net        | [paper](https://onlinelibrary.wiley.com/doi/full/10.1002/arp.1886) | nan                                                   |    nan |
| image classification for hollow roads | Verschoof-van der Vaart and Landauer |   2021 | lidar visualisations | Resnet-34    | [paper](https://doi.org/10.1016/j.culher.2020.10.009)              | nan                                                   |    nan |
| object detection for mining pits      | Gallwey et al                        |   2019 | lidar DSM            | U-Net        | [paper](https://doi.org/10.3390/rs11171994)                        | [model](https://www.mdpi.com/2072-4292/11/17/1994/s1) |    nan |
| object detection for multiple classes | Verschoof-van der Vaart and Lambers  |   2019 | lidar visualisations | Faster R-CNN | [paper](https://doi.org/10.5334/jcaa.32)                           | nan                                                   |    nan |

## 🌏 spatial predictive modelling

| task                                   | authors              |   year | data type                 | technique    | paper                                                 | code                                                      | data                                                      |
|:---------------------------------------|:---------------------|-------:|:--------------------------|:-------------|:------------------------------------------------------|:----------------------------------------------------------|:----------------------------------------------------------|
| regression for roman sites             | Castiello and Tonini |   2021 | soil, topography          | RF           | [paper](https://doi.org/10.5334/jcaa.71)              | nan                                                       | nan                                                       |
| regression for formative period sites  | Yaworsky et al       |   2020 | environmental, topography | MaxEnt, RF   | [paper](https://doi.org/10.1371/journal.pone.0239424) | [code](https://doi.org/10.1371/journal.pone.0239424.s001) | [data](https://doi.org/10.1371/journal.pone.0239424.s002) |
| classification for habitat suitability | Jones et al          |   2019 | climate, topography       | RF           | [paper](https://doi.org/10.1111/jbi.13684)            | nan                                                       | nan                                                       |
| classification for soil geochemistry   | Oonk and Spijker     |   2015 | soil geochemistry         | KNN, SVM, NN | [paper](https://doi.org/10.1016/j.jas.2015.04.002)    | nan                                                       | nan                                                       |

## 📊 datasets

| task                                 | authors        |   year | data type                                                         | technique                                                   | paper                                               | code     | data                                                 |
|:-------------------------------------|:---------------|-------:|:------------------------------------------------------------------|:------------------------------------------------------------|:----------------------------------------------------|:---------|:-----------------------------------------------------|
| proposed null dataset for lithics    | Eren et al     |   2023 | tbc, qual and quant info from naturally fractured rocks           | nan                                                         | [paper](https://doi.org/10.15184/aqy.2023.4)        | [code]() | [data]()                                             |
| dataset for named entity recognition | Brandsen et al |   2020 | dutch language                                                    | named entity recognition                                    | [paper](https://aclanthology.org/2020.lrec-1.562)   | nan      | [data](https://doi.org/10.5281/zenodo.3544544)       |
| dataset for maya site detection      | Kokalj et al   |   2023 | lidar visualisations, lidar canopy height, SAR, optical satellite | object recognition, object detection, semantic segmentation | [paper](https://doi.org/10.1038/s41597-023-02455-x) | nan      | [data](https://doi.org/10.6084/m9.figshare.22202395) |

<!-- END -->

# 📖 glossary

| acronym | technique                     |
|---------|-------------------------------|
| BERT    | bidirectional encoder representations from transformers |
| DT      | decision tree                 |
| Faster R-CNN | a type of convolutional neural network |
| KNN     | k-nearest neighbours          |
| LDA     |  linear discriminant analysis |
| LR      | logistic regression           |
| LVQ     | learning vector quantisation  |
| MaxEnt  | maximum entropy               |
| MLP     | multi-layer perceptron        |
| NB      | naive bayes                   |
| NN      | neural network                |
| Resnet  | a type of convolutional neural network |
| RF      | random forest                 |
| SVM     | support vector machine        |
| U-Net   | a type of convolutional neural network |