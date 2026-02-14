
# ChemEXIN – Docker Deployment Guide

### Overview

ChemEXIN is a physicochemical parameter–based exon–intron boundary prediction tool developed at SCFBio, IIT Delhi
To cite: Sharma, D., Aslam, D., Sharma, K., Mittal, A., & Jayaram, B. (2025). Exon–intron boundary detection made easy by physicochemical properties of DNA. Molecular Omics, 21(3), 226-239.

This Docker container provides a fully reproducible execution environment including:

1. Python 3.8
2. TensorFlow (CPU)
3. Scientific Python stack (NumPy, SciPy, Pandas, scikit-learn)
4. All ChemEXIN source code

No manual installation of dependencies is required on the host system

---

### Building the Docker Image

From the root directory of the ChemEXIN repository (where the Dockerfile is located):

```bash
docker build -t chemexin .
```

---

### Required Directory Structure

```
ChemEXIN/
├── main.py
├── models/
├── param_files/
├── sequence/      ← place input FASTA files here
├── results/       ← outputs will be written here
├── src/
```

---

### Running the Container (Interactive Mode – Recommended)

From inside the ChemEXIN root directory:

```bash
docker run -it --rm   -v $(pwd):/drive   -w /drive   chemexin
```
-v $(pwd):/drive mounts your current directory into the container
-w /drive sets the working directory

This launches:

```bash
python /app/ChemEXIN/main.py
```

You will be prompted for:

- Input FASTA filename (*.fasta)
- Retrieval of single line sequence (y/n)
- Organism selection (h / m / c)
- Threshold value (0.70 / 0.80 / 0.85)

Input FASTA files must be placed inside the `sequence/` host directory
Output files will be written to the `results/` in the host directory

---

### Exporting the Image for Deployment

```bash
docker save chemexin | gzip > chemexin_v1.0.tar.gz
```

To load on another machine:

```bash
docker load -i chemexin_v1.0.tar.gz
docker run -it --rm -v $(pwd):/drive -w /drive chemexin
```
OR

```bash
gunzip -c chemexin_v1.0.tar.gz | docker load
docker run -it --rm -v $(pwd):/drive -w /drive chemexin
```

---

### Support and Contact

Email: danish@scfbio-iitd.res.in

Danish Aslam
SCFBio
Indian Institute of Technology Delhi
