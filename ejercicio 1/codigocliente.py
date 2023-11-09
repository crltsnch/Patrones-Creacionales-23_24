from factorias import SamurAbstractFactory

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
            v.mostrar_histograma()
            v.mostrar_grafico_barras()