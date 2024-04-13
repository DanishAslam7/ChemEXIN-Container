# General Information
**ChemEXIN** is a Physicochemical Parameter-Based Exon-Intron Boundary Prediction Method. It is based on 3D- CNN (Three-dimensional Convolutional Neural Network) architecture. Three organism-specific models have been built and implemented for the final prediction pipeline. The universality of ChemEXIN lies in its ability to predict exon-intron boundaries across varying length of known genes (~180 to ~25,00,000 bps) in the organisms under study (_Homo sapiens_, _Mus musculus_, and _Caenorhabditis elegans_). Models were trained with 80% of the data and then tested on the remaining 20% of the data.

# Installation:

## Create the project:
> git clone https://github.com/rnsharma478/ChemEXIN.git

## Go to the project directory:
> cd ChemEXIN

## Installing the virtual environment:
> conda env create -f ChemEXIN.yml

> conda activate ChemEXIN

## Usage:

> cd ChemEXIN

> python main.py
