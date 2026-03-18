# EJERCICIO INTEGRADOR - SISTEMA DE VENTAS (CSV COMO BASE DE DATOS)

Una libreria guarda el registro de ventas del dia en un archivo llamado:

`ventas.csv`

El archivo funciona como una pequena base de datos.

Tiene una fila de encabezado y luego los registros de ventas.

Estructura del archivo:

```csv
id,producto,precio,cantidad
```

Ejemplo de archivo `ventas.csv`:

```csv
id,producto,precio,cantidad
1,Lapiz,100,3
2,Cuaderno,500,2
3,Lapiz,100,1
4,Goma,80,5
5,Cuaderno,500,1
```

## PARTE 1 - LECTURA DEL ARCHIVO (BASE DE DATOS CSV)

Crear un programa que:

1. Abra el archivo `ventas.csv`.
2. Ignore la primera linea (encabezado).
3. Lea todos los registros.

Cada registro debe guardarse en una lista de diccionarios con la siguiente estructura:

```python
{
    "id": 1,
    "producto": "Lapiz",
    "precio": 100,
    "cantidad": 3
}
```

Ejemplo de lista final:

```python
ventas = [
    {"id": 1, "producto": "Lapiz", "precio": 100, "cantidad": 3},
    {"id": 2, "producto": "Cuaderno", "precio": 500, "cantidad": 2}
]
```

## PARTE 2 - MANEJO DE ERRORES

El programa debe manejar:

1. Si el archivo `ventas.csv` no existe.
2. Si una linea tiene menos columnas de las esperadas.
3. Si `precio`, `cantidad` o `id` no son numeros.

Las lineas incorrectas deben ignorarse mostrando un mensaje:

```text
Error en la linea: 6,Lapiz,abc,2
```

## PARTE 3 - PROCESAMIENTO DE DATOS

Usando la lista de ventas:

1. Calcular la facturacion total del dia.

La facturacion de cada venta es:

```text
precio * cantidad
```

2. Calcular cuantas unidades se vendieron de cada producto utilizando un diccionario.

Ejemplo:

```text
Lapiz : 4
Cuaderno : 3
Goma : 5
```

3. Determinar cual fue el producto mas vendido.

## PARTE 4 - ESTADISTICAS

Mostrar:

```text
Facturacion total: $XXXX

Ventas por producto:
Lapiz : 4
Cuaderno : 3
Goma : 5

Producto mas vendido: Goma
```

## PARTE 5 - BUSQUEDA

Pedir al usuario un producto.

Mostrar:

```text
Total vendido de Lapiz: 4 unidades
Facturacion del producto: $400
```

Si no existe:

```text
El producto no fue vendido hoy
```

## PARTE 6 - DESAFIO FINAL

Crear un nuevo archivo llamado:

`reporte.csv`

Este archivo tambien debe tener formato CSV:

```csv
producto,unidades_vendidas
```

Ejemplo:

```csv
producto,unidades_vendidas
Lapiz,4
Cuaderno,3
Goma,5
```
