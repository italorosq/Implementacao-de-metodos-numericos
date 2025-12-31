# 🚀 Métodos Numéricos de Otimização 🚀

Bem-vindo ao repositório de implementações para a disciplina de **Métodos Numéricos de Otimização**! Este projeto contém algoritmos para encontrar soluções para problemas de otimização, implementados em Python.

## 🎯 Objetivo

O objetivo deste repositório é aplicar e demonstrar o funcionamento de métodos numéricos clássicos de otimização, como parte dos estudos da disciplina.

---

## 🛠️ Métodos Implementados

Atualmente, os seguintes métodos estão disponíveis:

### 1. Método de Newton(`newton.py`)

- **O que faz?** Encontra o minimo de uma função unimodal.
- **Como funciona?** Utiliza uma abordagem iterativa que aproxima o minimo da função a partir de um ponto inicial, usando a tangente da curva. O script também plota o gráfico da função e o resultado encontrado.

### 2. Seção Áurea (`secao_aurea.py`)

- **O que faz?** Encontra o ponto de mínimo de uma função unimodal dentro de um intervalo.
- **Como funciona?** Reduz iterativamente o intervalo de busca, descartando a parte que não contém o mínimo, com base na proporção áurea. O script também plota um gráfico para visualizar o resultado.

### 3. Hooke-Jeeves (`hookejeeves.py`)

- **O que faz?** Encontra o ponto de mínimo de uma função multivariada através de busca exploratória.
- **Como funciona?** Utiliza uma estratégia de busca baseada em padrões (pattern search). Começa em um ponto inicial e faz buscas exploratórias ao longo de cada direção (eixo coordenado), aumentando ou diminuindo o passo conforme encontra melhorias na função objetivo. Quando um padrão bem-sucedido é encontrado, realiza uma busca acelerada nessa direção.

### 4. Rosenbrock (`rosenbrock.ipynb`)

- **O que faz?** Otimiza a função de Rosenbrock, um problema clássico de teste para algoritmos de otimização.
- **Como funciona?** A função de Rosenbrock é altamente não-convexa e representa um desafio para muitos otimizadores. O notebook aplica diferentes métodos de otimização para encontrar o mínimo global desta função (em f(x,y) = (1-x)² + 100(y-x²)²) e compara seus desempenhos, visualizando as trajetórias de busca em gráficos 3D e contornos.

### 5. Simplex Neldermead (`simplexneldermead.py`)

- **O que faz?** Encontra o ponto de mínimo de funções multivariadas sem requerer derivadas.
- **Como funciona?** Mantém um simplexo (polígono com n+1 vértices em n dimensões) ao redor da solução e iterativamente realiza operações de reflexão, expansão e contração para move-lo em direção ao mínimo. É um método robusto e eficiente para problemas sem derivadas disponíveis.

### 6. Gradiente Descendente (`Gradientedescendente.py`)

- **O que faz?** Encontra o ponto de mínimo de funções multivariadas utilizando informação do gradiente.
- **Como funciona?** Começa em um ponto inicial e calcula o gradiente (vetor de derivadas parciais) da função naquele ponto. Move-se iterativamente na direção oposta do gradiente (direção de máxima diminuição) com um tamanho de passo (taxa de aprendizado) pré-definido, até converger para um mínimo local.

### 7. Newton Multivariado (`newtonmultivariado.ipynb`)

- **O que faz?** Estende o método de Newton para funções de múltiplas variáveis.
- **Como funciona?** Utiliza tanto o gradiente (primeira derivada) quanto a matriz Hessiana (segundas derivadas) da função. Em cada iteração, resolve um sistema linear para encontrar a direção de busca quadraticamente ótima, convergindo muito rapidamente para o mínimo quando perto dele. É computacionalmente mais cara que gradiente descendente, mas converge em menos iterações.

### 8. Fletcher-Reeves (`fletcherreeves.ipynb`)

- **O que faz?** Encontra o mínimo de funções multivariadas usando o método dos gradientes conjugados.
- **Como funciona?** Melhora o gradiente descendente encontrando direções conjugadas (ortogonais com respeito à Hessiana). Combina a direção anterior com o gradiente atual de forma inteligente, permitindo convergência em no máximo n iterações para funções quadráticas n-dimensionais. É muito eficiente e requer menos iterações que o gradiente descendente simples.

## ⚙️ Como Usar

Para executar os scripts, você precisa ter o Python instalado, juntamente com algumas bibliotecas.

### 1. Pré-requisitos

Instale as dependências necessárias usando `pip`:

```bash
pip install numpy sympy matplotlib
```

### 2. Executando os Scripts

Navegue até o diretório `métodos numéricos` e execute o script desejado:

```bash
cd "métodos numéricos"
```

**Para o Método de Newton:**

```bash
python newton.py
```

**Para a Seção Áurea:**

```bash
python secao_aurea.py
```

O script solicitará os valores de entrada necessários (como o ponto inicial ou o intervalo de busca) diretamente no terminal.

---

## 🔮 Próximos Passos

- [ ] Criar uma interface gráfica simples para interagir com os métodos.
