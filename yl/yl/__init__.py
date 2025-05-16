"""Get dictionaries from other objects"""
__author__ = 'thorwhalen'

import json


def keyval_df(df, key_col=None, val_col=None, warn=False):
    # setting defaults
    if key_col is None:
        if 'key' in df.columns:
            key_col = 'key'
        else:
            key_col = df.columns[0]
            if warn:
                print('!!! using %s as the key_col' % key_col)
    if val_col is None:
        if 'val' in df.columns:
            val_col = 'val'
        else:
            val_col = df.columns[1]
            if warn:
                print('!!! using %s as the val_col' % val_col)
    return {k: v for (k, v) in zip(df[key_col], df[val_col])}


def json_str_file(filepath):
    return json.loads(json.load(open(filepath, 'r')))




import pandas as pd

def df_to_dict_list(df, key_col=None, val_cols=None, warn=False):
    """
    Converts a DataFrame into a list of dictionaries, where each dictionary corresponds to a row in the DataFrame.
    Optionally specify columns for keys and values.

    Parameters:
        df (pd.DataFrame): The DataFrame to convert.
        key_col (str, optional): Column to use as keys in the resulting dictionaries. Defaults to the first column.
        val_cols (list, optional): List of columns to include as values. Defaults to all columns except key_col.
        warn (bool, optional): If True, prints a warning when default columns are used. Defaults to False.

    Returns:
        list of dict: A list where each element is a dictionary with keys from key_col and values from val_cols.

    Example:
        >>> df = pd.DataFrame({
        ...     'id': [1, 2, 3],
        ...     'name': ['Alice', 'Bob', 'Charlie'],
        ...     'age': [25, 30, 35]
        ... })
        >>> df_to_dict_list(df, 'id', ['name', 'age'])
        [{1: {'name': 'Alice', 'age': 25}}, {2: {'name': 'Bob', 'age': 30}}, {3: {'name': 'Charlie', 'age': 35}}]
    """
    if key_col is None:
        key_col = df.columns[0]
        if warn:
            print('!!! using %s as the key_col' % key_col)
    if val_cols is None:
        val_cols = [col for col in df.columns if col != key_col]
        if warn:
            print('!!! using %s as the val_cols' % ', '.join(val_cols))

    return [{row[key_col]: {col: row[col] for col in val_cols}} for index, row in df.iterrows()]

def safe_json_str_file(filepath):
    """
    Safely reads a JSON file and returns the Python object decoded from JSON string.
    This function ensures the file is properly closed after reading.

    Parameters:
        filepath (str): The path to the JSON file.

    Returns:
        object: The Python object decoded from JSON string.

    Example:
        >>> # Assuming 'example.json' contains '{"key": "value"}'
        >>> safe_json_str_file('example.json')
        {'key': 'value'}
    """
    with open(filepath, 'r') as file:
        return json.load(file)




import pandas as pd

def df_to_keyed_dict(df, key_col=None, value_transformer=lambda x: x):
    """
    Converts a DataFrame into a dictionary, using one column as keys and the rest of the row as values.
    Optionally apply a transformation function to the row values.

    Parameters:
        df (pd.DataFrame): The DataFrame to convert.
        key_col (str, optional): Column to use as keys in the resulting dictionary. Defaults to the first column.
        value_transformer (function, optional): A function to apply to each row's values (excluding the key). Defaults to identity function.

    Returns:
        dict: A dictionary with keys from key_col and values as transformed rows.

    Example:
        >>> df = pd.DataFrame({
        ...     'id': [1, 2, 3],
        ...     'name': ['Alice', 'Bob', 'Charlie'],
        ...     'age': [25, 30, 35]
        ... })
        >>> df_to_keyed_dict(df, 'id', lambda row: row.to_dict())
        {1: {'name': 'Alice', 'age': 25}, 2: {'name': 'Bob', 'age': 30}, 3: {'name': 'Charlie', 'age': 35}}
    """
    if key_col is None:
        key_col = df.columns[0]

    return {row[key_col]: value_transformer(row.drop(key_col)) for index, row in df.iterrows()}

def filter_dicts_by_keys(dict_list, keys):
    """
    Filters a list of dictionaries, retaining only specified keys in each dictionary.

    Parameters:
        dict_list (list of dict): List of dictionaries to filter.
        keys (list of str): Keys to retain in each dictionary.

    Returns:
        list of dict: A list of dictionaries with only the specified keys retained.

    Example:
        >>> dict_list = [{'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'Bob', 'age': 30, 'city': 'Chicago'}]
        >>> filter_dicts_by_keys(dict_list, ['name', 'city'])
        [{'name': 'Alice', 'city': 'New York'}, {'name': 'Bob', 'city': 'Chicago'}]
    """
    return [{key: d[key] for key in keys if key in d} for d in dict_list]

def merge_dicts(*dicts, merge_strategy=lambda values: values[0]):
    """
    Merges multiple dictionaries into a single dictionary. In case of key collisions, a merge strategy function is used.

    Parameters:
        *dicts (variable number of dict): Dictionaries to merge.
        merge_strategy (function, optional): A function to resolve conflicts between values of the same key. Defaults to taking the first value.

    Returns:
        dict: A merged dictionary according to the specified merge strategy.

    Example:
        >>> d1 = {'name': 'Alice', 'age': 25}
        >>> d2 = {'name': 'Bob', 'city': 'New York'}
        >>> merge_dicts(d1, d2, merge_strategy=lambda values: ', '.join(map(str, values)))
        {'name': 'Alice, Bob', 'age': 25, 'city': 'New York'}
    """
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                result[key] = merge_strategy([result[key], value])
            else:
                result[key] = value
    return result
