# UU - Utility Library

A collection of Python utility modules for data processing and analysis.

## Modules

### by - Selection Tools

The `by` module provides utilities for selecting, matching, and pairing data points based on various criteria.

#### Key Features:

- **Nearest Neighbor Matching**: Find closest points between two datasets
- **Close Pair Generation**: Generate pairs of elements from iterables that are within a specified distance
- **Interval Subsetting**: Extract sublists that contain specified ranges

#### Main Functions:

- `gen_nearest_neighbor_matching_pairs`: Generate pairs of nearest neighbors between query and match point sets
- `gen_of_close_pairs_from_iterables`: Generate pairs of numbers from two iterables within a given distance
- `sublist_that_contains_segment`: Return a sublist of elements covering a specified interval

#### Usage Examples:

```python
import numpy as np
from uu.by import gen_nearest_neighbor_matching_pairs

# Find matching points within radius 1.0
query_points = np.array([[0, 0], [1, 1], [2, 2]])
match_points = np.array([[0.5, 0.5], [1.5, 1.5], [3, 3]])

# Get the matching pairs
pairs = list(gen_nearest_neighbor_matching_pairs(query_points, match_points, radius=1.0))
print(pairs)  # Will include points within radius 1.0

# Working with simple iterables
from uu.by import gen_of_close_pairs_from_iterables

# Find pairs from two lists within distance 1
list1 = [1, 5, 10, 15]
list2 = [2, 6, 11, 14]
pairs = list(gen_of_close_pairs_from_iterables(list1, list2, radius=1))
print(pairs)  # Will include pairs like (1, 2), (5, 6), etc.

# Get a sublist covering a range
from uu.by import sublist_that_contains_segment

values = [0, 5, 10, 15, 20, 25, 30]
segment = sublist_that_contains_segment(values, 8, 22)
print(segment)  # Will return [5, 10, 15, 20]
```

## Installation

This is a private package. To use it, ensure it's in your Python path.

## Dependencies

- NumPy
- scikit-learn
