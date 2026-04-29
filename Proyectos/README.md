# Consignas de Proyectos — Unidad 3 y 4

Cada alumno / grupo elige **un proyecto**. Todos están calibrados al mismo nivel de complejidad:

- 5 o 6 entidades principales.
- Al menos dos relaciones 1 a N y una relación N a M.
- CRUD completo de las entidades principales.
- Reglas de negocio que validar (estados, stock, saldo, unicidad, etc).
- Consultas "no-CRUD" que responden preguntas del negocio (top, historial, totales, filtros combinados).

## Formato de historia de usuario

> **Como** \<rol\>, **quiero** \<acción\>, **para** \<objetivo\>.

Cada historia trae sus **criterios de aceptación** en formato checklist. Para entregar la historia, **todos** los criterios tienen que estar marcados.

## Archivos

- [1. Spotify](./spotify.md)
- [2. Rappi](./rappi.md)
- [3. Adidas](./adidas.md)
- [4. UBER](./uber.md)
- [5. Binance](./binance.md)
- [6. Netflix](./netflix.md)

## Entregables comunes

1. **Modelo de datos** (diagrama simple, puede ser a mano o en draw.io).
2. **Script SQL** con `CREATE TABLE` de todas las entidades y al menos 5 filas de ejemplo por tabla.
3. **Modelos SQLAlchemy** en `app/models/`.
4. **Schemas Pydantic** (`Base`, `Create`, `Update`, `Read`) en `app/schemas/`.
5. **API REST** con FastAPI: CRUD + consultas especiales.
6. **README** con: cómo correrlo, qué endpoint cubre cada historia de usuario y ejemplos de request/response.
