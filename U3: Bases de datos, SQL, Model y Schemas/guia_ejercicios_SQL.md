# Guía de Ejercicios SQL — Base de datos: Librería

> Antes de empezar, asegurate de tener la base `libreria_db` creada y cargada.  
> Tablas disponibles: `autores`, `generos`, `libros`, `clientes`, `ventas`

---

## Nivel 1 — SELECT básico

**Ejercicio 1**  
Mostrar todos los datos de la tabla `clientes`.

**Ejercicio 2**  
Mostrar solo el `titulo` y el `precio` de todos los libros.

**Ejercicio 3**  
Mostrar el `nombre` y la `ciudad` de todos los clientes.

**Ejercicio 4**  
Mostrar todos los géneros disponibles.

**Ejercicio 5**  
Mostrar todos los libros ordenados por precio de mayor a menor.

**Ejercicio 6**  
Mostrar todos los autores ordenados alfabéticamente por nombre.

---

## Nivel 2 — WHERE (filtros)

**Ejercicio 7**  
Mostrar los libros que cuestan más de $1200.

**Ejercicio 8**  
Mostrar los clientes que viven en `'Buenos Aires'`.

**Ejercicio 9**  
Mostrar los libros publicados antes del año 1970.

**Ejercicio 10**  
Mostrar los libros que tienen un stock menor a 5 unidades.

**Ejercicio 11**  
Mostrar los clientes cuyo nombre empieza con la letra `'A'`.  
> Pista: usá `LIKE`.

**Ejercicio 12**  
Mostrar los libros cuyo título contiene la palabra `'Harry'`.

**Ejercicio 13**  
Mostrar los libros que cuestan entre $1000 y $1500 (ambos inclusive).  
> Pista: usá `BETWEEN`.

**Ejercicio 14**  
Mostrar los clientes que viven en `'Córdoba'` o en `'Mendoza'`.  
> Pista: usá `IN`.

---

## Nivel 3 — Funciones de agregación

**Ejercicio 15**  
¿Cuántos libros hay en total en la tabla?

**Ejercicio 16**  
¿Cuál es el precio promedio de los libros?

**Ejercicio 17**  
¿Cuál es el libro más caro y el más barato? (precio máximo y mínimo)

**Ejercicio 18**  
¿Cuántas unidades hay en total sumando el stock de todos los libros?

**Ejercicio 19**  
¿Cuántos clientes hay registrados en la base?

**Ejercicio 20**  
¿Cuál es el total recaudado por todas las ventas?

---

## Nivel 4 — GROUP BY y HAVING

**Ejercicio 21**  
¿Cuántos clientes hay por ciudad?

**Ejercicio 22**  
¿Cuántos libros escribió cada autor? Mostrar el `autor_id` y la cantidad.

**Ejercicio 23**  
¿Cuántas ventas se realizaron por fecha? Ordenar por fecha.

**Ejercicio 24**  
Mostrar solo las ciudades que tienen más de 1 cliente.  
> Pista: usá `HAVING`.

**Ejercicio 25**  
¿Cuánto se vendió en total por cada cliente (usando `cliente_id`)?  
Mostrar solo los que superaron los $2000 en total.

---

## Nivel 5 — JOIN

**Ejercicio 26**  
Mostrar el título de cada libro junto con el nombre de su autor.

**Ejercicio 27**  
Mostrar el título de cada libro junto con el nombre del género al que pertenece.

**Ejercicio 28**  
Mostrar título, nombre del autor y nombre del género para todos los libros.

**Ejercicio 29**  
Mostrar el nombre del cliente y el título del libro en cada venta.

**Ejercicio 30**  
Mostrar nombre del cliente, título del libro, cantidad y total de cada venta.  
Ordenar por fecha.

**Ejercicio 31**  
Mostrar todos los libros, incluso los que no tienen autor asignado.  
> Pista: usá `LEFT JOIN`.

**Ejercicio 32**  
Mostrar el nombre de cada autor y la cantidad de libros que tiene registrados.  
Incluir autores aunque no tengan libros.

---

## Nivel 6 — Subconsultas

**Ejercicio 33**  
Mostrar los libros que cuestan más que el precio promedio de todos los libros.

**Ejercicio 34**  
Mostrar el nombre del cliente que realizó la compra más costosa (mayor `total` en ventas).

**Ejercicio 35**  
Mostrar los libros que nunca fueron vendidos.  
> Pista: usá `NOT IN` con una subconsulta sobre `ventas`.

**Ejercicio 36**  
Mostrar los autores que tienen al menos un libro con stock menor a 5.

---

## Nivel 7 — Desafíos integradores

**Ejercicio 37**  
Listar el top 3 de libros más vendidos (por cantidad total vendida).

**Ejercicio 38**  
Mostrar cuánto gastó cada cliente en total, junto con su ciudad.  
Ordenar de mayor a menor gasto.

**Ejercicio 39**  
Mostrar el libro más caro de cada género.  
> Pista: usá subconsulta o `MAX` con `GROUP BY` + `JOIN`.

**Ejercicio 40**  
Crear un reporte de ventas del mes de marzo 2026: nombre del cliente, libro comprado, cantidad, total y fecha.

---

## Soluciones de referencia

<details>
<summary>Ejercicio 7</summary>

```sql
SELECT titulo, precio
FROM libros
WHERE precio > 1200;
```
</details>

<details>
<summary>Ejercicio 11</summary>

```sql
SELECT nombre FROM clientes
WHERE nombre LIKE 'A%';
```
</details>

<details>
<summary>Ejercicio 21</summary>

```sql
SELECT ciudad, COUNT(*) AS cantidad
FROM clientes
GROUP BY ciudad;
```
</details>

<details>
<summary>Ejercicio 26</summary>

```sql
SELECT l.titulo, a.nombre AS autor
FROM libros l
JOIN autores a ON l.autor_id = a.id;
```
</details>

<details>
<summary>Ejercicio 31</summary>

```sql
SELECT l.titulo, a.nombre AS autor
FROM libros l
LEFT JOIN autores a ON l.autor_id = a.id;
```
</details>

<details>
<summary>Ejercicio 33</summary>

```sql
SELECT titulo, precio
FROM libros
WHERE precio > (SELECT AVG(precio) FROM libros);
```
</details>

<details>
<summary>Ejercicio 35</summary>

```sql
SELECT titulo
FROM libros
WHERE id NOT IN (SELECT libro_id FROM ventas);
```
</details>

<details>
<summary>Ejercicio 37</summary>

```sql
SELECT l.titulo, SUM(v.cantidad) AS total_vendido
FROM ventas v
JOIN libros l ON v.libro_id = l.id
GROUP BY l.titulo
ORDER BY total_vendido DESC
LIMIT 3;
```
</details>

<details>
<summary>Ejercicio 40</summary>

```sql
SELECT c.nombre AS cliente, l.titulo AS libro,
       v.cantidad, v.total, v.fecha
FROM ventas v
JOIN clientes c ON v.cliente_id = c.id
JOIN libros l   ON v.libro_id   = l.id
WHERE v.fecha BETWEEN '2026-03-01' AND '2026-03-31'
ORDER BY v.fecha;
```
</details>
</details>
