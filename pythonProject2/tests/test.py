import pytest

from app.calc import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator


    def test_addition_success(self):
        assert self.calc.addition(self,1, 1) == 2


    def test_division_success(self):
        assert self.calc.division(self, 9,3) == 3


    def test_multiplication_success(self):
        assert self.calc.multiplication(self,2, 2) == 4


    def test_substraction_success(self):
        assert self.calc.subtraction(self, 5, 2) == 3


    def teardown(self):
        print('Выполнение метода "Teardown" ')