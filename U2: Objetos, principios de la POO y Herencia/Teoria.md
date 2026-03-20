# Programación Orientada a Objetos (POO)
## 1. ¿Qué es un objeto?

Un objeto es una entidad que tiene:

-   **Estado** → datos (atributos)
-   **Comportamiento** → acciones (métodos)

Ejemplo: Un auto tiene color, velocidad (estado) y puede acelerar o
frenar (comportamiento).

## 2. ¿Qué es una clase?

Una clase es un **molde** o **plantilla** para crear objetos. Todos los objetos que se crean a partir de una clase comparten la misma estructura y comportamiento. 

``` python
class Auto:
    ...
```


## 3. Atributos

Son variables que pertenecen al objeto. Definen su estado.

``` python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

Hay distintos tipos de atributos:

-   De instancia → propios de cada objeto. Para cada instancia, pueden tener valores diferentes.
-   De clase → compartidos. Para todos los objetos de la clase, el valor es el mismo (hardcodeado/fijo).


## 4. Métodos

Son funciones dentro de una clase.

``` python
class Persona:
    def saludar(self):
        print("Hola")
```



### Diferencia clave

-   Atributo → dato. Da información sobre el objeto (su estado).
-   Método → acción que el objeto puede realizar (su comportamiento).

---

## 6. self

Referencia al objeto actual.

Permite que cada objeto tenga sus propios datos.

De esta forma, cada objeto puede acceder a sus propios atributos y métodos.

---

## 7. Constructor (**init**)

El constructor es un método especial que se ejecuta automáticamente al crear un objeto. Se utiliza para inicializar los atributos del objeto.

``` python
def __init__(self, nombre):
    self.nombre = nombre
```

---

## 8. Encapsulamiento

Los atributos y métodos pueden ser **públicos** o **privados**.

Que un atributo o método sea público significa que se puede acceder directamente desde fuera de la clase. En Python, esto es lo predeterminado:

``` python
self.saldo #-> Público
```

Que un atributo o método sea privado significa que no se puede acceder directamente desde fuera de la clase. En Python, esto se logra con un guion bajo:

``` python
self.__saldo #-> privado 
```

Que un atributo o método sea protegido significa que se puede acceder desde la clase y sus subclases, pero no desde fuera. En Python, esto se logra con un solo guion bajo:

``` python
self._saldo #-> protegido 
```

**ACLARACION**: En Python, el encapsulamiento es una convención y no una restricción estricta. Aunque se utilicen guiones bajos para indicar que un atributo o método es privado o protegido, todavía es posible acceder a ellos desde fuera de la clase. Sin embargo, es importante seguir estas convenciones para mantener un código limpio y fácil de entender.

---

## 9. Herencia

Permite reutilizar código. Una clase puede heredar atributos y métodos de otra clase. La clase que hereda se llama **subclase** o **clase hija**, y la clase de la que se hereda se llama **superclase** o **clase padre**.

En el siguiente ejemplo, Animal es la **clase padre** y Perro la **clase hija**

``` python
class Animal:
    pass

class Perro(Animal):
    pass
```

Como hago para indicar que la clase `Perro` hereda de `Animal`?

En Python, para indicar que una clase hereda de otra, se coloca el nombre de la clase padre entre paréntesis después del nombre de la clase hija. 

Ademas, la clase hija tendra los mismos atributos y métodos que la clase padre, pero tambien puede tener sus propios atributos y métodos adicionales o incluso sobrescribir los métodos de la clase padre para que se comporten de manera diferente.

Para tener estos atributos y métodos adicionales, debemos especificarlo dentro del constructor de la clase hija. Para ello, utilizamos la función `super()` para llamar al constructor de la clase padre y así inicializar los atributos heredados.

``` python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre) # Llamamos al constructor de la clase padre para inicializar el atributo 'nombre'
        self.raza = raza # Atributo adicional específico de la clase hija 'Perro'   
``` 

---

## 10. Polimorfismo

Cuando hablamos de polimorfismo, nos referimos a la capacidad de un objeto para tomar muchas formas. En el contexto de la programación orientada a objetos, esto significa que una clase hija puede redefinir un método de la clase padre para que se comporte de manera diferente.

``` python
class Animal:
    def hacer_sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")
```

A esto se lo conoce como **sobrescritura de métodos** o como se llama en la programacion **override**. 

El método `hacer_sonido` en la clase `Perro` sobrescribe el método `hacer_sonido` de la clase `Animal`, permitiendo que cada clase tenga su propia implementación del mismo método.


## 11. Composición

La composición es una forma de reutilización de código que consiste en incluir objetos de otras clases como atributos dentro de una clase. Esto permite construir objetos complejos a partir de objetos más simples.

``` python
class Motor:
    def arrancar(self):
        print("Motor arrancado")

class Auto:
    def __init__(self):
        self.motor = Motor()

    def poner_en_marcha(self):
        self.motor.arrancar()
```

---

## 12. Abstracción

Oculta la complejidad.

La abstracción es un principio de la programación orientada a objetos que consiste en ocultar los detalles internos de una clase y mostrar solo la funcionalidad esencial. Esto permite a los usuarios interactuar con el objeto sin preocuparse por cómo funciona internamente.

``` python
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial
    
    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente")
    
    def obtener_saldo(self):
        return self.__saldo
```

Segun lo que vimos antes, el atributo `__saldo` es privado, lo que significa que no se puede acceder directamente desde fuera de la clase. En cambio, se proporcionan métodos públicos (`depositar`, `retirar`, `obtener_saldo`) para interactuar con el saldo de la cuenta bancaria, ocultando así la complejidad interna de cómo se maneja el saldo.

De esta manera, los usuarios de la clase `CuentaBancaria` pueden realizar operaciones como depositar, retirar y consultar el saldo sin preocuparse por los detalles de cómo se almacena y gestiona el saldo internamente. Esto es un ejemplo de abstracción en la programación orientada a objetos.

---

## 13. Ejemplo completo

``` python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def total(self):
        suma = 0
        for p in self.productos:
            suma += p.precio
        return suma
```

En este ejemplo, tenemos una clase `Producto` que representa un producto con un nombre y un precio. Luego, tenemos una clase `Carrito` que representa un carrito de compras, el cual puede contener múltiples productos. La clase `Carrito` tiene un método `agregar` para agregar productos al carrito y un método `total` para calcular el precio total de los productos en el carrito.