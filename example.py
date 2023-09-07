from typing import Any, TypeVar, Generic
import pickle

T = TypeVar('T')

class Poly(Generic[T]):
    def __init__(self, data: Any):
        self.data = data
        self.type_mapping = {}
        self.alias_mapping = {}

    def determine(self):
        data = type(self.data)
        if data not in self.type_mapping:
            self.type_mapping[data] = data
        return self.type_mapping[data]

    def select(self):
        return self.determine()

    def shift(self, target):
        try:
            return target(self.data)
        except ValueError:
            raise TypeError(f"Cannot shift {self.data} to {target}")

    def validate(self, target):
        if not isinstance(self.data, target):
            raise TypeError(f"{self.data} is not of type {target}")
        return True

    def add_alias(self, alias, target):
        self.alias_mapping[alias] = target

    def annotate(self, annotation):
        self.data: annotation

    def extend(self, extension):
        class ExtendedType(type(self.data), extension):
            pass
        self.data = ExtendedType(self.data)

    def serialize(self):
        return pickle.dumps(self.data)

    def deserialize(self, serialized_data):
        self.data = pickle.loads(serialized_data)
        return self.data
    
    def __instancecheck__(self, instance):
        return isinstance(instance, self.select())
    


def my_func(a: Poly):
    print(type(a))

my_func('10')


