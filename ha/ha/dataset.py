"""Interface to joke datasets"""

from functools import partial
import json
import os
from typing import Optional, Iterable, Union

from dol import wrap_kvs, Pipe, add_ipython_key_completions, flatten
from graze import graze as _graze, Graze as _Graze
from config2py import get_app_data_folder  # TODO: Remove display of sources


def list_of_dicts_to_dict(
    list_of_dicts: Iterable[dict],
    idx_key: Optional[str] = None,
    remove_idx_key: bool = False,
) -> dict:
    """Transform a list of dicts into a dict of dicts.
    If idx_key is None, then the (integer) index of the list is used as the key.
    If idx_key is not None, then the value of the dict at idx_key is used as the key.

    :param list_of_dicts: A list of dicts
    :param idx_key: The key to use as the index, defaults to None
    :param remove_idx_key: Whether to pop the idx_key from the value dict, defaults to False
    :return: A dict of dicts

    >>> list_of_dicts = [{'a': 'an', 'b': 2}, {'a': 'apple', 'b': 4}]
    >>> list_of_dicts_to_dict(list_of_dicts)
    {0: {'a': 'an', 'b': 2}, 1: {'a': 'apple', 'b': 4}}
    >>> list_of_dicts_to_dict(list_of_dicts, idx_key='a')
    {'an': {'a': 'an', 'b': 2}, 'apple': {'a': 'apple', 'b': 4}}
    >>> list_of_dicts_to_dict(list_of_dicts, idx_key='a', remove_idx_key=True)
    {'an': {'b': 2}, 'apple': {'b': 4}}

    """
    if idx_key is None:
        assert remove_idx_key is False, "Can't remove idx_key if idx_key is None"
        return {i: d for i, d in enumerate(list_of_dicts)}
    else:
        if not remove_idx_key:
            return {d[idx_key]: d for d in list_of_dicts}
        else:
            return {d.pop(idx_key): d for d in list_of_dicts}


# get a app-specific data folder for grazing stuff
ha_graze_root = get_app_data_folder('ha/graze', ensure_exists=True)

graze = partial(_graze, rootdir=ha_graze_root)
Graze = partial(_Graze, rootdir=ha_graze_root)

joke_source = {
    'reddit_jokes': 'https://raw.githubusercontent.com/taivop/joke-dataset/master/reddit_jokes.json',
    'stupidstuff': 'https://raw.githubusercontent.com/taivop/joke-dataset/master/stupidstuff.json',
    'wocka': 'https://raw.githubusercontent.com/taivop/joke-dataset/master/wocka.json',
}


joke_datasets = add_ipython_key_completions(
    wrap_kvs(joke_source, obj_of_data=Pipe(graze, json.loads))
)


extract_indices = partial(list_of_dicts_to_dict, idx_key='id', remove_idx_key=False)


def all_jokes_store() -> dict:
    """Get a store (i.e. Mapping) of all jokes from all sources.

    Will download the jokes if they are not already downloaded.
    """
    _jokes = wrap_kvs(joke_datasets, obj_of_data=extract_indices)
    return flatten(_jokes, levels=2)
