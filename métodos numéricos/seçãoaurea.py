import math
import matplotlib.pyplot as plt 

def funcao(x):
    return x**2
def secao_aurea(a, b):
    phi = (1 + math.sqrt(5)) / 2
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    return x1, x2   
def secao_aurea_iter(func, a, b, max_iter=10):
    for _ in range(max_iter):
        x1, x2 = secao_aurea(a, b)
        if funcao(x1) < funcao(x2):
            b = x2
        else:
            a = x1
        if abs(funcao(x1) - funcao(x2)) < 0.000001:
            break
    return (a + b) / 2

input_a = float(input("Digite um valor para a: "))
input_b = float(input("Digite um valor para b: "))
resultado = secao_aurea_iter(funcao, input_a, input_b)
print(f"O ponto mínimo aproximado é: {resultado:.6f}")
plt.plot([funcao(x  ) for x in range(int(input_a), int(input_b) + 10)], label='f(x) = x^2')
plt.plot(resultado, funcao(resultado), 'go')
plt.axvline(x=resultado, color='g', linestyle='-')
plt.title('Função e Ponto Mínimo Aproximado')
plt.xlabel('x')     
plt.ylabel('y')
plt.grid()
plt.show()
