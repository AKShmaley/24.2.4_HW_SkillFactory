import pytest
from app.calc import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()
    def test_adding_positive_numbers(self):
        assert self.calc.adding(2, 3) == 5
    def test_subtraction_positive_numbers(self):
        assert self.calc.subtraction(5, 2) == 3
    def test_multiply_positive_numbers(self):
        assert self.calc.multiply(4, 3) == 12
    def test_division_positive_numbers(self):
        assert self.calc.division(10, 2) == 5.0
    def teardown_method(self):
        print("Тест завершен")