# by

Selection tools for matching, pairing, and subsetting operations.

## Installation

```
pip install by
```

## Features

This package provides utilities for:

### Nearest Neighbor Matching

Find nearest neighbors between point sets with optional radius constraints:

```python
from by import gen_nearest_neighbor_matching_pairs

# Find matching pairs between query and reference points
query_points = [[1, 2], [3, 4], [5, 6]]
reference_points = [[1.1, 2.1], [3.2, 4.2], [10, 10]]

# Generate matches within a radius of 1.0
matches = list(gen_nearest_neighbor_matching_pairs(
    query_points, 
    reference_points,
    radius=1.0
))
```

### Proximity-Based Pairing

Generate pairs from sorted iterables based on distance criteria:

```python
from by import gen_of_close_pairs_from_iterables

# Find pairs from two lists that are within radius=2 of each other
list1 = [4, 7, 8, 11]
list2 = [5, 10, 15]

pairs = list(gen_of_close_pairs_from_iterables(list1, list2, radius=2))
# Result: [(4, 5), (8, 10)]
```

### Interval-Based Selection

Select sublists that cover specified intervals:

```python
from by import sublist_that_contains_segment

segments = [0, 5, 10, 15, 20, 25, 30]

# Find segments covering the interval [11, 21]
covering_segments = sublist_that_contains_segment(segments, 11, 21)
# Result: [10, 15, 20]
```

## License

MIT
