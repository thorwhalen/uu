# AW: ML Model Serialization Utilities

A Python library for managing, serializing, and deserializing machine learning models and their attributes.

## Features

- Extract model attributes and parameters into serializable dictionaries
- Convert ML models to JSON-friendly formats
- Save and load model parameters to/from JSON
- Handle NumPy arrays, SciPy sparse matrices and other complex data types
- Create transformers from non-transformer objects

## Main Functions

### Model Attribute Management

- `trailing_underscore_attributes_with_include_and_exclude(obj, include=(), exclude=())`: Get attributes with trailing underscore, with custom inclusion/exclusion
- `get_model_attributes(model, include=(), exclude=(), model_name_as_dict_root=True, as_is_types=default_as_is_types)`: Export model parameters to a dict

### Serialization

- `get_model_attributes_dict_for_json(model, include=(), exclude=(), model_name_as_dict_root=True, as_is_types=default_as_is_types)`: Get model attributes as a JSON-compatible dictionary
- `export_model_params_to_json(model, include=(), exclude=(), model_name_as_dict_root=True, as_is_types=default_as_is_types, filepath='', version=None, include_date=False, indent=None)`: Export model parameters to JSON file or string
- `import_model_from_spec(spec, objects={}.copy(), type_conversions=(), field_conversions={}.copy(), force_dict_wrap=False)`: Reconstruct a model from specification dictionary

### JSON Support

- `json_friendly_dict(obj)`: Convert Python objects to JSON-serializable format
- `NumpyAwareJSONEncoder`: JSON encoder that handles NumPy arrays and other special types

### Transformers

- `ExtrapolateTransformation(transformer, extrapolator=LinearRegression())`: Wrap a transformer to provide transform method using a regression model

## Usage Example

```python
from sklearn.cluster import KMeans
import numpy as np
from aw import export_model_params_to_json, import_model_from_spec
import json

# Create a model
kmeans = KMeans(n_clusters=3)
kmeans.fit(np.random.rand(100, 5))

# Export model parameters to JSON
json_str = export_model_params_to_json(kmeans)

# Load the JSON string
model_spec = json.loads(json_str)

# Recreate the model from spec
reconstructed_model = import_model_from_spec(model_spec, objects={'KMeans': KMeans})
```

## Requirements

- NumPy
- SciPy
- scikit-learn
- dill

## License

[License information goes here]
