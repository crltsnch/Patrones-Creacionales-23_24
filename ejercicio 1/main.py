from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ejercicio 1/data/data_final.csv', sep=';', encoding='ISO-8859-1', parse_dates=['FECHA'])

class SamurAbstractFactory(ABC):
    """
    The Samur Abstract Factory interface declares a set of methods that return
    different abstract products.
    """
    @abstractmethod
    def realizarAnalisis(self) -> AbstractAnalisis:
        pass

    @abstractmethod
    def mostrarVisualizacion(self) -> AbstractVisualizacion:
        pass


class ConcreteAnalisisFactory(SamurAbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def realizarAnalisis(self) -> AbstractAnalisis:
        return Media(), Mediana(), Moda()

    def mostrarVisualizacion(self) -> AbstractVisualizacion:
        return None


class ConcreteVisualizacionFactory(SamurAbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def realizarAnalisis(self) -> AbstractAnalisis:
        return None

    def mostrarVisualizacion(self) -> AbstractVisualizacion:
        return Histograma(), GraficoDeBarras()
    

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
        media = data.groupby(data['FECHA'].dt.date)['Unnamed: 0'].mean()
        return f"La media de la fecha de inicio de las actividades es: {media}" 

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
        return plt.show()

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
        return plt.show()

    def mostrar_histograma(self):
        pass


def client_code(factory: SamurAbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    analisis = factory.realizarAnalisis()
    visualizacion = factory.mostrarVisualizacion()

    
    if analisis is not None:
        for a in analisis:
            print(f"{a.calcular_media()}\n", end="")
            print(f"{a.calcular_mediana()}\n", end="")
            print(f"{a.calcular_moda()}\n", end="")
    
    if visualizacion is not None:
        for v in visualizacion:
            print(f"{v.mostrar_histograma()}")
            print(f"{v.mostrar_grafico_barras()}")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteAnalisisFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteVisualizacionFactory())