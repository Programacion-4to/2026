# Proyecto 2 — Rappi

App de delivery. Clientes piden comida a restaurantes, se asigna un repartidor y se registra cada pedido con su estado.

## Entidades sugeridas

- `Cliente` (id, nombre, email, direccion, telefono)
- `Restaurante` (id, nombre, categoria, direccion, calificacion_promedio)
- `Plato` (id, nombre, descripcion, precio, disponible, restaurante_id)
- `Repartidor` (id, nombre, vehiculo, disponible)
- `Pedido` (id, cliente_id, restaurante_id, repartidor_id, fecha, estado, total, direccion_entrega)
- `Calificacion` (id, pedido_id, puntaje, comentario, fecha)
- Relación N a M `pedido_platos` (pedido_id, plato_id, cantidad, precio_unitario)

## Historias de usuario

### HU1 — Alta de restaurantes y menú
Como administrador, quiero dar de alta restaurantes y cargar sus platos.

- [ ] Cada plato pertenece a un solo restaurante.
- [ ] El precio del plato es mayor a 0.
- [ ] Un plato puede marcarse como "no disponible" sin borrarlo.
- [ ] `GET /restaurantes/{id}/menu` devuelve solo los platos disponibles.

### HU2 — Alta de clientes y repartidores
Como administrador, quiero registrar clientes y repartidores.

- [ ] El email del cliente es único.
- [ ] El repartidor tiene un estado `disponible` booleano.
- [ ] `GET /repartidores/disponibles` lista los que están libres.

### HU3 — Buscar restaurantes
Como cliente, quiero buscar restaurantes por nombre o categoría.

- [ ] `GET /restaurantes?q=texto` filtra por nombre parcial.
- [ ] `GET /restaurantes?categoria=sushi` filtra por categoría exacta.
- [ ] Se pueden combinar ambos filtros.
- [ ] Los resultados se ordenan por calificación_promedio descendente.

### HU4 — Crear pedido
Como cliente, quiero armar un pedido con varios platos.

- [ ] Todos los platos del pedido deben ser del mismo restaurante.
- [ ] Solo se pueden pedir platos marcados como `disponible`.
- [ ] La cantidad por plato es mayor a 0.
- [ ] Se guarda el `precio_unitario` del momento del pedido (no cambia si después cambia el precio).
- [ ] El pedido se crea con estado `pendiente`.

### HU5 — Asignación de repartidor
Como sistema, quiero asignar un repartidor disponible al pedido.

- [ ] Solo se asignan repartidores con `disponible = true`.
- [ ] Al asignar, el repartidor pasa a `disponible = false`.
- [ ] Si no hay repartidores disponibles, el pedido queda en estado `sin_repartidor`.
- [ ] `POST /pedidos/{id}/asignar` intenta asignar un repartidor.

### HU6 — Cambio de estado del pedido
Como repartidor, quiero actualizar el estado del pedido durante el recorrido.

- [ ] Los estados válidos son: `pendiente`, `confirmado`, `en_preparacion`, `en_camino`, `entregado`, `cancelado`.
- [ ] Las transiciones inválidas se rechazan (ej: de `pendiente` a `entregado`).
- [ ] Cuando el pedido pasa a `entregado`, el repartidor vuelve a `disponible = true`.
- [ ] Un pedido `entregado` o `cancelado` no se puede modificar más.

### HU7 — Total del pedido
Como cliente, quiero ver el total del pedido con el desglose.

- [ ] `GET /pedidos/{id}` devuelve platos, cantidades, subtotales y total.
- [ ] El total se calcula en el servidor sumando `cantidad * precio_unitario`.

### HU8 — Historial del cliente
Como cliente, quiero ver mi historial de pedidos.

- [ ] `GET /clientes/{id}/pedidos` devuelve los pedidos ordenados por fecha desc.
- [ ] Se puede filtrar por estado: `GET /clientes/{id}/pedidos?estado=entregado`.
- [ ] Incluye el total gastado acumulado del cliente.

### HU9 — Calificar pedido
Como cliente, quiero calificar un pedido después de recibirlo.

- [ ] Solo se puede calificar un pedido en estado `entregado`.
- [ ] El puntaje va de 1 a 5.
- [ ] Un pedido se puede calificar una sola vez.
- [ ] Al calificar, se recalcula `calificacion_promedio` del restaurante.

### HU10 — Ranking de restaurantes y platos
Como administrador, quiero saber qué se vende más.

- [ ] `GET /restaurantes/top` devuelve los 5 con más pedidos entregados.
- [ ] `GET /platos/top` devuelve los 10 platos más vendidos (por cantidad total).
- [ ] Ambos listados se ordenan de mayor a menor.

### HU11 — Cupones de descuento
Como cliente, quiero aplicar un cupón a mi pedido.

- [ ] El código del cupón es único y tiene un porcentaje entre 1 y 100.
- [ ] Un cupón tiene fecha de vencimiento y `usos_maximos`.
- [ ] No se acepta un cupón vencido o sin usos disponibles.
- [ ] El descuento se aplica sobre el subtotal del pedido.
- [ ] Al confirmar el pedido se incrementa `usos_actuales`; si se cancela antes de `confirmado`, no cuenta.

### HU12 — Zonas de cobertura
Como administrador, quiero limitar a qué direcciones entrega cada restaurante.

- [ ] Cada restaurante tiene una o varias `Zona` (id, restaurante_id, nombre, codigo_postal).
- [ ] Al crear un pedido, la `direccion_entrega` debe coincidir con alguna zona del restaurante (se valida por `codigo_postal`).
- [ ] Si la dirección está fuera de zona, el pedido se rechaza con 400.
- [ ] `GET /restaurantes?codigo_postal=1414` devuelve solo los que cubren esa zona.

### HU13 — Notificaciones de pedido
Como cliente, quiero recibir un registro de cada cambio de estado de mi pedido.

- [ ] Cada cambio de estado genera un registro en `Notificacion` (id, pedido_id, estado_nuevo, fecha, leida).
- [ ] `GET /clientes/{id}/notificaciones` devuelve las notificaciones del cliente, no leídas primero.
- [ ] `PATCH /notificaciones/{id}` permite marcar como leída.
- [ ] No se generan notificaciones para transiciones inválidas.

### HU14 — Reporte de ventas por restaurante
Como administrador del restaurante, quiero ver mis ventas.

- [ ] `GET /restaurantes/{id}/reporte?desde=...&hasta=...` devuelve cantidad de pedidos entregados, facturación total y ticket promedio.
- [ ] Solo cuentan pedidos en estado `entregado`.
- [ ] Incluye los 5 platos más vendidos en el rango.
- [ ] Si no hay pedidos en el rango, los totales son 0 y la lista vacía.
