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
This project was inspired by the [satellite-image-deep-learning](https://github.com/satellite-image-deep-learning/) and [AncientMetagenomeDir](https://github.com/SPAAM-community/AncientMetagenomeDir) projects, and was kicked off as part of [Open Seeds cohort 8](https://openlifesci.org/openseeds/ols-8/).

## 📁 repository contents
The repository is structured into sections by application area (e.g. remote sensing), and then by machine learning technique, with linked examples illustrating the uses of each technique. Use the contents list below ⬇️ to browse the application areas included so far and jump to specific sections, or scroll down to view everything.

### 🛰️ remote sensing
> 1. [classification](https://github.com/lakillo/archaeology-machine-learning/tree/main#classification)
> 2. [segmentation](https://github.com/lakillo/archaeology-machine-learning/tree/main#segmentation)
<!-- > 3. [technique](link) -->

### 📚️ textual analysis
> 1. [language models](https://github.com/lakillo/archaeology-machine-learning/tree/main#language_models)
> 2. [named entity recognition](https://github.com/lakillo/archaeology-machine-learning/tree/main#named_entity_recognition)
<!-- > 3. [technique](link) -->

---

## 🛰️ remote sensing
### classification
|title | authors | year | data type | technique | paper | code | data |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|<!-- -->Using CarcassonNet to automatically detect and trace hollow roads in LiDAR data from the Netherlands | Verschoof-van der Vaart and Landauer | 2021 | lidar | classification | [paper](https://doi.org/10.1016/j.culher.2020.10.009) | code:tbc | data:tbc<!-- -->|

### segmentation
| title | authors | year | data type | technique | paper | code | data |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|<!-- -->Investigating ancient agricultural field systems in Sweden from airborne LIDAR data by using convolutional neural network | Küçükdemirci et al | 2022 | lidar | segmentation | [paper](https://onlinelibrary.wiley.com/doi/full/10.1002/arp.1886) | code:tbc | data:tbc<!-- -->|


## 📚️ textual analysis
### language models
|title | authors | year | type | technique | language | paper | model | 
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|<!-- -->ArchaeoBERT | Alex Brandsen | 2023 | BERT | Masked Language Modelling | English | [paper](https://doi.org/10.5281/zenodo.8300777) | [model](https://huggingface.co/alexbrandsen/ArchaeoBERT) <!-- -->|
|<!-- -->ArchaeoBERT-NER | Alex Brandsen | 2023 | BERT | Named Entity Recognition | English | [paper](https://doi.org/10.5281/zenodo.8300777) | [model](https://huggingface.co/alexbrandsen/ArchaeoBERT-NER) <!-- -->|
|<!-- -->ArcheoBERTje | Alex Brandsen | 2023 | BERT | Masked Language Modelling | Dutch | [paper](https://doi.org/10.5281/zenodo.8300777) | [model](https://huggingface.co/alexbrandsen/ArcheoBERTje) <!-- -->|
|<!-- -->ArcheoBERTje-NER | Alex Brandsen | 2023 | BERT | Named Entity Recognition | Dutch | [paper](https://doi.org/10.5281/zenodo.8300777) | [model](https://huggingface.co/alexbrandsen/ArcheoBERTje-NER) <!-- -->|
|<!-- -->bert-base-german-cased-archaeo | Alex Brandsen | 2023 | BERT | Masked Language Modelling | German | [paper](https://doi.org/10.5281/zenodo.8300777) | [model](https://huggingface.co/alexbrandsen/bert-base-german-cased-archaeo) <!-- -->|
|<!-- -->bert-base-german-cased-archaeo-NER | Alex Brandsen | 2023 | BERT | Named Entity Recognition | German | [paper](https://doi.org/10.5281/zenodo.8300777) | [model](https://huggingface.co/alexbrandsen/bert-base-german-cased-archaeo-NER) <!-- -->|

### named entity recognition
|title | authors | year | type | format | language | paper | data | 
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|<!-- -->Creating a Dataset for Named Entity Recognition in the Archaeology Domain | Brandsen et al. | 2020 | data | CoNNL | Dutch | [paper](https://aclanthology.org/2020.lrec-1.562) | [data](https://doi.org/10.5281/zenodo.3544544)<!-- -->|
