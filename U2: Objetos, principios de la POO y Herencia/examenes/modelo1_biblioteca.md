# Modelo 1 — Biblioteca

## Clase `Autor`

| Tipo | Descripción |
|---|---|
| Atributo | `nombre` — nombre del autor |
| Atributo | `nacionalidad` — país de origen |
| Método | `mostrar()` — muestra los datos del autor |

## Clase `Libro` *(base)*

| Tipo | Descripción |
|---|---|
| Atributo | `titulo` — título del libro |
| Atributo | `autor` — autor del libro |
| Método | `mostrar()` — muestra los datos del libro |

## Clase `LibroDigital` *(hereda de `Libro`)*

| Tipo | Descripción |
|---|---|
| Atributo | `formato` — formato del archivo (PDF, EPUB, etc.) |
| Método | `mostrar()` — muestra los datos del libro incluyendo el formato |

## Clase `Biblioteca`

| Tipo | Descripción |
|---|---|
| Atributo | `nombre` — nombre de la biblioteca |
| Atributo | `libros` — libros disponibles |
| Método | `agregar_libro(libro)` — incorpora un libro a la biblioteca |
| Método | `buscar_por_autor(nombre_autor)` — retorna los libros de ese autor |
| Método | `listar()` — muestra todos los libros disponibles |
