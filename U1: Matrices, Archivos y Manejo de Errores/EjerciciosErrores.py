"""
Ejercicio 1: Manejo de errores

Crear un programa que pida al usuario un número y lo divida por 10. Manejar los siguientes errores:

-   Si el usuario ingresa algo que no es un número, mostrar un mensaje de error.
-   Si el usuario ingresa 0, mostrar un mensaje de error indicando que no se puede dividir por cero.

"""

def dividir_por_diez():
    try:
        numero = float(input("Ingrese un número: "))
        resultado = numero / 10
        print(f"El resultado de dividir {numero} por 10 es: {resultado}")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

dividir_por_diez()

lista = [1, 2, 3, 4, 5]
result = [x for x in lista]
print(result)