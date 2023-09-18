from shapeless.main import Poly, shapeless
import pytest

@shapeless
class MyClass:
    x = 0
    y = ""

    def add(self, a, b):
        return a + b

def test_shapeless():
    obj = MyClass()
    assert isinstance(obj.x, Poly)
    assert isinstance(obj.y, Poly)
    assert isinstance(obj.add, object)

