# 🚀 Métodos Numéricos de Otimização 🚀

Bem-vindo ao repositório de implementações para a disciplina de **Métodos Numéricos de Otimização**! Este projeto contém algoritmos para encontrar soluções para problemas de otimização, implementados em Python.

## 🎯 Objetivo

O objetivo deste repositório é aplicar e demonstrar o funcionamento de métodos numéricos clássicos de otimização, como parte dos estudos da disciplina.

---

## 🛠️ Métodos Implementados

Atualmente, os seguintes métodos estão disponíveis:

### 1. Método de Newton(`newton.py`)

- **O que faz?** Encontra o minimo de uma função
- **Como funciona?** Utiliza uma abordagem iterativa que aproxima o minimo da função a partir de um ponto inicial, usando a tangente da curva. O script também plota o gráfico da função e o resultado encontrado.

### 2. Seção Áurea (`secao_aurea.py`)

- **O que faz?** Encontra o ponto de mínimo de uma função unimodal dentro de um intervalo.
- **Como funciona?** Reduz iterativamente o intervalo de busca, descartando a parte que não contém o mínimo, com base na proporção áurea. O script também plota um gráfico para visualizar o resultado.

### 3. Hooke-Jeeves (`hookejeeves.py`)

---

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
