# ba: Making Diagrams Easily

`ba` is a simple yet powerful library for creating and visualizing directed graphs. It provides a flexible mini-language for defining nodes, edges, and their attributes, making it easy to create complex diagrams with minimal code.

## Installation

```bash
pip install ba
```

Additionally, you'll need the GraphViz backend:

- **Mac**: `brew install graphviz`
- **Linux**: `sudo apt-get install graphviz`
- **Windows**: Download from the [GraphViz website](https://graphviz.org/download/)

## Quick Start

```python
from ba import dgdisp

# Create a simple workflow diagram
diagram = dgdisp("""
    input -> [process] -> (output)
    [process] -> /log/
""")

# Display the diagram
diagram
```

## Features

- **Simple syntax** for defining multiple edges at once
- **Inline node formatting** with shape mini-language
- **Bulk specification** of node properties
- **Support for different graphviz engines**

## Mini-language Syntax

### Edge Paths
```
node1 -> node2 -> node3
```

### Many-to-many Connections
```
node1, node2 -> node3, node4, node5
```

### Inline Node Formatting
```
[square_node] -> (circular_node) -> /parallelogram/
```

Common shape markers:
- `[name]` - box
- `(name)` - circle
- `/name/` - parallelogram
- `<name>` - diamond
- `[[name]]` - 3D box
- `((name))` - double circle

### Node Attributes
```
node1, node2: circle
special_node: {"shape": "box", "color": "red", "style": "filled"}
```

### Raw GraphViz Statements
```
node1 [shape=box style=filled fillcolor=lightblue]
```

### Default Settings
```
--dflt_node_attr: shape
--fillcolor: lightgrey
```

## Examples

### Basic Workflow

```python
dgdisp("""
    key, wf: circle
    chk: doublecircle
    fv: {"shape": "plaintext", "fontcolor": "blue"}
    key -> wf -> [chunker] -> chk -> /featurizer/ -> fv
    fv -> ([model])
""")
```

### Horizontal Layout

```python
from ba import dgdisp

# Use the horizontal layout helper
dgdisp.h("""
    A -> B -> C
    B -> D -> E
""")
```

### Choosing Different Engines

```python
dgdisp("""
    A -> B -> C -> A
    B -> D -> E -> B
""", engine=dgdisp.engines.circo)
```

## API Reference

### Main Functions

- **`dgdisp(commands, node_shapes=None, attrs_for_node=None, minilang=ModifiedDot, engine=None, **kwargs)`**  
  Create a directed graph visualization using the mini-language.

- **`horizontal_dgdisp(*args, **kwargs)`** or **`dgdisp.h(*args, **kwargs)`**  
  Create a horizontally oriented directed graph.

## Available Engines

- `dot` - Hierarchical layout (default)
- `neato` - Spring model layout
- `fdp` - Force-directed placement
- `sfdp` - Scalable force-directed placement
- `twopi` - Radial layout
- `circo` - Circular layout

Access via `dgdisp.engines.dot`, `dgdisp.engines.neato`, etc.

## License

MIT
