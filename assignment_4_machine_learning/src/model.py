"""Functions for training and evaluating ridge regression models."""

# Import Libraries/Modules
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import KFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Defining Functions
def perform_ridge_cv(
    features: np.ndarray,
    targets: np.ndarray,
    alpha: float = 1.0,
    n_splits: int = 10,
    random_state: int = 42,
) -> float:
    """
    Run K-fold cross-validation with ridge regression and return mean R².

    Parameters
    ----------
    features : np.ndarray
        Feature matrix X.
    targets : np.ndarray
        Target vector y.
    alpha : float, optional
        Ridge regularization strength.
    n_splits : int, optional
        Number of cross-validation folds.
    random_state : int, optional
        Random seed used when shuffling folds.

    Returns
    -------
    float
        Mean R² score across all folds.
    """
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    model = make_pipeline(StandardScaler(), Ridge(alpha=alpha))

    r2_scores = []

    for train_idx, test_idx in kf.split(features):
        X_train, X_test = features[train_idx], features[test_idx]
        y_train, y_test = targets[train_idx], targets[test_idx]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2_scores.append(r2_score(y_test, y_pred))

    return float(np.mean(r2_scores))