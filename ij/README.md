# ij

Text feature extraction

To install:	```pip install ij```


# Examples

## TreeTokenizer

A tokenizer that is the result of multiple different tokenizers that might either all be applied to the
same text, or are used recursively to break up the text into finner pieces.
In a deep_tokenizer tokenizers[0] tokenizes the text, then the next tokenizer, tokeizers[1] is applied to these
tokens, and so forth. By default, the union of the tokens are returned. If token_prefixes is specified (usually,
a different one for each tokenizer), they are prepended to the tokens to distinguish what level of tokenization
they come from.

If text_collection is specified, along with max_df and/or min_df, the text_collection will serve to learn a
vocabulary for each tokenizer by collecting only those tokens whose frequency is at least min_df and no more than
max_df.

Params:
    * tokenizers: A list of tokenizers (function taking text and outputing a list of strings
    * token_prefixes: A list of prefixes to add in front of the tokens matched for each tokenizer
    (or a single string that will be used for all tokenizers
    * max_df and min_df: Only relevant when leaning text_collection is specified.
    These are respectively the max and min frequency that tokens should have to be included.
    The frequency can be expressed as a count, or a ratio of the total count.
    Note that in the case of max_df, it will always be relative to the total count of tokens at the current level.
    * return_tokenizer_info: Boolean (default False) indicating whether to return the tokenizer_info_list as well

Fit input X is a collection of the text to learn the vocabulary with


```python
>>> from ij import TreeTokenizer
>>> import re
>>>
>>> t = [re.compile('[\w-]+').findall, re.compile('\w+').findall]
>>> p = ['level_1=', 'level_2=']
>>> ttok = TreeTokenizer(tokenizers=t, token_prefixes=p)
>>> ttok.tokenize('A-B C B')
['level_1=A-B', 'level_1=C', 'level_1=B', 'level_2=A', 'level_2=B', 'level_2=C', 'level_2=B']
>>> s = ['A-B-C A-B A B', 'A-B C B']
>>> ttok = TreeTokenizer(tokenizers=t, token_prefixes=p, min_df=2)
>>> _ = ttok.fit(text_collection=s)
>>> ttok.transform(['A-B C B']).tolist()
[['level_1=A-B', 'level_1=B', 'level_2=C']]
```
