import pytest
from shapeless.main import fluid 


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    ("hi", "there", "hithere"),
    ([1,2], [3], [1,2,3])
])
def test_fluid(a, b, expected):
    @fluid
    def add(x, y):
        return x + y
    
    assert add(a, b) == expected
