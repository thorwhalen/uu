# yl
Get dictionaries from other objects

To install:	```pip install yl```

## Overview
The `yl` package provides a set of utilities to convert data structures into more usable dictionary formats, particularly focusing on data extraction and transformation from pandas DataFrames. It also includes functionalities to safely read JSON files and merge dictionaries with customizable strategies.

## Features

### DataFrame to Dictionary Conversion
- **`keyval_df`**: Convert a DataFrame into a dictionary using one column for keys and another for values.
- **`df_to_dict_list`**: Transform a DataFrame into a list of dictionaries, with options to specify which columns to use for keys and values.
- **`df_to_keyed_dict`**: Convert a DataFrame into a dictionary, using one column as keys and applying an optional transformation function to the rest of the data in each row.

### JSON Utilities
- **`json_str_file`**: Load and parse a JSON file into a Python object.
- **`safe_json_str_file`**: Safely read a JSON file, ensuring the file is properly closed after reading.

### Dictionary Utilities
- **`filter_dicts_by_keys`**: Filter a list of dictionaries, retaining only specified keys.
- **`merge_dicts`**: Merge multiple dictionaries into one, with a customizable strategy for handling key collisions.

## Usage Examples

### Convert DataFrame to Dictionary
```python
import pandas as pd
df = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})
result = df_to_keyed_dict(df, 'id')
print(result)
# Output: {1: {'name': 'Alice', 'age': 25}, 2: {'name': 'Bob', 'age': 30}, 3: {'name': 'Charlie', 'age': 35}}
```

### Read JSON File Safely
```python
json_data = safe_json_str_file('example.json')
print(json_data)
# Assuming 'example.json' contains '{"key": "value"}'
# Output: {'key': 'value'}
```

### Filter List of Dictionaries
```python
dict_list = [{'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'Bob', 'age': 30, 'city': 'Chicago'}]
filtered = filter_dicts_by_keys(dict_list, ['name', 'city'])
print(filtered)
# Output: [{'name': 'Alice', 'city': 'New York'}, {'name': 'Bob', 'city': 'Chicago'}]
```

### Merge Dictionaries with Custom Strategy
```python
d1 = {'name': 'Alice', 'age': 25}
d2 = {'name': 'Bob', 'city': 'New York'}
merged = merge_dicts(d1, d2, merge_strategy=lambda values: ', '.join(map(str, values)))
print(merged)
# Output: {'name': 'Alice, Bob', 'age': 25, 'city': 'New York'}
```

## Documentation
Each function in the `yl` package is documented with Python docstrings, providing detailed descriptions of their purpose, parameters, return values, and examples. This documentation can be accessed using the help function in Python, e.g., `help(df_to_keyed_dict)`.