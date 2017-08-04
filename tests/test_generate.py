import pytest

from nlppln.generate import to_bool


def test_to_bool_correct():
    assert to_bool('y') is True
    assert to_bool('n') is False


def test_to_bool_error():
    with pytest.raises(ValueError):
        to_bool('foo')
