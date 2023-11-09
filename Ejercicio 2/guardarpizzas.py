'''Crear una funcion que guarde las pizzas concretas creadas en un archivo .csv con cada parte de la pizza'''

import csv
def guardar_pizza_personalizada(pizza_personalizada):
    with open('pizzas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        index = True
        writer.writerow(pizza_personalizada)
    print("/nPizza guardada con éxito")
