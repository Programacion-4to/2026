# Proyecto 1 — Spotify

Plataforma de streaming de música. Los usuarios arman playlists, siguen artistas, marcan canciones como favoritas y registran qué escucharon.

## Entidades sugeridas

- `Usuario` (id, email, nombre, fecha_registro, plan)
- `Artista` (id, nombre, pais, genero_musical)
- `Album` (id, titulo, anio, artista_id)
- `Cancion` (id, titulo, duracion_seg, album_id)
- `Playlist` (id, nombre, usuario_id, fecha_creacion, es_publica)
- `Reproduccion` (id, usuario_id, cancion_id, fecha, segundos_escuchados)
- Relación N a M `playlist_canciones` (playlist_id, cancion_id, orden, fecha_agregada)
- Relación N a M `favoritos` (usuario_id, cancion_id)
- Relación N a M `seguidores` (usuario_id, artista_id)

## Historias de usuario

### HU1 — Registro de usuario
Como visitante, quiero registrarme con email y plan para usar la plataforma.

- [ ] El email es único, no se pueden registrar dos usuarios con el mismo email.
- [ ] El plan solo puede ser `free`, `premium` o `familiar`.
- [ ] Al registrarse se guarda `fecha_registro` automática.
- [ ] `POST /usuarios` devuelve 201 y el usuario creado sin datos sensibles.

### HU2 — Alta de artistas, álbumes y canciones
Como administrador, quiero cargar artistas con sus álbumes y canciones.

- [ ] No puede existir un álbum sin artista.
- [ ] No puede existir una canción sin álbum.
- [ ] La duración de la canción está en segundos y es mayor a 0.
- [ ] Se puede obtener `GET /artistas/{id}/albumes` con todos sus álbumes.
- [ ] Se puede obtener `GET /albumes/{id}/canciones` con todas sus canciones.

### HU3 — Crear y editar playlists
Como usuario, quiero crear playlists propias y ponerles nombre.

- [ ] Una playlist siempre pertenece a un usuario.
- [ ] Un mismo usuario no puede tener dos playlists con el mismo nombre.
- [ ] La playlist puede marcarse como pública o privada.
- [ ] Solo el dueño puede editarla o borrarla (validar con `usuario_id`).

### HU4 — Agregar y quitar canciones de una playlist
Como usuario, quiero armar el contenido de mis playlists.

- [ ] La misma canción no puede estar dos veces en la misma playlist.
- [ ] Al agregar se guarda el `orden` (posición) dentro de la playlist.
- [ ] Al quitar una canción se reordenan las posiciones restantes.
- [ ] `GET /playlists/{id}` devuelve las canciones en el orden correcto.

### HU5 — Favoritos
Como usuario, quiero marcar canciones como favoritas.

- [ ] No se puede marcar dos veces la misma canción como favorita.
- [ ] `GET /usuarios/{id}/favoritos` devuelve todas las canciones favoritas del usuario.
- [ ] Se puede quitar de favoritos con `DELETE /usuarios/{id}/favoritos/{cancion_id}`.

### HU6 — Seguir artistas
Como usuario, quiero seguir artistas para que aparezcan en mi feed.

- [ ] Un usuario no puede seguir dos veces al mismo artista.
- [ ] `GET /usuarios/{id}/seguidos` lista los artistas que sigue.
- [ ] `GET /artistas/{id}/seguidores` lista cuántos y quiénes siguen al artista.

### HU7 — Registrar reproducciones
Como sistema, quiero guardar cada reproducción para calcular estadísticas.

- [ ] Se guarda fecha, usuario, canción y segundos escuchados.
- [ ] `segundos_escuchados` no puede superar la duración de la canción.
- [ ] Si los segundos escuchados son menores al 30% de la canción, no cuenta para estadísticas.

### HU8 — Búsqueda
Como usuario, quiero buscar canciones, artistas o álbumes por texto.

- [ ] `GET /buscar?q=texto` devuelve coincidencias parciales en los tres tipos.
- [ ] La respuesta separa los resultados en `canciones`, `artistas` y `albumes`.
- [ ] La búsqueda no distingue mayúsculas y minúsculas.

### HU9 — Top y estadísticas
Como usuario, quiero ver mis canciones y artistas más escuchados.

- [ ] `GET /usuarios/{id}/top-canciones` devuelve las 10 canciones más reproducidas por ese usuario.
- [ ] `GET /usuarios/{id}/top-artistas` devuelve los 10 artistas más escuchados.
- [ ] Solo cuentan las reproducciones "válidas" (criterio de HU7).
- [ ] Los resultados están ordenados de mayor a menor cantidad.

### HU10 — Duración total y resumen de playlist
Como usuario, quiero ver la duración total de una playlist.

- [ ] `GET /playlists/{id}/resumen` devuelve cantidad de canciones y duración total formateada (hh:mm:ss).
- [ ] El cálculo se hace en el servidor, no en el cliente.

### HU11 — Playlists colaborativas
Como usuario, quiero invitar a otros usuarios a editar mis playlists.

- [ ] Una playlist puede marcarse como `colaborativa = true`.
- [ ] `POST /playlists/{id}/colaboradores` agrega un colaborador por `usuario_id`.
- [ ] Solo el dueño puede agregar o quitar colaboradores.
- [ ] Los colaboradores pueden agregar y quitar canciones, pero no borrar la playlist ni renombrarla.
- [ ] `GET /playlists/{id}` muestra dueño y colaboradores.

### HU12 — Recomendaciones por género
Como usuario, quiero recibir recomendaciones según lo que escucho.

- [ ] `GET /usuarios/{id}/recomendaciones` devuelve 10 canciones de los géneros más escuchados por el usuario.
- [ ] Se excluyen canciones ya reproducidas por el usuario en los últimos 30 días.
- [ ] Si el usuario tiene menos de 5 reproducciones válidas, se devuelven canciones del top global.
- [ ] El criterio de "género más escuchado" usa el `genero_musical` del artista de cada canción.

### HU13 — Resumen anual del usuario (Wrapped)
Como usuario, quiero un resumen de mi año musical.

- [ ] `GET /usuarios/{id}/resumen?anio=2026` devuelve top 5 canciones, top 5 artistas y top 3 géneros del año.
- [ ] Incluye total de minutos escuchados y cantidad de canciones distintas.
- [ ] Solo cuentan reproducciones válidas (criterio HU7) del año pedido.
- [ ] Si el usuario no tuvo reproducciones en ese año, devuelve 404.

### HU14 — Letras y duración escuchada por canción
Como administrador, quiero saber qué tan completas se escuchan las canciones.

- [ ] `GET /canciones/{id}/estadisticas` devuelve cantidad de reproducciones, reproducciones válidas y porcentaje promedio escuchado.
- [ ] El porcentaje se calcula como `promedio(segundos_escuchados / duracion_seg) * 100`.
- [ ] Se puede filtrar por rango de fechas.
- [ ] Si la canción no tiene reproducciones, devuelve los campos en 0.
