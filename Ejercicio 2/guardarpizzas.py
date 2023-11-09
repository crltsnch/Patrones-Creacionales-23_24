'''Crear una funcion que guarde las pizzas concretas creadas en un archivo .csv con cada parte de la pizza'''
import csv
import os

def guardar_pizza_personalizada(pizza_personalizada):
    carpeta_ejercicio2 = 'Ejercicio 2'
    ruta_archivo = os.path.join(carpeta_ejercicio2, 'pizzas.csv')

    with open(ruta_archivo, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["masa", "salsabase", "ingredientes", "coccion", "presentacion", "maridaje", "extras"], delimiter=';')

        if file.tell() == 0:
            writer.writeheader()


        datos = {
            "masa": pizza_personalizada[0],
            "salsabase": pizza_personalizada[1],
            "ingredientes": pizza_personalizada[2],
            "coccion": pizza_personalizada[3],
            "presentacion": pizza_personalizada[4],
            "maridaje": pizza_personalizada[5],
            "extras": pizza_personalizada[6]
        }

        writer.writerow(datos)

    print("\nPizza guardada con éxito")
