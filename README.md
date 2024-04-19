# ChemEXIN

An open-source, deep learning integrated, physicochemical parameter-based exon-intron boundary prediction method. It is based on a three-dimensional convolutional neural network (3D- CNN) architecture. Three organism-specific (_Homo sapiens_, _Mus musculus_, and _Caenorhabditis elegans_) models have been built and implemented in the final prediction pipeline. The universality of ChemEXIN lies in its ability to predict exon-intron boundaries across varying lengths of known genes (~180 to ~25,00,000 bps) in the organisms under study.

"ChemEXIN:  A Physicochemical Parameter-Based Exon-Intron Boundary Prediction Method"

Authors: Dinesh Sharma, Danish Aslam, Kopal Sharma, Aditya Mittal, and B Jayaram

Note: ChemEXIN is a TensorFlow implementation.

## Setup

### Prerequisites
- **Conda**, to facilitate the management of packages and environments required for ChemEXIN across Windows, macOS, and Linux operating systems.
- URL: https://conda.io/projects/conda/en/latest/user-guide/install/index.html 

### Installation
### Create the project:
 `git clone https://github.com/rnsharma478/ChemEXIN.git`

 <div class="code-container">
    <code>
        // Your code here
    </code>
    <button class="copy-button" onclick="copyCode()">Copy</button>
</div>

<script>
    function copyCode() {
        var codeBlock = document.querySelector('.code-container code');
        var range = document.createRange();
        range.selectNode(codeBlock);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);
        document.execCommand('copy');
        window.getSelection().removeAllRanges();
        alert("Code copied!");
    }
</script>

<style>
    .code-container {
        position: relative;
    }
    .copy-button {
        position: absolute;
        top: 5px;
        right: 5px;
        border: none;
        background-color: transparent;
        cursor: pointer;
        font-size: 14px;
        color: #007bff;
        outline: none;
    }
</style>


### Go to the project directory:
> cd ChemEXIN

### Installing the virtual environment:
> conda env create -f ChemEXIN.yml

> conda activate ChemEXIN

### Usage:

> cd ChemEXIN

> python main.py
