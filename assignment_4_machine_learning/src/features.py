"""Functions for building shape matrices and preparing model features."""

# Import Libraries/Modules
import numpy as np
import pandas as pd
from typing import Union

from src.encoding import dna_one_mer, dna_two_mer

# Constants
SHAPE_FEATURES = ["MGW", "ProT", "Roll", "HelT"]

# Defining Functions
def build_shape_matrix(
    shape_data: dict[str, dict[str, np.ndarray]],
    tf: str,
    feature: Union[str, None] = None,
) -> np.ndarray:
    """
    Build a shape feature matrix for one transcription factor.

    Parameters
    ----------
    shape_data : dict[str, dict[str, np.ndarray]]
        Nested dictionary containing shape arrays for each TF and feature.
    tf : str
        Transcription factor name.
    feature : str or None, optional
        Shape feature to use. If None or "all", all shape features are concatenated.

    Returns
    -------
    np.ndarray
        Shape matrix for the requested TF and feature choice.
    """
    if feature is None or feature == "all":
        return np.hstack([shape_data[tf][feat] for feat in SHAPE_FEATURES])

    return shape_data[tf][feature]


def prepare_features(
    sequence_data: dict[str, pd.DataFrame],
    shape_data: dict[str, dict[str, np.ndarray]],
    tf: str,
    encoding_type: str = "1-mer",
    shape_feature: Union[str, None] = None,
):
    """
    Prepare feature matrix X and target vector y for one transcription factor.

    Parameters
    ----------
    sequence_data : dict[str, pd.DataFrame]
        Dictionary mapping TF names to normalized sequence-affinity DataFrames.
    shape_data : dict[str, dict[str, np.ndarray]]
        Nested dictionary containing shape arrays for each TF and feature.
    tf : str
        Transcription factor name.
    encoding_type : str, optional
        Feature encoding to use: '1-mer', '2-mer', '1-mer+shape', or '2-mer+shape'.
    shape_feature : str or None, optional
        Shape feature to use. Use None or "all" for all shape features.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Feature matrix X and target vector y.
    """
    df = sequence_data[tf]
    sequences = df["Sequence"].to_numpy()
    y = df["Affinity"].to_numpy()

    if encoding_type == "1-mer":
        X = np.vstack([dna_one_mer(seq) for seq in sequences])

    elif encoding_type == "2-mer":
        X = np.vstack([dna_two_mer(seq) for seq in sequences])

    elif encoding_type == "1-mer+shape":
        seq_x = np.vstack([dna_one_mer(seq) for seq in sequences])
        shape_x = build_shape_matrix(shape_data, tf, shape_feature)
        X = np.hstack([seq_x, shape_x])

    elif encoding_type == "2-mer+shape":
        seq_x = np.vstack([dna_two_mer(seq) for seq in sequences])
        shape_x = build_shape_matrix(shape_data, tf, shape_feature)
        X = np.hstack([seq_x, shape_x])

    else:
        raise ValueError(
            "encoding_type must be one of: '1-mer', '2-mer', '1-mer+shape', '2-mer+shape'"
        )

    return X, y