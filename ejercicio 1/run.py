from __future__ import annotations
from codigocliente import client_code
from factorias import ConcreteAnalisisFactory, ConcreteVisualizacionFactory

if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteAnalisisFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteVisualizacionFactory())