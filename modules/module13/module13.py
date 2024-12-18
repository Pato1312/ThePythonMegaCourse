"""
This exercise consist in locating the coordenates of the directions in the supermarkets data frame
for this is importe the geopy library (pip install geopy) and the whole coordinates, the longitude
and latitude are added as colums to the dataframe
"""

# Importar las librerías necesarias
import pandas
from geopy.geocoders import ArcGIS

# Crear una instancia del geocodificador ArcGIS
nom = ArcGIS()

# Probar geocodificación con una dirección de ejemplo
n = nom.geocode("3995 23rd St, San Francisco, CA 94114")
print("longitude : ", n.longitude, " - latitude : ", n.latitude)

# Leer el archivo CSV que contiene los datos de supermercados
geoDf = pandas.read_csv(
    "C:\\Users\\pato1\\OneDrive\\Documentos\\PythonMegaCourse\\modules\\module13\\supermarkets\\supermarkets.csv"
)

# Crear la columna 'Full Address' concatenando las columnas relevantes
geoDf["Full Address"] = (
    geoDf["Address"]
    + ", "
    + geoDf["City"]
    + ", "
    + geoDf["State"]
    + ", "
    + geoDf["Country"]
)

# Obtener las coordenadas para cada dirección utilizando geocodificación
geoDf["Coordinates"] = geoDf["Full Address"].apply(nom.geocode)

# Obtener la latitud y longitud, manejando los casos en que no se pueda geocodificar
geoDf["Latitude"] = geoDf["Coordinates"].apply(
    lambda x: x.latitude if x != None else None
)
geoDf["Longitude"] = geoDf["Coordinates"].apply(
    lambda x: x.longitude if x != None else None
)

# Eliminar la colummna "Full Address" ya que esta se creo solo para llamar a la geodecodificación
geoDf = geoDf.drop(columns=["Full Address"])

# Mostrar el DataFrame resultante
print(geoDf)
