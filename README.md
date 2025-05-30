[![license: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13220872.svg)](https://doi.org/10.5281/zenodo.13220872)
<!-- ![GitHub issues](https://img.shields.io/github/issues/lakillo/archaeology-machine-learning) -->
<!-- [![visits](https://hits.sh/github.com/lakillo/archaeology-machine-learning.svg?label=visits&color=11cc9a)](https://hits.sh/github.com/lakillo/archaeology-machine-learning/) -->

# 👋 welcome to the archaeology machine learning repository

## 📖 introduction to the project
Machine learning (ML) methods present new ways of approaching archaeological research questions and interest in applying these methods continues to grow. 

This repository collects resources relating to the application of ML methods to archaeological data, aiming to:

* provide an overview of the ways ML is being applied in archaeology
* spark new ideas whilst reducing duplication of work
* encourage the sharing of code, data, and other resources
* make resources more **[FAIR](https://www.nature.com/articles/sdata201618) (Findable, Accessible, Interoperable, and Reuseable)**

By doing this, we hope to support practitioners to **learn about, critically apply, or contribute to conversations about, ML in archaeology**.

## ✅ how to contribute
Check out our **[🗺️ roadmap](https://github.com/lakillo/archaeology-machine-learning/issues/3)** for an overview of what we're working on, or go straight to the **[✅ contributor guidelines](https://github.com/lakillo/archaeology-machine-learning/blob/main/CONTRIBUTING.md)**.

## 🔗 citeable releases
Please cite the project if you've found it useful. Releases are made at regular intervals and **[archived on Zenodo](https://zenodo.org/records/13220872)**.

# ⚙️ resources

> 1. ML case studies (split by application area)
>    - [🏺 artefact analysis](#-artefact-analysis)
>    - [🌱 ecofact analysis](#-ecofact-analysis)
>    - [📚️ natural language processing](#%EF%B8%8F-natural-language-processing)
>    - [🛰️ remote sensing feature detection](#%EF%B8%8F-remote-sensing-feature-detection)
>    - [🌏 spatial predictive modelling](#-spatial-predictive-modelling)
> 2. [📊 datasets](#-datasets)
> 3. [📖 glossary of technique names](#-glossary)

---

<!-- START -->

## 🏺 artefact analysis

| task                                          | authors             |   year | data type                                                | technique                                         | paper                                                 | code                                                                                     | data                                                                                     |
|:----------------------------------------------|:--------------------|-------:|:---------------------------------------------------------|:--------------------------------------------------|:------------------------------------------------------|:-----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| segmentation for carved reliefs               | Ji et al.           |   2023 | RGB images [digital photos], depth map, soft-edge images | CNN [DenseNet121]                                 | [paper](https://doi.org/10.3390/rs15040956)           | nan                                                                                      | nan                                                                                      |
| classification for ceramic elemental analysis | Ruschioni et al.    |   2023 | x-ray fluorescence                                       | LR, LDA, MLP, SVM, DT, RF, NB, KNN                | [paper](https://doi.org/10.1016/j.jasrep.2023.103995) | [code](https://github.com/dariomalchiodi/JAS-Tarquinia-classification)                   | [data](https://github.com/dariomalchiodi/JAS-Tarquinia-classification)                   |
| classification for ceramic sherds             | Helden et al.       |   2022 | RGB images [smartphone photos], synthetic data           | CNN [VGG19, Mobilenetv2, ResNet50v2, Inceptionv3] | [paper](https://doi.org/10.5334/jcaa.92)              | [models](https://github.com/ArchiScn)                                                    | [data](https://github.com/ArchiScn)                                                      |
| classification for multiple artefact types    | Resler et al.       |   2021 | RGB images [digital camera photos]                       | CNN [EfficientNetB3], KNN                         | [paper](https://doi.org/10.1057/s41599-021-00970-z)   | nan                                                                                      | [data](http://www.antiquities.org.il/t/default_en.aspx)                                  |
| classification for ceramic petrography        | Lyons               |   2021 | RGB images [microscope photos]                           | CNN [VGG19, ResNet50]                             | [paper](https://doi.org/10.5334/jcaa.75)              | nan                                                                                      | nan                                                                                      |
| object detection for rock carvings            | Tsigkas et al.      |   2020 | RGB images [digital camera photos]                       | CNN [YOLOv2, TinyYOLOv2]                          | [paper](https://doi.org/10.1016/j.patrec.2020.03.026) | nan                                                                                      | nan                                                                                      |
| classification for lithics                    | Grove and Blinkhorn |   2020 | lithic types, period                                     | NN                                                | [paper](https://doi.org/10.1371/journal.pone.0237528) | [code](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0237528#sec026) | [data](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0237528#sec026) |
| classification for ceramic elemental analysis | Charalambous et al. |   2016 | x-ray fluorescence                                       | KNN, DT, LVQ                                      | [paper](https://doi.org/10.1016/j.jasrep.2015.08.010) | nan                                                                                      | nan                                                                                      |

## 🌱 ecofact analysis

| task                                     | authors               |   year | data type                                 | technique               | paper                                                   | code                                                                            | data                                                      |
|:-----------------------------------------|:----------------------|-------:|:------------------------------------------|:------------------------|:--------------------------------------------------------|:--------------------------------------------------------------------------------|:----------------------------------------------------------|
| classification for multi-cell phytoliths | Berganzo-Besga et al. |   2022 | RGB images [microscope photos]            | CNN [VGG19, ResNet50v2] | [paper](https://doi.org/10.1016/j.jas.2022.105654)      | [code](https://ars.els-cdn.com/content/image/1-s2.0-S0305440322001121-mmc1.zip) | nan                                                       |
| classification for contexts              | Vos et al.            |   2021 | geochemistry, phytolith type and quantity | DT                      | [paper](https://doi.org/10.1371/journal.pone.0248261)   | nan                                                                             | [data](https://doi.org/10.1371/journal.pone.0248261.s001) |
| classification for starch granules       | Arráiz et al.         |   2016 | morphometric and optical measurements     | RF                      | [paper](http://dx.doi.org/10.1016/j.jasrep.2016.03.039) | nan                                                                             | nan                                                       |

## 📚️ natural language processing

| task                                                     | authors       |   year | data type                             | technique          | paper                                                 | code                                                                            | data                                                                                     |
|:---------------------------------------------------------|:--------------|-------:|:--------------------------------------|:-------------------|:------------------------------------------------------|:--------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| masked language modelling for archaeological text        | Brandsen      |   2023 | english language                      | BERT               | [paper](https://doi.org/10.5281/zenodo.8300777)       | [model](https://huggingface.co/alexbrandsen/ArchaeoBERT)                        | nan                                                                                      |
| named entity recognition for archaeological text         | Brandsen      |   2023 | english language                      | BERT               | [paper](https://doi.org/10.5281/zenodo.8300777)       | [model](https://huggingface.co/alexbrandsen/ArchaeoBERT-NER)                    | nan                                                                                      |
| masked language modelling for archaeological text        | Brandsen      |   2023 | dutch language                        | BERT               | [paper](https://doi.org/10.5281/zenodo.8300777)       | [model](https://huggingface.co/alexbrandsen/ArcheoBERTje)                       | nan                                                                                      |
| named entity recognition for archaeological text         | Brandsen      |   2023 | dutch language                        | BERT               | [paper](https://doi.org/10.5281/zenodo.8300777)       | [model](https://huggingface.co/alexbrandsen/ArcheoBERTje-NER)                   | [data](https://doi.org/10.5281/zenodo.3544544)                                           |
| masked language modelling for archaeological text        | Brandsen      |   2023 | german language                       | BERT               | [paper](https://doi.org/10.5281/zenodo.8300777)       | [model](https://huggingface.co/alexbrandsen/bert-base-german-cased-archaeo)     | nan                                                                                      |
| named entity recognition for archaeological text         | Brandsen      |   2023 | german language                       | BERT               | [paper](https://doi.org/10.5281/zenodo.8300777)       | [model](https://huggingface.co/alexbrandsen/bert-base-german-cased-archaeo-NER) | nan                                                                                      |
| restoration/attribution for ancient Greek inscriptions   | Assael et al. |   2022 | transcribed inscriptions, place, time | transformer        | [paper](https://doi.org/10.1038/s41586-022-04448-z)   | [code](https://github.com/google-deepmind/ithaca)                               | [data](https://github.com/sommerschield/iphi)                                            |
| transliteration and segmentation of cuneiform characters | Gordin et al. |   2020 | encoded Unicode cuneiform             | bidirectional LSTM | [paper](https://doi.org/10.1371/journal.pone.0240511) | [code](https://github.com/gaigutherz/Akkademia)                                 | [data](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0240511#sec013) |

## 🛰️ remote sensing feature detection

| task                                       | authors                              |   year | data type                                                      | technique                                                | paper                                                              | code                                                  | data       |
|:-------------------------------------------|:-------------------------------------|-------:|:---------------------------------------------------------------|:---------------------------------------------------------|:-------------------------------------------------------------------|:------------------------------------------------------|:-----------|
| semantic segmentation of buildings, platforms and aguadas | Kokalj et al.  |   2023 | multimodal data [lidar visualisations, Canopy Height Model, Sentinel-1, Sentinel-2]  | CNN  | [paper](https://doi.org/10.1038/s41597-023-02455-x)                           | nan                                                   | [figshare](10.6084/m9.figshare.22202395.v1)         |
| transfer learning between geographic areas | Sech et al.                          |   2023 | lidar visualisations [e2MSTP]                                  | CNN [U-Net, DeepLabv3+, ResNet, EfficientNet, SegFormer] | [paper](10.1109/IGARSS52108.2023.10282694)                         | nan                                                   | nan        |
| segmentation for mounds on maps            | Berganzo-Besga et al.                |   2023 | RGB images [historical maps], synthetic data                   | CNN [Mask R-CNN]                                         | [paper](https://doi.org/10.1038/s41598-023-38190-x)                | nan                                                   | on request |
| segmentation for field systems             | Küçükdemirci et al.                  |   2022 | lidar DTMs                                                     | CNN [U-Net]                                              | [paper](https://onlinelibrary.wiley.com/doi/full/10.1002/arp.1886) | nan                                                   | nan        |
| classification for hollow roads            | Verschoof-van der Vaart and Landauer |   2021 | lidar visualisations [local relief model, openness], lidar DTM | CNN [ResNet34]                                           | [paper](https://doi.org/10.1016/j.culher.2020.10.009)              | nan                                                   | nan        |
| classification of buildings, platforms and aguadas  | Somrak and Kokalj  |   2020 | lidar visualisations [visualization for archaeological topography (VAT), VAT Flat, local dominance, red relief image map, VAT-channels; VAT-HS]  | CNN [VGG-19]  | [paper](https://doi.org/10.3390/rs12142215)  | nan   | nan        |
| classification for land use                | Mboga et al.                         |   2020 | panchromatic images [historical aerial photographs]            | CNN [FCN-ATR-SKIP, U-Net]                                | [paper](https://doi.org/10.1016/j.isprsjprs.2020.07.005)           | nan                                                   | nan        |
| classification for war landforms           | de Matos-Machado et al.              |   2019 | morphometric measurements                                      | SOM, HAC                                                 | [paper](https://doi.org/10.1002/esp.4586)                          | nan                                                   | nan        |
| object detection for mining pits           | Gallwey et al.                       |   2019 | lidar DSM                                                      | U-Net                                                    | [paper](https://doi.org/10.3390/rs11171994)                        | [model](https://www.mdpi.com/2072-4292/11/17/1994/s1) | nan        |
| object detection for multiple classes      | Verschoof-van der Vaart and Lambers  |   2019 | lidar visualisations [simple local relief model]               | CNN [Faster R-CNN]                                       | [paper](https://doi.org/10.5334/jcaa.32)                           | nan                                                   | nan        |

## 🌏 spatial predictive modelling

| task                                   | authors              |   year | data type                                                              | technique    | paper                                                 | code                                                      | data                                                      |
|:---------------------------------------|:---------------------|-------:|:-----------------------------------------------------------------------|:-------------|:------------------------------------------------------|:----------------------------------------------------------|:----------------------------------------------------------|
| regression for neolithic sites         | Li et al.            | 2023.3 | topography, hydrology                                                  | RF           | [paper](https://doi.org/10.1515/geo-2022-0467)        | nan                                                       | nan                                                       |
| regression for neolithic sites         | Li et al.            | 2023   | topography, hydrology                                                  | RF           | [paper](https://doi.org/10.1515/geo-2022-0467)        | nan                                                       | nan                                                       |
| classification for site dating         | Reese                | 2021   | ceramic types, dendochronology dates                                   | NN           | [paper](https://doi.org/10.1016/j.jas.2021.105413)    | [code](https://github.com/kmreese-io/Reese_2021-JAS)      | [data]()                                                  |
| regression for roman sites             | Castiello and Tonini | 2021   | soil, topography                                                       | RF           | [paper](https://doi.org/10.5334/jcaa.71)              | nan                                                       | nan                                                       |
| regression for formative period sites  | Yaworsky et al.      | 2020   | environmental, topography                                              | MaxEnt, RF   | [paper](https://doi.org/10.1371/journal.pone.0239424) | [code](https://doi.org/10.1371/journal.pone.0239424.s001) | [data](https://doi.org/10.1371/journal.pone.0239424.s002) |
| regression for strontium isoscapes     | Bataille et al.      | 2020   | strontium, coordinates, geology, climate, environmental, anthropogenic | RF           | [paper](https://doi.org/10.1016/j.palaeo.2020.109849) | [code](https://doi.org/10.1016/j.palaeo.2020.109849)      | [data](https://doi.org/10.1016/j.palaeo.2020.109849)      |
| regression for strontium isoscapes     | Funck et al.         | 2020   | strontium, coordinates, geology, climate, environmental                | RF           | [paper](https://doi.org/10.1002/jqs.3262)             | nan                                                       | [data](https://doi.org/10.1002/jqs.3262)                  |
| classification for habitat suitability | Jones et al.         | 2019   | climate, topography                                                    | RF           | [paper](https://doi.org/10.1111/jbi.13684)            | nan                                                       | nan                                                       |
| regression for strontium isoscapes     | Bataille et al.      | 2018   | strontium, geology, climate, environmental, topographic                | RF           | [paper](https://doi.org/10.1371/journal.pone.0197386) | [code](https://doi.org/10.1371/journal.pone.0197386.s001) | nan                                                       |
| classification for soil geochemistry   | Oonk and Spijker     | 2015   | soil geochemistry                                                      | KNN, SVM, NN | [paper](https://doi.org/10.1016/j.jas.2015.04.002)    | nan                                                       | nan                                                       |

## 📊 datasets

| task                                 | authors         |   year | data type                                                                    | technique                                                   | paper                                               |   code | data                                                 |
|:-------------------------------------|:----------------|-------:|:-----------------------------------------------------------------------------|:------------------------------------------------------------|:----------------------------------------------------|-------:|:-----------------------------------------------------|
| proposed null dataset for lithics    | Eren et al.     |   2023 | tbc, qual and quant info from naturally fractured rocks                      | nan                                                         | [paper](https://doi.org/10.15184/aqy.2023.4)        |    nan | nan                                                  |
| dataset for named entity recognition | Brandsen et al. |   2020 | dutch language                                                               | named entity recognition                                    | [paper](https://aclanthology.org/2020.lrec-1.562)   |    nan | [data](https://doi.org/10.5281/zenodo.3544544)       |
| dataset for maya site detection      | Kokalj et al.   |   2023 | lidar visualisations [multiple], lidar canopy height, SAR, optical satellite | object recognition, object detection, semantic segmentation | [paper](https://doi.org/10.1038/s41597-023-02455-x) |    nan | [data](https://doi.org/10.6084/m9.figshare.22202395) |

<!-- END -->

# 📖 glossary

| acronym | technique                             |
|---------|---------------------------------------|
| BERT    | bidirectional encoder representations from transformers |
| CNN     | convolutional neural network          |
| DT      | decision tree                         |
| HAC     | hierarchical agglomerative clustering |
| KNN     | k-nearest neighbours                  |
| LDA     | linear discriminant analysis          |
| LR      | logistic regression                   |
| LSTM    | long short-term memory network        |
| LVQ     | learning vector quantisation          |
| MaxEnt  | maximum entropy                       |
| MLP     | multi-layer perceptron                |
| NB      | naive bayes                           |
| NN      | neural network                        |
| RF      | random forest                         |
| SOM     | self-organizing map                   |
| SVM     | support vector machine                |
