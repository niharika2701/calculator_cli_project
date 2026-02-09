import pytest
from src.calculator import Calculator

class TestCalculator:
    def test_add_two_positive_numbers(self):

        calc=Calculator()

        result=calc.add(2,3)

        assert result == 5
        