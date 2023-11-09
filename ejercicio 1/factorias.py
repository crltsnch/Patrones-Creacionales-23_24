from __future__ import annotations
from abc import ABC, abstractmethod
from analisis import AbstractAnalisis, Media, Mediana, Moda
from visualizacion import AbstractVisualizacion, Histograma, GraficoDeBarras

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
    