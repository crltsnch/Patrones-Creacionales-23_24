from pizzabuilder import PizzaBuilder


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
        masa_escogida = self.builder.produce_masa()
        salsa_escogida = self.builder.produce_salsa()
        self.builder.produce_ingredientes()
        self.builder.produce_coccion(masa_escogida)   #le pasamos la masa escogida para hacer uso en la funcion coccion para que nos recomiende la técnica de cocción
        self.builder.produce_presentacion()
        self.builder.produce_maridaje(salsa_escogida)  #le pasamos la salsa escogida para hacer uso en la funcion maridaje de la salsa base escogida
        self.builder.produce_extras()