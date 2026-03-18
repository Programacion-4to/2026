## Ejercicio 1: Manejo de errores

Crear un programa que pida al usuario un número y lo divida por 10. Si el usuario ingresa algo que no es un número, mostrar un mensaje de error.

## Ejercicio 2: Archivos
Crear un programa que:
1. Pida al usuario un nombre de archivo.
2. Intente abrir el archivo y leer su contenido.
3. Si el archivo no existe, mostrar un mensaje de error.
4. Si el archivo existe, mostrar su contenido en pantalla.

## Ejercicio 3: Validación de datos
Crear un programa que pida al usuario su edad. Validar que la edad sea un número entero positivo. Si el usuario ingresa un valor no válido, mostrar un mensaje de error y pedir la edad nuevamente hasta que se ingrese un valor correcto.

## Ejercicio 4: Manejo de excepciones
Crear un programa que pida al usuario dos números y los divida. Manejar las siguientes excepciones:
-   `ValueError` → si el usuario ingresa algo que no es un número.
-   `ZeroDivisionError` → si el usuario intenta dividir por cero.
-   Cualquier otra excepción → mostrar un mensaje de error genérico.

## Ejercicio 5: Lectura de archivos con errores
Crear un programa que lea un archivo de texto línea por línea. Si el archivo no existe, mostrar un mensaje de error. Si el archivo existe, pero una línea tiene más de 80 caracteres, mostrar un mensaje de advertencia indicando que la línea es demasiado larga. Continuar leyendo el resto del archivo a pesar de las advertencias.

## Ejercicio 6: Menú interactivo robusto
Crear un menú con opciones numéricas para operar una lista (agregar, borrar, buscar, salir). Si el usuario ingresa una opción no válida, mostrar un mensaje de error y volver a mostrar el menú.

Nunca debe romperse por entradas malas del usuario.

La unica forma de salir del programa debe ser seleccionando la opción "salir".

Errores para practicar: ValueError, IndexError, TypeError, KeyboardInterrupt.

## Ejercicio 7: Mini gestor de usuarios (diccionarios + validaciones)
Importar de un archivo csv una lista con la informacion de usuarios (el archivo tiene las columnas: id, nombre, apellido, email, edad, telefono)
Evitar IDs repetidos, email inválido y edades fuera de rango, telefonos con formato argentino (+54)

Mostrar la informacion del usuario si no tiene errores. En caso de tener errores, escribir eso en un archivo llamado `error_log.txt` donde diga que linea tiene error y el porque del fallo.

Ejemplo: 

```
id,nombre,apellido,email,edad,telefono
0,ana,maria,anamaria@gmail.com,20,+54911123456789 -> Error en el ID
1,juan,perez,juanperez34@gmail,30,+5491112345678 -> Error en el email y el telefono
2,luis,lopez,luislopez@gmail.com,25,+54911123456789 -> Error en el telefono
3,sofia,gome2,sofiagomez17@gmail.com,28,+54911123456789 -> Error en el apellido
4,dieg0,fernandez,diegofernandez@gmail.com,abc,911123456789 -> Error en la edad, el nombre y el telefono
```

Log de errores:
```
Linea 1: Error en el ID
Linea 2: Error en el email y el telefono
Linea 3: Error en el telefono
Linea 4: Error en el apellido
Linea 5: Error en la edad, el nombre y el telefono

```
