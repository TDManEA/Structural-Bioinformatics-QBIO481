"""Functions for plotting model performance comparisons."""

# Import Libraries/Modules
from pathlib import Path
from typing import Union

import matplotlib.pyplot as plt

# Defining Functions
def plot_r2_comparison(
    results: dict,
    tf_names: list[str],
    save_path: Union[Path, None] = None,
):
    """
    Plot comparison of 1-mer vs 2-mer R² scores.

    Parameters
    ----------
    results : dict
        Dictionary containing R² scores for each TF and encoding type.
    tf_names : list[str]
        List of transcription factor names.
    save_path : Path or None, optional
        Path to save the figure. If None, figure is not saved.
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    for tf in tf_names:
        ax.scatter(results[(tf, "1-mer")], results[(tf, "2-mer")], label=tf, s=80)

    ax.plot([0, 1], [0, 1], "k--", label="1:1 line")
    ax.set_xlim(0.7, 1.0)
    ax.set_ylim(0.7, 1.0)
    ax.set_xlabel("1-mer R²")
    ax.set_ylabel("2-mer R²")
    ax.set_title("1-mer vs 2-mer R² Comparison")
    ax.legend()
    ax.grid(True)

    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path, dpi=300, bbox_inches="tight")

    return fig, ax


def plot_shape_comparison(
    results: dict,
    tf_names: list[str],
    save_path: Union[Path, None] = None,
):
    """
    Plot effect of shape features on model performance.

    Parameters
    ----------
    results : dict
        Dictionary containing R² scores for each TF and feature combination.
    tf_names : list[str]
        List of transcription factor names.
    save_path : Path or None, optional
        Path to save the figure. If None, figure is not saved.
    """
    shape_order = ["all", "MGW", "ProT", "Roll", "HelT"]
    markers = {"Max": "o", "Mad": "s", "Myc": "^"}
    colors = {
        "all": "orange",
        "MGW": "red",
        "ProT": "blue",
        "Roll": "green",
        "HelT": "purple",
    }

    fig, ax = plt.subplots(figsize=(10, 8))

    for tf in tf_names:
        x = results[(tf, "1-mer")]
        for feature in shape_order:
            key = (tf, "1-mer+shape", feature)
            if key not in results:
                continue

            ax.scatter(
                x,
                results[key],
                marker=markers[tf],
                color=colors[feature],
                s=100,
                label=f"{tf} ({feature})",
            )

    ax.plot([0, 1], [0, 1], "k--", label="1:1 line")
    ax.set_xlim(0.7, 1.0)
    ax.set_ylim(0.7, 1.0)
    ax.set_xlabel("1-mer R²")
    ax.set_ylabel("1-mer+shape / shape-feature R²")
    ax.set_title("Effect of Shape Features on R²")
    ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    ax.grid(True)

    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path, dpi=300, bbox_inches="tight")

    return fig, ax


def plot_2mer_vs_shape_comparison(
    r2_values: dict,
    tf_names: list[str],
    save_path: Union[Path, None] = None,
):
    """
    Plot comparison of 2-mer vs shape-based model performance.

    Parameters
    ----------
    r2_values : dict
        Dictionary containing R² scores for each TF and feature type.
    tf_names : list[str]
        List of transcription factor names.
    save_path : Union[Path, None], optional
        Path to save the figure. If None, figure is not saved.
    """
    markers = {
        "1-mer+shape": "o",
        "MGW": "x",
        "ProT": "^",
        "Roll": "s",
        "HelT": "D",
    }
    colors = {"Max": "blue", "Mad": "green", "Myc": "red"}

    fig, ax = plt.subplots(figsize=(10, 8))

    for tf in tf_names:
        for feature, marker in markers.items():
            ax.scatter(
                r2_values[tf]["2-mer"],
                r2_values[tf][feature],
                label=f"{tf} ({feature})",
                marker=marker,
                color=colors[tf],
            )

    ax.plot([0, 1], [0, 1], "k--", label="1:1 line")
    ax.set_xlim(0.7, 1.0)
    ax.set_ylim(0.7, 1.0)
    ax.set_title("2-mer vs Shape-Based R² Comparison")
    ax.set_xlabel("2-mer R²")
    ax.set_ylabel("Shape-based R²")
    ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    ax.grid(True)

    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path, dpi=300, bbox_inches="tight")

    return fig, ax