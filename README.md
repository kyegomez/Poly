[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)

# Poly
A simple Fluid, PolyMorphic,and shapeless package that activates radically flexiblity and simplicity in your programs

-----

## Installation

You can install the package using pip

```bash
pip install shapeless
```
----

# Usage

Here's a simple example of how to use the `Poly` class:

```python
from shapeless import Poly

# Create a Poly object with an integer
p = Poly(10)

# Determine the type of the data
print(p.determine())  # <class 'int'>

# Shift the data to a string
print(p.shift(str))  # '10'

# Validate that the data is a string
print(p.validate(str))  # True
```

You can also use `Poly` as a type hint in your functions:

```python
from shapeless import Poly

def my_func(a: Poly):
    print(type(a))

# Create a Poly object with a string
p = Poly('10')

# Pass the Poly object to my_func
my_func(p)  # <class '__main__.Poly'>
```
------

# Documentation

The `Poly` class is a utility class tailored towards dynamic type handling in Python. It provides functionalities that allow developers to determine, select, shift, validate, alias, annotate, extend, serialize, and deserialize types, making it a versatile tool in many programming scenarios. The class also focuses on thread safety and comes with an optional logging mechanism.

## Class Definition:

```python
class Poly(Generic[T]):
    """
    The Poly class is a utility class that provides dynamic type handling.
    It allows users to determine, select, shift, validate, alias, annotate, extend, serialize, and deserialize types.
    It also provides thread safety and optional logging.

    Parameters:
    - data (Any): The data whose type is to be managed.
    - verbose (bool, optional): If True, operations will be logged. Default is False.
    """
```

### Initialization:

```python
def __init__(self, data: Any, verbose: bool = False):
    """
    Initialize a new Poly object.

    Parameters:
    - data (Any): The data whose type is to be handled.
    - verbose (bool, optional): If True, log all operations. Default is False.
    """
```

### Methods:

#### determine:

```python
def determine(self):
    """
    Determine the type of the data.

    Returns:
    - Type of the data.
    """
```

#### select:

```python
def select(self, target):
    """
    Select the type of the data.

    Parameters:
    - target: The target type to select.

    Returns:
    - The selected type.
    """
```

#### shift:

```python
def shift(self, target):
    """
    Attempt to shift the data to the target type.

    Parameters:
    - target: The target type to shift to.

    Returns:
    - The data shifted to the target type.

    Raises:
    - TypeError: If the data cannot be shifted to the target type.
    """
```

#### validate:

```python
def validate(self, target):
    """
    Validate that the data is of the target type.

    Parameters:
    - target: The target type to validate against.

    Returns:
    - True if data is of target type, otherwise False.

    Raises:
    - TypeError: If the data is not of the target type.
    """
```

#### add_alias:

```python
def add_alias(self, alias, target):
    """
    Add an alias for a type.

    Parameters:
    - alias: The alias name.
    - target: The target type.
    """
```

#### annotate:

```python
def annotate(self, annotation):
    """
    Annotate the data with a type.

    Parameters:
    - annotation: The type annotation.
    """
```

#### extend:

```python
def extend(self, extension):
    """
    Extend the type of the data with a new type.

    Parameters:
    - extension: The new type to extend with.
    """
```

#### serialize:

```python
def serialize(self):
    """
    Serialize the data.

    Returns:
    - The serialized data in byte format.
    """
```

#### deserialize:

```python
def deserialize(self, serialized_data):
    """
    Deserialize the data.

    Parameters:
    - serialized_data: The data in serialized format.

    Returns:
    - The deserialized data.
    """
```

#### __instancecheck__:

```python
def __instancecheck__(self, instance):
    """
    Check if an instance is of the selected type.

    Parameters:
    - instance: The instance to check.

    Returns:
    - True if the instance is of the selected type, False otherwise.
    """
```

## Usage Examples:

### Example 1: Basic Type Handling
```python
from shapeless import Poly

p = Poly(42)
print(p.determine())  # <class 'int'>
```

### Example 2: Shifting and Validation
```python
from shapeless import Poly

p = Poly("123")
p.shift(int)         # Transforms "123" to 123
p.validate(int)      # Validates data is of type 'int'
```

### Example 3: Aliasing and Serialization
```python
from shapeless import Poly

p = Poly(42)
p.add_alias("Integer", int)
serialized_data = p.serialize()
print(serialized_data)  # b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00K*.'

deserialized_data = p.deserialize(serialized_data)
print(deserialized_data)  # 42
```

## Mathematical Formula:

The `Poly` class does not have an inherent mathematical formula as its operations are based on dynamic type handling in a programming context. Instead, it can be thought of as a utility that operates on the set of Python types, with various operations (determination, selection, shifting, etc.) acting as transformations within this set.

## Additional Information:

- **Thread Safety**: All operations on the `Poly` class are thread-safe, ensuring data consistency and integrity in multi-threaded environments.
  
- **Logging**: The `Poly` class has a verbose mode that can be activated upon initialization. This mode logs all operations, which can be helpful for debugging or understanding the sequence of operations applied to the data.

## References:

For more information on Python's dynamic type system, you can refer to the official Python documentation: [Python Types](https://docs.python.org/3/library/types.html)

For a deeper understanding of generics in Python, consider reading PEP 484: [Type Hints](https://www.python.org/dev/peps/pep-0484/).

-----

# Vision
In today's world, programming languages are often divided into statically-typed and dynamically-typed. While statically-typed languages provide type safety and performance benefits, they often lack the flexibility and simplicity that dynamically-typed languages offer. This has led to a growing demand for tools that can bring the benefits of both worlds together.

We believe the future of programming lies in the ability to handle types in a fluid and flexible manner, without sacrificing the benefits of static typing. However, achieving this is not easy. It requires a deep understanding of both static and dynamic typing, as well as the ability to create a tool that is easy to use, performant, and thread-safe.

Many have tried to solve this problem, but none have succeeded. The challenge lies in creating a tool that is both powerful and simple to use. It requires a radical new approach, one that is not constrained by the traditional boundaries of static and dynamic typing.

That's where Poly comes in. Our secret is our deep understanding of the problems with static types. As creators of multi-modality and fluid intelligences with no defined shape, we have the unique insight and expertise needed to solve this problem. We have created a tool that allows you to handle dynamic types in a flexible and thread-safe manner, without sacrificing the benefits of static typing.

We are confident that Poly is the best solution to this problem. With our unique approach and deep expertise, we are perfectly positioned to bring this vision to life. Join us on this journey and experience the future of programming today.

Contribute Now


-----


# License
MIT

