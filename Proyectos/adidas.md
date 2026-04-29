# Proyecto 3 — Adidas

Tienda online de indumentaria deportiva. Productos con variantes de talle/color, stock, compras con múltiples ítems y cupones de descuento.

## Entidades sugeridas

- `Categoria` (id, nombre, descripcion)
- `Producto` (id, nombre, descripcion, precio_base, categoria_id, activo)
- `Variante` (id, producto_id, talle, color, stock, sku)
- `Cliente` (id, nombre, email, direccion)
- `Cupon` (id, codigo, porcentaje_descuento, fecha_vencimiento, usos_maximos, usos_actuales)
- `Compra` (id, cliente_id, fecha, total, estado, cupon_id)
- Relación N a M `compra_items` (compra_id, variante_id, cantidad, precio_unitario)

## Historias de usuario

### HU1 — Alta de categorías y productos
Como administrador, quiero crear categorías y productos dentro de ellas.

- [ ] El nombre de categoría es único.
- [ ] Todo producto pertenece a una categoría.
- [ ] El `precio_base` es mayor a 0.
- [ ] Un producto puede marcarse como `activo = false` sin borrarlo.

### HU2 — Variantes de producto
Como administrador, quiero cargar variantes con talle, color y stock.

- [ ] No pueden existir dos variantes con el mismo talle y color para el mismo producto.
- [ ] El stock nunca es negativo.
- [ ] El `sku` es único en todo el sistema.
- [ ] `GET /productos/{id}/variantes` lista todas las variantes del producto.

### HU3 — Buscar productos
Como cliente, quiero filtrar productos por categoría, talle y color.

- [ ] `GET /productos?categoria=running&talle=42&color=negro` combina los tres filtros.
- [ ] Solo se muestran productos con `activo = true`.
- [ ] Solo aparecen productos que tengan al menos una variante con stock > 0 que cumpla los filtros.

### HU4 — Cupones de descuento
Como administrador, quiero crear cupones con porcentaje y fecha de vencimiento.

- [ ] El código del cupón es único.
- [ ] El porcentaje está entre 1 y 100.
- [ ] No se puede usar un cupón vencido.
- [ ] No se puede usar un cupón que ya alcanzó `usos_maximos`.

### HU5 — Crear compra
Como cliente, quiero comprar varias variantes en una sola operación.

- [ ] Todos los ítems tienen cantidad mayor a 0.
- [ ] Cada ítem debe tener stock suficiente.
- [ ] Si cualquier ítem falla por stock, no se descuenta nada (todo o nada).
- [ ] Se guarda el `precio_unitario` del momento de la compra.
- [ ] La compra se crea en estado `pendiente_pago`.

### HU6 — Aplicar cupón en la compra
Como cliente, quiero usar un cupón en mi compra para obtener descuento.

- [ ] El cupón se valida (existe, no vencido, usos disponibles).
- [ ] El total final se calcula como `subtotal * (1 - porcentaje / 100)`.
- [ ] Al confirmar la compra, se incrementa `usos_actuales` del cupón.
- [ ] Si la compra se cancela antes de pagar, el uso del cupón no cuenta.

### HU7 — Descuento de stock
Como sistema, quiero descontar el stock cuando se paga la compra.

- [ ] Solo se descuenta stock cuando la compra pasa a estado `pagada`.
- [ ] Si una compra se cancela después de pagar, el stock se repone.
- [ ] Estados válidos: `pendiente_pago`, `pagada`, `enviada`, `entregada`, `cancelada`.
- [ ] Las transiciones inválidas se rechazan.

### HU8 — Historial del cliente
Como cliente, quiero ver todas mis compras.

- [ ] `GET /clientes/{id}/compras` devuelve compras ordenadas por fecha desc.
- [ ] Cada compra incluye sus ítems y el total.
- [ ] Se puede filtrar por estado.

### HU9 — Productos más vendidos
Como administrador, quiero saber qué se vende más.

- [ ] `GET /productos/top` devuelve los 10 productos con más unidades vendidas.
- [ ] Solo cuentan compras en estado `pagada`, `enviada` o `entregada`.
- [ ] El resultado incluye cantidad total vendida y facturación acumulada.

### HU10 — Stock bajo
Como administrador, quiero detectar variantes con stock crítico.

- [ ] `GET /variantes/stock-bajo?umbral=5` devuelve todas las variantes con stock menor o igual al umbral.
- [ ] Incluye datos del producto al que pertenecen.
- [ ] Se ordena por stock ascendente.

### HU11 — Carrito persistente
Como cliente, quiero armar un carrito antes de confirmar la compra.

- [ ] Cada cliente tiene un único carrito activo (`Carrito` con `cliente_id` único).
- [ ] `POST /clientes/{id}/carrito/items` agrega una variante con cantidad; si ya estaba, suma cantidades.
- [ ] No se puede agregar al carrito una variante sin stock disponible.
- [ ] `GET /clientes/{id}/carrito` devuelve los ítems con subtotal y total calculados al precio actual.
- [ ] Confirmar la compra desde el carrito vacía el carrito y crea la `Compra` (HU5).

### HU12 — Reseñas de productos
Como cliente, quiero dejar una reseña de un producto comprado.

- [ ] Solo puede reseñar un producto quien lo haya comprado en una compra `entregada`.
- [ ] Puntaje entre 1 y 5, con comentario opcional.
- [ ] Un cliente solo deja una reseña por producto; si vuelve a reseñar, se actualiza.
- [ ] `GET /productos/{id}` incluye el promedio y la cantidad de reseñas.
- [ ] `GET /productos/{id}/resenas` lista las reseñas, más recientes primero.

### HU13 — Devoluciones
Como cliente, quiero solicitar la devolución de una compra entregada.

- [ ] Solo se permite solicitar devolución dentro de los 30 días posteriores a `entregada`.
- [ ] La devolución se aplica a ítems específicos de la compra, no necesariamente a toda.
- [ ] Estados de la devolución: `solicitada`, `aprobada`, `rechazada`, `reintegrada`.
- [ ] Al pasar a `reintegrada` se repone el stock de las variantes devueltas.
- [ ] Una compra con devolución `reintegrada` no se puede volver a devolver por los mismos ítems.

### HU14 — Reporte de facturación
Como administrador, quiero un reporte de facturación por período.

- [ ] `GET /reportes/facturacion?desde=...&hasta=...` devuelve total facturado y cantidad de compras.
- [ ] Solo cuentan compras en estado `pagada`, `enviada` o `entregada`.
- [ ] Se descuentan los montos de devoluciones `reintegradas` del período.
- [ ] Incluye desglose por categoría de producto.
