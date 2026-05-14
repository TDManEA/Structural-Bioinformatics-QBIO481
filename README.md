# Structural-Bioinformatics

Coursework repository for QBIO 481 (Structural Bioinformatics) covering protein structure, DNA structure, molecular simulation, electrostatics, and machine-learning-based DNA binding affinity prediction.

## Overview

This repository is organized by assignment and is intended to be run from the repository root using relative paths whenever possible.

---

## Repository structure

```text
Structural-Bioinformatics/
├── assignment_1_protein_structure/
├── assignment_2_dna_structure/
├── assignment_3_md_verlet/
└── assignment_4_machine_learning/
```

## Assignment summaries

### Assignment 1: Protein structure and molecular interactions

**Topics covered:**
- amino-acid side-chain interactions
- hydrogen bonding in secondary structure
- ionic and Lennard-Jones interactions
- protein secondary structure visualization in PyMOL
- AlphaFold-based structure comparison
- protein-DNA recognition concepts
- force-field energy minimization and torsion terms

### Assignment 2: DNA structure and electrostatics

**Topics covered:**
- DNA duplex stabilization
- A-DNA, B-DNA, and Z-DNA comparison
- 3DNA shape parameters
- APBS / Poisson-Boltzmann electrostatics in PyMOL
- simple force-field energy minimization
- protein-DNA recognition mechanisms

### Assignment 3: Molecular dynamics and numerical methods

**Topics covered:**
- MD vs Monte Carlo
- gradient descent and minimization
- Verlet integration
- electron density interpretation

### Assignment 4: Machine learning for DNA binding affinity

This assignment implements a modular machine-learning workflow to predict DNA binding affinity from sequence and shape features.

**Design goals:**
- the notebook is only an orchestration layer
- all reusable logic lives in `src/`
- all paths are relative
- outputs are written to results/figures, results/tables, and results/fasta
- runs from **Restart Kernel → Run All**

## Requirements

**Common packages used:**
- Python 3.9
- numpy
- pandas
- matplotlib
- scikit-learn
- jupyter
- scipy
- PyMOL

**External tools used:**
- AlphaFold server
- 3DNA web server
- APBS Electrostatics (PyMOL plugin)

## Installation

### Clone the repository

```bash
git clone https://github.com/TDManEA/Structural-Bioinformatics.git
cd Structural-Bioinformatics
```

### Setup environment (Assignment 4)

```bash
conda env create -f assignment_4_machine_learning/environment.yml
conda activate qbio481
```

Or update existing:

```bash
conda env update -n qbio481 -f assignment_4_machine_learning/environment.yml --prune
conda activate qbio481
```

## How to run

### Assignment 1–3

Open the notebook/script in each assignment folder and run all cells.

### Assignment 4

1. Open: `assignment_4_machine_learning/machine_learning.ipynb`
2. Select kernel: `qbio481`
3. Restart kernel
4. Run all cells

## Example usage (Assignment 4)

```python
from src.data_loader import load_sequence_affinity
from src.features import prepare_features
from src.model import perform_ridge_cv

sequence_data = load_sequence_affinity("data/Max.txt")
X, y = prepare_features(sequence_data, feature_type="1-mer")
r2 = perform_ridge_cv(X, y)
```

## Output locations

Generated outputs:
- `assignment_4_machine_learning/results/figures/`
- `assignment_4_machine_learning/results/tables/`
- `assignment_4_machine_learning/results/fasta/`

## Reproducibility

- Use relative paths (no `/Users/...`)
- Keep logic in `src/`
- Notebook = orchestration only
- Run from fresh kernel

**Ignored files:**
- `__pycache__/`
- `.ipynb_checkpoints/`
- `*.pyc`
- `.DS_Store`

## Notes

- Assignments 1–2: structural biology + PyMOL
- Assignment 3: numerical simulation
- Assignment 4: fully modular ML pipeline

## License

Coursework repository for educational use.