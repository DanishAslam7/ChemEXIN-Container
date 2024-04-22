# ChemEXIN

An open-source, deep learning integrated, physicochemical parameter-based exon-intron boundary prediction method. It is based on a three-dimensional convolutional neural network (3D- CNN) architecture. Three organism-specific (_Homo sapiens_, _Mus musculus_, and _Caenorhabditis elegans_) models have been built and implemented in the final prediction pipeline. The universality of ChemEXIN lies in its ability to predict exon-intron boundaries across varying lengths of known genes (180 to ~25,00,000 bps) in the organisms under study.

"ChemEXIN:  A Physicochemical Parameter-Based Exon-Intron Boundary Prediction Method"

Authors: Dinesh Sharma, Danish Aslam, Kopal Sharma, Aditya Mittal, and B Jayaram

Note: ChemEXIN is a TensorFlow implementation.

## Installation

### Prerequisites
- **Conda**,  to create an environment for ChemEXIN across Windows, macOS, and Linux operating systems. This environment will include all the required dependencies. 
- Conda is available at https://conda.io/projects/conda/en/latest/user-guide/install/index.html.

### Setup (one-time setup)
### Clone the ChemEXIN project repository:
```bash
 git clone https://github.com/rnsharma478/ChemEXIN.git
 ```
### Go to the project directory:
```bash
 cd ChemEXIN/
```
### Installing the virtual environment:
```bash
conda env create -f ChemEXIN.yml
```
```bash
conda activate ChemEXIN
```
### Usage:
```bash
cd ChemEXIN/
```
```bash
python main.py
```
