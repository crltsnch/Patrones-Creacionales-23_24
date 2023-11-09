from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd

data = pd.read_csv('ejercicio 1/data/data_final.csv', sep=';', encoding='ISO-8859-1', parse_dates=['FECHA'])

class AbstractAnalisis(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def calcular_media(self):
        pass

    @abstractmethod
    def calcular_mediana(self):
        pass

    @abstractmethod
    def calcular_moda(self):
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""

class Media(AbstractAnalisis):
    def calcular_media(self):
        activaciones_por_dia = data.groupby(data['FECHA']).size()
        media = activaciones_por_dia.mean()
        return f"La media de activaciones por dia es: {media}" 

    def calcular_mediana(self):
        pass

    def calcular_moda(self):
        pass


class Mediana(AbstractAnalisis):
    def calcular_mediana(self):
        mediana = data["FECHA"].median()
        return f"La mediana de la columna fecha es: {mediana}"
    
    def calcular_media(self):
        pass

    def calcular_moda(self):
        pass

class Moda(AbstractAnalisis):
    def calcular_moda(self):
        moda = data["TIPO"].mode()

        if len(moda) > 1:
            #Si hay varios elementos en la moda, los separamos por comas
            moda_str = ", ".join(moda)
            return f"La moda de la columna tipo es: {moda_str}"
        
        else:
            #Si solo hay un elemento en la moda, lo devolvemos como string
            return f"La moda de la columna tipo es {moda.to_string(index=False)}"

    def calcular_media(self):
        pass

    def calcular_mediana(self):
        pass