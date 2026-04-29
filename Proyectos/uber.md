# Proyecto 4 — UBER

App de viajes. Pasajeros piden viajes, el sistema asigna un conductor disponible, se calcula la tarifa según distancia, se registra calificación y método de pago.

## Entidades sugeridas

- `Pasajero` (id, nombre, email, telefono)
- `Conductor` (id, nombre, licencia, calificacion_promedio, disponible)
- `Vehiculo` (id, conductor_id, patente, modelo, anio, categoria)
- `MetodoPago` (id, pasajero_id, tipo, ultimos_digitos)
- `Viaje` (id, pasajero_id, conductor_id, vehiculo_id, metodo_pago_id, origen, destino, distancia_km, fecha_solicitud, fecha_inicio, fecha_fin, estado, tarifa)
- `Calificacion` (id, viaje_id, puntaje_pasajero, puntaje_conductor, comentario)
- `Tarifa` (id, categoria, precio_base, precio_por_km)

## Historias de usuario

### HU1 — Alta de pasajeros y conductores
Como administrador, quiero registrar pasajeros y conductores.

- [ ] El email del pasajero es único.
- [ ] La licencia del conductor es única.
- [ ] El conductor arranca con `calificacion_promedio = 0` y `disponible = true`.

### HU2 — Vehículos del conductor
Como conductor, quiero asociar uno o varios vehículos a mi cuenta.

- [ ] La patente es única.
- [ ] La categoría del vehículo es `economico`, `confort` o `premium`.
- [ ] Un vehículo pertenece a un solo conductor.
- [ ] `GET /conductores/{id}/vehiculos` lista sus vehículos.

### HU3 — Métodos de pago
Como pasajero, quiero cargar y elegir métodos de pago.

- [ ] Tipos válidos: `tarjeta_credito`, `tarjeta_debito`, `efectivo`, `billetera_virtual`.
- [ ] Solo se guardan los últimos 4 dígitos en tarjetas.
- [ ] `GET /pasajeros/{id}/metodos-pago` lista los métodos del pasajero.

### HU4 — Tarifas por categoría
Como administrador, quiero definir tarifas por categoría de vehículo.

- [ ] Existe una sola tarifa activa por categoría.
- [ ] `precio_base` y `precio_por_km` son mayores a 0.
- [ ] `GET /tarifas` devuelve las tarifas vigentes.

### HU5 — Solicitar viaje
Como pasajero, quiero pedir un viaje indicando origen, destino y categoría.

- [ ] El viaje se crea en estado `pendiente`.
- [ ] Debe elegirse un método de pago válido del pasajero.
- [ ] La tarifa se calcula como `precio_base + precio_por_km * distancia_km`.
- [ ] La tarifa se guarda al crear el viaje (no cambia si después cambia la tarifa).

### HU6 — Asignación de conductor
Como sistema, quiero asignar un conductor disponible al viaje.

- [ ] Solo se asignan conductores con `disponible = true`.
- [ ] El conductor debe tener al menos un vehículo de la categoría pedida.
- [ ] Al asignar, el conductor pasa a `disponible = false`.
- [ ] Si no hay conductor, el viaje pasa a estado `sin_conductor`.

### HU7 — Flujo del viaje
Como conductor, quiero marcar el avance del viaje.

- [ ] Estados: `pendiente`, `asignado`, `en_curso`, `finalizado`, `cancelado`.
- [ ] `asignado -> en_curso` registra `fecha_inicio`.
- [ ] `en_curso -> finalizado` registra `fecha_fin` y libera al conductor (`disponible = true`).
- [ ] Un viaje solo puede cancelarse si está en `pendiente` o `asignado`.
- [ ] Transiciones inválidas se rechazan.

### HU8 — Calificación mutua
Como pasajero y como conductor, quiero calificarnos al finalizar el viaje.

- [ ] Solo se puede calificar un viaje en estado `finalizado`.
- [ ] Los puntajes van de 1 a 5.
- [ ] Cada viaje tiene una sola calificación (pasajero y conductor se califican ahí).
- [ ] Al calificar al conductor se recalcula su `calificacion_promedio`.

### HU9 — Historial del pasajero
Como pasajero, quiero ver mi historial y cuánto gasté.

- [ ] `GET /pasajeros/{id}/viajes` devuelve sus viajes con conductor, tarifa y estado.
- [ ] Se puede filtrar por rango de fechas.
- [ ] Incluye el total gastado en viajes `finalizados`.

### HU10 — Ranking de conductores
Como administrador, quiero ver a los mejores conductores.

- [ ] `GET /conductores/top` devuelve los 10 con mejor `calificacion_promedio`.
- [ ] Solo se consideran conductores con al menos 5 viajes finalizados.
- [ ] El resultado incluye cantidad de viajes y calificación.

### HU11 — Tarifa dinámica por horario pico
Como administrador, quiero aplicar un multiplicador en horarios de alta demanda.

- [ ] Existe `MultiplicadorHorario` (id, dia_semana, hora_desde, hora_hasta, factor) con factor > 1.
- [ ] Al crear un viaje, si la `fecha_solicitud` cae en una franja activa, la tarifa se multiplica por `factor`.
- [ ] El multiplicador aplicado se guarda en el viaje (no cambia si después se edita la franja).
- [ ] No pueden superponerse dos franjas para el mismo `dia_semana`.

### HU12 — Cancelación con penalidad
Como sistema, quiero cobrar penalidad si el pasajero cancela tarde.

- [ ] Si el viaje está en `asignado` y se cancela, se aplica una penalidad fija (configurable).
- [ ] La penalidad se registra como un `Cargo` asociado al viaje.
- [ ] Si el viaje se cancela en `pendiente`, no hay penalidad.
- [ ] El conductor cancelado vuelve a `disponible = true`.
- [ ] `GET /pasajeros/{id}/viajes` muestra los cargos por penalidad si existen.

### HU13 — Cupones de viaje
Como pasajero, quiero usar un cupón para descontar el viaje.

- [ ] Cupón con `codigo` único, `porcentaje_descuento` (1–100) y `fecha_vencimiento`.
- [ ] El cupón se aplica al solicitar el viaje y queda asociado al `Viaje`.
- [ ] Cada pasajero puede usar el mismo cupón una sola vez.
- [ ] La tarifa final guardada incluye el descuento (no se recalcula).
- [ ] No se acepta cupón vencido.

### HU14 — Reporte mensual del conductor
Como conductor, quiero ver mi resumen mensual.

- [ ] `GET /conductores/{id}/reporte?anio=2026&mes=4` devuelve cantidad de viajes finalizados, ingresos totales y kilómetros recorridos.
- [ ] Incluye calificación promedio del mes.
- [ ] Si el conductor no operó en ese mes, los totales son 0.
- [ ] Solo cuentan viajes en estado `finalizado`.
