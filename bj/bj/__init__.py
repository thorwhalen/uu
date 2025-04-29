"""Generating hierarchical data

This module provides tools for generating synthetic hierarchical cluster data.
The main functionality is creating nested, hierarchical blob clusters for
testing clustering algorithms and hierarchical data visualization techniques.
"""

__author__ = 'thor'

from sklearn.datasets import make_blobs
from numpy import triu_indices, ndarray
from scipy.spatial.distance import cdist


def make_hblobs(
    n_samples=100,
    n_features=2,
    centers=(2, 3),
    cluster_std=1.0,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=None,
):
    """Generate hierarchical blob clusters for clustering analysis.

    This function extends the sklearn.datasets.make_blobs functionality to create
    hierarchical, nested cluster structures. It works recursively to generate multi-level
    hierarchical data.

    Parameters
    ----------
    n_samples : int, default=100
        The total number of points to generate.
    n_features : int, default=2
        The number of features for each sample.
    centers : int or list of int, default=(2, 3)
        If int: Number of centers to generate (passed directly to make_blobs).
        If list of int: Creates hierarchical centers where each number represents
        the branching factor at each level. The total number of leaf centers
        will be the product of all numbers in the list.
    cluster_std : float or list of float, default=1.0
        The standard deviation of the clusters.
        If float: Same standard deviation for all levels.
        If list: Must match the length of centers, with each value representing
        the relative spread at each hierarchical level.
    center_box : tuple of float (min, max), default=(-10.0, 10.0)
        The bounding box for each cluster center.
    shuffle : bool, default=True
        Whether to shuffle the samples.
    random_state : int or RandomState instance, default=None
        Determines random number generation for dataset creation.

    Returns
    -------
    X : ndarray of shape (n_samples, n_features)
        The generated samples.
    y : ndarray of shape (n_samples,)
        The integer labels for cluster membership of each sample.

    Examples
    --------
    >>> from bj import make_hblobs
    >>> # Generate a simple hierarchy with 2 main clusters, each with 3 sub-clusters
    >>> X, y = make_hblobs(n_samples=100, centers=[2, 3])
    >>>
    >>> # More complex hierarchy: 2 main clusters, each with 3 sub-clusters,
    >>> # each with 4 sub-sub-clusters
    >>> X, y = make_hblobs(n_samples=500, centers=[2, 3, 4], cluster_std=[1.0, 0.5, 0.3])
    """

    if isinstance(centers, (list, tuple, ndarray)):
        if len(centers) == 1:
            return make_blobs(
                n_samples,
                n_features,
                centers[0],
                cluster_std,
                center_box,
                shuffle,
                random_state,
            )
        else:
            # assert prod(centers) <= n_samples, "prod(centers) < n_samples !!!"
            if isinstance(cluster_std, (float, int)):
                cluster_std = [cluster_std] * len(centers)
            assert len(cluster_std) == len(centers)

            level_centers, _ = make_blobs(
                n_samples=centers[0],
                n_features=n_features,
                centers=centers[0],
                cluster_std=cluster_std[0],
                center_box=center_box,
                shuffle=shuffle,
                random_state=random_state,
            )

            for this_center, _cluster_std in zip(centers[1:], cluster_std[1:]):
                n = this_center * len(level_centers)
                min_dist = cdist(level_centers, level_centers)[
                    triu_indices(len(level_centers), k=1)
                ].min()
                level_centers, y = make_blobs(
                    n_samples=min(n_samples, n),
                    n_features=n_features,
                    centers=level_centers,
                    cluster_std=min_dist * _cluster_std,
                    center_box=center_box,
                    shuffle=shuffle,
                    random_state=random_state,
                )

        min_dist = cdist(level_centers, level_centers)[
            triu_indices(len(level_centers), k=1)
        ].min()

        return make_blobs(
            n_samples=n_samples,
            n_features=n_features,
            centers=level_centers,
            cluster_std=min_dist * cluster_std[-1],
            center_box=center_box,
            shuffle=shuffle,
            random_state=random_state,
        )

    else:
        return make_blobs(
            n_samples,
            n_features,
            centers,
            cluster_std,
            center_box,
            shuffle,
            random_state,
        )
