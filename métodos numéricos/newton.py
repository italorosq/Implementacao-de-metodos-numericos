import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def newton_raphson(func, x0, tol=1e-4, max_iter=100):
    x = float(x0)
    xsym = sp.symbols('x')
    fsym = func(xsym)
    dfsy = sp.diff(fsym, xsym)
    df2sy = sp.diff(dfsy, xsym)

    fnum = sp.lambdify(xsym, fsym)
    dfnum = sp.lambdify(xsym, dfsy)
    df2num = sp.lambdify(xsym, df2sy)

    for i in range(max_iter):
        df = dfnum(x)
        df2 = df2num(x)
        x1 = x - dfnum(x) / df2num(x)
        if abs(x1 - x) < tol:
            break
        x = x1
    return x

def f(x):
    return x**3 - x - 2
input_x= float(input("Digite um valor inicial para x: "))
resultado = newton_raphson(f, input_x)
print("O resultado é:", resultado)
plt.plot(np.linspace(0.1, 10, 100), [f(x) for x in np.linspace(0.1, 10, 100)], label='f(x)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.scatter([input_x], [f(input_x)], color='red', label='Ponto Inicial')
plt.scatter([resultado], [f(resultado)], color='green', label='Raiz Aproximada')    
plt.title('Método de Newton-Raphson')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()
