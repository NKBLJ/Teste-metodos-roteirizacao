import folium
from functions import gerar_coord_aleat


coord_sede = (-5.069952794832667, -42.82680303516773)
coords = gerar_coord_aleat(11)
# Gerar mapa
m = folium.Map(location=coord_sede, tiles="cartodbpositron", zoom_start=13)
folium.Marker(location=coord_sede).add_to(m)
for coord in coords:
    folium.Marker(location=coord).add_to(m)
m.save('mapa.html')