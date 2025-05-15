# if
Beautiful Soup

To install:	```pip install if```

## Overview
The 'if' package provides a Python interface for parsing HTML and XML documents into a tree structure, making it easy to navigate, search, and modify the tree. It is built on top of the `BeautifulSoup` library and includes several classes that extend its functionality to handle different parsing strategies and document types.

## Features
- Parses both valid and invalid XML/HTML documents.
- Converts documents to a tree structure, allowing easy navigation and modification.
- Handles a variety of encodings and can automatically detect and convert character encodings.
- Supports both XML and HTML parsing strategies through different classes.
- Provides methods for searching and navigating parsed documents.
- Can handle documents with mixed content, such as tags within comments or CDATA sections.

## Installation
To install the package, use the following pip command:
```bash
pip install if
```

## Usage

### Basic Parsing
To parse a document and create a BeautifulSoup object:
```python
from if import BeautifulSoup

# Example HTML content
html_doc = "<html><head><title>The Dormouse's story</title></head>"
html_doc += "<body><p class='title'><b>The Dormouse's story</b></p>"

# Create a BeautifulSoup object
soup = BeautifulSoup(html_doc)

# Access the title tag
print(soup.title)
# Output: <title>The Dormouse's story</title>

# Find a tag by class
print(soup.find_all('p', class_='title'))
# Output: [<p class='title'><b>The Dormouse's story</b></p>]
```

### Navigating the Tree
You can navigate the parse tree using tag names or find methods:
```python
# Access the body tag
print(soup.body.b)
# Output: <b>The Dormouse's story</b>

# Using find method
print(soup.find('b'))
# Output: <b>The Dormouse's story</b>
```

### Modifying the Tree
You can easily modify the tree structure:
```python
tag = soup.b
tag.name = "strong"  # Change the tag name from 'b' to 'strong'
print(soup)
# Output: <html><head><title>The Dormouse's story</title></head>
# <body><p class='title'><strong>The Dormouse's story</strong></p>
```

### Encoding
The package can detect and handle various encodings, ensuring that you always work with Unicode internally:
```python
# Assuming 'html_doc' is a byte string in a specific encoding
soup = BeautifulSoup(html_doc)
print(soup.originalEncoding)  # Prints the detected encoding
```

## Documentation
For more detailed documentation, visit the official Beautiful Soup documentation at [Beautiful Soup Documentation](http://www.crummy.com/software/BeautifulSoup/documentation.html).

## License
This project is licensed under the New-style BSD license. See the source files for more license information.