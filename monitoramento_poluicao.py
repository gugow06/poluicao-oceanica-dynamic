import numpy as np

def calcular_distancia(ponto1, ponto2):
    """
    Calcula a distância Euclidiana entre dois pontos no plano 2D.
    Args:
        ponto1 (tuple): Coordenadas (x, y) do primeiro ponto.
        ponto2 (tuple): Coordenadas (x, y) do segundo ponto.
    Returns:
        float: Distância entre os pontos.
    """
    x1, y1 = ponto1
    x2, y2 = ponto2
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def encontrar_distribuicao_otima_sensores(pontos, num_sensores):
    """
    Encontra a distribuição ótima de sensores subaquáticos usando programação dinâmica.
    Args:
        pontos (list): Lista de coordenadas (x, y) dos pontos onde os sensores podem ser alocados.
        num_sensores (int): Número de sensores a serem alocados.
    Returns:
        list: Índices dos pontos selecionados para a alocação dos sensores.
    """
    n = len(pontos)
    dp = np.inf * np.ones((n, num_sensores + 1))
    dp[0][0] = 0

    for i in range(1, n):
        for j in range(num_sensores + 1):
            dp[i][j] = dp[i - 1][j]
            for k in range(i):
                dp[i][j] = min(dp[i][j], dp[k][j - 1] + calcular_distancia(pontos[k], pontos[i]))

    # Reconstruir a solução
    indices_selecionados = []
    i, j = n - 1, num_sensores
    while j > 0:
        if dp[i][j] != dp[i - 1][j]:
            indices_selecionados.append(i)
            j -= 1
        i -= 1

    return indices_selecionados[::-1]

# Exemplo de uso
pontos = [(0, 0), (1, 2), (3, 1), (4, 3), (5, 4)]
num_sensores = 2
sensores_selecionados = encontrar_distribuicao_otima_sensores(pontos, num_sensores)

print("A distribuição ótima calculada para a quantidade de sensores determinadas são nos selecionados pontos:\n")
print(f'Pontos selecionados: {pontos}\n')
for indice in sensores_selecionados:
    print(f"Sugestão de sensor no seguinte ponto {indice}: {pontos[indice]}")