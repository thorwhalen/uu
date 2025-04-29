# bh: Fuzzy Linear Discriminant Analysis

`bh` is a Python library implementing Fuzzy Linear Discriminant Analysis (FLDA), an extension of traditional Linear Discriminant Analysis that handles fuzzy or probabilistic class memberships.

## Installation

```bash
pip install bh
```

## Features

- **Fuzzy Linear Discriminant Analysis**: Extends traditional LDA to work with fuzzy class memberships
- **scikit-learn compatible**: Implements scikit-learn's estimator interface
- **Dimensionality reduction**: Transform high-dimensional data into a lower-dimensional space while preserving class separability
- **Classification**: Predict class probabilities and labels for new data points
- **Data preprocessing**: Includes utilities like `sphericize` to transform data to have spherical covariance

## Usage

### Basic Example

```python
import numpy as np
from bh import FuzzyLDA

# Create some sample data
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# Fuzzy class membership: each point can partially belong to multiple classes
y = [
    {'class1': 0.8, 'class2': 0.2},
    {'class1': 0.9, 'class2': 0.1},
    {'class1': 1.0, 'class2': 0.0},
    {'class1': 0.1, 'class2': 0.9},
    {'class1': 0.0, 'class2': 1.0},
    {'class1': 0.2, 'class2': 0.8},
]

# Fit model
flda = FuzzyLDA()
flda.fit(X, y)

# Transform data
X_transformed = flda.transform(X)

# Predict on new data
new_data = np.array([[0.8, 1]])
probabilities = flda.predict_proba(new_data)
predicted_class = flda.predict(new_data)
```

### Using with Hard Labels

FLDA also works with traditional hard labels:

```python
from bh import FuzzyLDA

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
y = [0, 0, 0, 1, 1, 1]  # Hard labels are automatically converted to fuzzy format

flda = FuzzyLDA()
flda.fit(X, y)
```

### Data Preprocessing

```python
from bh import sphericize

X_spherical = sphericize(X, y)
```

## Theory

Fuzzy Linear Discriminant Analysis extends traditional LDA by allowing samples to partially belong to multiple classes. This is particularly useful in scenarios where:

- Class membership is inherently probabilistic
- There is uncertainty in class assignments
- Data points can naturally belong to multiple categories

The algorithm finds a linear transformation that maximizes the ratio of between-class scatter to within-class scatter, while accounting for fuzzy memberships.

## License

[License information goes here]

## Citation

If you use this software in your research, please cite it.
