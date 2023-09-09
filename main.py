from functions import gerar_coord_aleat, matriz_dist
from roteirizacoes import rota_aleatoria, rota_knn, rota_heuristica
import numpy as np
import time
import csv


inicio = time.time()
coord_sede = (-5.069952794832667, -42.82680303516773)

with open("dados.csv", 'a', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    for _ in range(100):
        coords = gerar_coord_aleat(40)
        distancias = np.array(matriz_dist([coord_sede]+coords))
        resultados = [rota_aleatoria(distancias), rota_knn(distancias), rota_heuristica([coord_sede]+coords)]
        if type(resultados[2]) is not int:
            continue
        writer.writerow(resultados)
tempo = time.time()-inicio
print(f"Demorou: {tempo} s")
