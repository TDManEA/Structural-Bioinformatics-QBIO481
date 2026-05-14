"""Functions for loading sequence, shape, and FASTA data."""

# Import Libraries/Modules
from pathlib import Path
from typing import Union

import numpy as np
import pandas as pd

# Defining Functions
def load_sequence_affinity(file_path: Union[Path, str]) -> pd.DataFrame:
    """
    Load a tab-separated file containing DNA sequences and binding affinities.

    Parameters
    ----------
    file_path : Path or str
        Path to the input .txt file.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns ['Sequence', 'Affinity'].
    """
    return pd.read_csv(file_path, sep="\t", header=None, names=["Sequence", "Affinity"])


def normalize_affinity(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize affinity values to the range [0, 1].

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing an 'Affinity' column.

    Returns
    -------
    pd.DataFrame
        Copy of the DataFrame with normalized affinity values.
    """
    df = df.copy()
    min_val = df["Affinity"].min()
    max_val = df["Affinity"].max()

    if max_val == min_val:
        df["Affinity"] = 0.0
    else:
        df["Affinity"] = (df["Affinity"] - min_val) / (max_val - min_val)

    return df


def load_shape_file(file_path: Union[Path, str]) -> np.ndarray:
    """
    Load a DNA shape file as a numeric matrix.

    Parameters
    ----------
    file_path : Path or str
        Path to a shape file with comma-separated values.

    Returns
    -------
    np.ndarray
        2D array of shape values.
    """
    rows = []

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(">"):
                continue
            rows.append([float(x) for x in line.split(",")])

    return np.atleast_2d(np.array(rows, dtype=float))


def load_all_shape_data(shape_files: dict) -> dict:
    """
    Load all shape files into a nested dictionary.

    Parameters
    ----------
    shape_files : dict
        Dictionary mapping TF names to shape feature file paths.

    Returns
    -------
    dict
        Nested dictionary of the form TF -> feature -> numpy array.
    """
    return {
        tf: {
            feature: load_shape_file(path)
            for feature, path in feature_dict.items()
        }
        for tf, feature_dict in shape_files.items()
    }


def write_fasta(df: pd.DataFrame, output_file: Union[Path, str]) -> None:
    """
    Write sequences from a DataFrame to a FASTA file.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing a 'Sequence' column.
    output_file : Path or str
        Path to the output FASTA file.
    """
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w") as f:
        for i, sequence in enumerate(df["Sequence"], start=1):
            f.write(f">Sequence_{i}\n{sequence}\n")


def convert_to_fasta(input_file: Union[Path, str], output_file: Union[Path, str]) -> None:
    """
    Convert a sequence-affinity text file into FASTA format.

    Parameters
    ----------
    input_file : Path or str
        Path to the input .txt file.
    output_file : Path or str
        Path to the output .fasta file.
    """
    df = load_sequence_affinity(input_file)
    write_fasta(df, output_file)