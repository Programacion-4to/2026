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

## 5. self

Referencia al objeto actual.

Permite que cada objeto tenga sus propios datos.

De esta forma, cada objeto puede acceder a sus propios atributos y métodos.

---

## 6. Constructor (**init**)

El constructor es un método especial que se ejecuta automáticamente al crear un objeto. Se utiliza para inicializar los atributos del objeto.

``` python
def __init__(self, nombre):
    self.nombre = nombre
```

---

## 7. Encapsulamiento

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

## 8. `@property`, getters y setters

### ¿Qué es un decorador?

Antes de seguir, una aclaración sobre la sintaxis `@algo` que vamos a usar de acá en adelante.

Un **decorador** es una función que recibe otra función (o método) y le agrega comportamiento extra **sin modificar su código**. Se escribe poniendo `@nombre_del_decorador` justo arriba de la definición.

``` python
@property
def saldo(self):
    return self.__saldo
```

Eso es equivalente, en concepto, a decir: *"tomá la función `saldo` y pasala por `property` para transformarla"*. El `@` es solo una forma corta y prolija de aplicar esa transformación.

Por ahora alcanza con saber que:

-   `@property` → convierte un método en un atributo "calculado" (se accede sin paréntesis).
-   `@classmethod` → marca un método como método de clase (recibe `cls`).
-   `@staticmethod` → marca un método como estático (no recibe `self` ni `cls`).
-   `@abstractmethod` → marca un método como abstracto (obligatorio de implementar en las subclases).

No hace falta entender cómo se construye un decorador por dentro: solo qué efecto tiene cada uno cuando lo aplicamos.

### Volviendo a `@property`

Cuando tenemos un atributo privado pero queremos exponerlo de forma controlada, en lugar de escribir métodos `obtener_x()` y `establecer_x()` al estilo Java, Python ofrece el decorador `@property`. Permite que un método se acceda como si fuera un atributo, y agregar validaciones al asignar valores.

``` python
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    @property
    def saldo(self):           # getter
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):    # setter con validación
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self.__saldo = valor


cuenta = CuentaBancaria(100)
print(cuenta.saldo)   # se accede como atributo, no como método
cuenta.saldo = 200    # invoca al setter
```

Ventaja: la interfaz pública queda limpia (`cuenta.saldo`) pero internamente seguimos teniendo control total sobre cómo se lee o modifica el dato.

---

## 9. Métodos de clase y métodos estáticos

Además de los métodos de instancia (los que reciben `self`), existen dos variantes:

-   **Método de clase** (`@classmethod`): recibe la clase como primer parámetro (`cls`) en lugar de la instancia. Útil para constructores alternativos o para operar sobre atributos de clase.
-   **Método estático** (`@staticmethod`): no recibe ni `self` ni `cls`. Es una función que vive dentro de la clase porque está relacionada conceptualmente, pero no necesita acceder al estado.

``` python
class Persona:
    cantidad = 0  # atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.cantidad += 1

    @classmethod
    def desde_string(cls, texto):
        # constructor alternativo: "Juan,30" -> Persona("Juan")
        nombre, _ = texto.split(",")
        return cls(nombre)

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18
```

---

## 10. Herencia

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

## 11. Polimorfismo

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

---

## 12. Sobrecarga de operadores (dunder methods)

Los **dunder methods** ("double underscore", como `__init__`) son métodos especiales que Python invoca automáticamente en ciertas situaciones. Permiten que nuestros objetos se comporten como tipos nativos: imprimirse, compararse, sumarse, medir su longitud, etc.

| Método      | Cuándo se invoca                          |
|-------------|-------------------------------------------|
| `__str__`   | `str(obj)` / `print(obj)`                 |
| `__repr__`  | Representación para debug (`repr(obj)`)   |
| `__eq__`    | Comparación con `==`                      |
| `__lt__`    | Comparación con `<`                       |
| `__len__`   | `len(obj)`                                |
| `__add__`   | Operador `+`                              |

``` python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.precio == otro.precio

    def __add__(self, otro):
        return self.precio + otro.precio


p1 = Producto("Pan", 500)
p2 = Producto("Leche", 800)
print(p1)        # Pan ($500)
print(p1 + p2)   # 1300
```

---

## 13. Composición

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

En este caso, el `Motor` se crea dentro del `Auto`: si el auto deja de existir, el motor también. La vida del componente está atada a la del contenedor.

---

## 14. Tipos de asociación

Cuando dos clases se relacionan, no siempre lo hacen de la misma manera. Las relaciones más importantes son:

### 14.1 Asociación simple ("usa-un")

Es la relación más débil: una clase **usa** otra, pero ninguna es dueña de la otra. Existen de forma independiente.

``` python
class Profesor:
    def dictar(self, curso):
        print(f"Dictando {curso.nombre}")

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
```

### 14.2 Agregación ("tiene-un", vida independiente)

Una clase contiene a otra, pero las partes pueden vivir sin el todo. Si el contenedor desaparece, las partes siguen existiendo.

``` python
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []   # los jugadores se reciben/agregan desde afuera

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
```

Si se borra el equipo, los jugadores siguen existiendo como personas.

### 14.3 Composición ("parte-de", vida dependiente)

Una clase está formada por otras que **no tienen sentido sin ella**. Se crean dentro del contenedor y mueren con él. Es el caso del ejemplo `Auto` y `Motor` de la sección anterior, o:

``` python
class Habitacion:
    def __init__(self, nombre):
        self.nombre = nombre

class Casa:
    def __init__(self):
        self.habitaciones = [Habitacion("Cocina"), Habitacion("Living")]
```

Si se demuele la casa, las habitaciones dejan de existir.

### 14.4 Herencia / Generalización ("es-un")

Ya vista en la sección 10. Una clase es un tipo especializado de otra: un `Perro` **es un** `Animal`.

### 14.5 Dependencia (uso temporal)

Una clase usa a otra de forma puntual, normalmente como parámetro de un método o variable local. No la guarda como atributo.

``` python
class Impresora:
    def imprimir(self, documento):   # depende de Documento solo durante la llamada
        print(documento.texto)
```

### Resumen visual

| Relación     | Sentido     | Vida de las partes        | Símbolo UML        |
|--------------|-------------|---------------------------|--------------------|
| Asociación   | usa-un      | Independiente             | línea simple       |
| Agregación   | tiene-un    | Independiente             | rombo vacío ◇      |
| Composición  | parte-de    | Atada al contenedor       | rombo lleno ◆      |
| Herencia     | es-un       | —                         | triángulo vacío △  |
| Dependencia  | usa temporalmente | —                   | flecha punteada    |

---

## 15. Abstracción

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

## 16. Clases abstractas

Una **clase abstracta** es una clase que no se puede instanciar directamente: solo sirve como plantilla para que otras clases hereden de ella. Define qué métodos deben existir, pero deja que las subclases decidan **cómo** se implementan.

En Python se usa el módulo `abc`:

``` python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


# Figura()      -> TypeError: no se puede instanciar una clase abstracta
r = Rectangulo(3, 4)
print(r.area())   # 12
```

Si una subclase no implementa todos los métodos abstractos, Python no la deja instanciar. Esto **obliga** a respetar el contrato definido por la clase padre.

---

## 17. UML — Diagrama de clases

UML (*Unified Modeling Language*) es un lenguaje visual para describir el diseño de un sistema orientado a objetos. El diagrama más usado es el **diagrama de clases**, que muestra qué clases existen y cómo se relacionan.

### Notación de una clase

Cada clase se dibuja como un rectángulo dividido en tres compartimentos:

```
┌─────────────────────────────┐
│       CuentaBancaria        │   <- nombre
├─────────────────────────────┤
│ - saldo: float              │   <- atributos
│ + titular: str              │
├─────────────────────────────┤
│ + depositar(monto: float)   │   <- métodos
│ + retirar(monto: float)     │
│ + obtener_saldo(): float    │
└─────────────────────────────┘
```

### Visibilidad

| Símbolo | Significado | En Python      |
|---------|-------------|----------------|
| `+`     | Público     | `self.x`       |
| `-`     | Privado     | `self.__x`     |
| `#`     | Protegido   | `self._x`      |

### Tipado

Se escribe `nombre: tipo` para atributos y `metodo(param: tipo): tipo_retorno` para métodos.

### Atributos / métodos de clase

Se subrayan para distinguirlos de los de instancia.

### Multiplicidad

En las relaciones entre clases se indica cuántas instancias participan:

-   `1` → exactamente una
-   `0..1` → cero o una
-   `*` → cero o muchas
-   `1..*` → una o muchas

### Relaciones (ya vistas en la sección 14)

```
Animal  △───── Perro        (herencia)
Auto    ◆───── Motor        (composición)
Equipo  ◇───── Jugador      (agregación)
Profesor ────── Curso       (asociación)
Impresora ─ ─ ▶ Documento   (dependencia)
```

### Ejemplo completo

```
┌──────────────┐         1     *  ┌──────────────┐
│   Carrito    │◆────────────────│   Producto   │
├──────────────┤                  ├──────────────┤
│ - productos  │                  │ + nombre: str│
├──────────────┤                  │ + precio:float│
│ + agregar(p) │                  └──────────────┘
│ + total(): float │
└──────────────┘
```

Un `Carrito` está compuesto por muchos `Producto` (relación de composición, multiplicidad 1 a *).

---

## 18. Principios SOLID

SOLID es un conjunto de 5 principios de diseño orientado a objetos. Acá los nombramos brevemente; se profundizan en unidades posteriores:

-   **S — Single Responsibility Principle**: cada clase debe tener una única responsabilidad / razón para cambiar.
-   **O — Open/Closed Principle**: las clases deben estar **abiertas a la extensión** (se las puede extender por herencia/composición) pero **cerradas a la modificación** (no hace falta tocar su código para agregar funcionalidad).
-   **L — Liskov Substitution Principle**: una subclase debe poder usarse en lugar de su clase padre sin romper el programa.
-   **I — Interface Segregation Principle**: es mejor tener varias interfaces pequeñas y específicas que una grande y general.
-   **D — Dependency Inversion Principle**: depender de abstracciones (clases abstractas / interfaces) y no de implementaciones concretas.

Los más importantes para esta unidad son **SRP** (cada clase hace una sola cosa) y **OCP** (extender mejor que modificar), porque guían cómo separar responsabilidades al diseñar las clases de los ejercicios.

---

## 19. Ejemplo completo

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
