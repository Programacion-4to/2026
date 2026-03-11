## 2. Archivos

### ¿Qué es un archivo?

Un **archivo** es un lugar donde se guardan datos en el disco para poder utilizarlos posteriormente.
Los archivos pueden tener distintos **formatos**, dependiendo del tipo de información que contienen.

Algunos ejemplos de formatos son:

* **txt** → texto plano
* **csv** → texto plano separado por comas
* **json** → texto plano con estructura de objetos
* **xls / xlsx** → formato de Excel
* **doc / docx** → formato de Word
* **pdf** → documento portable

Existen muchos otros formatos dependiendo del tipo de archivo.

---

### Abrir archivos en Python

Para trabajar con archivos en Python es necesario **abrir el archivo primero**.
Para esto se utiliza la función `open()`.

Esta función recibe como parámetros:

1. **El nombre del archivo**
2. **El modo de apertura**

Ejemplo:

```python
archivo = open("archivo.txt", "r")
```

---

### Modos de apertura

| Modo | Descripción                                        |
| ---- | -------------------------------------------------- |
| `r`  | Lectura                                            |
| `w`  | Escritura (sobrescribe el archivo si ya existe)    |
| `a`  | Escritura agregando contenido al final del archivo |
| `x`  | Crea el archivo y lanza un error si ya existe      |
| `b`  | Modo binario (para imágenes, pdf, etc.)            |
| `t`  | Modo texto (modo por defecto)                      |
| `r+` | Leer y escribir            |

---

### Combinación de modos

Los modos también se pueden **combinar**.

Ejemplos:

* `rt` → lectura en modo texto (por defecto)
* `wb` → escritura en modo binario
* `rb` → lectura en modo binario

---

### Operaciones que podemos hacer con archivos

Una vez abierto el archivo se pueden realizar diversas operaciones como:

* **Leer el contenido**
* **Escribir contenido**
* **Agregar información**

---

### Cerrar un archivo

Siempre que abrimos un archivo es importante **cerrarlo al finalizar** para liberar los recursos del sistema.

Esto se hace utilizando el método:

```python
close()
```

---

### Ejemplo de uso
En este ejemplo:

1. Se crea o abre el archivo `archivo.txt`
2. Se escribe el texto **Hola mundo**
3. Se cierra el archivo

## Escribir en un archivo

```python
archivo = open("datos.txt", "w")

archivo.write("Hola mundo\n")
archivo.write("Python\n")

archivo.close()
```

Contenido del archivo:

```
Hola mundo
Python
```


## Leer un archivo completo

```python
archivo = open("datos.txt", "r")

contenido = archivo.read()

print(contenido)

archivo.close()
```


## Leer archivo línea por línea

```python
archivo = open("datos.txt", "r")

for linea in archivo:
    print(linea)

archivo.close()
```

## Usar `with` (forma recomendada)

Python puede cerrar el archivo automáticamente.

```python
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```

## Ejemplo práctico

Guardar nombres en un archivo:

```python
with open("nombres.txt", "w") as archivo:

    for i in range(3):
        nombre = input("Nombre: ")
        archivo.write(nombre + "\n")
```

---

