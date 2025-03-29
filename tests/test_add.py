import pytest
from typing import Union

from main import add


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),  # Test with two integers
        (1.5, 2.5, 4.0),  # Test with two floats
        (1, 2.5, 3.5),  # Test with int and float
        (1.5, 2, 3.5),  # Test with float and int
    ],
)
def test_add(a: Union[int, float], b: Union[int, float], expected: Union[int, float]):
    assert add(a, b) == expected
