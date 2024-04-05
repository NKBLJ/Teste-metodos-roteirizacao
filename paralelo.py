from functions import gerar_coord_aleat, matriz_dist
from roteirizacoes import rota_aleatoria, rota_knn, rota_heuristica, rota_prog_dinam, rota_local_search, rota_lin
import numpy as np
import time
import csv
from joblib import Parallel, delayed


def roteirizar():
    coords = gerar_coord_aleat(10)
    distancias = np.array(matriz_dist([coord_sede] + coords))
    heurist = rota_heuristica([coord_sede] + coords)
    if type(heurist) is int:
        resultados = [heurist, rota_prog_dinam(distancias), rota_local_search(distancias), rota_lin(distancias)]
        return resultados
    else:
        return None



inicio = time.time()
coord_sede = (-5.069952794832667, -42.82680303516773)

with open("dados.csv", 'a', newline='') as arquivo_csv:
    resultados = Parallel(n_jobs=4)(delayed(roteirizar)() for _ in range(4))
    print(resultados)
    # writer = csv.writer(arquivo_csv)
    # writer.writerow(resultados)


tempo = time.time()-inicio
print(f"Demorou: {tempo} s")