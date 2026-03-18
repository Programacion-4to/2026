# Unidad 1 — Matrices, Archivos y Manejo de Errores

## Objetivos de la Unidad

Al finalizar esta unidad el alumno será capaz de:

* Comprender qué es una **matriz** y cómo utilizarla en Python.
* Leer y escribir **archivos en disco**.
* Manejar **errores y excepciones** para evitar que los programas se rompan.
* Aplicar estos conceptos para resolver problemas reales.

---

# 1. Matrices

## ¿Qué es una matriz?

Una **matriz** es una estructura de datos **bidimensional** compuesta por **filas y columnas**.

Ejemplo matemático:

|   |   |   |
| - | - | - |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

En Python se representa como una **lista de listas**.

```python
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
```

---

## Acceder a elementos de una matriz

La sintaxis es:

```
matriz[fila][columna]
```

Ejemplo:

```python
print(matriz[0][1])
```

Resultado:

```
2
```

---

## Recorrer una matriz

Para recorrer una matriz usamos **dos ciclos for**.

```python
for fila in matriz:
    for elemento in fila:
        print(elemento)
```

---

## Mostrar una matriz ordenada

```python
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
```

Salida:

```
1 2 3
4 5 6
7 8 9
```

---

## Crear una matriz vacía

```python
filas = 3
columnas = 3

matriz = []

for i in range(filas):
    fila = []
    
    for j in range(columnas):
        fila.append(0)
        
    matriz.append(fila)

print(matriz)
```

---

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

# Otros modos de archivos

Además de los modos básicos (`r`, `w`, `a`, `x`), Python permite **otros modos combinados** que agregan funcionalidades como **leer y escribir al mismo tiempo** o trabajar en **modo binario**.



| Modo | Descripción |
|-----|-------------|
| `r+` | Abre el archivo para **leer y escribir**. El archivo debe existir. |
| `w+` | Abre el archivo para **leer y escribir**, pero **borra el contenido existente**. |
| `a+` | Abre el archivo para **leer y escribir**, agregando contenido al final. |
| `x+` | Crea el archivo para **leer y escribir**, pero falla si ya existe. |

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

---
## Ejemplos de Combinaciones
### Ejemplo de `r+`

Permite leer y luego escribir en el mismo archivo.

```python
archivo = open("datos.txt", "r+")
contenido = archivo.read()
print(contenido)
archivo.write("\nNueva linea")

archivo.close()

```


# Funciones Útiles

En Python existen varias funciones que permiten **leer, escribir y controlar la posición dentro de un archivo**.

En esta guía veremos las siguientes funciones:

* `readline()`
* `readlines()`
* `seek()`
* `tell()`
* `flush()`

## readline()

La función `readline()` permite **leer una sola línea del archivo**.

Cada vez que se ejecuta, el cursor avanza a la siguiente línea.

## Ejemplo

```python
with open("datos.txt", "r") as archivo:
    linea = archivo.readline()
    print(linea)
```

Si queremos leer varias líneas:

```python
with open("datos.txt", "r") as archivo:
    print(archivo.readline())
    print(archivo.readline())
```

### Salida posible

```
Hola
Python
```

Cada llamada a `readline()` devuelve **la siguiente línea del archivo**.


## readlines()

La función `readlines()` **lee todas las líneas del archivo y las guarda en una lista**.

Cada elemento de la lista representa una línea del archivo.

## Ejemplo

```python
with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()

print(lineas)
```

### Resultado

```
['Hola\n', 'Python\n', 'Archivos\n']
```

Observación:
Cada línea incluye el **salto de línea `\n`**.

Luego se pueden recorrer las líneas con un `for`.

```python
for linea in lineas:
    print(linea)
```

## seek()

La función `seek()` permite **mover el cursor dentro del archivo**.

El **cursor** indica desde qué posición se leerá o escribirá el archivo.

## Ejemplo

```python
archivo = open("datos.txt", "r")
archivo.seek(0)
contenido = archivo.read()
print(contenido)
archivo.close()
```

`seek(0)` mueve el cursor **al inicio del archivo**.

También se puede mover a otras posiciones:

```python
archivo.seek(5)
```

Esto mueve el cursor **al carácter número 5 del archivo**.



## tell()

La función `tell()` permite **saber en qué posición del archivo se encuentra el cursor**.

## Ejemplo

```python
archivo = open("datos.txt", "r")
print(archivo.tell())
archivo.read(5)
print(archivo.tell())
archivo.close()
```

### Salida posible

```
0
5
```

Esto significa que el cursor **avanzó 5 caracteres** después de la lectura.



## flush()

La función `flush()` **fuerza a que los datos se guarden inmediatamente en el archivo**.

Normalmente Python guarda los datos cuando:

* se cierra el archivo
* o el buffer se llena

`flush()` permite **forzar la escritura antes de cerrar el archivo**.

## Ejemplo

```python
archivo = open("datos.txt", "w")
archivo.write("Hola mundo")
archivo.flush()
archivo.close()
```

Esto asegura que el contenido se **escriba inmediatamente en el disco**.


---

# 3. Manejo de Errores

## ¿Qué es una excepción?

Una **excepción** es un error que ocurre durante la ejecución del programa.

Ejemplo de error:

```python
print(10/0)
```

Resultado:

```
ZeroDivisionError
```

---

## try / except

El bloque `try/except` permite manejar errores sin que el programa se detenga.

```python
try:
    numero = int(input("Ingrese un número: "))
except:
    print("Debe ingresar un número válido")
```

---

## Ejemplo con división

```python
try:
    a = int(input("Numero: "))
    b = int(input("Numero: "))

    resultado = a / b

    print(resultado)

except:
    print("Error en la operación")
```

---

## Capturar errores específicos

```python
try:
    numero = int(input("Numero: "))
except ValueError:
    print("Entrada inválida")
```

---

## finally

El bloque `finally` se ejecuta **siempre**, haya o no errores.

```python
try:
    print("Inicio del programa")
except:
    print("Ocurrió un error")
finally:
    print("Fin del programa")
```

## Raise

La palabra clave `raise` permite **lanzar una excepción de forma manual**. Esto corta el programa y muestra el mensaje de error.

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
```




## Tipos de errores comunes
| Error | Descripción |
|------|-------------- |
| `SyntaxError` | Ocurre al escribir código con errores de sintaxis.
| `IndentationError` | Ocurre al escribir código con errores de indentación.
| `ValueError` | Ocurre al intentar convertir un valor a un tipo incompatible.
| `TypeError` | Ocurre al intentar realizar una operación con tipos de datos incompatibles. 
| `IndexError` | Ocurre al intentar acceder a un índice fuera del rango de una lista o matriz. |
| `KeyError` | Ocurre al intentar acceder a una clave que no existe en un diccionario. |
| `NameError` | Ocurre al intentar usar una variable que no ha sido definida. | 
| `ZeroDivisionError` | Ocurre al intentar dividir por cero. |
| `FileNotFoundError` | Ocurre al intentar abrir un archivo que no existe. | 
| `AttributeError` | Ocurre al intentar acceder a un atributo o método que no existe en un objeto. |
| `ImportError` | Ocurre al intentar importar un módulo que no existe. |

