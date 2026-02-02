import pytest # type: ignore
from app.operations import addition, subtraction, multiplication, division


def test_addition_positive():
    assert addition(5, 4) == 9
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    


def test_addition_negative():
    assert addition(-1, -6) == -7
    assert addition(-3, 0) == -3


def test_subtraction_positive():
    assert subtraction(10, 4) == 6
    assert subtraction(0, 0) == 0
    assert subtraction(21, 1) == 20


def test_subtraction_negative():
    assert subtraction(-8, -1) == -7
    assert subtraction(3, 9) == -6


def test_multiplication_positive():
    assert multiplication(4, 1) == 4
    assert multiplication(0, 3) == 0
    assert multiplication(-4, -3) == 12


def test_multiplication_negative():
    assert multiplication(4, -3) == -12
    assert multiplication(-3, 3) == -9


def test_division_positive():
    assert division(9, 3) == 3
    assert division(-10, -5) == 2


def test_division_negative():
    assert division(6, -3) == -2
    assert division(-6, 3) == -2


def test_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(4, 0)
