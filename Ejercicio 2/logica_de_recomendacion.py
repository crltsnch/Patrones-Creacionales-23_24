import pandas as pd

data = pd.read_csv('/Users/carlotasanchezgonzalez/Documents/class/Patrones-Creacionales-23_24/Ejercicio 2/data/data_final.csv')

class RecomendacionOpcion:
    def __init__(self):
        pass

    def masa_opcion(self, masa_seleccionada):
        masas = data["tipo_masa"].unique()
        if masa_seleccionada in masas:
            return masa_seleccionada
        else:
            return "masa no disponible"
    
    