# eu

It's good practice to write code that can be run as is on someone else's computer (or server).

To install:	```pip install eu```

## Description

The `eu` package provides a practical example of how to dynamically determine and use absolute file paths in a Python script, which is crucial for ensuring that the code is portable and can run on different machines without modification. This approach avoids the pitfalls of hard-coded absolute paths, which can lead to errors when the code is run in different environments.

The main functionality demonstrated in the `__init__.py` file includes:
- Determining the absolute path of the current file (`__file__`).
- Finding the directory containing the current file using `os.path.dirname`.
- Constructing an absolute path from a relative path, ensuring that file references remain valid regardless of the current working directory.

This functionality is essential for applications that need to access files relative to the script's location, such as configuration files, data files, or other resources.

## Usage

### Determining File Paths

To use the functionality provided by the `eu` package, you can follow these steps:

1. Ensure that the file you want to reference is in the same directory as your script or specify the correct relative path.
2. Import the package to automatically execute the code that determines the paths.

Example:
```python
import eu  # This will execute the path setup code in __init__.py

# Now you can safely use `eu.absolute_path_from_relative_path` to access files
with open(eu.absolute_path_from_relative_path, 'r') as file:
    content = file.read()
    print(content)
```

This example assumes that there is a file named `hello_relative_world.txt` in the same directory as your script. The script reads the content of this file and prints it.

### Checking Current and Script Directories

The package also prints out the current working directory and the directory containing the script. This can be useful for debugging or when you need to understand where your Python environment is operating.

## Documentation

- `current_file_absolute_path`: A string containing the absolute path to the current Python file (`__file__`).
- `containing_folder`: A string containing the absolute path to the directory that contains the current Python file.
- `relative_path`: A string specifying a relative path to a file from the script's directory.
- `absolute_path_from_relative_path`: A string containing the absolute path constructed from the `containing_folder` and `relative_path`.

These variables are set up when the package is imported and are available for use in your scripts to handle file paths dynamically.
