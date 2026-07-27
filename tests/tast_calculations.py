import pytest
from app.calculations import Fibonacci, Factorial, Loan


class TestFibonacci:
    def test_zero(self):
        assert Fibonacci(0) == 0

    def test_one(self):
        assert Fibonacci(1) == 1

    def test_negative(self):
        with pytest.raises(ValueError):
            Fibonacci(-1)

    def test_non_integer(self):
        with pytest.raises(TypeError):
            Fibonacci(4.2)

    def test_normal(self):
        assert Fibonacci(10) == 55
        assert Fibonacci(15) == 610




class TestFactorial:
    def test_zero(self):
        assert Factorial(0) == 1
    
    def test_one(self):
        assert Factorial(1) == 1

    def test_negative(self):
        with pytest.raises(ValueError):
            Factorial(-1)
    
    def test_non_integer(self):
        with pytest.raises(TypeError):
            Factorial(4.2)

    def test_normal(self):
        assert Factorial(4) == 24
        assert Factorial(8) == 40320

    def test_large(self):
        result = Factorial(100)
        assert result > 0
        assert isinstance(result, int)



class TestLoan:
    def test_interest_zero(self):
        assert Loan(10000, 0, 10) == 1000.00
    
    def test_interest_negative(self):
        with pytest.raises(ValueError):
            Loan(10000, -2, 10)
    
    def test_months_zero(self):
        with pytest.raises(ValueError):
            Loan(10000, 5, 0)
    
    def test_months_negative(self):
        with pytest.raises(ValueError):
            Loan(10000, 5, -2)

    def test_months_non_integer(self):
        with pytest.raises(TypeError):
            Loan(10000, 5, 4.2)

    def test_principal_negative(self):
        with pytest.raises(ValueError):
            Loan(-10000, 5, 10)

    def test_principal_zero(self):
        with pytest.raises(ValueError):
            Loan(0, 5, 10)

    def test_normal(self):
        assert Loan(10000, 5, 10) == 1023.06

    def test_normal_non_integer(self):
        result = Loan (12500.49, 4.78, 15)
        assert result == round(result, 2)
