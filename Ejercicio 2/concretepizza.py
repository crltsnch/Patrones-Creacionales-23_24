from __future__ import annotations
from pizzabuilder import PizzaBuilder
from pizza import Pizza
import pandas as pd


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
            return masa_escogida

        
    def produce_salsa(self) -> None:
        salsas = data["salsa_base"].unique()
        salsa_escogida = input(f"Elige el tipo de salsa que deseas entre {salsas}:")
        if salsa_escogida not in salsas:
            print("No tenemos esa salsa, por favor elige otra")
            self.produce_salsa()
        else:
            self._pizza.add(f"Salsa Base: {salsa_escogida}")
            return salsa_escogida

    def produce_ingredientes(self) -> None:
        ingredientes = []

        ingredientes1 = data["ingrediente1"].unique()
        ingrediente1 = input(f"Ingrese un ingrediente que desees de {ingredientes1}: ")
        if ingrediente1 not in ingredientes1:
            print("No tenemos ese ingrediente, por favor elige otro")
            self.produce_ingredientes()
        else:
            ingredientes.append(ingrediente1)
            

        #queremos pedile 3 ingredientes mas, recomendandole los ingredientes de las mismas filas que el ingrediente1 escogido
        ingredientes2 = data[data["ingrediente1"] == ingrediente1]["ingrediente2"].unique()
        ingrediente2 = input(f"Ingrese el segundo ingrediente que desees, te recomendamos {ingredientes2}: ")
        ingredientes.append(ingrediente2)

        ingredientes3 = data[data["ingrediente1"] == ingrediente1]["ingrediente3"].unique()
        ingredientes3_sin_nan = [ingrediente for ingrediente in ingredientes3 if not pd.isna(ingrediente)]
        ingrediente3 = input(f"Ingrese el tercer ingrediente que desees, te recomendamos {ingredientes3_sin_nan}: ")
        ingredientes.append(ingrediente3)

        ingredientes4 = data[data["ingrediente1"] == ingrediente1]["ingrediente4"].unique()
        ingredientes4_sin_nan = [ingrediente for ingrediente in ingredientes4 if not pd.isna(ingrediente)]
        ingrediente4 = input(f"Ingrese el cuarto ingrediente que desees, te recomendamos {ingredientes4_sin_nan}: ")
        ingredientes.append(ingrediente4)

        self._pizza.add(f"Ingredientes: {ingredientes}")
    
    def produce_coccion(self, masa_escogida: str) -> None:
        tecnicas = ["horno de leña", "horno convencional", "parrilla"]

        if masa_escogida == "fina":
            coccion = input(f"Ingrese la técnica de cocción que deseas {tecnicas}, como has elegido masa fina, te recomendamos horno de leña: ")
            if coccion not in tecnicas:
                print("No tenemos esa técnica de cocción, por favor elige otra")
                self.produce_coccion(masa_escogida)
            else:
                self._pizza.add(f"Técnica de Cocción: {coccion}")

        elif masa_escogida == "gruesa":
            coccion = input(f"Ingrese la técnica de cocción que deseas {tecnicas}, como has elegido masa gruesa, te recomendamos parrilla: ")
            if coccion not in tecnicas:
                print("No tenemos esa técnica de cocción, por favor elige otra")
                self.produce_coccion(masa_escogida)
            else:
                self._pizza.add(f"Técnica de Cocción: {coccion}")

        elif masa_escogida == "integral" or masa_escogida == "sin gluten":
            coccion = input(f"Ingrese la técnica de cocción que deseas {tecnicas}, como has elegigo masa {masa_escogida} te recomendamos horno convencional: ")
            if coccion not in tecnicas:
                print("No tenemos esa técnica de cocción, por favor elige otra")
                self.produce_coccion(masa_escogida)
            else:
                self._pizza.add(f"Técnica de Cocción: {coccion}")
    
    def produce_presentacion(self) -> None:
        presentaciones = ["estilo clasico", "estilo mediterraneo", "estilo moderno"]
        presentacion = input(f"Ingrese la presentación que deseas {presentaciones}: ")
        if presentacion not in presentaciones:
            print("No tenemos esa presentación, por favor elige otra")
            self.produce_presentacion()
        else:
            self._pizza.add(f"Presentación: {presentacion}")

    def produce_maridaje(self, salsa_escogida: str) -> None:
        maridajes = ["Garnacha", "Chardonnay", "Viura", "Albariño", "cerveza de trigo", "cerveza rubia", "cerveza tostada", "cerveza con limon", "limonada casera", "agua con gas", "agua", "cola", "leche"]
        print(f"Nuestra seleccion de maridajes es {maridajes}")

        if salsa_escogida == "tomate":
            maridaje = input(f"Ingrese el maridaje que deseas, como has elegido salsa de tomate, te recomendamos un Garnacha, cerveza de trigo o nuestra limonada casera: ")
            if maridaje not in maridajes:
                print("No tenemos ese maridaje, por favor elige otro")
                self.produce_maridaje(salsa_escogida)
            else:
                self._pizza.add(f"Maridaje: {maridaje}")

        elif salsa_escogida == "pesto":
            maridaje = input(f"Ingrese el maridaje que deseas, como has elegido salsa de pesto, te recomendamos un Chardonnay, una cerveza rubia o agua con gas: ")
            if maridaje not in maridajes:
                print("No tenemos ese maridaje, por favor elige otro")
                self.produce_maridaje(salsa_escogida)
            else:
                self._pizza.add(f"Maridaje: {maridaje}")

        elif salsa_escogida == "salsa blanca":
            maridaje = input(f"Ingrese el maridaje que deseas, como has elegido salsa blanca, te recomendamos un Viura, una cerveza tostada o cola: ")
            if maridaje not in maridajes:
                print("No tenemos ese maridaje, por favor elige otro")
                self.produce_maridaje(salsa_escogida)
            else:
                self._pizza.add(f"Maridaje: {maridaje}")
        
        else:
            maridaje = input(f"Ingrese el maridaje que deseas, como has elegido salsa picante, te recomendamos un Albariño, una cerveza con limon o leche: ")
            if maridaje not in maridajes:
                print("No tenemos ese maridaje, por favor elige otro")
                self.produce_maridaje(salsa_escogida)
            else:
                self._pizza.add(f"Maridaje: {maridaje}")

    
    def produce_extras(self) -> None:
        finalizacion = ["caviar", "trufa", "foie", "aceite picante", "rucula"]
        extra = input(f"Ingrese el extra que deseas {finalizacion}: ")
        if extra not in finalizacion:
            print("No tenemos ese extra, por favor elige otro")
            self.produce_extras()
        else:
            self._pizza.add(f"Extra y finalización: {extra}")