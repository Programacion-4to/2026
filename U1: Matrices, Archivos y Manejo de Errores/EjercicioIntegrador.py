"""
EJERCICIO INTEGRADOR — SISTEMA DE VENTAS (CSV COMO BASE DE DATOS)

Una librería guarda el registro de ventas del día en un archivo llamado:

ventas.csv

El archivo funciona como una pequeña base de datos.

Tiene una fila de encabezado y luego los registros de ventas.

Estructura del archivo:

id,producto,precio,cantidad

Ejemplo de archivo ventas.csv:

id,producto,precio,cantidad
1,Lapiz,100,3
2,Cuaderno,500,2
3,Lapiz,100,1
4,Goma,80,5
5,Cuaderno,500,1


---------------------------------------------
PARTE 1 — LECTURA DEL ARCHIVO (BASE DE DATOS CSV)

Crear un programa que:

1. Abra el archivo ventas.csv
2. Ignore la primera línea (encabezado)
3. Lea todos los registros

Cada registro debe guardarse en una lista de diccionarios
con la siguiente estructura:

{
    "id": 1,
    "producto": "Lapiz",
    "precio": 100,
    "cantidad": 3
}

Ejemplo de lista final:

ventas = [
    {"id": 1, "producto": "Lapiz", "precio": 100, "cantidad": 3},
    {"id": 2, "producto": "Cuaderno", "precio": 500, "cantidad": 2}
]


---------------------------------------------
PARTE 2 — MANEJO DE ERRORES

El programa debe manejar:

1. Si el archivo ventas.csv no existe
2. Si una línea tiene menos columnas de las esperadas
3. Si precio, cantidad o id no son números

Las líneas incorrectas deben ignorarse mostrando un mensaje:

Error en la linea: 6,Lapiz,abc,2


---------------------------------------------
PARTE 3 — PROCESAMIENTO DE DATOS

Usando la lista de ventas:

1. Calcular la facturación total del día.

La facturación de cada venta es:

precio * cantidad


2. Calcular cuántas unidades se vendieron de cada producto
utilizando un diccionario.

Ejemplo:

Lapiz : 4
Cuaderno : 3
Goma : 5


3. Determinar cuál fue el producto más vendido.


---------------------------------------------
PARTE 4 — ESTADÍSTICAS

Mostrar:

Facturación total: $XXXX

Ventas por producto:
Lapiz : 4
Cuaderno : 3
Goma : 5

Producto más vendido: Goma


---------------------------------------------
PARTE 5 — BÚSQUEDA

Pedir al usuario un producto.

Mostrar:

Total vendido de Lapiz: 4 unidades
Facturación del producto: $400

Si no existe:

El producto no fue vendido hoy


---------------------------------------------
PARTE 6 — DESAFÍO FINAL

Crear un nuevo archivo llamado:

reporte.csv

Este archivo también debe tener formato CSV:

producto,unidades_vendidas

Ejemplo:

producto,unidades_vendidas
Lapiz,4
Cuaderno,3
Goma,5

"""