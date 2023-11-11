from director import Director
from concretepizza import ConcretePizzaBuilder
from guardarpizzas import guardar_pizza_personalizada

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
    pizza_personalizada = builder.pizza
    pizza_personalizada.list_parts()
    
    guardar_pizza_personalizada(pizza_personalizada.parts)

    # Remember, the Builder pattern can be used without a Director class.
''' print("Custom product: ")
    builder.produce_masa()
    builder.produce_salsa()
    builder.produce_ingredientes()
    builder.produce_coccion()
    builder.produce_presentacion()
    builder.produce_maridaje()
    builder.produce_extras()
    builder.pizza.list_parts()'''