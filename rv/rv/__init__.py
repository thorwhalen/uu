"""Utils to work with randomness"""

__author__ = 'thor'

import numpy as np
from decimal import Decimal
from numpy import random


def rand_numbers_summing_to_one(n_numbers, granularity=0.01):
    n_choices = 1.0 / granularity
    assert round(n_choices) == int(
        n_choices
    ), 'granularity must be an integer divisor of 1.0'
    x = np.linspace(granularity, 1.0 - granularity, n_choices - 1)
    x = sorted(
        x[np.random.choice(list(range(1, len(x))), size=n_numbers - 1, replace=False)]
    )
    x = np.concatenate([[0.0], x, [1.0]])
    x = np.diff(x)
    x = np.array([Decimal(xi).quantize(Decimal(str(granularity))) for xi in x])
    return x


def weighted_choice(choices):
    r = random.uniform(0, sum(choices))
    upto = 0
    for i, w in enumerate(choices):
        if upto + w >= r:
            return i
        upto += w
    assert False, "Shouldn't get here"

    
 # forged strings

"""Functions to generate strings"""

import random
import string
from functools import reduce, partial
from operator import add

# Note: Probably want to use another package for generation of fake data.
#   For example, https://github.com/joke2k/faker


dflt_formatter = string.Formatter()


def _assert_condition(condition, err_msg='', err_cls=AssertionError):
    if not condition:
        raise err_cls(err_msg)


class NotValid(ValueError, TypeError):
    """To use to indicate when an object doesn't fit expected properties"""


class KeyValidationError(NotValid):
    """Error to raise when a key is not valid"""


__assert_condition = partial(_assert_condition, err_cls=KeyValidationError)


lower_case_letters = string.ascii_lowercase
alphanumeric = string.digits + lower_case_letters
non_alphanumeric = ''.join(set(string.printable).difference(alphanumeric))


def random_word(length, alphabet, concat_func=add):
    """Make a random word by concatenating randomly drawn elements from alphabet together
    Args:
        length: Length of the word
        alphabet: Alphabet to draw from
        concat_func: The concatenation function (e.g. + for strings and lists)

    Note: Repeated elements in alphabet will have more chances of being drawn.

    Returns:
        A word (whose type depends on what concatenating elements from alphabet produces).

    Not making this a proper doctest because I don't know how to seed the global random temporarily
    
    >>> t = random_word(4, 'abcde');  # e.g. 'acae'
    >>> t = random_word(5, ['a', 'b', 'c']);  # e.g. 'cabba'
    >>> t = random_word(4, [[1, 2, 3], [40, 50], [600], [7000]]);  # e.g. [40, 50, 7000, 7000, 1, 2, 3]
    >>> t = random_word(4, [1, 2, 3, 4]);  # e.g. 13 (because adding numbers...)
    >>> # ... sometimes it's what you want:
    >>> t = random_word(4, [2 ** x for x in range(8)]);  # e.g. 105 (binary combination)
    >>> t = random_word(4, [1, 2, 3, 4], concat_func=lambda x, y: str(x) + str(y));  # e.g. '4213'
    >>> t = random_word(4, [1, 2, 3, 4], concat_func=lambda x, y: int(str(x) + str(y)));  # e.g. 3432
    """
    if isinstance(alphabet, bytes) or isinstance(alphabet[0], bytes):
        # convert to list of bytes, or the function will return ints instead of bytes
        alphabet = _list_of_bytes_singletons(alphabet)
    return reduce(concat_func, (random.choice(alphabet) for _ in range(length)))


def _list_of_bytes_singletons(bytes_alphabet):
    """Convert to list of bytes, or the function will return ints instead of bytes"""
    return list(map(lambda x: bytes([x]), bytes_alphabet))


def random_string(length=7, alphabet=lower_case_letters):
    """Same as random_word, but it optimized for strings
    (5-10% faster for words of length 7, 25-30% faster for words of size 1000)"""
    return ''.join(random.choice(alphabet) for _ in range(length))


def random_word_gen(word_size_range=(1, 10), alphabet=lower_case_letters, n=100):
    """Random string generator
    Args:
        word_size_range: An int, 2-tuple of ints, or list-like object that defines the choices of word sizes
        alphabet: A string or iterable defining the alphabet to draw from
        n: The number of elements the generator will yield

    Returns:
        Random string generator
    """
    if isinstance(word_size_range, int):
        word_size_range = range(1, word_size_range + 1)
    elif not isinstance(word_size_range, range):
        word_size_range = range(*word_size_range)

    for _ in range(n):
        length = random.choice(word_size_range)
        yield random_word(length, alphabet)


def random_tuple_gen(
    tuple_length=3, word_size_range=(1, 10), alphabet=lower_case_letters, n: int = 100,
):
    """Random tuple (of strings) generator

    Args:
        tuple_length: The length of the tuples generated
        word_size_range: An int, 2-tuple of ints, or list-like object that defines the choices of word sizes
        alphabet: A string or iterable defining the alphabet to draw from
        n: The number of elements the generator will yield

    Returns:
        Random tuple (of strings) generator
    """
    for _ in range(n):
        yield tuple(random_word_gen(word_size_range, alphabet, tuple_length))


def random_dict_gen(
    fields=('a', 'b', 'c'),
    word_size_range=(1, 10),
    alphabet=lower_case_letters,
    n: int = 100,
):
    """Random dict (of strings) generator

    Args:
        fields: Field names for the random dicts
        word_size_range: An int, 2-tuple of ints, or list-like object that defines the choices of word sizes
        alphabet: A string or iterable defining the alphabet to draw from
        n: The number of elements the generator will yield

    Returns:
        Random dict (of strings) generator
    """
    tuple_length = len(fields)
    yield from (
        dict_of_tuple(x, fields)
        for x in random_tuple_gen(tuple_length, word_size_range, alphabet, n)
    )


def random_formatted_str_gen(
    format_string='root/{}/{}_{}.test',
    word_size_range=(1, 10),
    alphabet=lower_case_letters,
    n=100,
):
    """Random formatted string generator

    Args:
        format_string: A format string
        word_size_range: An int, 2-tuple of ints, or list-like object that defines the choices of word sizes
        alphabet: A string or iterable defining the alphabet to draw from
        n: The number of elements the generator will yield

    Returns:
        Yields random strings of the format defined by format_string

    Examples:
        # >>> list(random_formatted_str_gen('root/{}/{}_{}.test', (2, 5), 'abc', n=5))
        [('root/acba/bb_abc.test',),
         ('root/abcb/cbbc_ca.test',),
         ('root/ac/ac_cc.test',),
         ('root/aacc/ccbb_ab.test',),
         ('root/aab/abb_cbab.test',)]

    >>> # The following will be made not random (by restricting the constraints to "no choice"
    >>> # ... this is so that we get consistent outputs to assert for the doc test.
    >>>
    >>> # Example with automatic specification
    >>> list(random_formatted_str_gen('root/{}/{}_{}.test', (3, 4), 'a', n=2))
    [('root/aaa/aaa_aaa.test',), ('root/aaa/aaa_aaa.test',)]
    >>>
    >>> # Example with manual specification
    >>> list(random_formatted_str_gen('indexed field: {0}: named field: {name}', (2, 3), 'z', n=1))
    [('indexed field: zz: named field: zz',)]
    """
    args_template, kwargs_template = empty_arg_and_kwargs_for_format(format_string)
    n_args = len(args_template)
    args_gen = random_tuple_gen(n_args, word_size_range, alphabet, n)
    kwargs_gen = random_dict_gen(kwargs_template.keys(), word_size_range, alphabet, n)
    yield from zip(
        format_string.format(*args, **kwargs)
        for args, kwargs in zip(args_gen, kwargs_gen)
    )


#########################################################################################
# Utils


def _is_not_none(x):
    return x is not None


def tuple_of_dict(d, fields):
    __assert_condition(
        len(fields) == len(d), f'len(d)={len(d)} but len(fields)={len(fields)}'
    )
    return tuple(d[f] for f in fields)


def dict_of_tuple(d, fields):
    __assert_condition(
        len(fields) == len(d), f'len(d)={len(d)} but len(fields)={len(fields)}'
    )
    return {f: x for f, x in zip(fields, d)}


def is_manual_format_string(format_string):
    """Says if the format_string uses a manual specification
    See Also: is_automatic_format_string and
    >>> is_manual_format_string('Manual: indices: {1} {2}, named: {named} {fields}')
    True
    >>> is_manual_format_string('Auto: only un-indexed and un-named: {} {}...')
    False
    >>> is_manual_format_string('Hybrid: at least a {}, and a {0} or a {name}')
    False
    >>> is_manual_format_string('No formatting is both manual and automatic formatting!')
    True
    """
    return is_manual_format_params(format_params_in_str_format(format_string))


def is_manual_format_params(format_params):
    """Says if the format_params is from a manual specification
    See Also: is_automatic_format_params
    """
    assert not isinstance(
        format_params, str
    ), "format_params can't be a string (perhaps you meant is_manual_format_string?)"
    return all((x is not None) for x in format_params)


def is_automatic_format_params(format_params):
    """Says if the format_params is from an automatic specification
    See Also: is_manual_format_params and is_hybrid_format_params
    """
    assert not isinstance(
        format_params, str
    ), "format_params can't be a string (perhaps you meant to use is_automatic_format_string?)"
    return all((x is None) for x in format_params)


def is_hybrid_format_params(format_params):
    """Says if the format_params is from a hybrid of auto and manual.
    Note: Hybrid specifications are considered non-valid and can't be formatted with format_string.format(...).
    Yet, it can be useful for flexibility of expression (but will need to be resolved to be used).
    See Also: is_manual_format_params and is_automatic_format_params
    """
    assert not isinstance(
        format_params, str
    ), "format_params can't be a string (perhaps you meant is_hybrid_format_string?)"
    return (not is_manual_format_params(format_params)) and (
        not is_automatic_format_params(format_params)
    )


def format_params_in_str_format(format_string):
    """
    Get the "parameter" indices/names of the format_string

    Args:
        format_string: A format string (i.e. a string with {...} to mark parameter placement and formatting

    Returns:
        A list of parameter indices used in the format string, in the order they appear, with repetition.
        Parameter indices could be integers, strings, or None (to denote "automatic field numbering".
        
    >>> format_string = '{0} (no 1) {2}, and {0} is a duplicate, {} is unnamed and {name} is string-named'
    >>> format_params_in_str_format(format_string)
    [0, 2, 0, None, 'name']
    """
    return list(
        map(
            lambda x: int(x) if str.isnumeric(x) else x if x != '' else None,
            filter(_is_not_none, (x[1] for x in dflt_formatter.parse(format_string)),),
        )
    )


def is_hybrid_format_string(format_string):
    """Says if the format_params is from a hybrid of auto and manual.
    Note: Hybrid specifications are considered non-valid and can't be formatted with format_string.format(...).
    Yet, it can be useful for flexibility of expression (but will need to be resolved to be used).

    >>> is_hybrid_format_string('Manual: indices: {1} {2}, named: {named} {fields}')
    False
    >>> is_hybrid_format_string('Auto: only un-indexed and un-named: {} {}...')
    False
    >>> is_hybrid_format_string('Hybrid: at least a {}, and a {0} or a {name}')
    True
    >>> is_manual_format_string('No formatting is both manual and automatic formatting (so hybrid is both)!')
    True
    """
    return is_hybrid_format_params(format_params_in_str_format(format_string))


no_hybrid_format_error = ValueError(
    'cannot switch from manual field specification (i.e. {{number}} or {{name}}) '
    'to automatic (i.e. {{}}) field numbering.'
)


def args_and_kwargs_indices(format_string):
    """Get the sets of indices and names used in manual specification of format strings, or None, None if auto spec.
    Args:
        format_string: A format string (i.e. a string with {...} to mark parameter placement and formatting

    Returns:
        None, None if format_string is an automatic specification
        set_of_indices_used, set_of_fields_used if it is a manual specification

    >>> format_string = '{0} (no 1) {2}, {see} this, {0} is a duplicate (appeared before) and {name} is string-named'
    >>> assert args_and_kwargs_indices(format_string) == ({0, 2}, {'name', 'see'})
    >>> format_string = 'This is a format string with only automatic field specification: {}, {}, {} etc.'
    >>> assert args_and_kwargs_indices(format_string) == (set(), set())
    """
    if is_hybrid_format_string(format_string):
        raise no_hybrid_format_error
    d = {True: set(), False: set()}
    for x in format_params_in_str_format(format_string):
        if x is not None:
            d[isinstance(x, int)].add(x)
    args_keys, kwargs_keys = d[True], d[False]
    return args_keys, kwargs_keys


def empty_arg_and_kwargs_for_format(format_string, fill_val=None):
    format_params = format_params_in_str_format(format_string)
    if is_manual_format_params(format_params):
        args_keys, kwargs_keys = args_and_kwargs_indices(format_string)
        args = [fill_val] * (
            max(args_keys) + 1
        )  # max because e.g., sometimes, we have {0} and {2} without a {1}
        kwargs = {k: fill_val for k in kwargs_keys}
    elif is_automatic_format_params(format_params):
        args = [fill_val] * len(format_params)
        kwargs = {}
    else:
        raise no_hybrid_format_error
        # filled_format_string = mk_manual_spec_format_string(format_string, names=())

    return args, kwargs
