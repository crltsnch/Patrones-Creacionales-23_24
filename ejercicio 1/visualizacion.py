from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ejercicio 1/data/data_final.csv', sep=';', encoding='ISO-8859-1', parse_dates=['FECHA'])


class AbstractVisualizacion(ABC):
    """
    Here's the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def mostrar_histograma(self):
        pass

    @abstractmethod
    def mostrar_grafico_barras(self):
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class Histograma(AbstractVisualizacion):
    def mostrar_histograma(self):
        activaciones_por_dia = data['FECHA'].dt.date.value_counts().sort_index()
        plt.figure(figsize=(12, 6))
        plt.bar(activaciones_por_dia.index, activaciones_por_dia.values, width=0.8, align='center')
        plt.xlabel('Fecha')
        plt.ylabel('Número de Activaciones')
        plt.title('Histograma de Activaciones por Día')
        plt.xticks(rotation=45)
        plt.show()

    def mostrar_grafico_barras(self):
        pass


class GraficoDeBarras(AbstractVisualizacion):
    def mostrar_grafico_barras(self):
        activaciones_por_tipo = data['TIPO'].value_counts()
        plt.figure(figsize=(12, 6))
        plt.bar(activaciones_por_tipo.index, activaciones_por_tipo.values, width=0.8, align='center')
        plt.xlabel('Tipo de Activación')
        plt.ylabel('Número de Activaciones')
        plt.title('Gráfico de Barras de Activaciones por Tipo')
        plt.xticks(rotation=45)
        plt.show()

    def mostrar_histograma(self):
        pass
