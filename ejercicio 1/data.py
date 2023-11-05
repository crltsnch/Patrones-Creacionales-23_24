import pandas as pd

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

# Leer CSV desde la URL
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')
print(data.head())  # Mostrar las primeras filas para visualizar los datos


#Eliminamos las columnas vacías
colum_eliminar = ["PRECIO", "DIAS-EXCLUIDOS", "DESCRIPCION", "AUDIENCIA", "Unnamed: 29"]
data = data.drop(colum_eliminar, axis=1)
print(data.head())