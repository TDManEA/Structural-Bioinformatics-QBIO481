# Assignment 4 – Machine Learning for DNA Binding Affinity

## Overview

This project implements supervised machine learning models to predict DNA binding affinity from sequence data. The workflow compares different feature representations, including 1-mer encoding, 2-mer encoding, and DNA shape features, using ridge regression with cross-validation.

All core logic is implemented in modular Python scripts (`src/`), and the notebook (`machine_learning.ipynb`) serves as a clean orchestration layer.

---

## Project Structure

```
assignment_4_machine_learning/
├── data/                  # Input sequence and shape data
├── results/
│   ├── figures/          # Generated plots
│   ├── tables/           # Model results (CSV)
│   └── fasta/            # FASTA outputs
├── src/                  # Core Python modules
│   ├── data_loader.py
│   ├── encoding.py
│   ├── features.py
│   ├── model.py
│   └── plots.py
├── machine_learning.ipynb
├── environment.yml
└── README.md
```

---

## Requirements

This project uses a conda environment.

### Create environment

```bash
conda env create -f environment.yml
conda activate qbio481
```

### Core dependencies

* Python 3.9
* numpy
* pandas
* matplotlib
* scikit-learn
* jupyter

No additional PATH configuration is required.

---

## How to Run

### Run full analysis

1. Open `machine_learning.ipynb`
2. Select kernel: **Python (qbio481)**
3. Restart kernel
4. Run all cells

---

### Example usage

#### Load and normalize data

```python
df = load_sequence_affinity("data/Max.txt")
df = normalize_affinity(df)
```

#### Build features and evaluate model

```python
X, y = prepare_features(sequence_data, shape_data, "Max", "1-mer")
r2 = perform_ridge_cv(X, y)
```

---

## Outputs

All outputs are automatically saved to:

* `results/tables/` → CSV files with R² scores
* `results/figures/` → comparison plots
* `results/fasta/` → FASTA sequence files

---

## Reproducibility

* All paths are relative (no hardcoded local paths)
* The notebook runs from a fresh kernel
* Running **Restart Kernel → Run All** reproduces all results

---

## Notes

* The notebook contains no core logic; all functionality is implemented in `src/`
* Models are evaluated using K-fold cross-validation with ridge regression
* Feature comparisons include sequence-only and sequence + shape features
