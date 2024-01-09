"""

This module utilises ``Pytest`` to test functions in ``calc.py``

"""
import pytest
from calc import add

def test_add_integers():
    assert add(1, 4) == 5
    assert add(4) == 102

def test_add_inf():
    with pytest.raises(OverflowError):
        add(1, float('inf'))

    with pytest.raises(OverflowError):
        add(float('inf'), 1.0)

    with pytest.raises(OverflowError):
        add(float('inf'))

def test_add_nan():
    with pytest.raises(ValueError):
        add(1, float('nan'))

    with pytest.raises(ValueError):
        add(float('nan'), 1.0)

    with pytest.raises(ValueError):
        add(float('nan'))

def test_add_types():
    with pytest.raises(TypeError):
        add(1, 'nana')

    with pytest.raises(TypeError):
        add('nana', 1.0)

    with pytest.raises(TypeError):
        add('nana')

    with pytest.raises(TypeError):
        add(1, ('n', 'a', 'n', 'a'))

    with pytest.raises(TypeError):
        add(['n', 'a', 'n', 'a'], 1.0)

    with pytest.raises(TypeError):
        add({'nana': 'Trevor Noah', 'age': 56})

