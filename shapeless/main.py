import logging
import threading
from typing import Any, TypeVar, Generic
import pickle

T = TypeVar('T')

class Poly(Generic[T]):
    def __init__(
            self, 
            data: Any, 
            verbose: bool = False
        ):
        self.data = data
        self.type_mapping = {}
        self.alias_mapping = {}
        self.lock = threading.Lock()
        if self.verbose:
            logging.info(f"Created a new Poly object with data: {self.data}")

    
    def determine(self):
        with self.lock:
            data = type(self.data)
            if data not in self.type_mapping:
                self.type_mapping[data] = data
            if self.verbose:
                logging.info(f"Determines type of data: {data}")
            return self.type_mapping[data]
    
    def select(self, target):
        selected =  self.determine()
        if self.verbose:
            logging.info(f"Selected type: {selected}")
        return selected
    
    def shift(self, target):
        try:
            return target(self.data)
        except ValueError:
            raise TypeError(f"Cannot shape shift {self.data} to {target}")
    
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