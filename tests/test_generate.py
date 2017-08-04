import pytest

from nlppln.generate import to_bool


def test_to_bool_correct():
    assert to_bool('y') == True
    assert to_bool('n') == False


def test_to_bool_error():
    with pytest.raises(ValueError):
        to_bool('foo')
