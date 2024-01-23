# rv

Utils to work with randomness

To install:	```pip install rv```


# Examples

## random_word

Make a random word by concatenating randomly drawn elements from alphabet together

    >>> t = random_word(4, 'abcde');  # e.g. 'acae'
    >>> t = random_word(5, ['a', 'b', 'c']);  # e.g. 'cabba'
    >>> t = random_word(4, [[1, 2, 3], [40, 50], [600], [7000]]);  # e.g. [40, 50, 7000, 7000, 1, 2, 3]
    >>> t = random_word(4, [1, 2, 3, 4]);  # e.g. 13 (because adding numbers...)
    >>> # ... sometimes it's what you want:
    >>> t = random_word(4, [2 ** x for x in range(8)]);  # e.g. 105 (binary combination)
    >>> t = random_word(4, [1, 2, 3, 4], concat_func=lambda x, y: str(x) + str(y));  # e.g. '4213'
    >>> t = random_word(4, [1, 2, 3, 4], concat_func=lambda x, y: int(str(x) + str(y)));  # e.g. 3432


## random_romatted_str_gen

Random formatted string generator

The following will be made not random (by restricting the constraints to "no choice". This is so that we get consistent outputs to assert for the doc test.

    >>> list(random_formatted_str_gen('root/{}/{}_{}.test', (2, 5), 'abc', n=5))
    [('root/acba/bb_abc.test',),
        ('root/abcb/cbbc_ca.test',),
        ('root/ac/ac_cc.test',),
        ('root/aacc/ccbb_ab.test',),
        ('root/aab/abb_cbab.test',)]

Example with automatic specification: 

    >>> list(random_formatted_str_gen('root/{}/{}_{}.test', (3, 4), 'a', n=2))
    [('root/aaa/aaa_aaa.test',), ('root/aaa/aaa_aaa.test',)]

Example with manual specification

    >>> list(random_formatted_str_gen('indexed field: {0}: named field: {name}', (2, 3), 'z', n=1))
    [('indexed field: zz: named field: zz',)]


## Utils

Get the "parameter" indices/names of the format_string

    >>> from rv import format_params_in_str_format
    >>> format_string = '{0} (no 1) {2}, and {0} is a duplicate, {} is unnamed and {name} is string-named'
    >>> format_params_in_str_format(format_string)
    [0, 2, 0, None, 'name']



