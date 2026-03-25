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



__Clase `Producto`__

| Tipo | Descripción |
|---|---|
| Atributo | `nombre` |
| Atributo | `precio` |

__Clase `Pedido`__

| Tipo | Descripción |
| --- | --- |
| Atributo | `lista de productos` |
| Método | `agregar_producto(producto)` |
| Método | `total()` |

__Clase `Cliente`__

| Tipo | Descripción |
| --- | --- |
| Atributo | `nombre` |
| Atributo | `lista de pedidos` -> historial de pedidos realizados |
| Método | `hacer_pedido(pedido)` -> agrega el pedido a la lista de pedidos, registra el gasto y vacia el pedido actual |
| Método | `total_gastado()` -> suma el total de todos los pedidos realizados |


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

## Ejercicio 7 — Herencia básica

Crear una `clase base Animal`:

| Tipo | Descripción |
|---|---|
| Atributo | `nombre` |
| Método | `hacer_ruido()` → imprime "Hace un sonido" |

Crear una `clase Perro` que __herede__ de `Animal`:

| Tipo | Descripción |
|---|---|
| Método | `hacer_ruido()` → imprime "Guau" |

Ayuda: usar override (sobreescritura)

## Ejercicio 8 — Herencia + lógica

Crear una clase `CuentaBancaria`:

| Tipo | Descripción |
|---|---|
| Atributo | `_saldo` (saldo actual) |
| Método | `ver_saldo()` (muestra el saldo actual) |
| Metodo | `depositar(monto)` |

Crear dos clases __hijas__:

- `CajaAhorro`:

| Tipo | Descripción |
|---|---|
| Método | `retirar(monto)` (no permite saldo negativo) |

- `CuentaCorriente`

| Tipo | Descripción |
|---|---|
| Método | `retirar(monto)` (permite saldo negativo) |





## Ejercicio 9 — Herencia con uso de super()

Crear una `clase Persona` (Base):

| Tipo | Descripción |
|---|---|
| Atributos | nombre |
| Atributos | edad |

Crear una `clase Empleado` que __herede__ de 
`Persona`:

| Tipo | Descripción |
|---|---|
| Atributo | sueldo |
| Metodo | mostrar_datos() → imprime nombre, edad y sueldo |

## Ejercicio 10 — Herencia + composición

Crear: `Clase Empleado`

| Tipo | Descripción |
|---|---|
| Atributo | nombre del empleado |
| Atributo | sueldo del empleado |
| Metodo | mostrar_datos() → imprime nombre y sueldo |


`Clase Gerente` (hereda de Empleado)

| Tipo | Descripción |
|---|---|
| Atributo | lista de empleados a cargo |
| Metodo | agregar_empleado(emp) → agrega un empleado a la lista |
| Metodo | total_sueldos() → suma de sueldos de todos los empleados 

## Ejercicio 11 — Sistema completo (MercadoLibre)

Crear un sistema de usuarios:

### Clase `Usuario` *(base)*

| Atributo | Descripción |
|---|---|
| `nombre` | Nombre del usuario |
| `email` | Correo electrónico |
| `_contrasena` | Contraseña *(atributo protegido)* |

| Método | Descripción |
|---|---|
| `mostrar_datos()` | Muestra los datos del usuario |
| `verificar_contrasena(contrasena)` | Retorna `True` si coincide con `_contrasena`, `False` si no |

---

### Clase `Cliente` *(hereda de `Usuario`)*

| Atributo | Descripción |
|---|---|
| `carrito` | Lista de objetos `Producto` |

| Método | Descripción |
|---|---|
| `agregar_producto_al_carrito(producto)` | Agrega un `Producto` al carrito |
| `vaciar_carrito()` | Vacía la lista del carrito |
| `total_carrito()` | Retorna la suma de los precios de los productos del carrito |

---

### Clase `Admin` *(hereda de `Usuario`)*

| Atributo | Descripción |
|---|---|
| `tienda` | Referencia al objeto `Tienda` |

| Método | Descripción |
|---|---|
| `crear_producto(nombre, precio)` | Crea y retorna un nuevo objeto `Producto`, y lo agrega a `tienda` |
| `eliminar_producto(producto)` | Elimina el producto de la `tienda` asociada |

---

### Clase `Producto`

| Atributo | Descripción |
|---|---|
| `nombre` | Nombre del producto |
| `precio` | Precio del producto |

---

### Clase `Tienda`

| Atributo | Descripción |
|---|---|
| `lista_productos` | Lista de objetos `Producto` |
| `lista_usuarios` | Lista de objetos `Usuario` |

| Método | Descripción |
|---|---|
| `agregar_producto(producto)` | Agrega un `Producto` a `lista_productos` |
| `eliminar_producto(producto)` | Elimina un `Producto` de `lista_productos` |
| `registrar_usuario(usuario)` | Agrega un `Usuario` a `lista_usuarios` |
| `mostrar_productos()` | Muestra todos los productos disponibles |

---

### Clase `App`

| Atributo | Descripción |
|---|---|
| `tienda` | Referencia al objeto `Tienda` |

| Método | Descripción |
|---|---|
| `login(email, contrasena)` | Busca en `tienda.lista_usuarios` y retorna el usuario si las credenciales son correctas, `None` si no |
| `mostrar_menu(usuario)` | Muestra opciones según el tipo: menú de compras si es `Cliente`, menú de administración si es `Admin` |

### Ejemplo de uso esperado:

#### Usuarios de prueba

| Login | User | Password | Vista |
|---|---|---|---|
| — | facundo@mail.com | 1234 | Cliente |
| — | admin@mail.com | admin123 | Admin |

#### Funcionalidades por tipo de usuario

**Cliente:** ve los productos, los agrega al carrito, ve el total, vacía o compra.

**Admin:** ve todos los productos, los elimina, y crea nuevos con nombre y precio.
