[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)

# Poly
A simple Fluid, PolyMorhic,and shapeless package that activates radically flexiblity and simplicity in your programs

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


The `Poly` class provides the following methods:

-   `determine()`: Determine the type of the data.
-   `select(target)`: Select the type of the data.
-   `shift(target)`: Attempt to shift the data to the target type.
-   `validate(target)`: Validate that the data is of the target type.
-   `add_alias(alias, target)`: Add an alias for a type.
-   `annotate(annotation)`: Annotate the data with a type.
-   `extend(extension)`: Extend the type of the data with a new type.
-   `serialize()`: Serialize the data.
-   `deserialize(serialized_data)`: Deserialize the data.


# License
MIT

