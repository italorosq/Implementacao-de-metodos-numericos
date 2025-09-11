import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

def funcao(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

def secao_aurea(f_uni, a, b, tol=1e-6, max_iter=100):
    phi = (1 + math.sqrt(5)) / 2
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    f1 = f_uni(x1)
    f2 = f_uni(x2)
    
    for _ in range(max_iter):
        if (b - a) <= tol:
            break
        if f1 < f2:
            b = x2; x2 = x1; f2 = f1; x1 = b - (b - a) / phi; f1 = f_uni(x1)
        else:
            a = x1; x1 = x2; f1 = f2; x2 = a + (b - a) / phi; f2 = f_uni(x2)
            
    return (a + b) / 2

def hooke_jeeves(f, y0, max_iter=100, tol=1e-6):
    y1 = np.array(y0, dtype=float)
    y_anterior = y1.copy()
    
    d1 = np.array([1.0, 0.0])
    d2 = np.array([0.0, 1.0])
    
    history = [y1.copy()]
    
    for i in range(max_iter):
        
        print(f"\n--- Iteração {i+1}: Ponto Base (y1) = {y1}, f(y1) = {f(y1):.6f} ---")

        ##busca exploratória

        ## busca na direção d1
        f_alpha1 = lambda alpha: f(y1 + alpha * d1)
        alpha1 = secao_aurea(f_alpha1, -10, 10)
        y2 = y1 + alpha1 * d1
        
        ## busca na direção d2
        f_alpha2 = lambda alpha: f(y2 + alpha * d2)
        alpha2 = secao_aurea(f_alpha2, -10, 10)
        y3 = y2 + alpha2 * d2
        
        print(f"Ponto após busca exploratória (y3): {y3}, f(y3) = {f(y3):.6f}")

        ##busca padrão
        if f(y3) < f(y1):
            print("Sucesso. Realizando movimento de padrão...")
            
            dp = y3 - y1
            
            f_alphap = lambda alpha: f(y3 + alpha * dp)
            alphap = secao_aurea(f_alphap, 0, 2.0)
            yp = y3 + alphap * dp
            
            y_anterior = y1.copy()
            y1 = yp.copy()
            
            history.append(y1.copy())
            print(f"Novo ponto base (yp -> y1): {y1}, f(y1) = {f(y1):.6f}")

        else:
            print("Falha. A busca não melhorou o ponto.")
            if np.linalg.norm(y3 - y1) < tol:
                print("\nConvergência atingida.")
                break
            y_anterior = y1.copy()
    
    print("\nOtimização concluída.")
    return y1, f(y1), history

print("Digite o valor inicial y0:")
y0_input = np.array([float(input("y0[0]: ")), float(input("y0[1]: "))])

ponto_minimo, valor_minimo, historico_pontos = hooke_jeeves(funcao, y0_input)

print("\n RESULTADO FINAL")
print(f"Ponto mínimo encontrado: {ponto_minimo}")
print(f"Valor da função no ponto mínimo: {valor_minimo}")

df = pd.DataFrame(historico_pontos, columns=['x1', 'x2'])
print("\nHistórico de pontos base encontrados:")
print(df)

plt.plot(df['x1'], df['x2'], marker='o')
plt.title('Trajetória do Método de Hooke-Jeeves')
plt.xlabel('x1')
plt.ylabel('x2')
plt.grid(True)
plt.show()