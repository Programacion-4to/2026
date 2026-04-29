# Proyecto 5 — Binance

Exchange de criptomonedas. Los usuarios cargan saldo en USD, compran y venden cripto, manejan una cartera y arman órdenes limitadas que se ejecutan cuando se alcanza un precio.

## Entidades sugeridas

- `Usuario` (id, email, nombre, saldo_usd, fecha_registro)
- `Criptomoneda` (id, simbolo, nombre, precio_usd, activa)
- `HistorialPrecio` (id, cripto_id, precio_usd, fecha)
- `Tenencia` (id, usuario_id, cripto_id, cantidad)
- `Transaccion` (id, usuario_id, cripto_id, tipo, cantidad, precio_unitario, total_usd, fecha)
- `Orden` (id, usuario_id, cripto_id, tipo, modo, cantidad, precio_objetivo, estado, fecha_creacion, fecha_ejecucion)
- `MovimientoSaldo` (id, usuario_id, tipo, monto_usd, fecha, descripcion)

## Historias de usuario

### HU1 — Registro y carga de saldo
Como usuario, quiero registrarme y cargar saldo en dólares.

- [ ] El email es único.
- [ ] El saldo inicial es 0.
- [ ] Solo se aceptan cargas con monto > 0.
- [ ] Cada carga genera un `MovimientoSaldo` con tipo `deposito`.
- [ ] `GET /usuarios/{id}/saldo` devuelve el saldo actual.

### HU2 — Alta y actualización de criptomonedas
Como administrador, quiero cargar criptos y actualizar su precio.

- [ ] El `simbolo` es único (ej: BTC, ETH).
- [ ] El precio es mayor a 0.
- [ ] Cada actualización de precio genera un registro en `HistorialPrecio`.
- [ ] Una cripto puede desactivarse (`activa = false`) sin borrarla.

### HU3 — Compra a precio de mercado
Como usuario, quiero comprar cripto al precio actual.

- [ ] La cripto debe estar `activa`.
- [ ] El `total_usd = cantidad * precio_usd` no puede superar el saldo.
- [ ] El precio de la transacción se toma del momento exacto de la compra.
- [ ] Se descuenta el saldo y se suma a la `Tenencia` correspondiente.
- [ ] Si no existe tenencia previa, se crea; si existe, se suma la cantidad.

### HU4 — Venta a precio de mercado
Como usuario, quiero vender cripto al precio actual.

- [ ] No se puede vender más cantidad que la que hay en `Tenencia`.
- [ ] Se descuenta la cantidad de la tenencia y se suma el `total_usd` al saldo.
- [ ] Si la tenencia queda en 0, se elimina o se deja en 0 (criterio del grupo, documentado).
- [ ] Se genera `MovimientoSaldo` tipo `venta`.

### HU5 — Órdenes limitadas
Como usuario, quiero crear una orden de compra/venta que se ejecute cuando la cripto llegue a un precio.

- [ ] Tipos de orden: `compra` o `venta`.
- [ ] Modos: `mercado` (ejecuta ya) o `limite` (espera precio).
- [ ] Una orden limitada de compra requiere que el saldo alcance en el momento de ejecución, no al crearla.
- [ ] Estados: `abierta`, `ejecutada`, `cancelada`.
- [ ] El usuario puede cancelar una orden `abierta`.

### HU6 — Ejecución de órdenes limitadas
Como sistema, quiero ejecutar órdenes cuando el precio alcanza el objetivo.

- [ ] Al actualizar el precio de una cripto, revisar órdenes abiertas de esa cripto.
- [ ] Orden `compra limite` se ejecuta si `precio_usd <= precio_objetivo`.
- [ ] Orden `venta limite` se ejecuta si `precio_usd >= precio_objetivo`.
- [ ] Si al ejecutar no alcanza saldo/tenencia, la orden se marca como `cancelada`.
- [ ] La ejecución genera la `Transaccion` correspondiente.

### HU7 — Cartera del usuario
Como usuario, quiero ver mi cartera valuada en USD.

- [ ] `GET /usuarios/{id}/cartera` devuelve cada cripto con cantidad y valuación actual.
- [ ] Incluye el saldo en USD.
- [ ] Incluye el total (saldo + suma de tenencias valuadas).

### HU8 — Historial de transacciones
Como usuario, quiero ver todas mis operaciones.

- [ ] `GET /usuarios/{id}/transacciones` devuelve transacciones ordenadas por fecha desc.
- [ ] Se puede filtrar por cripto y por tipo (`compra`/`venta`).
- [ ] Incluye el precio unitario histórico de cada operación.

### HU9 — Historial de precios
Como usuario, quiero ver cómo evolucionó el precio de una cripto.

- [ ] `GET /criptos/{id}/historial` devuelve los últimos N precios con fecha.
- [ ] Se puede filtrar por rango de fechas.
- [ ] Se calcula la variación porcentual entre el primero y el último del rango.

### HU10 — Ganancia o pérdida
Como usuario, quiero saber cuánto gané o perdí por cripto.

- [ ] `GET /usuarios/{id}/pnl` devuelve por cada cripto el costo promedio de compra, la valuación actual y la diferencia.
- [ ] El costo promedio se calcula con el promedio ponderado de las compras.
- [ ] El resultado indica si es ganancia (positivo) o pérdida (negativo).

### HU11 — Comisiones por operación
Como administrador, quiero cobrar una comisión configurable por cada compra y venta.

- [ ] Existe una `comision_porcentaje` global configurable (entre 0 y 5).
- [ ] En compras, se descuenta del saldo `total_usd * (1 + comision/100)`.
- [ ] En ventas, se acredita al saldo `total_usd * (1 - comision/100)`.
- [ ] El monto de comisión cobrado se guarda en la `Transaccion`.
- [ ] `GET /admin/comisiones?desde=...&hasta=...` devuelve el total recaudado en el rango.

### HU12 — Retiros de saldo
Como usuario, quiero retirar saldo en USD a una cuenta bancaria.

- [ ] El retiro tiene un monto mínimo configurable (ej: 10 USD).
- [ ] No se puede retirar más que el saldo disponible.
- [ ] Estados del retiro: `pendiente`, `aprobado`, `rechazado`.
- [ ] Al crear un retiro, el monto se "reserva" (no puede usarse para comprar).
- [ ] Si se rechaza, el monto vuelve a estar disponible; si se aprueba, se descuenta y genera `MovimientoSaldo` tipo `retiro`.

### HU13 — Alertas de precio
Como usuario, quiero que me avisen cuando una cripto alcance un precio.

- [ ] `Alerta` (id, usuario_id, cripto_id, precio_objetivo, direccion, estado).
- [ ] `direccion` puede ser `sube_a` o `baja_a`.
- [ ] Al actualizar el precio de una cripto, se evalúan las alertas activas y se marcan como `disparada` si corresponde.
- [ ] Las alertas disparadas no vuelven a dispararse.
- [ ] `GET /usuarios/{id}/alertas` devuelve activas y disparadas separadas.

### HU14 — Reporte fiscal anual
Como usuario, quiero un resumen anual para impuestos.

- [ ] `GET /usuarios/{id}/reporte-fiscal?anio=2026` devuelve total comprado, total vendido, ganancia/pérdida realizada y comisiones pagadas.
- [ ] La ganancia realizada se calcula con FIFO sobre las ventas del año.
- [ ] Incluye desglose por criptomoneda.
- [ ] Si no hubo operaciones en el año, devuelve los totales en 0.
