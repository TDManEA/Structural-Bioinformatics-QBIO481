"""Functions for encoding DNA sequences using 1-mer and 2-mer representations."""

# Import Libraries/Modules
import numpy as np
from itertools import product

# Defining Constants
BASES = "ACGT"
TWO_MERS = ["".join(p) for p in product(BASES, repeat=2)]

ONE_MER_MAP = {
    base: [1 if i == j else 0 for i in range(4)]
    for j, base in enumerate(BASES)
}

TWO_MER_MAP = {
    mer: [1 if i == j else 0 for i in range(16)]
    for j, mer in enumerate(TWO_MERS)
}

# Defining Functions
def dna_one_mer(sequence: str) -> np.ndarray:
    """
    Encode a DNA sequence using 1-mer (single nucleotide) one-hot encoding.

    Parameters
    ----------
    sequence : str
        DNA sequence consisting of characters A, C, G, T.

    Returns
    -------
    np.ndarray
        1D array representing the one-hot encoded sequence.
    """
    return np.array(
        [bit for base in sequence for bit in ONE_MER_MAP[base]],
        dtype=int,
    )


def dna_two_mer(sequence: str) -> np.ndarray:
    """
    Encode a DNA sequence using overlapping 2-mer one-hot encoding.

    Parameters
    ----------
    sequence : str
        DNA sequence consisting of characters A, C, G, T.

    Returns
    -------
    np.ndarray
        1D array representing the 2-mer encoded sequence.
    """
    return np.array(
        [
            bit
            for i in range(len(sequence) - 1)
            for bit in TWO_MER_MAP[sequence[i : i + 2]]
        ],
        dtype=int,
    )