import pytest
from src.calculator import Calculator

class TestCalculator:
    def setup_method(self):

        self.calc=Calculator()

    def test_add_two_positive_numbers(self):
        
        assert self.calc.add(2,3) == 5
    
    def test_add_two_negative_numbers(self):
        
        assert self.calc.add(-2,-3) == -5
    
    def test_add_two_mixed_signs(self):
        
        assert self.calc.add(-5,3) == -2
    
    def test_subtract_positive_numbers(self):
        
        assert self.calc.subtract(5, 3) == 2
    
    def test_subtract_negative_result(self):
        
        assert self.calc.subtract(3, 5) == -2

    def test_multiply_positive_numbers(self):
        
        assert self.calc.multiply(4, 3) == 12
    
    def test_multiply_by_zero(self):
        
        assert self.calc.multiply(5, 0) == 0
    
    def test_multiply_negative_numbers(self):
        
        assert self.calc.multiply(-3, -4) == 12
    
    def test_divide_positive_numbers(self):
        
        assert self.calc.divide(10, 2) == 5
    
    def test_divide_results_in_float(self):
        
        assert self.calc.divide(5, 2) == 2.5
    
    def test_divide_by_zero_raises_error(self):
        
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)


