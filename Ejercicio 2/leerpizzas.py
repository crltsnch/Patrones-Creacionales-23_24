import csv

def leer_pizzas_desde_csv(archivo_csv):
    pizzas = []
    with open(archivo_csv, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            pizzas.append(row)
    return pizzas

def reconstruir_pizza(datos):
    pizza = f"Tipo de Masa: {datos['masa']}\n"
    pizza += f"Salsa Base: {datos['salsabase']}\n"
    pizza += f"Ingredientes: {datos['ingredientes']}\n"
    pizza += f"Técnica de Cocción: {datos['coccion']}\n"
    pizza += f"Presentación: {datos['presentacion']}\n"
    pizza += f"Maridaje: {datos['maridaje']}\n"
    pizza += f"Extra y finalización: {datos['extras']}\n"
    return pizza

if __name__ == "__main__":
    archivo_csv = 'Ejercicio 2/pizzas.csv'

    # Leer datos del archivo CSV
    pizzas = leer_pizzas_desde_csv(archivo_csv)

    # Reconstruir y mostrar cada pizza
    for pizza in pizzas:
        pizza_reconstruida = reconstruir_pizza(pizza)
        print(pizza_reconstruida)
