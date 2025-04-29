# bj

Generating hierarchical data for machine learning and data science applications

## Installation

```bash
pip install bj
```

## Description

`bj` is a Python package that provides tools for generating synthetic hierarchical cluster data. It extends scikit-learn's `make_blobs` function to create nested, hierarchical blob clusters useful for:

- Testing hierarchical clustering algorithms
- Evaluating dimensionality reduction techniques
- Creating visualization examples for nested data structures
- Benchmarking clustering algorithms on hierarchical data

## Usage

The main function is `make_hblobs`, which generates hierarchical blob clusters with configurable depth and branching.

```python
from bj import make_hblobs
import matplotlib.pyplot as plt

# Generate a simple two-level hierarchy:
# 2 main clusters, each with 3 sub-clusters
X, y = make_hblobs(n_samples=300, centers=[2, 3])

# Plot the result
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', alpha=0.8)
plt.title('Hierarchical Blob Clusters (2x3)')
plt.show()

# Create a more complex three-level hierarchy with varying cluster spreads:
# 2 main clusters, each with 3 sub-clusters, each with 4 sub-sub-clusters
X_complex, y_complex = make_hblobs(
    n_samples=500, 
    centers=[2, 3, 4],
    cluster_std=[1.0, 0.5, 0.2]  # Decreasing spread at each level
)
```

## Parameters

The `make_hblobs` function supports:

- `n_samples`: Total number of points to generate
- `n_features`: Number of features for each sample
- `centers`: Integer or list of integers representing the hierarchy structure
- `cluster_std`: Float or list of floats controlling the spread at each level
- `center_box`: Bounding box for cluster centers
- `shuffle`: Whether to shuffle the samples
- `random_state`: For reproducibility

## Examples

### Simple Two-Level Hierarchy

```python
from bj import make_hblobs

# Create a two-level hierarchy with 2 main clusters, each with 3 sub-clusters
X, y = make_hblobs(n_samples=200, centers=[2, 3])
```

### Complex Multi-Level Hierarchy

```python
# Create a three-level hierarchy with varying cluster spread
X, y = make_hblobs(
    n_samples=500,
    centers=[2, 3, 4],  # 2 main clusters -> 3 sub-clusters -> 4 sub-sub-clusters
    cluster_std=[1.0, 0.5, 0.3]  # Decreasing spread at each level
)
```

## License

MIT
