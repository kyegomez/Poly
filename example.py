# !pip install shapeless
from shapeless.main import Poly
    
def my_func(a: Poly):
    print(type(a))

example = type(my_func('10'))


