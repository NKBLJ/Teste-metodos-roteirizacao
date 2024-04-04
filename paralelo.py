from functions import gerar_coord_aleat, matriz_dist
from roteirizacoes import rota_aleatoria, rota_knn, rota_heuristica, rota_prog_dinam, rota_local_search, rota_lin
import numpy as np
import time
import csv

inicio = time.time()
result = []
coord_sede = (-5.069952794832667, -42.82680303516773)

with open("dados.csv", 'a', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    for _ in range(65):
        coords = gerar_coord_aleat(20)
        distancias = np.array(matriz_dist([coord_sede]+coords))
        heurist = rota_heuristica([coord_sede] + coords)
        if type(heurist) is not int:
            print('não foi')
            continue
        resultados = [heurist, rota_prog_dinam(distancias), rota_local_search(distancias), rota_lin(distancias)]
        # print(resultados)
        # # resultados = [rota_aleatoria(distancias), rota_knn(distancias), rota_heuristica([coord_sede]+coords), rota_kernighan(distancias)]
        writer.writerow(resultados)

tempo = time.time()-inicio
print(f"Demorou: {tempo} s")