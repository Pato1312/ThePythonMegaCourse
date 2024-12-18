import pandas as pd
import folium as fl

"""
This is my version for the app of the section 15 of "The Python Mega Course"

The changes i did from the code presented in the course are:
    * I the implementation of the challenge of making html popup for the markers, 
    also adding volcano at the end of the name to get better search results
    * My map is a satellite version using Esri 
    * PopulationColour Function for better understanding
"""


def elevationColour(elevation):
    if elevation < 1500:
        return "green"
    elif 1500 <= elevation < 3500:
        return "orange"
    else:
        return "red"


def populationColour(population):
    if population < 10_000_000:
        return "green"
    elif 10_000_000 <= population < 20_000_000:
        return "orange"
    else:
        return "red"


# HTML para los popups en el mapa
html = """
Volcano information:<br>
Name: <a href="https://www.google.com/search?q=%s+volcano" target="_blank">%s</a><br>
Elevation: %s m<br>
Location: %s<br>
Status: %s<br>
"""

# Cargar el archivo de datos
volcanoes = pd.read_csv(
    "C:\\Users\\pato1\\OneDrive\\Documentos\\PythonMegaCourse\\Apps\\App1 web mapping\\Volcanoes.txt"
)

# Crear listas para las columnas de datos necesarias
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
elev = list(volcanoes["ELEV"])
name = list(volcanoes["NAME"])
locat = list(volcanoes["LOCATION"])
stat = list(volcanoes["STATUS"])

# Crear el mapa inicial
map = fl.Map(
    location=[38.58, -99.09],
    zoom_start=5,
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri",
    overlay=False,
    control=True,
)

# Crear un grupo de características
fgV = fl.FeatureGroup(name="Volcanoes in the USA")

for lt, ln, nm, el, lc, st in zip(lat, lon, name, elev, locat, stat):
    iframe = fl.IFrame(html=html % (nm, nm, el, lc, st), width=250, height=150)
    fgV.add_child(
        fl.CircleMarker(
            location=[lt, ln],
            popup=fl.Popup(iframe),
            fill=True,
            fill_color=elevationColour(el),
            color=elevationColour(el),
            fill_opacity=0.7,
        )
    )

fgP = fl.FeatureGroup(name="2005 Population")
fgP.add_child(
    fl.GeoJson(
        data=open(
            "C:\\Users\\pato1\\OneDrive\\Documentos\\PythonMegaCourse\\Apps\\App1 web mapping\\world.json",
            "r",
            encoding="utf-8-sig",
        ).read(),
        style_function=lambda x: {
            "fillColor": populationColour(x["properties"]["POP2005"])
        },
    )
)


# Añadir el grupo al mapa
map.add_child(fgV)
map.add_child(fgP)

map.add_child(fl.LayerControl())

# Guardar el mapa en un archivo HTML
map.save("volcanoesPopulationMap.html")
