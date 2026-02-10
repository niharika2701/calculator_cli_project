import pytest
from src.calculator import Calculator

class TestCalculator:
    def setup_method(self):

        self.calc=Calculator()

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),           
        (-2, -3, -5), 
        (-5, 3, -2),         
        (0, 0, 0),           
        (100, -100, 0),      
        (0.1, 0.2, 0.3),
    ])

    def test_add(self, a, b, expected):
        assert self.calc.add(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 2),
        (3, 5, -2),
        (0, 5, -5),
        (-3, -5, 2),
    ])

    def test_subtract(self, a, b, expected):
        assert self.calc.subtract(a, b) == expected
    
    @pytest.mark.parametrize("a, b, expected", [
        (4, 3, 12),
        (5, 0, 0),
        (0, 5, 0),
        (-3, -4, 12),
        (-3, 4, -12),
    ])

    def test_multiply(self, a, b, expected):
        assert self.calc.multiply(a, b) == expected
    
    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),
        (5, 2, 2.5),
        (-10, 2, -5),
        (10, -2, -5),
    ])

    def test_divide(self, a, b, expected):
        assert self.calc.divide(a, b) == expected
    
    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5,0)
    
    



