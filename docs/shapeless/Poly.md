# `Poly` Class Documentation

---

## Overview

The `Poly` class is a versatile utility class designed to provide dynamic type handling in Python. It empowers developers to determine, select, shift, validate, alias, annotate, extend, serialize, and deserialize types with ease. This class promotes flexibility and adaptability in handling data types in various scenarios.

## Introduction

Handling data of different types is a common task in Python development. The `Poly` class simplifies this process by offering a comprehensive set of methods for type management. Whether you need to check types, change types, or serialize and deserialize objects, the `Poly` class provides a robust solution.

## Class Definition

```python
class Poly(Generic[T]):
    def __init__(self, data: Any, verbose: bool = False)
    def determine(self) -> Type[T]
    def select(self, target: Type[T]) -> Type[T]
    def shift(self, target: Type[T]) -> T
    def validate(self, target: Type[T]) -> bool
    def add_alias(self, alias: str, target: Type[T])
    def annotate(self, annotation: Type[T])
    def extend(self, extension: Type[T])
    def serialize(self) -> bytes
    def deserialize(self, serialized_data: bytes) -> T
    def __instancecheck__(self, instance) -> bool
```

### Parameters:

- `data (Any)`: The data whose type is to be handled.

- `verbose (bool)`: If True, all operations will be logged. Default is False.

## Core Methods:

### `determine() -> Type[T]`

Determines the type of the data.

### `select(target: Type[T]) -> Type[T]`

Selects the type of the data based on the provided target.

### `shift(target: Type[T]) -> T`

Attempts to shift the data to the target type.

### `validate(target: Type[T]) -> bool`

Validates whether the data is of the target type.

### `add_alias(alias: str, target: Type[T])`

Adds an alias for a type.

### `annotate(annotation: Type[T])`

Annotates the data with a type.

### `extend(extension: Type[T])`

Extends the type of the data with a new type.

### `serialize() -> bytes`

Serializes the data.

### `deserialize(serialized_data: bytes) -> T`

Deserializes the data.

### `__instancecheck__(self, instance) -> bool`

Checks if an instance is of the selected type.

## Purpose and Usage

The `Poly` class is designed to simplify type handling tasks, especially when working with diverse data sources and formats. It offers the following use cases:

1. **Determine and Select Types**: Easily determine and select the type of your data using `determine()` and `select(target)` methods.

2. **Shift and Validate Types**: Shift the data to a new type using `shift(target)` and validate that the data is of the target type using `validate(target)`.

3. **Add Aliases**: Create aliases for types using `add_alias(alias, target)` to simplify type references.

4. **Annotate and Extend Types**: Annotate the data with a type using `annotate(annotation)` and extend the data type with a new type using `extend(extension)`.

5. **Serialize and Deserialize**: Serialize data with `serialize()` to save or send it and deserialize with `deserialize(serialized_data)` to restore the original data.

## Usage Examples:

Certainly! Here are 7 to 8 additional examples demonstrating various use cases of the `Poly` class:

**1. Alias Types:**

```python
from shapeless import Poly

# Create a Poly object with a float
poly = Poly(3.14)

# Add an alias for float type
poly.add_alias("floating_point", float)

# Determine the type using the alias
data_type = poly.select("floating_point")
print(data_type)  # Output: <class 'float'>
```

**2. Type Shifting with Validation:**

```python
from shapeless import Poly

# Create a Poly object with a string
poly = Poly("Hello")

# Shift data to int type
shifted_data = poly.shift(int)

# Attempt to validate if the data is of int type (will raise a TypeError)
try:
    poly.validate(int)
except TypeError as e:
    print(e)  # Output: "Hello is not of type <class 'int'>"
```

**3. Annotate and Extend Types:**

```python
from shapeless import Poly

# Create a Poly object with a list
poly = Poly([1, 2, 3])

# Annotate the data with a tuple type
poly.annotate(tuple)

# Determine the type with annotation
data_type = poly.determine()
print(data_type)  # Output: <class 'tuple'>

# Extend the type with a set type
poly.extend(set)

# Determine the extended type
data_type = poly.determine()
print(data_type)  # Output: <class 'set'>
```

**4. Serialization and Deserialization:**

```python
from shapeless import Poly

# Create a Poly object with a dictionary
poly = Poly({"key": "value"})

# Serialize data
serialized_data = poly.serialize()

# Deserialize data
deserialized_data = poly.deserialize(serialized_data)
print(deserialized_data)  # Output: {'key': 'value'}
```

**5. Using `Poly` as a Function Argument:**

```python
from shapeless import Poly

# Create a function that accepts a Poly argument
def my_func(a: Poly):
    print(type(a))

# Create a Poly object with a boolean
poly = Poly(True)

# Pass the Poly object to my_func
my_func(poly)  # Output: <class '__main__.Poly'>
```

**6. Nested Poly Objects:**

```python
from shapeless import Poly

# Create a nested Poly object
nested_poly = Poly(Poly(42))

# Determine the type of the nested Poly
nested_type = nested_poly.determine()
print(nested_type)  # Output: <class '__main__.Poly'>
```

**7. Using Multiple Alias Types:**

```python
from shapeless import Poly

# Create a Poly object with a float
poly = Poly(3.14)

# Add aliases for float and int types
poly.add_alias("floating_point", float)
poly.add_alias("integer", int)

# Determine the type using an alias
data_type = poly.select("integer")
print(data_type)  # Output: <class 'int'>
```

These examples showcase various scenarios in which the `Poly` class can be used, including aliasing types, type shifting with validation, annotating and extending types, serialization and deserialization, using `Poly` as a function argument, nesting `Poly` objects, and utilizing multiple alias types for dynamic type handling.

## Notes and Recommendations:

- Use the `Poly` class when you need to handle data of diverse types and want a convenient and consistent way to work with them.

- Leverage the logging feature by setting `verbose=True` during the `Poly` object creation for detailed information on operations.

- Take advantage of the `add_alias`, `annotate`, and `extend` methods to make type management more expressive and flexible.

## References:

1. [Python Type Checking (PEP 3107)](https://www.python.org/dev/peps/pep-3107/)
2. [Python Serialization (pickle)](https://docs.python.org/3/library/pickle.html)

## Additional Resources:

1. [Python Typing Documentation](https://docs.python.org/3/library/typing.html)
2. [Understanding Serialization in Python](https://realpython.com/python-serialization/)
3. [An Introduction to Python Type Annotations](https://realpython.com/python-type-checking/#introducing-python-type-checking)