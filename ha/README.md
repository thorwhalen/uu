<img width="350" alt="image" src="https://github.com/thorwhalen/uu/assets/1906276/9bbcee19-c28e-44d8-8769-b04fbd98efcf">

# ha

A medley of joke datasets and tools.

To install:	```pip install ha```

# Examples

## Joke datasets

List the datasets (keys):

```python
import ha
list(ha.joke_datasets)
# ['reddit_jokes', 'stupidstuff', 'wocka']
```


Get a dataset. The datasets are lists of dicts. 

```python
reddit_jokes = ha.joke_datasets['reddit_jokes']
reddit_jokes[1000:1003]
```

    [{'body': 'Why did the chicken cross the road? ...',
    'id': '5tdwk4',
    'score': 1,
    'title': 'Why did the chicken cross the road?'},
    {'body': 'A little boy goes to his dad and asks, ..."',
    'id': '5tdssi',
    'score': 123,
    'title': 'What is Politics?'},
    {'body': 'A teacher asked her 4th grade students a ...',
    'id': '5tdsmb',
    'score': 40,
    'title': 'A teacher asked her students...'}]

The values of the `joke_datasets` mapping are lists of dicts containing the joke 
data. For example, to list the datasets and their sizes, you'd do:

```python
print({k: len(v) for k, v in ha.joke_datasets.items()})
# {'reddit_jokes': 194553, 'stupidstuff': 3773, 'wocka': 10019}
```

Get an aggregate of all the datasets.

```python
len(jokes)
```

    208345


The keys of the aggregate come as `(dataset_name, id)` pairs. 
Let's look at the first two and the first last keys.

```python
print(list(jokes)[:2])
print(list(jokes)[-2:])
```

    [('reddit_jokes', '5tz52q'), ('reddit_jokes', '5tz4dd')]
    [('wocka', 18199), ('wocka', 18200)]


Get a joke (data) by using it's key:

```python
jokes['wocka', 18199]
```


## Joke (vendorized) tools

### pyjokes

Install: `pip install ha[pyjokes]` (or independently, doing `pip install pyjokes`).

```python
from ha.pyjokes import get_joke
get_joke()  # gets a random joke, with default characteristics
```

"Two bytes meet. The first byte asks, 'Are you ill?' The second byte replies, 'No, just feeling a bit off.'"


### laugh


```python
import laugh
thor_joke = laugh.NamedJokes(name='Thor')
thor_joke()  # random joke
```

    'The stock market monitors Thor.'


```python
thor_joke('god')  # random joke containing the word "god" (or None if none found)
```

    'The guy that God prays to goes to Thor for forgiveness!'



