#importação da biblioteca scipy para usar o método Nelder-Mead já implementado

'''import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize
import pandas as pd


def funcao(x):
    return  (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

x0 = np.array([-1.2, 1.0])
history = []

def callback_fn(xk):
    history.append(xk)

res = minimize(funcao, x0, method='Nelder-Mead', options={'xatol': 1e-6, 'disp': True}, callback=callback_fn)
print(f"Resultado da otimização: {res.x}, f(x) = {res.fun}") 
dados = {
    'x1': [],
    'x2': [],
    'f(x)': []
}
for i in range(len(history)):
    dados['x1'].append(history[i][0])
    dados['x2'].append(history[i][1])
    dados['f(x)'].append(funcao(history[i]))
    
df = pd.DataFrame(dados)

sns.pairplot(df)
plt.suptitle("Histórico de pontos visitados pelo método de Nelder-Mead", y=1.02)
plt.show()

plt.figure(figsize=(10, 6))
plt.title("Método de Nelder-Mead")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(True)
plt.scatter(res.x[0], res.x[1], color='red', label='Ponto Ótimo')
plt.legend()
plt.show() '''



## implementação do método Nelder-Mead do zero

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def nelder_mead(f, x_inicial, passo=0.1, tol_x=1e-6, tol_f=1e-6, max_iter=1000):
    n = len(x_inicial)
    simples = [np.array(x_inicial, dtype=float)]
    scores = [f(simples[0])]
    historico = [np.array(x_inicial, dtype=float)]

    for i in range(n):
        ponto = np.array(x_inicial, dtype=float)
        ponto[i] += passo
        simples.append(ponto)
        scores.append(f(ponto))
        historico.append(ponto.copy())

    iter_count = 0
    while iter_count < max_iter:
        indices_ordenados = np.argsort(scores)
        simples = [simples[i] for i in indices_ordenados]
        scores = [scores[i] for i in indices_ordenados]
        melhor = simples[0]
        pior = simples[-1]

        historico.append(melhor.copy())

        if np.linalg.norm(melhor - pior) < tol_x and np.abs(scores[0] - scores[-1]) < tol_f:
            break

        centroide = np.mean(simples[:-1], axis=0)

        # Reflexão
        x_reflexao = centroide + 1.0 * (centroide - pior)
        score_reflexao = f(x_reflexao)

        if scores[0] <= score_reflexao < scores[-2]:
            simples[-1] = x_reflexao
            scores[-1] = score_reflexao
            iter_count += 1
            continue

        # Expansão
        if score_reflexao < scores[0]:
            x_expansao = centroide + 2.0 * (x_reflexao - centroide)
            score_expansao = f(x_expansao)
            if score_expansao < score_reflexao:
                simples[-1] = x_expansao
                scores[-1] = score_expansao
            else:
                simples[-1] = x_reflexao
                scores[-1] = score_reflexao
            iter_count += 1
            continue

        # Contração
        x_contracao = centroide + 0.5 * (pior - centroide)
        score_contracao = f(x_contracao)

        if score_contracao < scores[-1]:
            simples[-1] = x_contracao
            scores[-1] = score_contracao
            iter_count += 1
            continue

        # Encolhimento
        for i in range(1, len(simples)):
            simples[i] = simples[0] + 0.5 * (simples[i] - simples[0])
            scores[i] = f(simples[i])
            historico.append(simples[i].copy())
        iter_count += 1

    return simples[0], scores[0], historico

def funcao(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

x0 = [-1.2, 1.0]
resultado, valor, historico = nelder_mead(funcao, x0)
print(f"Resultado da otimização: {resultado}, f(x) = {valor}")

dados = {
    'x1': [],
    'x2': [],
    'f(x)': []
}

for ponto in historico:
    dados['x1'].append(ponto[0])
    dados['x2'].append(ponto[1])
    dados['f(x)'].append(funcao(ponto))

df = pd.DataFrame(dados)

sns.pairplot(df)
plt.suptitle("Histórico de pontos visitados pelo método de Nelder-Mead", y=1.02)
plt.show()

plt.figure(figsize=(10, 6))
plt.title("Método de Nelder-Mead")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(True)
plt.scatter(resultado[0], resultado[1], color='red', label='Ponto Ótimo')
plt.plot(df['x1'], df['x2'], marker='o', linestyle='-', color='blue', alpha=0.5, label='Caminho')
plt.legend()
plt.show()
