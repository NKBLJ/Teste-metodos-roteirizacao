import geopandas as gpd
import random
from fiona.drvsupport import supported_drivers
import requests
import os


supported_drivers['KML'] = 'rw'
api_key = os.get.environ('API-KEY')


def gerar_coord_aleat(quantidade):
    """Abre o arquivo KML e gera coordenadas aleatórias dentros das regiões do arquivo"""
    dados_geograficos = gpd.read_file('data/doc.kml', driver='KML')
    coordenadas_aleatorias = []

    for _ in range(quantidade):
        indice_aleatorio = random.randint(0, len(dados_geograficos) - 1)

        geometria_regiao = dados_geograficos['geometry'].iloc[indice_aleatorio]

        minx, miny, maxx, maxy = geometria_regiao.bounds

        x = random.uniform(minx, maxx)
        y = random.uniform(miny, maxy)

        coordenadas_aleatorias.append((y, x))

    return coordenadas_aleatorias


def matriz_dist(coordenadas):
    """Usa uma lista de coordenadas em [(lat, long)...] e retorna uma matriz de distâncias entre cada um dos pontos, usando a api do OPENROUTE"""
    # Corpo da requisição POST
    payload = {
        "locations": [list(reversed(coord)) for coord in coordenadas],
        "metrics": ["distance"],  # Solicitar distâncias e durações otimizadas
        "units": "m",  # Unidade de distância: metros
        "profile": "driving-car"  # Modo de transporte: carro
    }

    # URL da API do OpenRouteService para calcular a matriz de roteamento de carro
    url = f"https://api.openrouteservice.org/v2/matrix/driving-car"

    # Cabeçalho da requisição com a chave de API
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Faz a requisição à API
    response = requests.post(url, json=payload, headers=headers)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        resposta = response.json()
        return resposta['distances']
