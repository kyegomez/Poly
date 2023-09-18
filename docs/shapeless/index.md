[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)

# Poly 💧
<!-- ![Poly banner](shapeless.png) -->

A Fluid, PolyMorphic,and shapeless Types Package that activates radically flexiblity and simplicity in your programs

[Shapeless Announcement 💧](https://medium.com/@kyeg/embrace-shapelessness-the-design-philosophy-of-the-future-1d530c075789)

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

# `shapeless` Decorator
With the shapeless decorator you can wrap entire classes and transform all their variables into the `Poly` type!

```python
from shapeless import shapeless

@shapeless
class SimpleClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
sc = SimpleClass(1, 2)
print(sc.add())  # prints 3

```

-----


# `fluid` Decorator
Fluid is like the `shapeless` decorator but for classes, just wrap it around your function to transform all the variables to the `Poly` shapeless type.

```python
from shapeless import fluid

@fluid
def add(a, b):
    return a.data + b.data

print(add(1, 2))
print(add("hello", 'world'))

```

----

# Why use Shapeless?

Shapeless is a powerful tool for creating fluid programs because it allows developers to handle data types dynamically and polymorphically. This means that the same class or function can handle different types of data, making the program more flexible and versatile.

Shapeless also provides thread safety, which is crucial for multi-threaded applications. This ensures that the data remains consistent and prevents race conditions.

Furthermore, Shapeless provides logging, type aliasing, type annotation, type extension, and serialization and deserialization features. These features make it easier to write, debug, and understand the code, and they allow developers to create more complex and flexible data structures.

In conclusion, Shapeless is a powerful tool for creating fluid programs that can handle a wide range of data types and that are safe, flexible, and easy to understand.

## Benefits

1.  Dynamic Type Handling 🔄: Poly and Shapeless allow developers to handle data types dynamically. This means that the type of data can be determined, selected, shifted, validated, aliased, annotated, extended, serialized, and deserialized on the fly.

2.  Thread Safety 🔒: Both Poly and Shapeless provide thread safety, which is crucial for multi-threaded applications. This ensures that the data remains consistent and prevents race conditions.

3.  Logging 📝: With the verbose option, all operations can be logged. This is useful for debugging and understanding the flow of data and operations in the program.

4.  Polymorphism 🐾: Poly and Shapeless make it easy to create polymorphic classes and functions. This means that the same class or function can handle different types of data, making the program more flexible and versatile.

5.  Type Aliasing 🏷️: Poly allows developers to add aliases for types. This can make the code more readable and easier to understand.

6.  Type Annotation 🖊️: Poly provides a method to annotate the data with a type. This can be useful for static type checking and for making the code more self-explanatory.

7.  Type Extension 🧩: With Poly, the type of the data can be extended with a new type. This allows developers to create more complex and flexible data structures.

8.  Serialization and Deserialization 💾: Poly provides methods to serialize and deserialize the data. This is useful for saving and loading data, and for sending and receiving data over a network.


------

# Documentation
`Poly` is a utility class that encapsulates dynamic type handling for any data. It provides flexibility and convenience when working with types. With `Poly`, users can determine, select, shift, validate, alias, annotate, extend, serialize, and deserialize data types. The class also ensures thread safety and supports optional logging of operations.

## Class Definition:

```python
class Poly(Generic[T]):
```

### Parameters:

- **data (Any)**: Data whose type is to be managed.
- **verbose (bool, optional)**: If `True`, operations will be logged. Default is `False`.

## Methods:

### `__init__(self, data: Any, verbose: bool = False)`

Initializes a new instance of `Poly`.

### `determine(self) -> Type`

Determines the type of the contained data.

**Returns**: 
- **Type** - The type of the data.

### `select(self, target) -> Type`

Selects the type of the data.

**Parameters**:
- **target**: The target type to select.

**Returns**: 
- **Type** - The selected type.

### `shift(self, target: Type) -> Any`

Tries to convert the data to the specified target type.

**Parameters**:
- **target**: The desired type to convert the data to.

**Returns**: 
- **Any** - The data after conversion.

**Raises**: 
- **TypeError**: If the data cannot be shifted to the target type.

### `validate(self, target: Type) -> bool`

Checks if the data is of the given type.

**Parameters**:
- **target**: The type to check against.

**Returns**: 
- **bool** - `True` if the data is of the target type, `False` otherwise.

**Raises**:
- **TypeError**: If the data is not of the target type.

### `add_alias(self, alias: str, target: Type)`

Creates an alias for a specific type.

**Parameters**:
- **alias**: Alias name.
- **target**: Target type for which alias is created.

### `annotate(self, annotation: Type)`

Provides a type hint to the data.

**Parameters**:
- **annotation**: The type hint.

### `extend(self, extension: Type)`

Extends the current type of data with a new type.

**Parameters**:
- **extension**: The new type to be added to the current type.

### `serialize(self) -> bytes`

Converts the data into its byte representation.

**Returns**: 
- **bytes** - The byte representation of the data.

### `deserialize(self, serialized_data: bytes) -> Any`

Converts byte representation back to its original form.

**Parameters**:
- **serialized_data**: Byte representation of data.

**Returns**: 
- **Any** - The deserialized data.

### `__instancecheck__(self, instance: Any) -> bool`

Checks if an instance matches the selected type.

**Parameters**:
- **instance**: The instance to be checked.

**Returns**: 
- **bool** - `True` if the instance matches, otherwise `False`.

## Usage Examples:

### 1. Determining and Selecting Type

```python
from shapeless import Poly

data = 1234
p = Poly(data, verbose=True)
print(p.determine())  # Outputs: <class 'int'>
print(p.select(int))  # Outputs: <class 'int'>
```

### 2. Shifting and Validating Type

```python
p.shift(str)
print(p.data)  # Outputs: "1234"
p.validate(str)  # Validates if data is of type 'str'
```

### 3. Serialization and Deserialization

```python
serialized_data = p.serialize()
new_poly = Poly(0)
new_poly.deserialize(serialized_data)
print(new_poly.data)  # Outputs: "1234"
```

## Mathematical Representation:

Given data `d` and a set of types `T`, `Poly` allows for dynamic conversions and operations on `d` with respect to `T`. If `t` belongs to `T`, operations are possible. If not, errors might be raised.

Note:
Ensure thread-safety when using `Poly` in multi-threaded environments. Also, it is essential to be aware of potential pitfalls when serializing and deserializing data, especially when security is a concern.

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

