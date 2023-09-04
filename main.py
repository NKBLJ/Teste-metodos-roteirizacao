from functions import gerar_coord_aleat, matriz_dist
from roteirizacoes import rota_aleatoria, rota_knn, rota_heuristica
import numpy as np
import time
from fiona.drvsupport import supported_drivers
import geopandas as gpd

dados_geograficos = gpd.read_file('data/doc.kml', driver='KML')

coord_sede = (-5.069952794832667, -42.82680303516773)
ini1 = time.time()
coords = gerar_coord_aleat(40, dados_geograficos)
print(time.time()-ini1)

ini2 = time.time()
distancias = np.array(matriz_dist([coord_sede]+coords))
print(time.time()-ini2)
ini3 = time.time()
resultados = [rota_aleatoria(distancias), rota_knn(distancias), rota_heuristica([coord_sede]+coords)]
print(time.time()-ini3)
print(resultados)