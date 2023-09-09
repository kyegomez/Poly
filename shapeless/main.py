import logging
import threading
from typing import Any, TypeVar, Generic
import pickle

T = TypeVar('T')

class Poly(Generic[T]):
    """
    The Poly class is a utility class that provides dynamic type handling.
    It allows you to determine, select, shift, validate, alias, annotate, extend, serialize, and deserialize types.
    It also provides thread safety and optional logging.
    """

    def __init__(self, data: Any, verbose: bool = False):
        """
        Initialize a new Poly object.

        :param data: The data whose type is to be handled.
        :param verbose: If True, log all operations. Default is False.
        """
        self.data = data
        self.verbose = verbose
        self.type_mapping = {}
        self.alias_mapping = {}
        self.lock = threading.Lock()
        if self.verbose:
            logging.info(f"Created a new Poly object with data: {self.data}")

    def determine(self):
        """
        Determine the type of the data.

        :return: The type of the data.
        """
        with self.lock:
            data_type = type(self.data)
            if data_type not in self.type_mapping:
                self.type_mapping[data_type] = data_type
            if self.verbose:
                logging.info(f"Determined type of data: {data_type}")
            return self.type_mapping[data_type]

    def select(self, target):
        """
        Select the type of the data.

        :param target: The target type.
        :return: The selected type.
        """
        selected_type = self.determine()
        if self.verbose:
            logging.info(f"Selected type: {selected_type}")
        return selected_type

    def shift(self, target):
        """
        Attempt to shift the data to the target type.

        :param target: The target type.
        :return: The data after shifting to the target type.
        :raises TypeError: If the data cannot be shifted to the target type.
        """
        try:
            return target(self.data)
        except ValueError:
            if self.verbose:
                logging.error(f"Failed to shape shift {self.data} to {target}")
            raise TypeError(f"Cannot shape shift {self.data} to {target}")

    def validate(self, target):
        """
        Validate that the data is of the target type.

        :param target: The target type.
        :return: True if the data is of the target type, False otherwise.
        :raises TypeError: If the data is not of the target type.
        """
        if not isinstance(self.data, target):
            if self.verbose:
                logging.error(f"{self.data} is not of type {target}")
            raise TypeError(f"{self.data} is not of type {target}")
        return True

    def add_alias(self, alias, target):
        """
        Add an alias for a type.

        :param alias: The alias.
        :param target: The target type.
        """
        self.alias_mapping[alias] = target

    def annotate(self, annotation):
        """
        Annotate the data with a type.

        :param annotation: The type annotation.
        """
        self.data: annotation

    def extend(self, extension):
        """
        Extend the type of the data with a new type.

        :param extension: The new type.
        """
        class ExtendedType(type(self.data), extension):
            pass
        self.data = ExtendedType(self.data)

    def serialize(self):
        """
        Serialize the data.

        :return: The serialized data.
        """
        return pickle.dumps(self.data)

    def deserialize(self, serialized_data):
        """
        Deserialize the data.

        :param serialized_data: The serialized data.
        :return: The deserialized data.
        """
        self.data = pickle.loads(serialized_data)
        return self.data

    def __instancecheck__(self, instance):
        """
        Check if an instance is of the selected type.

        :param instance: The instance to check.
        :return: True if the instance is of the selected type, False otherwise.
        """
        return isinstance(instance, self.select())
    
def shapeless(cls):
    """
    A decorator that makes all the variables in a class polymorphic.
    """
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):
            def wrapper(*args, attr_value=attr_value, **kwargs):
                poly_args = [Poly(arg).data for arg in args]
                poly_kwargs = {k: Poly(v).data for k, v in kwargs.items()}
                return attr_value(*poly_args, **poly_kwargs)
            setattr(cls, attr_name, wrapper)
    return cls

def fluid(func):
    """
    A decorator that makes a function able to handle any type of arguments.

    :param func: The function to decorate.
    :return: The decorated function.
    """
    def wrapper(*args, **kwargs):
        # Convert all arguments to Poly
        poly_args = [Poly(arg) for arg in args]
        poly_kwargs = {k: Poly(v) for k, v in kwargs.items()}

        try:
            # Call the function with the converted arguments
            return func(*poly_args, **poly_kwargs)
        except Exception as e:
            # Log any errors that occur during the function call
            logging.error(f"Error in function applying the fluid wrapper {func.__name__}: {e}")
            raise

    return wrapper

def dynamic_import(module_name):
    """
    Dynamically import a module

    :param module_name: The Name of the module to import
    :return: The imported module
    :return: The imported module
    """
    return __import__(module_name)

def auto_cast(value):
    """
    Auto cast a value to the right type
    :param value: the value to cast
    :return the casted value
    """
    return Poly(value).data

def shapeless_array(*args):
    """
    Create an array that can store elements of any type

    :param args: The elements to store in the array.
    :return: The Array.
    """
    return [Poly(arg).data for arg in args]

def shapeless_dict(**kwargs):
    """
    Create a dict that use keys of any type

    :param kwargs: The keys and values to store in the dict
    :return: the dict
    """
    return {Poly(k).data: Poly(v).data for k, v in kwargs.items()}

# # Create an array that can store elements of any type
# array = shapeless_array(1, '2', 3.0, '4.0', [5], {6: '6'})
# print(array)  # Outputs: [1, '2', 3.0, '4.0', [5], {6: '6'}]


# # Create a dictionary that can use keys of any type
# # Create a dictionary that can use keys of any type
# dictionary = shapeless_dict(one=1, two='2', three=3.0, four='4.0')
# print(dictionary)  # Outputs: {'one': 1, 'two': '2', 'three': 3.0, 'four': '4.0'}


