# dn
Shapley value analysis

To install:	```pip install dn```

## Overview
The `dn` package provides tools for Shapley value analysis, useful in cooperative game theory and other applications where the distribution of a total payoff needs to be fairly allocated to the contributors based on their marginal contributions. The package includes functionalities to compute Shapley values from coalition values, handle data models for Shapley calculations, and generate random Shapley values for testing and simulation purposes.

## Main Features
- **Shapley Value Computation**: Calculate Shapley values using different methods, including direct formula-based calculations and data model-based approaches.
- **Data Models for Shapley Analysis**: Manage and manipulate data for Shapley value calculations through specialized data models.
- **Utility Functions**: Includes various utility functions to generate subsets, supersets, and handle coalition data effectively.

## Usage Examples

### Computing Shapley Values from Coalition Values
To compute Shapley values from a dictionary of coalition values:

```python
from dn import compute_shapley_values_from_coalition_values

coalition_values = {('A',): 10, ('B',): 15, ('A', 'B'): 25}
shapley_values = compute_shapley_values_from_coalition_values(coalition_values)
print(shapley_values)
```

### Using the Shapley Data Model
To use the `ShapleyDataModel` for managing and computing Shapley values:

```python
from dn import ShapleyDataModel

# Initialize the data model
dm = ShapleyDataModel()

# Absorb sequences into the model
dm.absorb_sequence_into_coalition_obs(['A', 'B', 'C'])
dm.absorb_sequence_into_coalition_obs(['A', 'C'])

# Compute coalition values
coalition_values = dm.coalition_values()

# Compute Shapley values
shapley_values = compute_shapley_values_from_coalition_values(coalition_values)
print(shapley_values)
```

### Generating Random Shapley Values
To generate random Shapley values for a set number of items:

```python
from dn import rand_shapley_values

random_shapley_values = rand_shapley_values(items=4)
print(random_shapley_values)
```

## Documentation

### Functions
- `compute_shapley_values_from_coalition_values(coalition_values, normalize=False, verbose=False)`: Computes Shapley values from a dictionary of coalition values. Set `normalize=True` to normalize the Shapley values so that they sum to 1. The `verbose` parameter can be used to print detailed computation steps.

### Classes
- **ShapleyDataModel**: A class for managing data relevant to Shapley value calculations. It can absorb individual items or collections of items as observations, and compute coalition values from these observations.

### Utility Functions
- `all_proper_subsets_iterator(superset)`: Generates all proper subsets of a given set.
- `all_subsets_or_eq_iterator(superset)`: Generates all subsets of a given set, including the set itself.
- `all_superset_iterator(subset, universe_set)`: Generates all supersets of a subset within a given universe set.

## Installation
To install the latest version of `dn`, use pip:

```bash
pip install dn
```

This package requires Python 3.x and has dependencies on `numpy`, `pandas`, `scipy`, and `itertools` which will be installed during the installation process.