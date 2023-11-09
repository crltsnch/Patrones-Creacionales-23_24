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
            resultado = a.calcular_media()
            if resultado is not None:
                print(resultado)
            resultado = a.calcular_mediana()
            if resultado is not None:
                print(resultado)
            resultado = a.calcular_moda()
            if resultado is not None:
                print(resultado)

    
    if visualizacion is not None:
        for v in visualizacion:
            v.mostrar_histograma()
            v.mostrar_grafico_barras()