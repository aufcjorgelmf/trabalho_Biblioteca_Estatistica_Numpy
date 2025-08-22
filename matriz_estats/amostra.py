"""
     Gera uma amostra de dados seguindo uma distribuição normal multivariada.

    Esta função demonstra o uso do submódulo numpy.random, incluindo o uso
    de uma semente para reprodutibilidade.

    Args:
        media (np.ndarray): O vetor de médias (1D array).
        matriz_cov (np.ndarray): A matriz de covariância (2D array).
        n_amostras (int): O número de amostras a serem geradas.
        seed (int, optional): Semente para o gerador de números aleatórios,
                              para garantir resultados reprodutíveis. Defaults to None.

    Returns:
        np.ndarray: Um array 2D onde cada linha é uma amostra gerada.
    """
import numpy as np

def gerar_amostra_multivariada(media: np.ndarray, matriz_cov: np.ndarray, n_amostras: int, seed: int = None) -> np.ndarray:
    """
    Gera uma amostra de dados seguindo uma distribuição normal multivariada.

    Esta função demonstra o uso do submódulo numpy.random, incluindo o uso
    de uma semente para reprodutibilidade.

    Args:
        media (np.ndarray): O vetor de médias (1D array).
        matriz_cov (np.ndarray): A matriz de covariância (2D array).
        n_amostras (int): O número de amostras a serem geradas.
        seed (int, optional): Semente para o gerador de números aleatórios,
                              para garantir resultados reprodutíveis. Defaults to None.

    Returns:
        np.ndarray: Um array 2D onde cada linha é uma amostra gerada.
    """
    # Define a semente aleatória para garantir que os resultados sejam os mesmos
    # sempre que a mesma semente for usada.
    if seed is not None:
        np.random.seed(seed)

    # Gera a amostra usando a função da distribuição normal multivariada
    amostra_gerada = np.random.multivariate_normal(media, matriz_cov, n_amostras)

    return amostra_gerada