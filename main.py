from functions import gerar_coord_aleat, matriz_dist
from roteirizacoes import rota_aleatoria, rota_knn, rota_heuristica, rota_prog_dinam, rota_local_search, rota_lin
from rotapulp import rota_prog_linear
import numpy as np
import time
import csv

inicio = time.time()
result = []
coord_sede = (-5.069952794832667, -42.82680303516773)

with open("dados.csv", 'a', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    for i in range(60):
        coords = gerar_coord_aleat(20)
        distancias = np.array(matriz_dist([coord_sede]+coords))
        heurist = rota_heuristica([coord_sede] + coords)
        if type(heurist) is not int:
            continue
        resultados = [heurist, rota_prog_linear(distancias), rota_local_search(distancias), rota_lin(distancias)]
        print(i, resultados)
        writer.writerow(resultados)

tempo = time.time()-inicio
print(f"Demorou: {tempo} s")