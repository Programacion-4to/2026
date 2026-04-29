# Proyecto 6 — Netflix

Plataforma de streaming de películas y series. Cada cuenta tiene varios perfiles, cada perfil ve contenido, marca episodios vistos, arma su lista y califica.

## Entidades sugeridas

- `Cuenta` (id, email, plan, fecha_alta)
- `Perfil` (id, cuenta_id, nombre, es_infantil, avatar)
- `Genero` (id, nombre)
- `Contenido` (id, titulo, tipo, anio, descripcion, duracion_min, clasificacion_edad)
- `Temporada` (id, contenido_id, numero, anio)
- `Episodio` (id, temporada_id, numero, titulo, duracion_min)
- `Vista` (id, perfil_id, episodio_id, fecha, segundos_vistos, terminado)
- `Calificacion` (id, perfil_id, contenido_id, puntaje, fecha)
- Relación N a M `contenido_generos` (contenido_id, genero_id)
- Relación N a M `mi_lista` (perfil_id, contenido_id, fecha_agregada)

## Historias de usuario

### HU1 — Alta de cuenta y planes
Como visitante, quiero registrar una cuenta eligiendo un plan.

- [ ] El email es único.
- [ ] Planes válidos: `basico`, `estandar`, `premium`.
- [ ] Según el plan, la cuenta puede tener máximo: `basico=1`, `estandar=2`, `premium=5` perfiles.

### HU2 — Perfiles dentro de la cuenta
Como titular, quiero crear perfiles dentro de mi cuenta.

- [ ] No se pueden crear más perfiles de los que permite el plan.
- [ ] No puede haber dos perfiles con el mismo nombre en la misma cuenta.
- [ ] Un perfil puede marcarse como `es_infantil = true`.
- [ ] `GET /cuentas/{id}/perfiles` lista los perfiles de la cuenta.

### HU3 — Catálogo: películas y series
Como administrador, quiero cargar películas y series con sus temporadas y episodios.

- [ ] `tipo` es `pelicula` o `serie`.
- [ ] Una película no tiene temporadas ni episodios; tiene `duracion_min` directa.
- [ ] Una serie tiene al menos una temporada, cada temporada al menos un episodio.
- [ ] No puede haber dos temporadas con el mismo número dentro de una serie.
- [ ] Cada contenido tiene al menos un género asociado.

### HU4 — Restricción infantil
Como cuenta, quiero que los perfiles infantiles solo vean contenido apto.

- [ ] Cada contenido tiene una `clasificacion_edad` (ATP, +13, +16, +18).
- [ ] Un perfil `es_infantil` solo puede listar/reproducir contenido `ATP`.
- [ ] Si se intenta reproducir contenido restringido desde un perfil infantil, la API devuelve 403.

### HU5 — Búsqueda y filtros del catálogo
Como perfil, quiero buscar contenido por título, género y tipo.

- [ ] `GET /contenidos?q=texto` filtra por título parcial.
- [ ] `GET /contenidos?genero=accion&tipo=serie` combina filtros.
- [ ] Se pueden pedir los contenidos más recientes con `?ordenar=anio_desc`.
- [ ] El endpoint respeta la restricción infantil si se pasa `perfil_id`.

### HU6 — Marcar vista y progreso
Como perfil, quiero que se guarde cuánto vi de un episodio o película.

- [ ] `segundos_vistos` no puede superar la duración del contenido/episodio.
- [ ] Si se superan el 90% de los segundos, se marca `terminado = true`.
- [ ] Si se vuelve a reproducir, se actualiza la vista existente, no se crea otra.
- [ ] En series, marcar un episodio como terminado no marca la serie como terminada.

### HU7 — Continuar viendo
Como perfil, quiero ver lo último que empecé y no terminé.

- [ ] `GET /perfiles/{id}/continuar` devuelve los 10 contenidos con vistas no terminadas más recientes.
- [ ] En series, muestra el próximo episodio no terminado.
- [ ] Lista ordenada por última fecha de reproducción.

### HU8 — Mi Lista
Como perfil, quiero agregar y sacar contenido de mi lista.

- [ ] Un contenido no puede estar dos veces en la misma lista.
- [ ] `GET /perfiles/{id}/mi-lista` devuelve los contenidos guardados.
- [ ] El contenido se puede quitar en cualquier momento.
- [ ] Mi Lista respeta la restricción infantil.

### HU9 — Calificación
Como perfil, quiero calificar contenidos.

- [ ] Puntaje del 1 al 5.
- [ ] Un perfil solo tiene una calificación por contenido (si vuelve a calificar, la actualiza).
- [ ] `GET /contenidos/{id}` incluye el promedio de calificaciones.
- [ ] Solo se puede calificar un contenido que el perfil haya empezado a ver.

### HU10 — Recomendaciones y tops
Como perfil, quiero ver recomendaciones basadas en lo que vi.

- [ ] `GET /perfiles/{id}/recomendaciones` devuelve 10 contenidos de los géneros más vistos por el perfil, excluyendo los que ya terminó.
- [ ] `GET /contenidos/top` devuelve los 10 más vistos de la plataforma (por cantidad de vistas terminadas).
- [ ] `GET /contenidos/top?genero=drama` filtra el top por género.

### HU11 — Control parental con PIN
Como titular, quiero proteger perfiles adultos con PIN.

- [ ] La cuenta puede setear un `pin` numérico de 4 dígitos.
- [ ] Si hay PIN configurado, acceder a perfiles no infantiles requiere validarlo.
- [ ] `POST /perfiles/{id}/desbloquear` valida el PIN y habilita el perfil por la sesión.
- [ ] Tras 3 intentos fallidos, el perfil queda bloqueado por 15 minutos.
- [ ] Los perfiles infantiles nunca requieren PIN.

### HU12 — Subtítulos e idiomas
Como administrador, quiero cargar idiomas y subtítulos disponibles por contenido.

- [ ] `Idioma` (id, codigo, nombre) y relación N a M `contenido_idiomas` con campo `tipo` (`audio` o `subtitulo`).
- [ ] Cada contenido tiene al menos un idioma de audio.
- [ ] `GET /contenidos/{id}/idiomas` devuelve audios y subtítulos disponibles.
- [ ] Se puede filtrar el catálogo por idioma de audio: `GET /contenidos?audio=es`.

### HU13 — Descargas offline con límite por plan
Como perfil, quiero descargar contenido para ver sin conexión.

- [ ] Límite simultáneo: `basico=0`, `estandar=10`, `premium=30` descargas activas por cuenta.
- [ ] `POST /perfiles/{id}/descargas` crea una descarga; falla si se supera el límite del plan.
- [ ] Una descarga vence a los 30 días o cuando el perfil la elimina.
- [ ] Las descargas vencidas no cuentan para el límite.
- [ ] Perfiles infantiles solo pueden descargar contenido `ATP`.

### HU14 — Reporte de visualización
Como administrador, quiero ver minutos vistos por contenido y por mes.

- [ ] `GET /reportes/visualizacion?anio=2026&mes=4` devuelve los 20 contenidos con más minutos vistos en el mes.
- [ ] Solo cuentan vistas con `terminado = true` o `segundos_vistos >= 90%`.
- [ ] Se incluye el desglose por género.
- [ ] Si no hay datos, devuelve lista vacía con totales en 0.
