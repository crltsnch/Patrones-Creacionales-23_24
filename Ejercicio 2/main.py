from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
import pandas as pd

data = pd.read_csv('ejercicio 2/data/data_final.csv', sep=';', encoding='ISO-8859-1')


class PizzaBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def produce_masa(self) -> None:
        pass

    @abstractmethod
    def produce_salsa(self) -> None:
        pass

    @abstractmethod
    def produce_ingredientes(self) -> None:
        pass

    @abstractmethod
    def produce_coccion(self) -> None:
        pass

    @abstractmethod
    def produce_maridaje(self) -> None:
        pass

    @abstractmethod
    def produce_extras(self) -> None:
        pass


class ConcretePizzaBuilder(PizzaBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._pizza = Pizza()

    @property
    def pizza(self) -> Pizza:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        pizza = self._pizza
        self.reset()
        return pizza

    def produce_masa(self) -> None:
        masas = data["tipo_masa"].unique()
        masa_escogida = input(f"Elige el tipo de masa que deseas entre {masas}:")

        if masa_escogida not in masas:
            print("No tenemos esa masa, por favor elige otra")
            self.produce_masa()
        else:
            self._pizza.add(f"Tipo de Masa: {masa_escogida}")

        
    def produce_salsa(self) -> None:
        salsas = data["salsa_base"].unique()
        salsa_escogida = input(f"Elige el tipo de salsa que deseas entre {salsas}:")
        if salsa_escogida not in salsas:
            print("No tenemos esa salsa, por favor elige otra")
            self.produce_salsa()
        else:
            self._pizza.add(f"Salsa Base: {salsa_escogida}")
        

    def produce_ingredientes(self) -> None:
        ingredientes = data["ingrediente1"].unique()
        ingrediente1 = input(f"Ingrese un ingrediente que desees de {ingredientes}: ")
        if ingrediente1 not in ingredientes:
            print("No tenemos ese ingrediente, por favor elige otro")
            self.produce_ingredientes()
        else:
            self._pizza.add(f"Ingredientes: {ingrediente1}")

        


        self._pizza.add(f"Ingredientes: {ingredientes}")
    
    def produce_coccion(self) -> None:
        coccion = input("Ingrese la técnica de cocción que deseas: ")
        self._pizza.add(f"Técnica de Cocción: {coccion}")
    
    def produce_maridaje(self) -> None:

        self._pizza.add("Maridaje")
    
    def produce_extras(self) -> None:
        self._pizza.add("Extra y finalización")


class Pizza():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> PizzaBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: PizzaBuilder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_pizza(self) -> None:
        self.builder.produce_masa()
        self.builder.produce_salsa()
        self.builder.produce_ingredientes()
        self.builder.produce_coccion()
        self.builder.produce_maridaje()
        self.builder.produce_extras()

if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """
    director = Director()
    builder = ConcretePizzaBuilder()
    director.builder = builder

    print("Construir pizza: ")
    director.build_pizza()
    builder.pizza.list_parts()

    # Remember, the Builder pattern can be used without a Director class.
'''    print("Custom product: ")
    builder.produce_masa()
    builder.produce_salsa()
    builder.produce_ingredientes()
    builder.produce_coccion()
    builder.produce_maridaje()
    builder.produce_extras()
    builder.pizza.list_parts()'''