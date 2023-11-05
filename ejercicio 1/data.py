import pandas as pd

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

# Leer CSV desde la URL
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')
print(data.head())  # Mostrar las primeras filas para visualizar los datos


#Eliminamos las columnas vacías y columnas que no me vayan a servir
colum_eliminar = ["PRECIO", "DIAS-EXCLUIDOS", "DESCRIPCION", "AUDIENCIA", "Unnamed: 29", ]
data = data.drop(colum_eliminar, axis=1)
print(data.head())

#En la columna "TIPO" queremos quedarnos con el tipo especifico de actividad por lo que vamos a quedarnos con lo que hay despues de la ultima /
data["TIPO"] = data["TIPO"].str.split("/").str[-1]
print(data.head())