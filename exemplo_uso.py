import numpy as np

# Importa as funções da nossa biblioteca
from matriz_estats.modulo_analise import descrever_matriz
from matriz_estats.amostra import gerar_amostra_multivariada



if __name__ == "__main__":
    print("===== DEMONSTRAÇÃO DA BIBLIOTECA MatrixStats =====")

    # --- 1. Exemplo de uso do módulo de Análise (numpy.linalg) ---
    print("\n--- 1. Análise de Propriedades de uma Matriz ---")
    
    # Matriz de correlação (positivamente correlacionada)
    matriz = np.array([
        [1.0, 0.8, 0.345],
        [0.8, 1.0, 0.75],
        [0.8, 1.06,0.013]
    ])
    
    print("\nAnalisando a matriz:")
    print(matriz)
    
    propriedades = descrever_matriz(matriz)
    
    print(f"\n> Determinante: {propriedades['determinante']:.4f}")
    print(f"> Matriz Inversa:\n{propriedades['matriz_inversa']}")
    print(f"> Autovalores: {propriedades['autovalores']}")

    # --- 2. Exemplo de uso do módulo de Amostragem (numpy.random) ---
    print("\n--- 2. Geração de Amostra Aleatória Multivariada ---")
    
    media = np.array([0, 0, 0])  # Média zero para as duas variáveis
    n_amostras = 5
    semente = 42 # Usando uma semente para resultados consistentes
    
    print(f"\nGerando {n_amostras} amostras com média [0, 0, 0] e semente={semente}:")
    
    amostra = gerar_amostra_multivariada(media, matriz, n_amostras, seed=semente)
    
    print(amostra)
    
    print("\nGerando novamente com a mesma semente para provar a reprodutibilidade:")
    amostra_repetida = gerar_amostra_multivariada(media, matriz, n_amostras, seed=semente)
    print(amostra_repetida)
    
    print("\nPerceba que as duas amostras geradas são idênticas!")