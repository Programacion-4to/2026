# Ejercicio: Mini Minecraft 2D

Tenés que armar una simulación 2D, vista desde arriba, inspirada en Minecraft. Usá `pygame` para la parte gráfica.

La simulación debe permitir:

- Un **mundo** formado por bloques de distintos tipos (al menos tres tipos diferentes, por ejemplo tierra, piedra y madera). Cada tipo debe verse distinto en pantalla.
- Un **jugador** que se mueve por el mundo con el teclado.
- **Romper** un bloque del mundo: cuando se rompe, deja un espacio vacío y el bloque pasa al inventario del jugador.
- **Colocar** un bloque del inventario en un espacio vacío del mundo.
- Un **inventario** visible en pantalla que muestre qué bloques tiene el jugador y cuántos de cada tipo.

Todo el código tiene que vivir en `minecraft.py`. Vos decidís los atributos, los parámetros y cómo se relacionan las clases entre sí.

## Clases y métodos

- `Bloque`
  - `dibujar`
- `Tierra` (hereda de `Bloque`)
- `Piedra` (hereda de `Bloque`)
- `Madera` (hereda de `Bloque`)
- `Mundo`
  - `obtener_bloque`
  - `romper_bloque`
  - `colocar_bloque`
  - `dibujar`
- `Jugador`
  - `mover`
  - `romper`
  - `colocar`
  - `dibujar`
- `Inventario`
  - `agregar`
  - `sacar`
  - `dibujar`
- `Juego`
  - `correr`

Cuando termines, ejecutar `python minecraft.py` debe abrir la ventana y dejar jugar.
