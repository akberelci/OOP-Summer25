# Naming Conventions

# Variable and function names should be written in lowercase, with words separated by underscores.
# Class names should be in CamelCase.
# Constants should be written in uppercase.

# Wrong Example:
class myclass:  # wrong
    def MyFunction(self):  # wrong
        MYVARIABLE = 10  # wrong

# Correct Example:
class MyClass:  # correct
    def my_function(self):  # correct
        my_variable = 10  # correct


# Indentation

# Use 4 spaces per indentation level. Do not mix tabs and spaces.

# Wrong Example:
def example_function():
	if True:  # wrong (mixing tabs and spaces)
        print("Hello, World!")

# Correct Example:
def example_function():
    if True:  # correct (using spaces for indentation)
        print("Hello, World!")


# Line Length

# Limit all lines to a maximum of 79 characters.

# Wrong Example:
long_string = "This is a very long string that exceeds the 79 character limit in a single line."  # wrong

# Correct Example:
long_string = (
    "This is a very long string that is properly broken into multiple lines "
    "so that it does not exceed the 79 character limit."
)  # correct


# Docstrings

# Always use docstrings for all public classes and methods. This explains what the function does.

# Wrong Example:
def add(a, b):  # wrong (missing docstring)
    return a + b

# Correct Example:
def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int): First number.
    b (int): Second number.

    Returns:
    int: The sum of a and b.
    """
    return a + b  # correct


# Imports

# Imports should be on separate lines and in the following order:
# - Standard library imports.
# - Related third-party imports.
# - Local application imports.

# Wrong Example:
import sys, os  # wrong (imports should be on separate lines)

# Correct Example:
import sys  # correct
import os   # correct
