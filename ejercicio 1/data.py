import pandas as pd

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

# Leer CSV desde la URL
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')
#print(data.head())  # Mostrar las primeras filas para visualizar los datos


#Verificar si hay filas duplicadas
#print(data.duplicated().sum())

#Eliminamos las columnas vacías y columnas que no me vayan a servir
colum_eliminar = ["PRECIO", "DIAS-EXCLUIDOS", "DESCRIPCION", "AUDIENCIA", "Unnamed: 29", "COORDENADA-Y", "COORDENADA-X", "LATITUD", "LONGITUD", "CONTENT-URL", "URL-ACTIVIDAD", "URL-INSTALACION"]
data_final = data.drop(colum_eliminar, axis=1)
#print(data_final.head())


#En la columna "TIPO" queremos quedarnos con el tipo especifico de actividad por lo que vamos a dividir y quedarnos con lo que hay despues de la ultima /
data["TIPO"] = data["TIPO"].str.split("/")
data_final["TIPO"] = data["TIPO"].str[-1]
#print(data_final.head())


#Tipos de datos que tenemos
#print(data.dtypes)


#Fecha, fecha-fin y hota son object por lo que vamos a convertirlos a datetime. Vamos a convertir FECHA, FECHA-FIN y HORA a formato fecha
data_final["FECHA"] = pd.to_datetime(data["FECHA"])
data_final["FECHA-FIN"] = pd.to_datetime(data["FECHA-FIN"])
data_final["HORA"] = pd.to_datetime(data["HORA"], format="%H:%M")


print(data_final.head())
#print(data_final.dtypes)

#guardamos el data final en un csv en la carpeta data
data_final.to_csv("/Users/carlotasanchezgonzalez/Documents/class/Patrones-Creacionales-23_24/ejercicio 1/data/data_final.csv", sep=";", index=False)