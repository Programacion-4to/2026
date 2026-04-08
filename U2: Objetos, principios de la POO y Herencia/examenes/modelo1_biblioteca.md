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

## Ejemplo de uso esperado

```python
a1 = Autor("Antoine de Saint-Exupéry", "Francesa")
a2 = Autor("Gabriel García Márquez", "Colombiana")

l1 = Libro("El Principito", a1)
l2 = LibroDigital("Vuelo Nocturno", a1, "PDF")
l3 = Libro("Cien años de soledad", a2)

bib = Biblioteca("Biblioteca Central")
bib.agregar_libro(l1)
bib.agregar_libro(l2)
bib.agregar_libro(l3)

bib.listar()
# El Principito - Antoine de Saint-Exupéry (Francesa)
# Vuelo Nocturno - Antoine de Saint-Exupéry (Francesa) [PDF]
# Cien años de soledad - Gabriel García Márquez (Colombiana)

encontrados = bib.buscar_por_autor("Antoine de Saint-Exupéry")
for libro in encontrados:
    libro.mostrar()
# El Principito - Antoine de Saint-Exupéry (Francesa)
# Vuelo Nocturno - Antoine de Saint-Exupéry (Francesa) [PDF]
```
