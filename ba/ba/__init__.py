"""
Making diagrams easily.

`ba` is a simple yet powerful library for creating and visualizing directed graphs.
It provides a flexible mini-language for defining nodes, edges, and their attributes,
making it easy to create complex diagrams with minimal code.

Key features:
- Simple syntax for defining multiple edges at once
- Inline node formatting with shape mini-language
- Bulk specification of node properties
- Support for different graphviz engines

Dependencies:
- graphviz (pip install graphviz)
- graphviz binary installation:
  - Mac: brew install graphviz
  - Linux: sudo apt-get install graphviz
  - Windows: google it
"""

import re
from typing import Optional
import json
from collections import defaultdict
from functools import wraps
from graphviz import Digraph, Source

from types import MethodType

# Note: Not used anywhere in the module anymore, but was
"""Get a `re.Pattern` instance (as given by re.compile()) with control over defaults of it's methods.
Useful to reduce if/else boilerplate when handling the output of search functions (match, search, etc.)

See [regex_search_hack.md](https://gist.github.com/thorwhalen/6c913e9be35873cea6efaf6b962fde07) for more explanatoins of the 
use case.

Example;
>>> dflt_result = type('dflt_search_result', (), {'groupdict': lambda x: {}})()
>>> p = re_compile('.*(?P<president>obama|bush|clinton)', search=dflt_result, match=dflt_result)
>>>
>>> p.search('I am beating around the bush, am I?').groupdict().get('president', 'Not found')
'bush'
>>>
>>> # if not match is found, will return 'Not found', as requested
>>> p.search('This does not contain a president').groupdict().get('president', 'Not found')
'Not found'
>>>
>>> # see that other non-wrapped re.Pattern methods still work
>>> p.findall('I am beating arcached_keysound the bush, am I?')
['bush']
"""

import re
from functools import wraps


def add_dflt(func, dflt_if_none):
    """
    Add a default return value to a function when it returns None.

    Args:
        func: The function to wrap
        dflt_if_none: Default value to return when func returns None

    Returns:
        A wrapped function that returns dflt_if_none when func returns None
    """

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is not None:
            return result
        else:
            return dflt_if_none

    return wrapped_func


def re_compile(pattern, flags=0, **dflt_if_none):
    """Get a `re.Pattern` instance (as given by re.compile()) with control over defaults of it's methods.
    Useful to reduce if/else boilerplate when handling the output of search functions (match, search, etc.)

    Args:
        pattern: Regular expression pattern string
        flags: Regular expression flags
        **dflt_if_none: Default values to return when regex methods return None

    Returns:
        Enhanced regex pattern object with default handling

    Example;
    >>> dflt_result = type('dflt_search_result', (), {'groupdict': lambda x: {}})()
    >>> p = re_compile('.*(?P<president>obama|bush|clinton)', search=dflt_result, match=dflt_result)
    >>>
    >>> p.search('I am beating around the bush, am I?').groupdict().get('president', 'Not found')
    'bush'
    >>> p.match('I am beating around the bush, am I?').groupdict().get('president', 'Not found')
    'bush'
    >>>
    >>> # if not match is found, will return 'Not found', as requested
    >>> p.search('This does not contain a president').groupdict().get('president', 'Not found')
    'Not found'
    >>>
    >>> # see that other non-wrapped re.Pattern methods still work
    >>> p.findall('I am beating around the bush, am I?')
    ['bush']
    """
    compiled_regex = re.compile(pattern, flags=flags)
    intercepted_names = set(dflt_if_none)

    my_regex_compilation = type('MyRegexCompilation', (object,), {})()

    for _name, _dflt in dflt_if_none.items():
        setattr(
            my_regex_compilation, _name, add_dflt(getattr(compiled_regex, _name), _dflt)
        )
    for _name in filter(
        lambda x: not x.startswith('__') and x not in intercepted_names,
        dir(compiled_regex),
    ):
        setattr(my_regex_compilation, _name, getattr(compiled_regex, _name))

    return my_regex_compilation


class rx:
    name = re.compile('^:(\w+)')
    lines = re.compile('\n|\r|\n\r|\r\n')
    comments = re.compile('#.+$')
    non_space = re.compile('\S')
    nout_nin = re.compile(r'(\w+)\W+(\w+)')
    arrow = re.compile(r'\s*->\s*')
    instruction = re.compile(r'(\w+):\s+(.+)')
    node_def = re.compile(r'([\w\s,]+):\s+(.+)')
    wsc = re.compile(r'[\w\s,]+')
    csv = re.compile(r'[\s,]+')
    pref_name_suff = re.compile(r'(\W*)(\w+)(\W*)')


class DDigraph(Digraph):
    @wraps(Digraph.__init__)
    def __init__(self, *args, **kwargs):
        if args:
            first_arg = args[0]
            if first_arg.startswith(':'):
                lines = rx.lines.split(first_arg)
                first_line = lines[0]
                name = rx.name.search(first_line).group(1)


class ModifiedDot:
    class rx:
        lines = re.compile('\n|\r|\n\r|\r\n')
        comments = re.compile('#.+$')
        non_space = re.compile('\S')
        nout_nin = re.compile(r'(\w+)\W+(\w+)')
        arrow = re.compile(r'\s*->\s*')
        instruction = re.compile(r'(\w+):\s+(.+)')
        node_def = re.compile(r'([\w\s,]+):\s+(.+)')
        wsc = re.compile(r'[\w\s,]+')
        csv = re.compile(r'[\s,]+')
        pref_name_suff = re.compile(r'(\W*)(\w+)(\W*)')

    @staticmethod
    def loose_edges(s):
        return list(
            map(
                lambda x: x.groups(),
                filter(
                    None,
                    map(ModifiedDot.rx.nout_nin.search, ModifiedDot.rx.lines.split(s)),
                ),
            )
        )

    # https://www.graphviz.org/doc/info/shapes.html#polygon
    shape_for_chars = {
        ('[', ']'): 'box',
        ('(', ')'): 'circle',
        (']', '['): 'square',
        ('/', '/'): 'parallelogram',
        ('<', '>'): 'diamond',
        ('([', '])'): 'cylinder',
        ('[[', ']]'): 'box3d',
        ('((', '))'): 'doublecircle',
        ('/', '\\'): 'triangle',
        ('\\', '/'): 'invtriangle',
        ('|/', '\\|'): 'house',
        ('|\\', '/|'): 'invhouse',
        ('/-', '-\\'): 'trapezium',
        ('-\\', '-/'): 'invtrapezium',
    }

    @staticmethod
    def _modified_dot_gen(s, dflt_node_attr='shape', **dflt_specs):
        csv_items = lambda x: ModifiedDot.rx.csv.split(x.strip())
        pipeline_items = lambda s: list(map(csv_items, s))
        for line in ModifiedDot.rx.lines.split(s):
            line = ModifiedDot.rx.comments.sub('', line)
            statements = ModifiedDot.rx.arrow.split(line)
            if len(statements) > 1:
                pipeline = pipeline_items(statements)
                for nouts, nins in zip(pipeline[:-1], pipeline[1:]):
                    for nout in nouts:
                        for nin in nins:
                            yield 'edge', nout, nin
            else:
                statement = statements[0].strip()
                if ':' in statement:
                    if statement.startswith(
                        '--'
                    ):  # it's a special instruction (typically, overriding a default)
                        statement = statement[2:]
                        instruction, specs = ModifiedDot.rx.node_def.search(statement)
                        if instruction == 'dflt_node_attr':
                            dflt_node_attr = specs.strip()
                        else:
                            dflt_specs[instruction] = specs.strip()
                    else:  # it's a node definition (or just some stuff to ignore)
                        if statement.startswith('#'):
                            continue  # ignore, it's just a comment
                        g = ModifiedDot.rx.node_def.search(statement)
                        if g is None:
                            continue
                        nodes, specs = g.groups()
                        nodes = csv_items(nodes)
                        if specs.startswith('{'):
                            specs = json.loads(specs)
                        else:
                            specs = {dflt_node_attr: specs}
                        for node in nodes:
                            assert isinstance(
                                specs, dict
                            ), f'specs for {node} be a dict at this point: {specs}'
                            yield 'node', node, dict(dflt_specs, **specs)
                elif ModifiedDot.rx.non_space.search(statement):
                    yield 'source', statement, None

    @staticmethod
    def parser(s, **dflt_specs):
        return list(ModifiedDot._modified_dot_gen(s, **dflt_specs))

    @staticmethod
    def interpreter(commands, node_shapes, attrs_for_node, engine, **digraph_kwargs):
        _edges = list()
        _nodes = defaultdict(dict)
        _sources = list()
        for kind, arg1, arg2 in commands:
            if kind == 'edge':
                from_node, to_node = arg1, arg2
                _edge = list()
                for node in (from_node, to_node):
                    pref, name, suff = ModifiedDot.rx.pref_name_suff.search(
                        node
                    ).groups()
                    if (
                        pref,
                        suff,
                    ) in node_shapes and name not in _nodes:  # implies that only first formatting (existence of pref and suff) counts
                        _nodes[name].update(shape=node_shapes[(pref, suff)])
                        _edge.append(name)
                    else:
                        _edge.append(name)

                _edges.append(_edge)
            elif kind == 'node':
                node, specs = arg1, arg2
                _nodes[node].update(**arg2)
            elif kind == 'source':
                _sources.append(arg1)

        digraph_kwargs['body'] = digraph_kwargs.get('body', []) + _sources
        d = Digraph(engine=engine, **digraph_kwargs)

        d.edges(_edges)
        for node, attrs in attrs_for_node.items():
            d.node(name=node, **attrs)
        for node, attrs in _nodes.items():
            d.node(name=node, **attrs)

        return d


def dgdisp(
    commands,
    node_shapes: Optional[dict] = None,
    attrs_for_node=None,
    minilang=ModifiedDot,
    engine=None,
    **digraph_kwargs,
):
    """
    Create a directed graph visualization using a flexible mini-language.
    
    This is the main interface function of the ba library. It converts text-based diagram
    specifications into graphviz Digraph objects that can be displayed or saved.
    
    Quick links:
    - attributes: https://www.graphviz.org/doc/info/attrs.html
    - shapes: https://www.graphviz.org/doc/info/shapes.html#polygon

    The mini-language (`ModifiedDot` by default) supports:
    
    1. Edge paths: Specify multiple edges in sequence
       `node1 -> node2 -> node3`
       
    2. Bulk connections: Create many-to-many connections with a single line
       `node1, node2 -> node3, node4` creates all possible edges between groups
       
    3. Node shape shorthand: Format nodes inline using special characters
       `[node]` for box, `(node)` for circle, etc.
       
    4. Bulk node attributes: Apply attributes to multiple nodes at once
       `node1, node2: circle` or `node3: {"shape": "box", "color": "red"}`
       
    5. Default overrides: Modify default settings within the diagram
       `--dflt_node_attr: shape` or `--fillcolor: red`
       
    6. Comments: Use # for comments
       `# This is a comment`

    Args:
        commands: String with diagram specifications or parsed commands
        node_shapes: Dict mapping character tuples to shape names, overriding defaults
        attrs_for_node: Dict mapping node names to attribute dicts
        minilang: Language processor object with parser and interpreter methods
        engine: Graphviz layout engine name ('dot', 'neato', 'fdp', etc.)
        **digraph_kwargs: Additional arguments passed to graphviz.Digraph

    Returns:
        graphviz.Digraph: A Digraph object that can be displayed or saved

    Examples:
        Basic usage with node formatting and edge paths:
        >>> dgdisp('''
        ...     key, wf: circle
        ...     chk: doublecircle
        ...     fv: {"shape": "plaintext", "fontcolor": "blue"}
        ...     key -> wf tag
        ...     wf -> [chunker] -> chk -> /featurizer/ -> fv
        ...     fv tag -> ([model])
        ... ''')
        
        More complex example with custom attributes:
        >>> d = dgdisp('''
        ...     group_tags, orig_tags -> [mapping] -> tags
        ...     predicted_tags, \\tags/ -> /confusion_matrix/
        ...     predict_proba, tag_list -> [[predict]] -> /predicted_tags\\
        ...     group_tags: {"fillcolor": "red", "fontcolor": "red"}
        ...     orig_tags [fontsize=30 fontcolor=blue]
        ... ''', format='svg')
        >>> d.render('diagram')  # Saves to diagram.svg
    """
    attrs_for_node = attrs_for_node or {}
    if node_shapes is False:
        node_shapes = {}
    else:
        if node_shapes is True:
            node_shapes = {}
        node_shapes = dict(minilang.shape_for_chars, **(node_shapes or {}))
    if isinstance(commands, str):
        commands = minilang.parser(commands)

    d = minilang.interpreter(
        commands, node_shapes, attrs_for_node, engine=engine, **digraph_kwargs
    )

    return d


dgdisp.shape_for_chars = ModifiedDot.shape_for_chars


@wraps(dgdisp)
def horizontal_dgdisp(*args, **kwargs):
    """
    Create a horizontally oriented directed graph visualization.

    This is a convenience wrapper around dgdisp that creates graphs with
    left-to-right layout instead of the default top-to-bottom layout.

    Args:
        *args: Positional arguments passed to dgdisp
        **kwargs: Keyword arguments passed to dgdisp

    Returns:
        graphviz.Digraph: A horizontally oriented Digraph object

    Examples:
        >>> horizontal_dgdisp('''
        ...     A -> B -> C
        ...     B -> D
        ... ''')
    """
    command, *_args = args
    return dgdisp('rankdir="LR"\n' + command, *_args, **kwargs)


dgdisp.h = horizontal_dgdisp


class Struct:
    def __init__(self, **kwargs):
        for attr, val in kwargs.items():
            setattr(self, attr, val)


dgdisp.engines = Struct(
    **{x: x for x in ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']}
)

dagdisp = dgdisp
