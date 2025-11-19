import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def funcao(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

def derivada_definida(f, x, h=1e-8):
    n = len(x)
    grad = np.zeros(n)
    for i in range(n):
        x1 = np.array(x, dtype=float)
        x2 = np.array(x, dtype=float)
        x1[i] += h
        x2[i] -= h
        grad[i] = (f(x1) - f(x2)) / (2 * h)
    return grad

def gradiente_descendente(f, x0, alpha=0.001, tol=1e-6, max_iter=1000):
    x = np.array(x0, dtype=float)
    history = [x.copy()]
    
    for i in range(max_iter):
        grad = derivada_definida(f, x)
        x_new = x - alpha * grad
        history.append(x_new.copy())
        
        print(f"Iteração {i+1}: x = {x_new}, f(x) = {f(x_new):.6f}, grad= {np.linalg.norm(grad):.6f}")
        
        if np.linalg.norm(grad) < tol:
            break
        x = x_new
        
    return x, history

input_x0 = [float(input("Digite o valor inicial para x1: ")), float(input("Digite o valor inicial para x2: "))]
resultado, historico = gradiente_descendente(funcao, input_x0)