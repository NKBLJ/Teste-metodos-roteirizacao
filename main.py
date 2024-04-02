from functions import gerar_coord_aleat, matriz_dist
from roteirizacoes import rota_aleatoria, rota_knn, rota_heuristica, rota_branch
import numpy as np
import time
import csv

inicio = time.time()
result = []
coord_sede = (-5.069952794832667, -42.82680303516773)

with open("dados.csv", 'a', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    for _ in range(3):
        coords = gerar_coord_aleat(20)
        distancias = np.array(matriz_dist([coord_sede]+coords))
        print(distancias)
        print(rota_branch(distancias))
        # resultados = [rota_heuristica([coord_sede]+coords), ]
        # # resultados = [rota_aleatoria(distancias), rota_knn(distancias), rota_heuristica([coord_sede]+coords), rota_kernighan(distancias)]
        # if type(resultados[2]) is not int:
        #     continue
        # writer.writerow(resultados)

tempo = time.time()-inicio
print(f"Demorou: {tempo} s")