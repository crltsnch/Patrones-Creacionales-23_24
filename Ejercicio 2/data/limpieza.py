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

'''Ingredientes'''
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
#Hay valores nulos, pero no nos importa a la hora de recomendar ingredientes

#que ingredientes hay en cada columna
print(data_final["ingrediente1"].unique())


'''Masas'''
#Tipos de tamaños de pizza
#print(data_final["pizza_size"].unique())

#Ahora vamos a transformar la columna tamaño por tipos de masas, de esta manera tendremos que el tamaño S es una masa fina, el tamaño M es una masa gruesa y el tamaño L es una masa rellena de queso
data_final["pizza_size"] = data_final["pizza_size"].replace({"S": "fina", "M": "gruesa", "L": "rellena de queso", "XL": "integral", "XXL": "sin gluten"})
#print(data_final["pizza_size"].unique())

#y cambiamos el nombre de la columna
data_final = data_final.rename(columns={"pizza_size": "tipo_masa"})
#print(data_final["tipo_masa"].head())

'''Salsas'''
#Hacemos el mismo proceso de transformación con la columna pizza_category
#print(data_final["pizza_category"].unique())

#Transformamos la columna por salsa_base, teniendo que classic es tomate, veggie es pesto, supreme es salsa blanca y chicken es salsa picante
data_final["pizza_category"] = data_final["pizza_category"].replace({"Classic": "tomate", "Veggie": "pesto", "Supreme": "salsa blanca", "Chicken": "salsa picante"})
#print(data_final["pizza_category"].unique())

#y cambiamos el nombre de la columna
data_final = data_final.rename(columns={"pizza_category": "salsa_base"})
#print(data_final["salsa_base"].head())



'''------Exportar datos-------'''
#guardamos el data final en un csv en la carpeta data
data_final.to_csv("/Users/carlotasanchezgonzalez/Documents/class/Patrones-Creacionales-23_24/Ejercicio 2/data/data_final.csv", sep=";", encoding='ISO-8859-1')
