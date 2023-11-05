from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd

data = pd.read_csv('data_final.csv', sep=';')

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
        return media(), mediana(), moda()

    def mostrarVisualizacion(self) -> AbstractVisulizacion:
        return None


class ConcreteVisualizacionFactory(SamurAbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def realizarAnalisis(self) -> AbstractAnalisis:
        return None

    def mostrarVisualizacion(self) -> AbstractVisualizacion:
        return histograma(), diagramaDeBarras()
    

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
        media = data.groupby(data['FECHA'].dt.date)['ACTIVACIONES'].mean()
        return f"La media de activaciones por dia es {media}" 


class Mediana(AbstractAnalisis):
    def useful_function_a(self) -> str:
        return "The result of the product A2."

class Moda(AbstractAnalisis):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())