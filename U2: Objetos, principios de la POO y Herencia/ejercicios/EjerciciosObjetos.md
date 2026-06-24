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

## Ejercicio 7 — Sistema de Biblioteca (3 clases)

Crear un sistema para gestionar préstamos de libros.

__Clase `Libro`__

| Tipo | Descripción |
|---|---|
| Atributo | `titulo` |
| Atributo | `autor` |
| Atributo | `disponible` (bool, arranca en `True`) |

__Clase `Prestamo`__

| Tipo | Descripción |
| --- | --- |
| Atributo | `lista de libros` |
| Método | `agregar_libro(libro)` -> agrega el libro y marca `disponible = False` |
| Método | `cantidad_libros()` -> retorna cuántos libros tiene el préstamo |

__Clase `Socio`__

| Tipo | Descripción |
| --- | --- |
| Atributo | `nombre` |
| Atributo | `lista de prestamos` -> historial de préstamos realizados |
| Método | `retirar_prestamo(prestamo)` -> agrega el préstamo al historial y vacía el préstamo actual |
| Método | `total_libros_leidos()` -> suma la cantidad de libros de todos los préstamos del historial |

### Ejemplo de uso esperado:
```python
l1 = Libro("Rayuela", "Cortázar")
l2 = Libro("El Aleph", "Borges")

prestamo = Prestamo()
prestamo.agregar_libro(l1)
prestamo.agregar_libro(l2)

socio = Socio("Facundo")
socio.retirar_prestamo(prestamo)

print(socio.total_libros_leidos())
```

## Ejercicio 8 — Sistema de Veterinaria (3 clases)

Crear un sistema de consultas veterinarias.

__Clase `Mascota`__

| Tipo | Descripción |
|---|---|
| Atributo | `nombre` |
| Atributo | `especie` |
| Atributo | `precio_consulta` |

__Clase `Consulta`__

| Tipo | Descripción |
| --- | --- |
| Atributo | `lista de mascotas atendidas` |
| Método | `atender_mascota(mascota)` -> agrega la mascota a la consulta |
| Método | `total()` -> suma los precios de consulta de todas las mascotas atendidas |

__Clase `Dueño`__

| Tipo | Descripción |
| --- | --- |
| Atributo | `nombre` |
| Atributo | `lista de consultas` -> historial de consultas realizadas |
| Método | `registrar_consulta(consulta)` -> agrega la consulta al historial y vacía la consulta actual |
| Método | `total_pagado()` -> suma el total de todas las consultas del historial |

### Ejemplo de uso esperado:
```python
m1 = Mascota("Firulais", "perro", 5000)
m2 = Mascota("Misu", "gato", 3500)

consulta = Consulta()
consulta.atender_mascota(m1)
consulta.atender_mascota(m2)

dueño = Dueño("Lucía")
dueño.registrar_consulta(consulta)

print(dueño.total_pagado())
```

## Ejercicio 9 — Sistema de Hotel (3 clases)

Crear un sistema de reservas de habitaciones.

__Clase `Habitacion`__

| Tipo | Descripción |
|---|---|
| Atributo | `numero` |
| Atributo | `precio_por_noche` |

__Clase `Reserva`__

| Tipo | Descripción |
| --- | --- |
| Atributo | `lista de habitaciones` |
| Atributo | `cantidad_noches` |
| Método | `agregar_habitacion(habitacion)` -> agrega la habitación a la reserva |
| Método | `total()` -> suma `precio_por_noche` de cada habitación multiplicado por `cantidad_noches` |

__Clase `Huesped`__

| Tipo | Descripción |
| --- | --- |
| Atributo | `nombre` |
| Atributo | `lista de reservas` -> historial de reservas realizadas |
| Método | `hacer_reserva(reserva)` -> agrega la reserva al historial y vacía la reserva actual |
| Método | `total_gastado()` -> suma el total de todas las reservas del historial |

### Ejemplo de uso esperado:
```python
h1 = Habitacion(101, 8000)
h2 = Habitacion(202, 12000)

reserva = Reserva(cantidad_noches=3)
reserva.agregar_habitacion(h1)
reserva.agregar_habitacion(h2)

huesped = Huesped("Mariana")
huesped.hacer_reserva(reserva)

print(huesped.total_gastado())
```

## Ejercicio 10 — Sistema de Delivery (3 clases)

Crear un sistema de pedidos de delivery con propina.

__Clase `Plato`__

| Tipo | Descripción |
|---|---|
| Atributo | `nombre` |
| Atributo | `precio` |

__Clase `Orden`__

| Tipo | Descripción |
| --- | --- |
| Atributo | `lista de platos` |
| Atributo | `costo_envio` |
| Método | `agregar_plato(plato)` -> agrega el plato a la orden |
| Método | `subtotal()` -> suma los precios de los platos |
| Método | `total()` -> retorna `subtotal() + costo_envio` |

__Clase `Repartidor`__

| Tipo | Descripción |
| --- | --- |
| Atributo | `nombre` |
| Atributo | `lista de ordenes entregadas` |
| Método | `entregar_orden(orden)` -> agrega la orden al historial y vacía la orden actual |
| Método | `total_facturado()` -> suma el total de todas las órdenes entregadas |
| Método | `propinas_estimadas()` -> retorna el 10% de `total_facturado()` |

### Ejemplo de uso esperado:
```python
p1 = Plato("Pizza", 3500)
p2 = Plato("Empanadas", 1800)

orden = Orden(costo_envio=500)
orden.agregar_plato(p1)
orden.agregar_plato(p2)

repartidor = Repartidor("Diego")
repartidor.entregar_orden(orden)

print(repartidor.total_facturado())
print(repartidor.propinas_estimadas())
```

## Ejercicio 11 — Herencia básica

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

## Ejercicio 12 — Herencia + lógica

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





## Ejercicio 13 — Herencia con uso de super()

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

## Ejercicio 14 — Herencia + composición

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

## Ejercicio 15 — Sistema completo (MercadoLibre)

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

## Ejercicio 16 — Sistema Bancario Completo

Crear un sistema bancario con cuentas, tarjetas, préstamos, inversiones, empleados y sucursales.

### Jerarquía de clases

```
Cuenta   ──►  CajaDeAhorro
         ──►  CuentaCorriente

Tarjeta  ──►  TarjetaDebito
         ──►  TarjetaCredito  (tiene lista de Seguros)

Persona  ──►  Cliente    (tiene Cuentas, Tarjetas, Prestamos, Inversiones)
         ──►  Empleado   ──►  Cajero
                         ──►  Asesor
                         ──►  Gerente  (tiene Sucursal a cargo)

Sucursal  (tiene Empleados y Clientes)
Banco     (gestiona todo el sistema)
```

---

### Excepciones personalizadas

Todas heredan de `BancoError`, que hereda de `Exception`.

| Clase | Cuándo se lanza |
|---|---|
| `BancoError` | Excepción base del sistema |
| `SaldoInsuficienteError` | No hay fondos suficientes para la operación |
| `LimiteSuperadoError` | Se superó el límite de descubierto o de crédito |
| `TarjetaBloqueadaError` | Se intenta operar con una tarjeta bloqueada |
| `PrestamoError` | Préstamo no aprobado, cuota ya pagada, etc. |
| `InversionError` | Inversión ya rescatada, etc. |

---

### Clase `Transaccion`

| Atributo | Descripción |
|---|---|
| `tipo` | `"deposito"`, `"extraccion"`, `"transferencia_entrada"` o `"transferencia_salida"` |
| `monto` | Monto de la operación |
| `descripcion` | Texto libre |

| Método | Descripción |
|---|---|
| `__str__()` | Retorna `"[DEPOSITO] +$500.00 — Sueldo"`. Usá `+` si el tipo es `deposito` o `transferencia_entrada`, `-` en los demás casos |

---

### Clase `Cuenta` *(base)*

| Atributo | Descripción |
|---|---|
| `numero` | String, p. ej. `"0001"` |
| `titular` | Objeto `Cliente` |
| `__saldo` | Float **privado**, arranca en `0.0` |
| `__historial` | Lista **privada** de `Transaccion`, arranca vacía |

| Método | Descripción |
|---|---|
| `get_saldo()` | Retorna el saldo actual |
| `get_historial()` | Retorna una **copia** de la lista con `list()` |
| `depositar(monto, descripcion)` | Si `monto <= 0` lanzar `ValueError`. Sumar al saldo y registrar `Transaccion("deposito", ...)` |
| `_registrar_extraccion(monto, descripcion)` | Método **protegido**: restar del saldo y registrar `Transaccion("extraccion", ...)`. Las subclases lo llaman después de validar |
| `_registrar_transferencia(monto, es_entrada, descripcion)` | Método **protegido**: si `es_entrada=True` sumar y registrar `transferencia_entrada`; si `False` restar y registrar `transferencia_salida` |
| `extraer(monto, descripcion)` | Solo lanzar `NotImplementedError`. Las subclases lo implementan |
| `__str__()` | Retorna `"Cuenta #0001 \| Titular: Juan \| Saldo: $1500.00"` |

---

### Clase `CajaDeAhorro` *(hereda de `Cuenta`)*

| Método | Descripción |
|---|---|
| `extraer(monto, descripcion)` | Si `monto <= 0` lanzar `ValueError`. Si `monto > saldo` lanzar `SaldoInsuficienteError("Saldo insuficiente. Saldo actual: $XXX.XX")`. Si pasa, llamar a `_registrar_extraccion()` |

---

### Clase `CuentaCorriente` *(hereda de `Cuenta`)*

| Atributo | Descripción |
|---|---|
| `limite_descubierto` | Cuánto puede quedar negativa la cuenta |

| Método | Descripción |
|---|---|
| `get_disponible()` | Retorna `saldo + limite_descubierto` |
| `extraer(monto, descripcion)` | Si `monto <= 0` lanzar `ValueError`. Si `monto > get_disponible()` lanzar `LimiteSuperadoError("Límite de descubierto alcanzado. Disponible: $XXX.XX")`. Si pasa, llamar a `_registrar_extraccion()` |

---

### Clase `Tarjeta` *(base)*

| Atributo | Descripción |
|---|---|
| `__numero` | String **privado** de 16 dígitos |
| `titular` | Objeto `Cliente` |
| `activa` | Bool, arranca en `True` |

| Método | Descripción |
|---|---|
| `get_numero_enmascarado()` | Retorna `"****-****-****-3456"` (últimos 4 dígitos visibles, usá `__numero[-4:]`) |
| `bloquear()` | Pone `activa = False` |
| `desbloquear()` | Pone `activa = True` |
| `_validar_activa()` | Método **protegido**: si no está activa lanzar `TarjetaBloqueadaError("Tarjeta bloqueada. No se puede operar.")` |
| `__str__()` | Retorna `"Tarjeta [****-****-****-3456] \| Titular: Juan \| Estado: ACTIVA"` |

---

### Clase `TarjetaDebito` *(hereda de `Tarjeta`)*

| Atributo | Descripción |
|---|---|
| `cuenta` | Objeto `CajaDeAhorro` vinculado |

| Método | Descripción |
|---|---|
| `__init__(numero, cuenta)` | Llamar a `super().__init__` con el número y el titular de la cuenta. Guardar `cuenta` |
| `pagar(monto, descripcion)` | Llamar a `_validar_activa()`. Si pasa, delegar a `self.cuenta.extraer()` |

---

### Clase `TarjetaCredito` *(hereda de `Tarjeta`)*

| Atributo | Descripción |
|---|---|
| `__limite` | Límite de crédito **privado** |
| `__deuda` | Deuda acumulada **privada**, arranca en `0.0` |
| `seguros` | Lista pública de `Seguro`, arranca vacía |

| Método | Descripción |
|---|---|
| `get_deuda()` | Retorna la deuda actual |
| `get_limite_disponible()` | Retorna `__limite - __deuda` |
| `contratar_seguro(seguro)` | Agrega el seguro a `self.seguros` |
| `cobrar_seguros(cuenta)` | Llama a `seguro.cobrar(cuenta)` en cada seguro de la lista |
| `pagar_con_tarjeta(monto, descripcion)` | Llamar a `_validar_activa()`. Si `monto > limite_disponible` lanzar `LimiteSuperadoError("Límite de crédito insuficiente. Disponible: $XXX.XX")`. Si pasa, sumar a `__deuda` |
| `pagar_deuda(monto, cuenta)` | Si `monto > __deuda`, ajustar `monto` al total de la deuda. Extraer de la cuenta. Restar de `__deuda` |
| `__str__()` | Retorna `"TarjetaCredito [****] \| Deuda: $X \| Disponible: $X \| Seguros activos: N"` |

---

### Clase `Seguro`

| Atributo | Descripción |
|---|---|
| `TIPOS_VALIDOS` | Constante de clase: `("robo", "fraude", "viaje")` |
| `tipo` | Uno de los tipos válidos |
| `costo_mensual` | Float |
| `activo` | Bool, arranca en `True` |

| Método | Descripción |
|---|---|
| `__init__(tipo, costo_mensual)` | Si `tipo` no está en `TIPOS_VALIDOS` lanzar `ValueError` |
| `cancelar()` | Si ya está cancelado lanzar `BancoError("El seguro ya está cancelado.")`. Si no, poner `activo = False` |
| `cobrar(cuenta)` | Si no está activo no hacer nada. Si está activo, intentar `cuenta.extraer(costo_mensual, ...)`. **Capturar** `SaldoInsuficienteError` y `LimiteSuperadoError` con `try/except` e imprimir el error sin relanzarlo |
| `__str__()` | Retorna `"Seguro de FRAUDE \| $500.00/mes \| ACTIVO"` |

---

### Clase `CuotaPrestamo`

| Atributo | Descripción |
|---|---|
| `numero` | Número de cuota (1, 2, 3...) |
| `monto` | Monto de la cuota |
| `pagada` | Bool, arranca en `False` |

| Método | Descripción |
|---|---|
| `pagar()` | Si ya está pagada lanzar `PrestamoError("La cuota #XX ya fue pagada.")`. Si no, poner `pagada = True` |
| `__str__()` | Retorna `"Cuota #01 \| $9166.67 \| PENDIENTE"` (número con 2 dígitos: `:02d`) |

---

### Clase `Prestamo`

| Atributo | Descripción |
|---|---|
| `monto` | Capital prestado |
| `tasa_mensual` | Float, p. ej. `0.03` = 3% mensual |
| `cantidad_cuotas` | Int |
| `cuenta_debito` | Objeto `Cuenta` donde se acredita y se cobran cuotas |
| `aprobado` | Bool, arranca en `False` |
| `cuotas` | Lista de `CuotaPrestamo` generada en `__init__` llamando a `_generar_cuotas()` |

| Método | Descripción |
|---|---|
| `_generar_cuotas()` | Calcular `monto_total = monto * (1 + tasa_mensual * cantidad_cuotas)`. Dividir entre `cantidad_cuotas` (redondear a 2 decimales). Retornar lista de `CuotaPrestamo` numeradas desde 1 |
| `acreditar()` | Si `aprobado == False` lanzar `PrestamoError`. Si no, depositar `monto` en `cuenta_debito` |
| `pagar_cuota()` | Si no aprobado lanzar `PrestamoError`. Buscar la primera cuota no pagada, extraer su monto de `cuenta_debito`, llamar a `cuota.pagar()` y retornarla. Si todas están pagadas lanzar `PrestamoError` |
| `cuotas_pendientes()` | Retorna lista de cuotas con `pagada == False` |
| `esta_saldado()` | Retorna `True` si todas las cuotas están pagadas |
| `__str__()` | Retorna `"Préstamo $100000.00 \| Tasa: 3.0%/mes \| 9/12 cuotas pendientes \| APROBADO"` |

---

### Clase `Inversion`

| Atributo | Descripción |
|---|---|
| `monto` | Capital invertido |
| `tasa_anual` | Float, p. ej. `0.60` = 60% anual |
| `meses` | Duración en meses |
| `cuenta_origen` | Cuenta de donde se extrae el capital |
| `rescatada` | Bool, arranca en `False` |

| Método | Descripción |
|---|---|
| `__init__(...)` | Si `monto <= 0` lanzar `ValueError`. Si `monto > saldo` lanzar `SaldoInsuficienteError("Saldo insuficiente para invertir. Disponible: $XXX.XX")`. Si pasa, extraer `monto` de `cuenta_origen` |
| `calcular_ganancia()` | `monto * (tasa_anual / 12) * meses`, redondeado a 2 decimales |
| `calcular_total()` | `monto + ganancia`, redondeado a 2 decimales |
| `rescatar(cuenta_destino)` | Si ya fue rescatada lanzar `InversionError("Esta inversión ya fue rescatada.")`. Si no, depositar `calcular_total()` en `cuenta_destino`, poner `rescatada = True` y retornar el total |
| `__str__()` | Retorna `"Inversión $20000.00 \| Tasa: 60% anual \| 6 meses \| Ganancia estimada: $6000.00 \| ACTIVA"` |

---

### Clase `Persona` *(base)*

| Atributo | Descripción |
|---|---|
| `nombre` | String público |
| `__dni` | String **privado** |
| `email` | String público |

| Método | Descripción |
|---|---|
| `get_dni()` | Retorna el DNI |
| `__str__()` | Retorna `"Juan López (DNI: 38123456)"` |

---

### Clase `Cliente` *(hereda de `Persona`)*

| Atributo | Descripción |
|---|---|
| `cuentas` | Lista de `Cuenta` |
| `tarjetas` | Lista de `Tarjeta` |
| `prestamos` | Lista de `Prestamo` |
| `inversiones` | Lista de `Inversion` |

| Método | Descripción |
|---|---|
| `agregar_cuenta(cuenta)` | Agrega a `self.cuentas` |
| `agregar_tarjeta(tarjeta)` | Agrega a `self.tarjetas` |
| `agregar_prestamo(prestamo)` | Agrega a `self.prestamos` |
| `agregar_inversion(inversion)` | Agrega a `self.inversiones` |
| `mostrar_resumen()` | Imprime nombre, DNI, email y las 4 listas. Si alguna está vacía mostrar `"Sin X."` |

---

### Clase `Empleado` *(hereda de `Persona`)*

| Atributo | Descripción |
|---|---|
| `legajo` | String |
| `sueldo` | Float |
| `sucursal` | Referencia a `Sucursal`, arranca en `None` |

| Método | Descripción |
|---|---|
| `mostrar_datos()` | Imprime tipo (`self.__class__.__name__`), nombre, legajo, sueldo y sucursal |
| `__str__()` | Retorna `"Cajero: Ana Pérez (Legajo: C001)"` (usar `self.__class__.__name__`) |

---

### Clase `Cajero` *(hereda de `Empleado`)*

| Método | Descripción |
|---|---|
| `realizar_deposito(cuenta, monto, descripcion)` | Llamar a `cuenta.depositar()`. **Capturar `ValueError`** e imprimir el error. Si sale bien, imprimir mensaje de éxito |
| `realizar_extraccion(cuenta, monto, descripcion)` | Llamar a `cuenta.extraer()`. **Capturar `SaldoInsuficienteError`/`LimiteSuperadoError`** y **`ValueError`** por separado e imprimir el error en cada caso |

---

### Clase `Asesor` *(hereda de `Empleado`)*

| Método | Descripción |
|---|---|
| `abrir_caja_ahorro(banco, cliente)` | Llamar a `banco.abrir_caja_ahorro(cliente)`. Si tiene sucursal, registrar al cliente en ella. Imprimir mensaje y retornar la cuenta |
| `abrir_cuenta_corriente(banco, cliente, limite_descubierto)` | Igual pero con `banco.abrir_cuenta_corriente(cliente, limite_descubierto)` |
| `tramitar_prestamo(cliente, monto, tasa_mensual, cantidad_cuotas, cuenta)` | Crear `Prestamo(...)`, agregarlo al cliente con `agregar_prestamo()`, imprimir que queda pendiente de aprobación y retornarlo |
| `crear_inversion(cliente, monto, tasa_anual, meses, cuenta)` | Crear `Inversion(...)`. **Capturar `SaldoInsuficienteError`** e imprimir el error. Si sale bien, agregar al cliente y retornar la inversión. Si falla, retornar `None` |

---

### Clase `Gerente` *(hereda de `Empleado`)*

| Atributo | Descripción |
|---|---|
| `sucursal_a_cargo` | Referencia a `Sucursal`, arranca en `None` |

| Método | Descripción |
|---|---|
| `asignar_sucursal(sucursal)` | Guardar en `self.sucursal_a_cargo` y en `self.sucursal`. Asignar `sucursal.gerente = self` |
| `aprobar_prestamo(prestamo)` | Si `prestamo.aprobado` lanzar `PrestamoError("El préstamo ya estaba aprobado.")`. Si no, poner `aprobado = True` y llamar a `prestamo.acreditar()`. **Capturar `PrestamoError`** e imprimir el error sin relanzarlo |
| `informe_sucursal()` | Si no tiene sucursal asignada imprimir aviso. Si tiene, llamar a `sucursal_a_cargo.imprimir_informe()` |

---

### Clase `Sucursal`

| Atributo | Descripción |
|---|---|
| `nombre` | String |
| `direccion` | String |
| `empleados` | Lista de `Empleado` |
| `clientes_atendidos` | Lista de `Cliente` |
| `gerente` | Referencia al `Gerente`, arranca en `None` |

| Método | Descripción |
|---|---|
| `contratar_empleado(empleado)` | Asignar `self` a `empleado.sucursal`. Si es instancia de `Gerente`, asignar `self.gerente`. Agregar a `self.empleados` |
| `registrar_cliente(cliente)` | Si el cliente **no está** en `clientes_atendidos`, agregarlo |
| `imprimir_informe()` | Imprimir nombre, dirección, gerente, total de empleados desglosado en cajeros y asesores (usar `isinstance()`), y lista de clientes |
| `__str__()` | Retorna `"Sucursal Centro \| Av. Corrientes 1234"` |

---

### Clase `Banco`

| Atributo | Descripción |
|---|---|
| `nombre` | String |
| `__clientes` | Lista **privada** de `Cliente` |
| `__cuentas` | Lista **privada** de `Cuenta` |
| `__sucursales` | Lista **privada** de `Sucursal` |
| `__contador_cuentas` | Int **privado**, arranca en `1` |

| Método | Descripción |
|---|---|
| `crear_sucursal(nombre, direccion)` | Crear `Sucursal`, agregarla a `__sucursales` y retornarla |
| `registrar_cliente(nombre, dni, email, sucursal=None)` | Crear `Cliente`, agregarlo a `__clientes`. Si se pasa sucursal, registrar al cliente en ella. Retornar el cliente |
| `abrir_caja_ahorro(cliente)` | Generar número con `_generar_numero_cuenta()`. Crear `CajaDeAhorro`, agregarla a `__cuentas` y al cliente. Retornarla |
| `abrir_cuenta_corriente(cliente, limite_descubierto)` | Igual pero con `CuentaCorriente(numero, cliente, limite_descubierto)` |
| `emitir_tarjeta_debito(cuenta)` | Si `cuenta` no es `CajaDeAhorro` lanzar `TypeError`. Crear `TarjetaDebito`, agregarla al titular y retornarla |
| `emitir_tarjeta_credito(cliente, limite)` | Crear `TarjetaCredito`, agregarla al cliente y retornarla |
| `transferir(cuenta_origen, cuenta_destino, monto)` | Si origen == destino lanzar `ValueError`. Validar fondos según el tipo de cuenta origen y lanzar `SaldoInsuficienteError` o `LimiteSuperadoError` si no alcanza. Registrar con `_registrar_transferencia()` en ambas cuentas |
| `buscar_cliente_por_dni(dni)` | Retorna el cliente con ese DNI o `None` |
| `listar_clientes()` | Imprime cada cliente |
| `listar_sucursales()` | Imprime cada sucursal |
| `_generar_numero_cuenta()` | Retorna `"0001"`, `"0002"`... Incrementar `__contador_cuentas` |
| `_generar_numero_tarjeta()` | Retorna string de 16 dígitos aleatorios usando `random.randint` |

### Ejemplo de uso esperado:

```python
banco = Banco("Banco Pythón")
sucursal = banco.crear_sucursal("Centro", "Av. Corrientes 1234")

gerente = Gerente("María Gómez", "30111222", "maria@banco.com", "G001", 200000)
asesor  = Asesor("Juan López",   "31222333", "juan@banco.com",  "A001", 120000)
cajera  = Cajero("Ana Pérez",    "32333444", "ana@banco.com",   "C001",  90000)

sucursal.contratar_empleado(gerente)
sucursal.contratar_empleado(asesor)
sucursal.contratar_empleado(cajera)
gerente.asignar_sucursal(sucursal)

pedro = banco.registrar_cliente("Pedro Sánchez", "40123456", "pedro@mail.com", sucursal)
ahorro = asesor.abrir_caja_ahorro(banco, pedro)
cajera.realizar_deposito(ahorro, 50000, "Sueldo")

prestamo = asesor.tramitar_prestamo(pedro, 100000, 0.03, 12, ahorro)
gerente.aprobar_prestamo(prestamo)

pedro.mostrar_resumen()
```

> Ejecutá `ej12_banco_runner.py` para probar tu implementación completa.

---

# Ejercicios complementarios

Los siguientes ejercicios refuerzan los temas agregados a la teoría: encapsulamiento con `@property`, métodos de clase/estáticos, polimorfismo, dunder methods, agregación vs composición y clases abstractas.

## Encapsulamiento y `@property`

### Ejercicio 17 — Temperatura con validación

Crear una clase `Temperatura` que guarde una temperatura en grados Celsius, pero **nunca permita** bajar de -273.15 (cero absoluto).

| Tipo | Descripción |
|---|---|
| Atributo privado | `__celsius` |
| Property | `celsius` → getter y setter. El setter debe lanzar `ValueError` si el valor es menor a -273.15 |
| Property (solo lectura) | `fahrenheit` → retorna `celsius * 9/5 + 32` |
| Property (solo lectura) | `kelvin` → retorna `celsius + 273.15` |

**Ejemplo de uso:**
```python
t = Temperatura()
t.celsius = 25
print(t.fahrenheit)   # 77.0
print(t.kelvin)       # 298.15
t.celsius = -300      # ValueError
```

### Ejercicio 18 — Producto con stock

Crear una clase `Producto` donde el stock no se pueda modificar libremente desde afuera.

| Tipo | Descripción |
|---|---|
| Atributos | `nombre`, `precio` |
| Atributo privado | `__stock` |
| Property | `stock` → getter (no setter) |
| Método | `reponer(cantidad)` → suma al stock. Si `cantidad <= 0` lanzar `ValueError` |
| Método | `vender(cantidad)` → resta del stock. Si no hay suficiente lanzar `ValueError("Stock insuficiente")` |

La idea: forzar al usuario a modificar el stock **solo** a través de `reponer()` y `vender()`, no escribiendo `producto.stock = 100`.

---

## Métodos de clase y estáticos

### Ejercicio 19 — Empleado con contador

Crear una clase `Empleado` que lleve la cuenta de cuántos empleados se crearon.

| Tipo | Descripción |
|---|---|
| Atributo de clase | `cantidad_empleados = 0` |
| Atributos | `nombre`, `legajo`, `sueldo` |
| `@classmethod` | `total_empleados()` → retorna `cls.cantidad_empleados` |
| `@classmethod` | `desde_string(texto)` → constructor alternativo. Recibe `"Ana,L001,50000"` y retorna un `Empleado` |
| `@staticmethod` | `es_sueldo_valido(monto)` → retorna `True` si `monto > 0` |

**Ejemplo de uso:**
```python
e1 = Empleado("Ana", "L001", 50000)
e2 = Empleado.desde_string("Juan,L002,60000")
print(Empleado.total_empleados())       # 2
print(Empleado.es_sueldo_valido(-100))  # False
```

### Ejercicio 20 — Fecha con factory methods

Crear una clase `Fecha` con `dia`, `mes`, `anio` y varios constructores alternativos.

| Tipo | Descripción |
|---|---|
| `__init__(dia, mes, anio)` | Constructor normal |
| `@classmethod` | `desde_string(texto)` → recibe `"24/06/2026"` y retorna una `Fecha` |
| `@classmethod` | `hoy()` → retorna la fecha actual (usar `datetime.date.today()`) |
| `@staticmethod` | `es_bisiesto(anio)` → retorna `True` si el año es bisiesto |

---

## Polimorfismo

### Ejercicio 21 — Figuras geométricas

Crear una jerarquía de figuras donde todas tengan el método `area()` pero cada una lo calcule distinto.

| Clase | Atributos | `area()` |
|---|---|---|
| `Figura` (base) | — | retorna `0` |
| `Circulo` | `radio` | `π * radio²` |
| `Rectangulo` | `base`, `altura` | `base * altura` |
| `Triangulo` | `base`, `altura` | `base * altura / 2` |

Luego crear una función **fuera** de las clases:

```python
def area_total(figuras):
    # recibe una lista de figuras y retorna la suma de sus áreas
    ...
```

La gracia del polimorfismo: `area_total()` no necesita saber qué tipo de figura es cada una, solo llama a `.area()`.

### Ejercicio 22 — Medios de pago

Crear una jerarquía de medios de pago:

| Clase | Método `pagar(monto)` |
|---|---|
| `MedioDePago` (base) | imprime `"Pago genérico de $X"` |
| `Efectivo` | imprime `"Pagado $X en efectivo"` |
| `TarjetaCredito` | imprime `"Pagado $X con tarjeta (en cuotas)"` |
| `Transferencia` | imprime `"Transferido $X por CBU"` |

Crear una clase `Caja` con un método `procesar_pagos(lista_pagos, monto)` que reciba una lista de medios de pago y llame a `pagar(monto)` en cada uno, sin preguntar de qué tipo es.

---

## Dunder methods (sobrecarga de operadores)

### Ejercicio 23 — Vector 2D

Crear una clase `Vector2D` que represente un vector en el plano y soporte operaciones como números:

| Método | Comportamiento |
|---|---|
| `__init__(x, y)` | Inicializa coordenadas |
| `__str__()` | Retorna `"(3, 4)"` |
| `__repr__()` | Retorna `"Vector2D(3, 4)"` |
| `__add__(otro)` | Retorna un nuevo `Vector2D` con la suma coordenada a coordenada |
| `__sub__(otro)` | Igual pero restando |
| `__eq__(otro)` | `True` si ambas coordenadas coinciden |
| `__abs__()` | Retorna el módulo (`sqrt(x² + y²)`) |

**Ejemplo:**
```python
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
print(v1 + v2)   # (4, 6)
print(abs(v1))   # 5.0
print(v1 == Vector2D(3, 4))  # True
```

### Ejercicio 24 — Carrito comparable

Reescribir el `Carrito` del ejercicio 5 para que soporte:

| Método | Comportamiento |
|---|---|
| `__len__()` | Retorna la cantidad de productos en el carrito |
| `__str__()` | Retorna `"Carrito con N productos. Total: $X"` |
| `__add__(otro)` | Retorna un nuevo `Carrito` que combina los productos de ambos |
| `__contains__(producto)` | Permite hacer `producto in carrito` |

---

## Agregación vs Composición

### Ejercicio 25 — Universidad (agregación)

Modelar una universidad donde:

- Si se cierra la universidad, los estudiantes **siguen existiendo** como personas (agregación).

| Clase | Atributos | Métodos |
|---|---|---|
| `Estudiante` | `nombre`, `dni` | — |
| `Universidad` | `nombre`, `estudiantes` (lista) | `inscribir(estudiante)`, `desinscribir(estudiante)` |

Los `Estudiante` se crean **afuera** y se pasan a `inscribir()`.

### Ejercicio 26 — Computadora (composición)

Modelar una computadora donde los componentes **mueren con ella** (composición).

| Clase | Atributos | Métodos |
|---|---|---|
| `CPU` | `modelo`, `ghz` | `procesar()` |
| `RAM` | `gb` | — |
| `Disco` | `gb`, `tipo` ("SSD"/"HDD") | — |
| `Computadora` | crea internamente su `CPU`, `RAM` y `Disco` en `__init__` | `info()` → imprime los specs |

La `Computadora` **no recibe** los componentes desde afuera: los construye ella misma en el constructor.

---

## Clases abstractas

### Ejercicio 27 — Empleados con sueldo distinto

Crear una clase abstracta `Empleado` y dos subclases que calculen el sueldo de forma diferente.

| Clase | Tipo | Atributos | Método |
|---|---|---|---|
| `Empleado` | abstracta | `nombre` | `@abstractmethod calcular_sueldo()` |
| `EmpleadoMensual` | concreta | `nombre`, `sueldo_base` | `calcular_sueldo()` → retorna `sueldo_base` |
| `EmpleadoPorHora` | concreta | `nombre`, `valor_hora`, `horas` | `calcular_sueldo()` → retorna `valor_hora * horas` |

Verificar:
```python
Empleado("Test")           # TypeError: no se puede instanciar
EmpleadoMensual("Ana", 80000).calcular_sueldo()        # 80000
EmpleadoPorHora("Juan", 2000, 40).calcular_sueldo()    # 80000
```

### Ejercicio 28 — Notificadores

Crear una clase abstracta `Notificador` que represente cualquier medio para enviar avisos.

| Clase | Tipo | Método |
|---|---|---|
| `Notificador` | abstracta | `@abstractmethod enviar(mensaje, destinatario)` |
| `NotificadorEmail` | concreta | `enviar()` → imprime `"[EMAIL a juan@mail.com] Hola"` |
| `NotificadorSMS` | concreta | `enviar()` → imprime `"[SMS a +54911...] Hola"` |
| `NotificadorPush` | concreta | `enviar()` → imprime `"[PUSH a juan_user] Hola"` |

Crear una clase `Sistema` con un método `avisar_a_todos(notificadores, mensaje, destinatario)` que reciba una lista de notificadores y dispare el mensaje en cada uno. **No** debe usar `isinstance` ni `if` por tipo: el polimorfismo se encarga.
