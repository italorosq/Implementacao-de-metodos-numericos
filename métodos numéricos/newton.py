import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def newton_raphson(func, x0, max_iter=100):
    x = x0
    for i in range(max_iter):
        x = sp.symbols('x')
        f = func(x)
        df = sp.diff(func, x)
        df2 = sp.diff(df, x)
        x_new = x - df / df2
        if abs(x_new - x) < 0.0001:
            break
        return x_new

def f(x):
    return 7*x - sp.ln(x)

