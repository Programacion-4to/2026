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

## Ejercicio 12 — Sistema Bancario Completo

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
