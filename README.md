# ChemEXIN-Container

Dockerized deployment of **ChemEXIN**, an open-source, deep learning-integrated, physicochemical property-based exon-intron boundary prediction method.

ChemEXIN is based on a three-dimensional convolutional neural network (3D-CNN) architecture and provides organism-specific prediction models for:

-   *Homo sapiens*
-   *Mus musculus*
-   *Caenorhabditis elegans*

It supports gene sequences ranging from 180 bp to ~2,500,000 bp.

------------------------------------------------------------------------

## Original Work

Title: "Exon-Intron Boundary Detection Made Easy by Physicochemical Properties of DNA"

Authors: Dinesh Sharma, Danish Aslam, Kopal Sharma, Aditya Mittal, and B Jayaram

Note: ChemEXIN is a TensorFlow implementation.

Manuscript: Sharma, D., Aslam, D., Sharma, K., Mittal, A., & Jayaram, B. (2025). Exon–intron boundary detection made easy by physicochemical properties of DNA. Molecular Omics. 2025, 21, 226-239.

Original repository: https://github.com/rnsharma478/ChemEXIN

## Docker Containerization & Deployment

For help and support, contact: Danish Aslam
Project Scientist, Computational Genomics
SCFBio
Indian Institute of Technology Delhi
Email: danish@scfbio-iitd.res.in

------------------------------------------------------------------------

## This Repository

This repository provides a fully reproducible Docker-based deployment of ChemEXIN.

The container includes:

-   Python 3.8
-   TensorFlow (CPU)
-   NumPy, SciPy, Pandas, scikit-learn\
-   All ChemEXIN source code and trained models

No Conda installation or dependency setup is required on the host system.

------------------------------------------------------------------------

## Directory Structure (Host Side)

    ChemEXIN/
    ├── main.py
    ├── models/
    ├── param_files/
    ├── sequence/      ← place input FASTA files here
    ├── results/       ← outputs will be written here
    ├── src/
    ├── Dockerfile

------------------------------------------------------------------------

## Build the Docker Image

``` bash
docker build -t chemexin .
```

------------------------------------------------------------------------

## Run ChemEXIN (Interactive Mode)

``` bash
docker run -it --rm -v $(pwd):/drive -w /drive chemexin
```

This launches:

``` bash
python /app/ChemEXIN/main.py
```
------------------------------------------------------------------------

## Interactive Prompts During Execution

### 1. Input FASTA Filename

Enter the name of a file placed inside the `sequence/` directory.

Example:

    example.fasta

### 2. Organism Selection

    h or H → H. sapiens  
    m or M → M. musculus  
    c or C → C. elegans

### 3. Single-Line Sequence Retrieval (Optional)

If your FASTA contains multi-line sequences:

    Do you want to retrieve the single-line sequence file? (Y/N)

If `y` is selected, a single-line version will be saved in the `results/` directory.

### 4. Probability Threshold Selection

    a or A → 0.70  
    b or B → 0.80  
    c or C → 0.85  
    ENTER  → default 0.75

------------------------------------------------------------------------

## Output

Results are written to:

    results/example_results.csv

The output file includes:

-   Predicted boundary windows
-   Primary start/end sites
-   Secondary extended window sites
-   Reliability threshold metadata

------------------------------------------------------------------------

## Exporting the Docker Image

``` bash
docker save chemexin | gzip > chemexin_v1.0.tar.gz
```

To load on another machine:

``` bash
docker load -i chemexin_v1.0.tar.gz
docker run -it --rm -v $(pwd):/drive -w /drive chemexin
```

------------------------------------------------------------------------

## License

GNU General Public License v3.0 (GPL-3.0)
