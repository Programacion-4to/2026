# Modelo 7 — Torneo de Fútbol

## Clase `Jugador` *(base)*

| Tipo | Descripción |
|---|---|
| Atributo de clase | `POSICIONES_VALIDAS = ("Arquero", "Defensor", "Mediocampista", "Delantero")` — únicas posiciones permitidas |
| Atributo | `nombre` — nombre del jugador |
| Atributo | `posicion` — posición en la cancha |
| Atributo | `goles` — goles anotados |
| Método | `anotar_gol()` — incrementa en 1 los goles del jugador |
| Método | `mostrar()` — muestra los datos del jugador |

> Si la posición no está en `POSICIONES_VALIDAS`, lanzar un `ValueError`.

## Clase `Capitan` *(hereda de `Jugador`)*

| Tipo | Descripción |
|---|---|
| Atributo de clase | `ROL = "Capitán"` — rol fijo para todos los capitanes |
| Atributo | `numero_camiseta` — número de camiseta del capitán |
| Método | `mostrar()` — muestra los datos del jugador indicando que es capitán y su número |

## Clase `Suplente` *(hereda de `Jugador`)*

| Tipo | Descripción |
|---|---|
| Atributo de clase | `ROL = "Suplente"` — rol fijo para todos los suplentes |
| Método | `mostrar()` — muestra los datos del jugador indicando que es suplente |

## Clase `Equipo`

| Tipo | Descripción |
|---|---|
| Atributo | `nombre` — nombre del equipo |
| Atributo | `jugadores` — jugadores que integran el equipo |
| Método | `agregar_jugador(jugador)` — incorpora un jugador al equipo |
| Método | `total_goles()` — retorna la suma de goles de todos los jugadores |
| Método | `goleador()` — retorna el jugador con más goles (lanzar `ValueError` si no hay jugadores) |
| Método | `guardar_estadisticas()` — guarda nombre del equipo y goles de cada jugador en un archivo |

## Clase `Torneo`

| Tipo | Descripción |
|---|---|
| Atributo de clase | `MAX_EQUIPOS = 8` — máximo de equipos permitidos |
| Atributo | `nombre` — nombre del torneo |
| Atributo | `equipos` — equipos participantes |
| Método | `registrar_equipo(equipo)` — registra un equipo (lanzar `ValueError` si ya está registrado o si se superó `MAX_EQUIPOS`) |
| Método | `lider()` — retorna el equipo con más goles |
| Método | `guardar_resultados()` — guarda la tabla de posiciones en un archivo |
| Método | `cargar_resultados(archivo)` — lee y muestra los resultados guardados |

## Ejemplo de uso esperado

```python
print(Jugador.POSICIONES_VALIDAS)  # ("Arquero", "Defensor", "Mediocampista", "Delantero")
print(Torneo.MAX_EQUIPOS)          # 8

try:
    j_inv = Jugador("Carlos", "Portero", 0)
except ValueError as e:
    print(e)  # Posición inválida: Portero

c1 = Capitan("Messi", "Delantero", 0, 10)
s1 = Suplente("Dybala", "Mediocampista", 0)

c1.mostrar()   # Capitán #10 | Messi | Delantero | 0 goles
s1.mostrar()   # Suplente | Dybala | Mediocampista | 0 goles

c1.anotar_gol()
c1.anotar_gol()

equipo1 = Equipo("Los Tigres")
equipo1.agregar_jugador(c1)
equipo1.agregar_jugador(s1)

print(equipo1.total_goles())   # 2
print(equipo1.goleador().nombre)  # Messi

torneo = Torneo("Copa Python")
torneo.registrar_equipo(equipo1)

try:
    torneo.registrar_equipo(equipo1)  # Ya registrado
except ValueError as e:
    print(e)

torneo.guardar_resultados()
# Genera: copa_python.txt

torneo.cargar_resultados("copa_python.txt")
# Los Tigres - 2 goles
```
