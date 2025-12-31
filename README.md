# 🚀 Métodos Numéricos de Otimização 🚀

Bem-vindo ao repositório de implementações para a disciplina de **Métodos Numéricos de Otimização**! Este projeto contém algoritmos para encontrar soluções para problemas de otimização, implementados em Python.

## 🎯 Objetivo

O objetivo deste repositório é aplicar e demonstrar o funcionamento de métodos numéricos clássicos de otimização, como parte dos estudos da disciplina.

---

## 🛠️ Métodos Implementados

Atualmente, os seguintes métodos estão disponíveis:

### 1. Método de Newton (`newton.py`)

- **O que faz?** Encontra o mínimo de uma função.
- **Como funciona?** Utiliza uma abordagem iterativa que aproxima o mínimo da função a partir de um ponto inicial, usando a primeira e a segunda derivada. O script também plota o gráfico da função e o resultado encontrado.

### 2. Seção Áurea (`secao_aurea.py`)

- **O que faz?** Encontra o ponto de mínimo de uma função unimodal dentro de um intervalo.
- **Como funciona?** Reduz iterativamente o intervalo de busca, descartando a parte que não contém o mínimo, com base na proporção áurea. O script também plota um gráfico para visualizar o resultado.

### 3. Hooke-Jeeves (`hookejeeves.py`)

<<<<<<< HEAD
- **O que faz?** Encontra o mínimo de uma função de múltiplas variáveis.
- **Como funciona?** É um método de busca direta que combina buscas exploratórias ao longo dos eixos coordenados com movimentos de padrão para acelerar a convergência. O script também plota a trajetória da otimização.

### 4. Gradiente Descendente (`Gradientedescndente.py`)

- **O que faz?** Encontra o mínimo de uma função de múltiplas variáveis.
- **Como funciona?** Move-se iterativamente na direção oposta ao gradiente da função em um ponto, buscando o caminho de maior declive para encontrar um mínimo local.

### 5. Nelder-Mead (`simplexneldermead.py`)

- **O que faz?** Encontra o mínimo de uma função de múltiplas variáveis.
- **Como funciona?** Utiliza um simplex (um polígono com n+1 vértices em n dimensões) que se adapta à topografia da função através de operações de reflexão, expansão, contração e encolhimento para encontrar o mínimo.

### 6. Newton Multivariado (`newtonmultivariado.ipynb`)

- **O que faz?** Encontra o ponto crítico (mínimo, máximo ou ponto de sela) de uma função de múltiplas variáveis.
- **Como funciona?** Generaliza o método de Newton para múltiplas dimensões, utilizando o gradiente e a matriz Hessiana da função para convergir rapidamente para uma solução.

### 7. Rosenbrock (`rosenbrock.ipynb`)

- **O que faz?** Encontra o mínimo de uma função de múltiplas variáveis.
- **Como funciona?** É um método de busca direta que ajusta continuamente um conjunto de direções de busca ortogonais, adaptando-se à forma da função para encontrar o mínimo.

---
=======
- **O que faz?** 
- **Como funiona ?** 

### 4. Rosenbrock (`rosenbrock.ipynb`)

- **O que faz?** 
- **Como funiona ?**

### 5. Simplex (`simplexneldermead.py`)

- **O que faz?** 
- **Como funiona ?**

### 6. Gradiente descendente (`Gradientedescendente.py`)

- **O que faz?** 
- **Como funiona ?**

### 7. Newton multivariado (`newtonmultivariado.ipynb`)

- **O que faz?** 
- **Como funiona ?**

### 8. fletcher reeves (`fletcherreeves.ipynb`)

- **O que faz?** 
- **Como funiona ?**
>>>>>>> c6a23aa (começando a descrição dos outros métodos implementados)

## ⚙️ Como Usar

Para executar os scripts, você precisa ter o Python instalado, juntamente com algumas bibliotecas.

### 1. Pré-requisitos

Instale as dependências necessárias usando `pip`:

```bash
pip install
numpy
sympy
matplotlib
pandas
seaborn
2. Executando os Scripts
Navegue até o diretório métodos numéricos e execute o script desejado:

cd "métodos numéricos"
Para os arquivos .py:

python nome_do_arquivo.py
Para os arquivos .ipynb (Jupyter Notebooks):

Você precisará ter o Jupyter Notebook ou o JupyterLab instalado:

pip install notebook
E então, para abrir:
Navegue novamente até a pasta com os aqrquivos e abra eles .

jupyter notebook
O script solicitará os valores de entrada necessários (como o ponto inicial ou o intervalo de busca) diretamente no terminal ou no próprio notebook.
