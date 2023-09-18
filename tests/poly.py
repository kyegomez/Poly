import pytest

from shapeless.main import Poly, fluid, shapeless


class TestPoly:

    def test_determine(self):
        p = Poly(5)
        assert p.determine() is int

        p = Poly("hello")
        assert p.determine() is str

    def test_select(self):
        p = Poly(5)
        assert p.select(int) is int

        with pytest.raises(TypeError):
            p.select(str)

    def test_shift(self):
        p = Poly(5)
        assert p.shift(str) == "5"

        p = Poly("5")
        assert p.shift(int) == 5

        p = Poly(5.5)
        with pytest.raises(TypeError):
            p.shift(bool)

    def test_validate(self):
        p = Poly("hello")
        p.validate(str)

        with pytest.raises(TypeError):
            p.validate(int)

    def test_add_alias(self):
        p = Poly("5")
        p.add_alias("num", int)
        assert p.alias_mapping["num"] is int

    def test_annotate(self):
        p = Poly("5")
        p.annotate(int)
        assert p.data == "5" # no change

    def test_extend(self):
        class MyClass:
            pass
        
        p = Poly(5)
        p.extend(MyClass)
        assert isinstance(p.data, MyClass)

    def test_serialize_deserialize(self):
        p = Poly([1, 2, 3])
        serialized = p.serialize()
        deserialized = Poly.deserialize(serialized)
        assert deserialized.data == [1, 2, 3]

    def test_instancecheck(self):
        p = Poly("hello")
        assert p._Poly__instancecheck__("hello")
        assert not p._Poly__instancecheck__(5)

