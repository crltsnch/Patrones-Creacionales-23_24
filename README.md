# Patrones-Creacionales-23_24

El link a mi repositorio es: [GitHub](https://github.com/crltsnch/Patrones-Creacionales-23_24.git)

## Ejercicio 1: Análisis Modular de las Activaciones del SAMUR-Protección Civil en Madrid con Abstract Factory

A lo largo del año, el SAMUR lleva a cabo múltiples "activaciones" en respuesta a diversas situaciones, desde accidentes de tráfico hasta emergencias médicas. La ciudad de Madrid, en su compromiso con la transparencia y la apertura de datos, publica un registro detallado de estas activaciones en formato CSV. Este registro incluye información como la fecha, hora, tipo de emergencia, y otros detalles relevantes de cada activación.

Mi tarea es desarrollar un programa en Python que haga uso del patrón de diseño "Abstract Factory" para modularizar y estandarizar el análisis de estos datos:
1. Acceder y leer el csv: [Activaciones del Samur](https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv)
2. Modelar y estructurar los datos para su análisis
3. Diseñar un "Abstract Factory" que permita crear diferentes tipos de análisis o representaciones de los datos.
4. Utilizar las fábricas creadas para generar distintos análisis y representaciones de los datos. Mostrar la media de activaciones por día, y un histograma de las activaciones.

Para este ejercicio primero hemos limpiado y estructurado los datos del data y lo hemos guardado en un nuevo csv en la carpeta data:

### data.py

```
import pandas as pd

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

# Leer CSV desde la URL
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')
#print(data.head())  # Mostrar las primeras filas para visualizar los datos


#Verificar si hay filas duplicadas
#print(data.duplicated().sum())

#Eliminamos las columnas vacías y columnas que no me vayan a servir
colum_eliminar = ["PRECIO", "DIAS-EXCLUIDOS", "DESCRIPCION", "AUDIENCIA", "Unnamed: 29", "COORDENADA-Y", "COORDENADA-X", "LATITUD", "LONGITUD", "CONTENT-URL", "URL-ACTIVIDAD", "URL-INSTALACION"]
data_final = data.drop(colum_eliminar, axis=1)
#print(data_final.head())


#En la columna "TIPO" queremos quedarnos con el tipo especifico de actividad por lo que vamos a dividir y quedarnos con lo que hay despues de la ultima /
data["TIPO"] = data["TIPO"].str.split("/")
data_final["TIPO"] = data["TIPO"].str[-1]
#print(data_final.head())


#Tipos de datos que tenemos
#print(data.dtypes)


#Fecha, fecha-fin y hota son object por lo que vamos a convertirlos a datetime. Vamos a convertir FECHA, FECHA-FIN y HORA a formato fecha
data_final["FECHA"] = pd.to_datetime(data["FECHA"])
data_final["FECHA-FIN"] = pd.to_datetime(data["FECHA-FIN"])
data_final["HORA"] = pd.to_datetime(data["HORA"])


print(data_final.head())
#print(data_final.dtypes)

#guardamos el data final en un csv en la carpeta data
data_final.to_csv("/Users/carlotasanchezgonzalez/Documents/class/Patrones-Creacionales-23_24/ejercicio 1/data/data_final.csv", sep=";", encoding='ISO-8859-1')
```
Después he aplicado el patrón abstract factory

### facotrias.py
En este ficheor creamos la factoria abstracta SammurAbstractFactory y las facotiras concretas, una sera para analisis estadísticos y otra para visualización de gráficas: ConcreteAnalisisFactory y ConcreteVisualizacionFactory

```
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
```

### analisis.py
En este implementamos la clase abstracta de analisis y los productos concretos media, moda y mediana.

```
from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd

data = pd.read_csv('ejercicio 1/data/data_final.csv', sep=';', encoding='ISO-8859-1', parse_dates=['FECHA'])

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
        activaciones_por_dia = data.groupby(data['FECHA']).size()
        media = activaciones_por_dia.mean()
        return f"La media de activaciones por dia es: {media}" 

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
```

### visualizacion.py
Aquí implementamos la clase abstracta visualizacion y los productos concretos de visualizacion histograma y gráfico de barras.

```
from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ejercicio 1/data/data_final.csv', sep=';', encoding='ISO-8859-1', parse_dates=['FECHA'])


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
        plt.show()

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
        plt.show()

    def mostrar_histograma(self):
        pass
```

### codigocliente.py
Aquí es donde trabaja con las facotiras y los productos solo mediante factorias y productos abstractos.
```
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

```

### run.py
Aqui ejecutamos el programa.
```
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

```

Como salida esto nos dará:
```
Client: Testing client code with the first factory type:
La media de activaciones por dia es: 1.8888888888888888
La mediana de la columna fecha es: 2023-10-02 00:00:00
La moda de la columna tipo es: ActividadesDeportivas, CarrerasMaratones
```

Y las dos gráficas: histogramas por activacion y gráfico de barras por tipo de actividades.
![histograma](https://github.com/crltsnch/Patrones-Creacionales-23_24/assets/91721777/1f6ea96b-f8fc-431a-8fa7-0f53e598c045)

![grafico_de_barras](https://github.com/crltsnch/Patrones-Creacionales-23_24/assets/91721777/d1911b1e-8368-41ef-8316-8ce38f230944)


## Ejercicio 2: Sistema Integral de Creación y Gestión de Pizzas Gourmet con Almacenamiento en CSV utilizando el Patrón Builder
La cadena de pizzerías gourmet "Delizioso" está desarrollando una plataforma digital que permitirá a los clientes personalizar sus pizzas con gran detalle. Las características clave incluyen una amplia variedad de opciones: tipo de masa, salsa base, ingredientes, técnicas de cocción, presentación, maridajes recomendados y extras. El objetivo del proyecto es:

- Diseñar un sistema utilizando el patrón Builder que permita a los clientes crear sus pizzas paso a paso.

- Validar cada elección del cliente para asegurarse de que sea compatible con las selecciones anteriores.

- Implementar un sistema de recomendaciones basado en las elecciones anteriores del cliente.

- Desarrollar un módulo que guarde los detalles de cada pizza personalizada en un archivo CSV.

- Crear una funcionalidad que permita leer el archivo CSV y reconstruir la pizza para su visualización, edición o reorden.

- Mantener la flexibilidad del sistema para futuras actualizaciones y modificaciones.

- Diseñar una interfaz de usuario amigable que guíe a los clientes en el proceso de creación y proporcione información relevante.

- Implementar medidas de seguridad para proteger la integridad de los datos y la privacidad de las elecciones de los clientes.

El uso del patrón Builder permite construir pizzas personalizadas de manera robusta y adaptable, lo que ofrece ventajas significativas en comparación con otros enfoques. 

#### Justificación del Diseño y Uso del Patrón Builder en la Aplicación de Creación de Pizzas

El patrón Builder es una solución de diseño fundamental en la creación de objetos complejos y altamente configurables, y se ha implementado con éxito en nuestra aplicación de creación de pizzas. A continuación, se proporciona una justificación detallada de cómo este patrón mejora la estructura y la flexibilidad de la aplicación:

Separación de Construcción y Representación:

El patrón Builder ha sido implementado en nuestra aplicación para separar claramente el proceso de construcción de pizzas de su representación final. Esto permite una construcción modular y coherente de pizzas personalizadas, evitando la necesidad de modificar la lógica de construcción principal para cada variante de pizza.

Configurabilidad Personalizada:

En el negocio de las pizzerías, la capacidad de configurar cada aspecto de una pizza (masa, salsa, ingredientes, cocción, presentación, maridaje y extras) es esencial para satisfacer las preferencias de los clientes. El patrón Builder ofrece una interfaz clara y coherente que permite a los clientes definir sus pizzas exactamente como desean.

Reusabilidad del Código:

La implementación del patrón Builder fomenta la reutilización del código. La lógica de construcción de pizza se encuentra en la clase PizzaBuilder, lo que significa que podemos crear múltiples instancias de constructores de pizza sin duplicar código. Esto mejora la calidad del código y reduce la posibilidad de errores.

Claridad y Mantenibilidad:

Cada paso del proceso de construcción se refleja en métodos descriptivos en el PizzaBuilder. Esto facilita la comprensión del código, lo que es beneficioso tanto para el desarrollador que trabaja en el código como para el mantenimiento futuro. La claridad del patrón Builder también facilita la colaboración en equipos de desarrollo.

Flexibilidad y Extensibilidad:

En un mercado en constante evolución, es esencial poder adaptar nuestra oferta de pizzas. El patrón Builder permite la introducción de nuevos tipos de masa, salsas, ingredientes y otras configuraciones con facilidad, sin impactar el código existente. Esto promueve la extensibilidad de la aplicación.

Creación de Objetos Complejos:

Las pizzas son objetos complejos con múltiples componentes. El patrón Builder garantiza que cada pizza esté en un estado válido en todo momento, evitando la creación de pizzas incompletas o incorrectas. Esto es crucial para mantener la calidad de nuestros productos.

Control Centralizado:

La clase Director ofrece un punto centralizado de control sobre el proceso de construcción de pizzas. Esto simplifica la interacción con el patrón Builder, permitiendo a la aplicación principal construir pizzas personalizadas sin necesidad de conocer los detalles internos de la construcción.

### Código
Tenemos varios ficheros para crear nuestra pizzeria. Primero he utilizado un dataset de Keaggle: ["Data-Model-Pizza.csv"](https://www.kaggle.com/datasets/shilongzhuang/pizza-sales) al cual le he hecho cambios y limpieza para poder usarlo en mi builder. El data liimpio lo hemos guardado en un csv en la carpeta data "data_final".

#### limpieza.py
```
import pandas as pd

data = pd.read_csv('/Users/carlotasanchezgonzalez/Documents/class/Patrones-Creacionales-23_24/Ejercicio 2/data/Data-Model-Pizza-Sales.csv')
#print(data.head())


'''------Limpieza de datos-------'''

#Eliminamos columnas que no me sirven
colum_eliminar = ["unit_price", "total_price", "order_id", "quantity", "order_details_id"]
data_final = data.drop(colum_eliminar, axis=1)

#print(data_final.head())

#Filas tienen valores nulos
#print(data_final.isnull().sum())
#No hay valores nulos


'''------Transformación de datos-------'''

'''Ingredientes'''
#Quiero saber los ingredientes diferentes que hay en la columna "ingredientes"
ingredientes_divididos = data_final["pizza_ingredients"].str.split(",", expand=True)

#Renombrar la soclumnas con nombres como ingrediente1
colum_names = [f"ingrediente{i+1}" for i in range(len(ingredientes_divididos.columns))]
ingredientes_divididos.columns = colum_names

#Añadir las columnas de ingredientes a data_final
data_final = pd.concat([data_final, ingredientes_divididos], axis=1)

#Eliminar la columna pizza_ingredients
data_final = data_final.drop("pizza_ingredients", axis=1)
#print(data_final.head())


#Ahora volvemos a comprobar si hay valores nulos
#print(data_final.isnull().sum())
#Hay valores nulos, pero no nos importa a la hora de recomendar ingredientes

#que ingredientes hay en cada columna
#print(data_final["ingrediente1"].unique())


'''Masas'''
#Tipos de tamaños de pizza
#print(data_final["pizza_size"].unique())

#Ahora vamos a transformar la columna tamaño por tipos de masas, de esta manera tendremos que el tamaño S es una masa fina, el tamaño M es una masa gruesa y el tamaño L es una masa rellena de queso
data_final["pizza_size"] = data_final["pizza_size"].replace({"S": "fina", "M": "gruesa", "L": "rellena de queso", "XL": "integral", "XXL": "sin gluten"})
#print(data_final["pizza_size"].unique())

#imprimeme solo las filas que tengas masa integral
#print(data_final[data_final["pizza_size"] == "integral"])

#y cambiamos el nombre de la columna
data_final = data_final.rename(columns={"pizza_size": "tipo_masa"})
#print(data_final["tipo_masa"].head())

'''Salsas'''
#Hacemos el mismo proceso de transformación con la columna pizza_category
#print(data_final["pizza_category"].unique())

#Transformamos la columna por salsa_base, teniendo que classic es tomate, veggie es pesto, supreme es salsa blanca y chicken es salsa picante
data_final["pizza_category"] = data_final["pizza_category"].replace({"Classic": "tomate", "Veggie": "pesto", "Supreme": "salsa blanca", "Chicken": "salsa picante"})
#print(data_final["pizza_category"].unique())

#y cambiamos el nombre de la columna
data_final = data_final.rename(columns={"pizza_category": "salsa_base"})
#print(data_final["salsa_base"].head())

#print(data_final.shape)

'''------Exportar datos-------'''
#guardamos el data final en un csv en la carpeta data
data_final.to_csv("/Users/carlotasanchezgonzalez/Documents/class/Patrones-Creacionales-23_24/Ejercicio 2/data/data_final.csv", sep=";", encoding='utf-8', index=True)
```

Lo segundo será crear nuestro patron Builder que cree las pizzas.

#### pizzabuilder.py
En este ficheor crearemos nuestra clase abstracta PizzaBuilder con las partes (metodos) que tendra la pizza.
```
from __future__ import annotations
from abc import ABC, abstractmethod


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
    def produce_presentacion(self) -> None:
        pass

    @abstractmethod
    def produce_maridaje(self) -> None:
        pass

    @abstractmethod
    def produce_extras(self) -> None:
        pass
```

#### concretepizza.py
Aqui crearemos la pizza concreta.
```
from __future__ import annotations
from pizzabuilder import PizzaBuilder
from pizza import Pizza
import pandas as pd

data = pd.read_csv('ejercicio 2/data/data_final.csv', sep=';', encoding='ISO-8859-1')


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
            self._pizza.add(masa_escogida)
            return masa_escogida

        
    def produce_salsa(self) -> None:
        salsas = data["salsa_base"].unique()
        salsa_escogida = input(f"Elige el tipo de salsa que deseas entre {salsas}:")

        if salsa_escogida not in salsas:
            print("No tenemos esa salsa, por favor elige otra")
            self.produce_salsa()
        else:
            self._pizza.add(salsa_escogida)
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

        self._pizza.add(f"{ingredientes}")
    
    def produce_coccion(self, masa_escogida: str) -> None:
        tecnicas = ["horno de leña", "horno convencional", "parrilla"]

        if masa_escogida == "fina":
            coccion = input(f"Ingrese la técnica de cocción que deseas {tecnicas}, como has elegido masa fina, te recomendamos horno de leña: ")

            if coccion not in tecnicas:
                print("No tenemos esa técnica de cocción, por favor elige otra")
                self.produce_coccion(masa_escogida)
            else:
                self._pizza.add(coccion)

        elif masa_escogida == "gruesa" or masa_escogida == "rellena de queso":
            coccion = input(f"Ingrese la técnica de cocción que deseas {tecnicas}, como has elegido masa gruesa, te recomendamos parrilla: ")

            if coccion not in tecnicas:
                print("No tenemos esa técnica de cocción, por favor elige otra")
                self.produce_coccion(masa_escogida)
            else:
                self._pizza.add(coccion)
        

        elif masa_escogida == "integral" or masa_escogida == "sin gluten":
            coccion = input(f"Ingrese la técnica de cocción que deseas {tecnicas}, como has elegigo masa {masa_escogida} te recomendamos horno convencional: ")

            if coccion not in tecnicas:
                print("No tenemos esa técnica de cocción, por favor elige otra")
                self.produce_coccion(masa_escogida)
            else:
                self._pizza.add(coccion)
    
    def produce_presentacion(self) -> None:
        presentaciones = ["estilo clasico", "estilo mediterraneo", "estilo moderno"]
        presentacion = input(f"Ingrese la presentación que deseas {presentaciones}: ")

        if presentacion not in presentaciones:
            print("No tenemos esa presentación, por favor elige otra")
            self.produce_presentacion()
        else:
            self._pizza.add(presentacion)

    def produce_maridaje(self, salsa_escogida: str) -> None:
        maridajes = ["Garnacha", "Chardonnay", "Viura", "Albariño", "cerveza de trigo", "cerveza rubia", "cerveza tostada", "cerveza con limon", "limonada casera", "agua con gas", "agua", "cola", "leche"]
        print(f"Nuestra seleccion de maridajes es {maridajes}")

        if salsa_escogida == "tomate":
            maridaje = input(f"Ingrese el maridaje que deseas, como has elegido salsa de tomate, te recomendamos un Garnacha, cerveza de trigo o nuestra limonada casera: ")

            if maridaje not in maridajes:
                print("No tenemos ese maridaje, por favor elige otro")
                self.produce_maridaje(salsa_escogida)
            else:
                self._pizza.add(maridaje)

        elif salsa_escogida == "pesto":
            maridaje = input(f"Ingrese el maridaje que deseas, como has elegido salsa de pesto, te recomendamos un Chardonnay, una cerveza rubia o agua con gas: ")

            if maridaje not in maridajes:
                print("No tenemos ese maridaje, por favor elige otro")
                self.produce_maridaje(salsa_escogida)
            else:
                self._pizza.add(maridaje)

        elif salsa_escogida == "salsa blanca":
            maridaje = input(f"Ingrese el maridaje que deseas, como has elegido salsa blanca, te recomendamos un Viura, una cerveza tostada o cola: ")

            if maridaje not in maridajes:
                print("No tenemos ese maridaje, por favor elige otro")
                self.produce_maridaje(salsa_escogida)
            else:
                self._pizza.add(maridaje)
        
        else:
            maridaje = input(f"Ingrese el maridaje que deseas, como has elegido salsa picante, te recomendamos un Albariño, una cerveza con limon o leche: ")

            if maridaje not in maridajes:
                print("No tenemos ese maridaje, por favor elige otro")
                self.produce_maridaje(salsa_escogida)
            else:
                self._pizza.add(maridaje)

    
    def produce_extras(self) -> None:
        finalizacion = ["caviar", "trufa", "foie", "aceite picante", "rucula"]
        extra = input(f"Ingrese el extra que deseas {finalizacion}: ")

        if extra not in finalizacion:
            print("No tenemos ese extra, por favor elige otro")
            self.produce_extras()
        else:
            self._pizza.add(extra)
```

#### pizza.py
Aquí se construye la pizza
```
from typing import Any

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
```

#### director.py
La clase Director cumple un papel importante en la implementación del patrón Builder. Su principal función es orquestar el proceso de construcción de un objeto Pizza utilizando un objeto PizzaBuilder
```
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
```

#### run.py
Por último, esto ejecutará nuestro programa. Pedira al usuario que ingrese lo que quiere para cada parte de la pizza e imprimira la pizza construída
```
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
'''    print("Custom product: ")
    builder.produce_masa()
    builder.produce_salsa()
    builder.produce_ingredientes()
    builder.produce_coccion()
    builder.produce_presentacion()
    builder.produce_maridaje()
    builder.produce_extras()
    builder.pizza.list_parts()'''
```

Por último hemos creado una función que guarde las pizzas que el cliente crea en un csv por si proximamente quiere hacer alguna modificacion a alguna de esas pizzas, quiere volver a pedirla etc.

#### guardarpizzas.py
En esta funcion creamos el csv ("pizzas.csv") que va a guardar las pizzas, implementando esta función también en el run.py
```
'''Crear una funcion que guarde las pizzas concretas creadas en un archivo .csv con cada parte de la pizza'''
import csv
import os

def guardar_pizza_personalizada(pizza_personalizada):
    carpeta_ejercicio2 = 'Ejercicio 2'
    ruta_archivo = os.path.join(carpeta_ejercicio2, 'pizzas.csv')

    with open(ruta_archivo, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["masa", "salsabase", "ingredientes", "coccion", "presentacion", "maridaje", "extras"], delimiter=';')

        if file.tell() == 0:
            writer.writeheader()


        datos = {
            "masa": pizza_personalizada[0],
            "salsabase": pizza_personalizada[1],
            "ingredientes": pizza_personalizada[2],
            "coccion": pizza_personalizada[3],
            "presentacion": pizza_personalizada[4],
            "maridaje": pizza_personalizada[5],
            "extras": pizza_personalizada[6]
        }

        writer.writerow(datos)

    print("\nPizza guardada con éxito")
```

#### leerpizzas.py
En este archivos creamos dos funciones una para leer las pizzas del csv anterior y otra para reconstruir la pizza y asi en un futuro poder hacer algun cambio o por si quiere volver a pedirla.

```
import csv

def leer_pizzas_desde_csv(archivo_csv):
    pizzas = []
    with open(archivo_csv, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            pizzas.append(row)
    return pizzas

def reconstruir_pizza(datos):
    pizza = f"Tipo de Masa: {datos['masa']}\n"
    pizza += f"Salsa Base: {datos['salsabase']}\n"
    pizza += f"Ingredientes: {datos['ingredientes']}\n"
    pizza += f"Técnica de Cocción: {datos['coccion']}\n"
    pizza += f"Presentación: {datos['presentacion']}\n"
    pizza += f"Maridaje: {datos['maridaje']}\n"
    pizza += f"Extra y finalización: {datos['extras']}\n"
    return pizza

if __name__ == "__main__":
    archivo_csv = 'Ejercicio 2/pizzas.csv'

    # Leer datos del archivo CSV
    pizzas = leer_pizzas_desde_csv(archivo_csv)

    # Reconstruir y mostrar cada pizza
    for pizza in pizzas:
        pizza_reconstruida = reconstruir_pizza(pizza)
        print(pizza_reconstruida)
```

Al ejecutar el problema nos pedirá las partes de la pizza que quiera el cliente:
<img width="1223" alt="Captura de pantalla 2023-11-09 a las 22 44 22" src="https://github.com/crltsnch/Patrones-Creacionales-23_24/assets/91721777/efdf9a79-e063-494c-99f2-1b3cd05657c3">

Y la pizza se nos guardará en el csv:
<img width="1440" alt="Captura de pantalla 2023-11-09 a las 22 43 20" src="https://github.com/crltsnch/Patrones-Creacionales-23_24/assets/91721777/d6c60c3a-02cc-4681-81f0-64d36962d089">
