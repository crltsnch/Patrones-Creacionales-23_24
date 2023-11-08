import pandas as pd

data = pd.read_csv('/Users/carlotasanchezgonzalez/Documents/class/Patrones-Creacionales-23_24/Ejercicio 2/data/Data-Model-Pizza-Sales.csv')
#print(data.head())


'''------Limpieza de datos-------'''

#Eliminamos columnas que no me sirven
colum_eliminar = ["unit_price", "total_price", "order_id", "quantity", "order_details_id"]
data_final = data.drop(colum_eliminar, axis=1)

#print(data_final.head())

#Filas tienen valores nulos
#print(data_final.isnull().sum())
#No hay valores nulos


'''------Transformación de datos-------'''
#Quiero saber los ingredientes diferentes que hay en la columna "ingredientes"
ingredientes_divididos = data_final["pizza_ingredients"].str.split(",", expand=True)

#Renombrar la soclumnas con nombres como ingrediente1
colum_names = [f"ingrediente{i+1}" for i in range(len(ingredientes_divididos.columns))]
ingredientes_divididos.columns = colum_names

#Añadir las columnas de ingredientes a data_final
data_final = pd.concat([data_final, ingredientes_divididos], axis=1)

#Eliminar la columna pizza_ingredients
data_final = data_final.drop("pizza_ingredients", axis=1)

#print(data_final.head())


#Ahora volvemos a comprobar si hay valores nulos
#print(data_final.isnull().sum())

