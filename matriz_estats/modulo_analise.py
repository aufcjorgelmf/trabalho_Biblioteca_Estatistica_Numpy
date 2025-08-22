import numpy as np

def descrever_matriz(matriz: np.ndarray) -> dict:
    """
    Analisa uma matriz quadrada e calcula suas principais propriedades de álgebra linear.

    Esta função demonstra o uso do submódulo numpy.linalg.

    Args:
        matriz (np.ndarray): Uma matriz quadrada (array NumPy 2D).

    Returns:
        dict: Um dicionário contendo o determinante, a matriz inversa (se existir),
              os autovalores e os autovetores.
              
    Raises:
        ValueError: Se a matriz não for quadrada.
    """
    # Validação inicial: verifica se a matriz é quadrada
    if matriz.shape[0] != matriz.shape[1]:
        raise ValueError("A matriz de entrada deve ser quadrada.")

    # Dicionário para armazenar os resultados
    propriedades = {}

    # 1. Cálculo do determinante
    propriedades['determinante'] = np.linalg.det(matriz)

    # 2. Cálculo da matriz inversa
    # Usamos try/except para o caso de matrizes singulares (determinante=0)
    try:
        propriedades['matriz_inversa'] = np.linalg.inv(matriz)
    except np.linalg.LinAlgError:
        propriedades['matriz_inversa'] = "Não existe (matriz singular)."

    # 3. Cálculo dos autovalores e autovetores
    autovalores, autovetores = np.linalg.eig(matriz)
    propriedades['autovalores'] = autovalores
    propriedades['autovetores'] = autovetores

    return propriedades