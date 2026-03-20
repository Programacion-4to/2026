## Ejercicio 1 — Clase básica

Crear una clase `Persona` que tenga:

- atributos: `nombre`, `edad`
- método: `saludar()` → imprime "Hola, soy <nombre>"



## Ejercicio 2 — Método con lógica

Crear una clase `Rectangulo` con:

- atributos: `base`, `altura`
- métodos:
    - `area()`
    - `perimetro()`

## Ejercicio 3 — Lista dentro de un objeto

Crear una clase `Alumno` que tenga:

- atributos: 
    - `nombre`
    - `notas (lista)`

- métodos:
    - `agregar_nota(nota)`
    - `promedio()`

## Ejercicio 4 — Encapsulamiento

Crear una clase `CuentaBancaria`:

- atributo protegido: `_saldo`
- métodos:
    - `depositar(monto)`
    - `retirar(monto)` (no permitir saldo negativo)
    - `ver_saldo()`

## Ejercicio 5 — Relación entre objetos

Crear:

- __Clase `Producto`__
    - atributos:
        - `nombre`
        - `precio`

- __Clase `Carrito`__
    - atributos:
        - `lista de productos`
    - métodos:
        - `agregar_producto(producto)`
        - `total()`

## Ejercicio 6 — Sistema completo (3 clases)

Crear un sistema de pedidos con:

- __Clase `Producto`__
    - atributos:
        - `nombre`
        - `precio`

- __Clase `Pedido`__
    - atributos:
        - `lista de productos`
    - métodos:
        - `agregar_producto(producto)`
        - `total()`

- __Clase `Cliente`__
    - atributos:
        - `nombre`
        - `lista de pedidos`

    - métodos:
        - `hacer_pedido(pedido)`
        - `total_gastado()`


### Ejemplo de uso esperado:
```python
p1 = Producto("Pan", 100)
p2 = Producto("Leche", 200)

pedido = Pedido()
pedido.agregar_producto(p1)
pedido.agregar_producto(p2)

cliente = Cliente("Facundo")
cliente.hacer_pedido(pedido)

print(cliente.total_gastado())
```
