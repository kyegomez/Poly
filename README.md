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

