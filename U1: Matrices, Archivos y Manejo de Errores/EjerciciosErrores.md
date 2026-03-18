## Ejercicio 1: Manejo de errores

Crear un programa que pida al usuario un número y lo divida por 10. Manejar los siguientes errores:

-   Si el usuario ingresa algo que no es un número, mostrar un mensaje de error.
-   Si el usuario ingresa 0, mostrar un mensaje de error indicando que no se puede dividir por cero.

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