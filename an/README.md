
# an
Scraping and parsing amazon


To install:	```pip install an```


# Amazon Scraping Library

## Overview
This Python library is designed for scraping and parsing data from Amazon product pages. It offers functionalities to extract various information like sales ranks, product reviews, and product titles from Amazon's different regional websites.

## Installation
This library is not a standalone package and should be incorporated directly into your existing Python project. Copy the code into your project's directory.

## Dependencies
- pandas
- numpy
- requests
- BeautifulSoup
- pymongo
- matplotlib

Ensure these dependencies are installed in your environment.


## Usage

### Extracting Sales Rank
The library can extract sales ranks of products from Amazon. Here's an example of how to get the sales rank of a product:

```python
asin = 'YOUR_PRODUCT_ASIN'
country = 'co.uk'  # Change to desired Amazon region
sales_rank = Amazon.get_sales_rank(asin=asin, country=country)
print(sales_rank)
```

### Parsing Product Title

To parse and get the product title from an Amazon product page:

```python
html_content = Amazon.slurp(what='product_page', asin=asin, country=country)
title = Amazon.parse_product_title(html_content)
print(title)
```

### Getting Number of Reviews
To retrieve the number of customer reviews for a product:

```python
number_of_reviews = Amazon.get_number_of_reviews(asin=asin, country=country)
print(number_of_reviews)
```

## Contributing
Contributions to this library are welcome. Please send pull requests with improvements or bug fixes.

