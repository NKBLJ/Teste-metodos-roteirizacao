from functions import gerar_coord_aleat, matriz_dist
from roteirizacoes import rota_aleatoria, rota_knn, rota_heuristica
import numpy as np
import time

inicio = time.time()
result = []
coord_sede = (-5.069952794832667, -42.82680303516773)

for _ in range(10):
    coords = gerar_coord_aleat(40)

    distancias = np.array(matriz_dist([coord_sede]+coords))
    resultados = [rota_aleatoria(distancias), rota_knn(distancias), rota_heuristica([coord_sede]+coords)]
    if type(resultados[2]) is not int:
        continue
    result.append(resultados)

print(result)
tempo = time.time()-inicio
print(f"Demorou: {tempo} s")