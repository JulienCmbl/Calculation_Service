import numpy as np 
import matplotlib.pyplot as plt
from decimal import Decimal, ROUND_HALF_UP
import sys

sys.set_int_max_str_digits(0) 


def Fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    if not isinstance(n, int):
        raise TypeError(f"n must be an integer, instead {n} is {type(n).__name__}")
    
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return a



def Factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError(f"n must be an integer, instead {n} is {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def Loan(P: float, r_annum: float, n:int) -> float:
    if P <= 0:
        raise ValueError(f"P must be stricyly superior to 0, got {P}")
    if r_annum < 0:
        raise ValueError(f"The monthly rate has to be positive, got {r_annum}")
    if not isinstance(n, int):
        raise TypeError(f"n must be an integer, instead {n} is {type(n).__name__}")
    if n <= 0:
        raise ValueError(f"The number of months has to be a positive integer, got {n}")
    
    P = Decimal(str(P))

    if r_annum == 0:
        M = P / Decimal(n)
    else:
        r = Decimal(str(r_annum)) / Decimal("100") / Decimal("12")
        M = P * ((r * (1 + r)**n) / ((1+r)**n - 1))

    return float(M.quantize(Decimal("0.01"), rounding = ROUND_HALF_UP))
