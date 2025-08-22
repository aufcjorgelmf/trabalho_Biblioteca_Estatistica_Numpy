# Biblioteca de Análise Estatística com NumPy

## [cite_start]Objetivo da Biblioteca [cite: 17]

[cite_start]Este projeto foi desenvolvido como uma atividade prática para a disciplina de Programação em Python, com o objetivo de consolidar os conceitos da linguagem e o uso da biblioteca NumPy para manipulação de dados numéricos[cite: 3, 31]. [cite_start]A biblioteca implementa funcionalidades básicas de álgebra linear e geração de números aleatórios[cite: 31].

## [cite_start]Funcionalidades Implementadas [cite: 18]

A biblioteca é organizada em módulos e oferece as seguintes funções:

* **`descrever_matriz(matriz)`**: Recebe uma matriz quadrada NumPy e retorna um dicionário com seu determinante, sua matriz inversa e seus autovalores/autovetores. [cite_start]Utiliza o submódulo `numpy.linalg`[cite: 7, 12].
* **`gerar_amostra_multivariada(media, matriz_cov, n_amostras)`**: Gera uma amostra de dados pseudo-aleatórios a partir de uma distribuição normal multivariada. [cite_start]Utiliza o submódulo `numpy.random`[cite: 8, 12].

## [cite_start]Instruções de Instalação [cite: 20]

1.  Clone este repositório.
2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  Instale as dependências:
    ```bash
    pip install numpy pandas
    ```

## [cite_start]Exemplos de Uso [cite: 19]

Para usar a biblioteca, execute o script `exemplo_uso.py`.

```python
# exemplo_uso.py
import numpy as np
import pandas as pd
from matriz_estats import descrever_matriz, gerar_amostra_multivariada

# --- 1. Análise de Propriedades de uma Matriz ---
matriz = np.array([[1.0, 0.8, 0.345], [0.8, 1.0, 0.75], [0.8, 1.06,0.013])
propriedades = descrever_matriz(matriz)
print("--- Análise de Matriz ---")
print(f"> Determinante: {propriedades['determinante']:.4f}")

# --- 2. Geração de Amostra e Planilha ---
media = np.array([0, 0, 0])
n_amostras = 50
amostra = gerar_amostra_multivariada(media, matriz, n_amostras, seed=42)
df = pd.DataFrame(amostra, columns=['Variavel_1', 'Variavel_2'])
df.to_csv('amostra_gerada.csv', index=False)
print("\n--- Geração de Amostra ---")
print(f"Geradas {n_amostras} amostras e salvas em 'amostra_gerada.csv'.")
```
