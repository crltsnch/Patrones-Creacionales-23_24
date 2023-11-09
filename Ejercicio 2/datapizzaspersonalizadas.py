import csv

def guardar_pizza_personalizada(pizza):
    with open("pizza_personalizada.csv", mode = "a", newline='') as file:
        writer = csv.writer(file, delimiter = ";")

        if file.tell() == 0