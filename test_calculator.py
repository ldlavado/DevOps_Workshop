import pytest

from calculator import division, multiplicacion, resta, suma


def test_resta():
    assert resta(10, 5) == 5


def test_multiplicacion():
    assert multiplicacion(4, 5) == 20


def test_suma():
    assert suma(10, 5) == 15


def test_division():
    assert division(10, 2) == 5


def test_division_entre_cero():
    with pytest.raises(ValueError):
        division(10, 0)
