# APIs: teoría completa, aspectos y errores

## ¿Qué es una API?

**API** = *Application Programming Interface* (Interfaz de Programación de Aplicaciones).

Es un **contrato** que permite que dos piezas de software se comuniquen entre sí, sin que una necesite saber cómo está implementada la otra. Define:

- **Qué operaciones** se pueden pedir.
- **Qué datos** hay que mandar.
- **Qué respuesta** se va a recibir.
- **Qué errores** pueden ocurrir.

> Analogía: una API es como el **menú de un restaurante**. Vos no entrás a la cocina ni sabés cómo cocinan; solo pedís lo que está en el menú con un formato específico, y recibís el plato.

---

## Tipos de APIs

| Tipo | Dónde se usa | Ejemplo |
|---|---|---|
| **API de librería** | Funciones que llamás desde tu código | `math.sqrt(9)` |
| **API del sistema operativo** | Procesos, archivos, red | `open()`, `read()` |
| **API web (HTTP)** | Comunicación entre cliente y servidor por internet | `GET /users/1` |
| **API de hardware** | Driver ↔ dispositivo | API de la GPU |

Cuando alguien dice "API" sin especificar, generalmente se refiere a una **API web**.

---

## Estilos de API web

### 1. REST (Representational State Transfer)
El más común hoy. Usa **recursos** (sustantivos) y los métodos HTTP como verbos.

```
GET    /users          → listar usuarios
GET    /users/1        → obtener usuario 1
POST   /users          → crear usuario
PUT    /users/1        → reemplazar usuario 1
PATCH  /users/1        → modificar parcialmente
DELETE /users/1        → borrar usuario 1
```

Principios:
- **Stateless**: el servidor no guarda estado de la sesión entre requests.
- **Recursos identificados por URL**.
- **Representaciones**: el mismo recurso puede devolverse en JSON, XML, etc.
- **Verbos HTTP estándar**.

### 2. GraphQL
El cliente pide **exactamente los campos que necesita** en una sola query. Un solo endpoint (`/graphql`).

```graphql
query {
  user(id: 1) { name, email, posts { title } }
}
```

Ventaja: evita over-fetching y under-fetching.
Desventaja: más complejo de cachear y de implementar.

### 3. SOAP
Antiguo, basado en XML. Muy estricto, usado en bancos y sistemas legacy.

### 4. gRPC
Binario (Protocol Buffers), muy rápido. Usado en comunicación entre microservicios.

### 5. WebSockets
Comunicación bidireccional en tiempo real (chat, notificaciones, juegos).

---

## Aspectos de una API HTTP

### 1. URL / Endpoint
La **dirección** del recurso.

```
https://api.miapp.com/v1/users/42?include=posts
└─────┘ └────────────┘ └┘ └────┘ └──────────────┘
protocolo  host         versión  recurso  query params
```

### 2. Método HTTP (verbo)
Indica la **intención** de la operación.

| Método | Uso | Idempotente | Body |
|---|---|---|---|
| `GET` | Leer | Sí | No |
| `POST` | Crear | No | Sí |
| `PUT` | Reemplazar | Sí | Sí |
| `PATCH` | Modificar parcial | No (a veces) | Sí |
| `DELETE` | Borrar | Sí | Opcional |
| `HEAD` | Como GET pero sin body | Sí | No |
| `OPTIONS` | Capacidades del endpoint (CORS) | Sí | No |

> **Idempotente** = ejecutarlo N veces produce el mismo efecto que ejecutarlo 1 vez.

### 3. Headers
Metadatos del request/response.

```http
Content-Type: application/json
Authorization: Bearer eyJhbGc...
Accept: application/json
User-Agent: Mozilla/5.0
X-Request-Id: abc-123
```

Headers comunes:
- **`Content-Type`**: formato del body que envío.
- **`Accept`**: formato que quiero recibir.
- **`Authorization`**: credenciales (Bearer token, Basic auth).
- **`Cache-Control`**: cómo cachear la respuesta.
- **`Cookie` / `Set-Cookie`**: sesiones.

### 4. Body
Datos enviados (en `POST`, `PUT`, `PATCH`). Suele ser JSON.

```json
{
  "email": "ana@mail.com",
  "age": 30
}
```

### 5. Query Params
Filtros, paginación, búsqueda.

```
GET /users?page=2&limit=20&role=admin&q=ana
```

### 6. Path Params
Identifican un recurso específico.

```
GET /users/{user_id}/posts/{post_id}
```

### 7. Status Code
Número de 3 dígitos que indica el resultado.

### 8. Response Body
Datos devueltos. Lo más común es JSON.

```json
{
  "id": 42,
  "email": "ana@mail.com",
  "age": 30
}
```

---

## Status Codes HTTP

### 1xx — Informativos
Rara vez usados directamente.
- `100 Continue`
- `101 Switching Protocols` (WebSockets)

### 2xx — Éxito
| Código | Nombre | Cuándo |
|---|---|---|
| `200` | OK | GET, PUT, PATCH exitosos |
| `201` | Created | POST creó un recurso |
| `202` | Accepted | Procesamiento asíncrono iniciado |
| `204` | No Content | DELETE exitoso, sin body |

### 3xx — Redirecciones
| Código | Nombre | Cuándo |
|---|---|---|
| `301` | Moved Permanently | El recurso se movió de URL |
| `302` | Found | Redirección temporal |
| `304` | Not Modified | Cache válido, no hace falta reenviar |

### 4xx — Error del cliente
**El cliente hizo algo mal.** Estos son los más importantes para diseñar bien una API.

| Código | Nombre | Cuándo |
|---|---|---|
| `400` | Bad Request | Body mal formado, JSON inválido |
| `401` | Unauthorized | No mandaste credenciales o son inválidas |
| `403` | Forbidden | Estás autenticado pero no tenés permiso |
| `404` | Not Found | El recurso no existe |
| `405` | Method Not Allowed | `DELETE` en un endpoint que solo acepta `GET` |
| `409` | Conflict | Conflicto de estado (email ya registrado) |
| `410` | Gone | El recurso existió pero se borró permanentemente |
| `415` | Unsupported Media Type | Mandaste XML cuando se esperaba JSON |
| `422` | Unprocessable Entity | JSON válido pero falla validación de negocio |
| `429` | Too Many Requests | Rate limit excedido |

> **401 vs 403**: 401 = "no sé quién sos", 403 = "sé quién sos pero no podés".

### 5xx — Error del servidor
**El servidor falló.** El cliente no hizo nada mal.

| Código | Nombre | Cuándo |
|---|---|---|
| `500` | Internal Server Error | Excepción no manejada |
| `502` | Bad Gateway | Un servicio del que dependés falló |
| `503` | Service Unavailable | Servidor caído o en mantenimiento |
| `504` | Gateway Timeout | Un servicio dependiente tardó demasiado |

---

## Anatomía de un request/response

### Request
```http
POST /api/v1/users HTTP/1.1
Host: api.miapp.com
Content-Type: application/json
Authorization: Bearer eyJhbGciOi...

{
  "email": "ana@mail.com",
  "password": "secreta123",
  "age": 30
}
```

### Response (éxito)
```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/v1/users/42

{
  "id": 42,
  "email": "ana@mail.com",
  "age": 30,
  "created_at": "2026-04-29T14:22:00Z"
}
```

### Response (error)
```http
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/json

{
  "error": "ValidationError",
  "message": "Datos inválidos",
  "details": [
    { "field": "password", "issue": "must be at least 8 characters" }
  ]
}
```

---

## Autenticación y autorización

| Concepto | Qué es |
|---|---|
| **Autenticación** | Verificar **quién sos** (login) |
| **Autorización** | Verificar **qué podés hacer** (permisos) |

### Mecanismos comunes

- **Basic Auth**: usuario y password en cada request (codificado base64). Inseguro sin HTTPS.
- **API Key**: token estático en el header. Simple pero no expira.
- **JWT (JSON Web Token)**: token firmado que contiene info del usuario. Más usado hoy.
- **OAuth 2.0**: estándar para delegar acceso (ej. "iniciá sesión con Google").
- **Sessions / Cookies**: el server guarda la sesión, manda una cookie al cliente.

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...
```

---

## Versionado de APIs

Cuando rompés el contrato, los clientes viejos se rompen. Para evitarlo, **versionás**:

| Estrategia | Ejemplo |
|---|---|
| **En la URL** | `/api/v1/users`, `/api/v2/users` |
| **En el header** | `Accept: application/vnd.miapp.v2+json` |
| **En query param** | `/api/users?version=2` |

La más común y simple es **en la URL**.

---

## Buenas prácticas REST

1. **Usar sustantivos en plural**: `/users`, no `/getUsers`.
2. **Anidar recursos relacionados**: `/users/1/posts`.
3. **No verbos en URLs**: `POST /users` mejor que `POST /createUser`.
4. **Status codes correctos**: no devolver `200` con `{ "error": "..." }`.
5. **Paginación**: `?page=2&limit=20` o cursor-based.
6. **Filtrado y ordenamiento**: `?role=admin&sort=-created_at`.
7. **HATEOAS** (avanzado): incluir links a recursos relacionados.
8. **Documentación**: OpenAPI/Swagger.
9. **Versionar**: `/v1/...`.
10. **HTTPS siempre**, nunca HTTP en producción.
11. **Idempotencia**: `PUT` y `DELETE` deben poder llamarse N veces sin efecto extra.
12. **Rate limiting**: para evitar abusos.

---

## Errores comunes al diseñar APIs

### 1. Devolver 200 con un error adentro
**Mal:**
```json
HTTP 200 OK
{ "success": false, "error": "Usuario no encontrado" }
```
**Bien:**
```json
HTTP 404 Not Found
{ "error": "User not found" }
```

### 2. Filtrar campos sensibles
Devolver el `password_hash`, `is_admin`, tokens internos. Siempre usar DTOs.

### 3. Confundir 401 y 403
- `401`: faltan credenciales o son inválidas.
- `403`: tenés credenciales válidas pero no permiso para esa acción.

### 4. Usar verbos en las URLs
**Mal:** `POST /createUser`, `GET /getAllProducts`.
**Bien:** `POST /users`, `GET /products`.

### 5. No versionar
Cualquier cambio breaking rompe a todos los clientes existentes.

### 6. Mensajes de error inútiles
**Mal:** `{ "error": "Error" }`.
**Bien:** `{ "error": "ValidationError", "message": "...", "details": [...] }`.

### 7. Exponer stack traces en producción
Filtra rutas internas y versiones de librerías → riesgo de seguridad.

### 8. Endpoints que devuelven todo
`/users` devolviendo 50.000 registros sin paginar = colapso.

### 9. No documentar
Si nadie sabe cómo usar tu API, no existe. Usá OpenAPI/Swagger.

### 10. Nombres inconsistentes
Mezclar `snake_case` y `camelCase`, plural y singular, etc. Elegí uno y mantenelo.

### 11. Cambios breaking sin aviso
Renombrar un campo o cambiar su tipo en `v1` rompe a todos. Si tenés que romper, lanzá `v2`.

### 12. No manejar CORS correctamente
Bloqueás al frontend o lo abrís a `*` en producción. Configurá orígenes específicos.

### 13. Falta de validación de entrada
Confiar en lo que manda el cliente → SQL injection, XSS, datos corruptos. **Validá siempre con schemas.**

### 14. No usar HTTPS
Credenciales y tokens viajando en texto plano.

### 15. Acoplar respuesta a estructura interna
Devolver el `Model` ORM directamente. Si cambiás la BD, cambia tu API. Usá DTOs.

### 16. No manejar timeouts
Si tu API depende de otra y esa otra no responde, te quedás colgado. Definí timeouts.

### 17. No loguear ni monitorear
Sin logs no sabés qué falla en producción. Mínimo: request ID, status, latencia, errores.

### 18. Race conditions en escritura
Dos `PUT` simultáneos sin control de concurrencia → datos perdidos. Usá `ETag` + `If-Match` o transacciones.

---

## Errores comunes al consumir APIs (cliente)

1. **No manejar errores de red**: timeouts, DNS fallido, sin internet.
2. **Asumir que siempre devuelve 200**: chequear el status code.
3. **No reintentar con backoff**: ante un `503` o `429`, esperar antes de reintentar.
4. **Hardcodear la URL**: usar variables de entorno.
5. **No validar la respuesta**: el server puede haber cambiado el contrato.
6. **Loggear datos sensibles**: tokens, passwords en logs del cliente.
7. **No cachear lo que es cacheable**: `GET` con `Cache-Control` puede ahorrarte requests.
8. **Llamar la API en bucle dentro de un componente**: causa loops infinitos en frontends.

---

## Documentación con OpenAPI / Swagger

OpenAPI es un **estándar** para describir APIs en YAML/JSON. Permite:
- Autogenerar documentación interactiva.
- Generar clientes en distintos lenguajes.
- Validar que la implementación cumpla el contrato.

FastAPI **genera Swagger automáticamente** en `/docs` a partir de los Pydantic schemas. Es una de sus mayores ventajas.

```
http://localhost:8000/docs       → Swagger UI
http://localhost:8000/redoc      → ReDoc
http://localhost:8000/openapi.json → spec JSON
```

---

## Resumen visual

```
         ┌─────────────────────────────────────────────┐
         │                  CLIENTE                    │
         │    (browser, mobile app, otro servicio)     │
         └────────────────────┬────────────────────────┘
                              │
                       HTTP Request
              (método + URL + headers + body)
                              │
                              ▼
         ┌─────────────────────────────────────────────┐
         │                   API                       │
         │  ┌───────────────────────────────────────┐  │
         │  │ Router → valida con Schema            │  │
         │  │   ↓                                   │  │
         │  │ Service (lógica)                      │  │
         │  │   ↓                                   │  │
         │  │ Repository → Model → BD               │  │
         │  └───────────────────────────────────────┘  │
         └────────────────────┬────────────────────────┘
                              │
                      HTTP Response
            (status code + headers + body JSON)
                              │
                              ▼
                          CLIENTE
```

---

## En una línea

Una API es **un contrato accesible por red** que define qué pedís, cómo lo pedís y qué recibís. Una buena API es **predecible, segura, versionada, documentada y honesta con sus errores**.
