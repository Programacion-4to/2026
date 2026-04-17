# Unidad 3 — Bases de Datos, SQL, Models y Schemas

## Objetivos de la Unidad

Al finalizar esta unidad el alumno será capaz de:

* Comprender qué es una **base de datos** y para qué sirve.
* Escribir consultas **SQL** para crear, leer, modificar y eliminar datos.
* Entender qué es un **Schema** y cómo define la estructura de los datos.
* Utilizar **Models** para interactuar con la base de datos desde Python.
* Aplicar estos conceptos para resolver problemas reales.

---

# 1. Bases de Datos

## ¿Qué es una base de datos?

Una **base de datos** es un sistema organizado para **almacenar, gestionar y recuperar información** de forma eficiente.

En lugar de guardar datos en archivos de texto, las bases de datos permiten:

* Buscar datos rápidamente
* Relacionar información entre distintas entidades
* Controlar el acceso a los datos
* Garantizar la integridad de la información

---

## Tipos de bases de datos

| Tipo | Descripción | Ejemplos |
|------|-------------|----------|
| **Relacional** | Organiza los datos en tablas con filas y columnas | MySQL, PostgreSQL, SQLite |
| **No relacional** | Organiza los datos en documentos, grafos o clave-valor | MongoDB, Redis |

En esta unidad trabajaremos con bases de datos **relacionales**.

---

## Base de datos relacional

Una base de datos relacional organiza los datos en **tablas**.

Cada tabla representa una **entidad** del sistema.

Ejemplo:

| id | nombre | edad |
|----|--------|------|
| 1  | Ana    | 25   |
| 2  | Juan   | 30   |
| 3  | María  | 22   |

* Cada **fila** es un registro (una instancia de la entidad).
* Cada **columna** es un atributo (una propiedad del registro).

---

## Conceptos clave

### Clave Primaria (Primary Key)

La **clave primaria** es un campo que **identifica de forma única** a cada registro en una tabla.

* No puede repetirse
* No puede ser nula

```sql
id INT PRIMARY KEY
```

### Clave Foránea (Foreign Key)

La **clave foránea** es un campo que **referencia la clave primaria de otra tabla**, creando una relación entre ellas.

```sql
cliente_id INT REFERENCES clientes(id)
```

---

# 2. SQL

## ¿Qué es SQL?

**SQL** (Structured Query Language) es el lenguaje estándar para interactuar con bases de datos relacionales.

Con SQL podemos:

* **Crear** tablas y bases de datos
* **Insertar** datos
* **Consultar** datos
* **Modificar** datos
* **Eliminar** datos

Las operaciones básicas se conocen como **CRUD**:

| Operación | SQL | Descripción |
|-----------|-----|-------------|
| **C**reate | `INSERT` | Insertar datos |
| **R**ead | `SELECT` | Leer datos |
| **U**pdate | `UPDATE` | Modificar datos |
| **D**elete | `DELETE` | Eliminar datos |

---

## Crear una tabla

```sql
CREATE TABLE productos (
    id      INTEGER PRIMARY KEY,
    nombre  TEXT    NOT NULL,
    precio  REAL    NOT NULL,
    stock   INTEGER DEFAULT 0
);
```

---

## Tipos de datos comunes

| Tipo | Descripción |
|------|-------------|
| `INTEGER` | Número entero |
| `REAL` / `FLOAT` | Número con decimales |
| `TEXT` / `VARCHAR` | Cadena de texto |
| `BOOLEAN` | Verdadero o falso |
| `DATE` | Fecha |
| `DATETIME` | Fecha y hora |

---

## INSERT — Insertar datos

```sql
INSERT INTO productos (nombre, precio, stock)
VALUES ('Laptop', 1500.00, 10);
```

Para insertar varios registros a la vez:

```sql
INSERT INTO productos (nombre, precio, stock)
VALUES
    ('Mouse', 25.00, 50),
    ('Teclado', 45.00, 30),
    ('Monitor', 300.00, 15);
```

---

## SELECT — Consultar datos

### Seleccionar todo

```sql
SELECT * FROM productos;
```

### Seleccionar columnas específicas

```sql
SELECT nombre, precio FROM productos;
```

### Filtrar con WHERE

```sql
SELECT * FROM productos WHERE precio > 100;
```

### Ordenar resultados

```sql
SELECT * FROM productos ORDER BY precio ASC;
```

`ASC` es ascendente (por defecto), `DESC` es descendente.

### Limitar resultados

```sql
SELECT * FROM productos LIMIT 5;
```

---

## Operadores en WHERE

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `=` | Igual | `precio = 100` |
| `!=` o `<>` | Distinto | `precio != 0` |
| `>` | Mayor que | `stock > 10` |
| `<` | Menor que | `precio < 500` |
| `>=` | Mayor o igual | `edad >= 18` |
| `<=` | Menor o igual | `stock <= 5` |
| `AND` | Y lógico | `precio > 10 AND stock > 0` |
| `OR` | O lógico | `precio < 10 OR stock = 0` |
| `LIKE` | Patrón de texto | `nombre LIKE 'A%'` |
| `IN` | Dentro de una lista | `id IN (1, 2, 3)` |

---

## UPDATE — Modificar datos

```sql
UPDATE productos
SET precio = 1400.00
WHERE nombre = 'Laptop';
```

> **Importante:** Siempre usar `WHERE` al actualizar para no modificar todos los registros.

---

## DELETE — Eliminar datos

```sql
DELETE FROM productos WHERE id = 1;
```

> **Importante:** Siempre usar `WHERE` al borrar para no eliminar todos los registros.

---

## Funciones de agregación

Las funciones de agregación permiten realizar cálculos sobre un conjunto de filas.

| Función | Descripción |
|---------|-------------|
| `COUNT(*)` | Cuenta la cantidad de filas |
| `SUM(col)` | Suma los valores de una columna |
| `AVG(col)` | Promedio de los valores |
| `MAX(col)` | Valor máximo |
| `MIN(col)` | Valor mínimo |

### Ejemplos

```sql
SELECT COUNT(*) FROM productos;

SELECT AVG(precio) FROM productos;

SELECT MAX(precio), MIN(precio) FROM productos;
```

---

## GROUP BY

`GROUP BY` agrupa los resultados según una columna.

```sql
SELECT categoria, COUNT(*) AS cantidad
FROM productos
GROUP BY categoria;
```

---

## JOIN — Relacionar tablas

`JOIN` permite combinar filas de dos tablas según una condición.

### Ejemplo

Tabla `clientes`:

| id | nombre |
|----|--------|
| 1  | Ana    |
| 2  | Juan   |

Tabla `pedidos`:

| id | cliente_id | producto  |
|----|-----------|-----------|
| 1  | 1         | Laptop    |
| 2  | 1         | Mouse     |
| 3  | 2         | Teclado   |

### INNER JOIN

Devuelve solo las filas que tienen coincidencia en ambas tablas.

```sql
SELECT clientes.nombre, pedidos.producto
FROM pedidos
INNER JOIN clientes ON pedidos.cliente_id = clientes.id;
```

Resultado:

| nombre | producto |
|--------|----------|
| Ana    | Laptop   |
| Ana    | Mouse    |
| Juan   | Teclado  |

---

# 3. Schema

## ¿Qué es un Schema?

Un **Schema** (esquema) define la **estructura** de la base de datos:

* Qué tablas existen
* Qué columnas tiene cada tabla
* Qué tipo de datos acepta cada columna
* Qué restricciones aplican (PRIMARY KEY, NOT NULL, UNIQUE, etc.)

El schema es como el **molde** que determina cómo deben lucir los datos antes de guardarlos.

---

## Restricciones (Constraints)

| Restricción | Descripción |
|-------------|-------------|
| `PRIMARY KEY` | Identifica de forma única cada fila |
| `NOT NULL` | El campo no puede estar vacío |
| `UNIQUE` | El valor no puede repetirse |
| `DEFAULT` | Valor por defecto si no se especifica |
| `FOREIGN KEY` | Referencia a la clave primaria de otra tabla |
| `CHECK` | Validación personalizada |

### Ejemplo de schema completo

```sql
CREATE TABLE clientes (
    id       INTEGER PRIMARY KEY,
    nombre   TEXT    NOT NULL,
    email    TEXT    UNIQUE NOT NULL,
    edad     INTEGER CHECK(edad >= 0)
);

CREATE TABLE pedidos (
    id          INTEGER PRIMARY KEY,
    cliente_id  INTEGER NOT NULL REFERENCES clientes(id),
    producto    TEXT    NOT NULL,
    fecha       DATE    DEFAULT CURRENT_DATE
);
```

---

# 4. Models

## ¿Qué es un Model?

En el contexto de la programación, un **Model** (modelo) es una **clase de Python** que representa una tabla de la base de datos.

Cada atributo del modelo corresponde a una columna de la tabla.

El modelo permite interactuar con la base de datos usando **código Python** en lugar de escribir SQL directamente.

---

## SQLite con Python (sin ORM)

Python tiene soporte nativo para SQLite a través del módulo `sqlite3`.

```python
import sqlite3

# Conectar a la base de datos (la crea si no existe)
conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()
```

### Crear una tabla

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id      INTEGER PRIMARY KEY,
        nombre  TEXT    NOT NULL,
        precio  REAL    NOT NULL
    )
""")
conexion.commit()
```

### Insertar datos

```python
cursor.execute(
    "INSERT INTO productos (nombre, precio) VALUES (?, ?)",
    ("Laptop", 1500.00)
)
conexion.commit()
```

> Se usa `?` como marcador de posición para evitar inyección SQL.

### Consultar datos

```python
cursor.execute("SELECT * FROM productos")
filas = cursor.fetchall()

for fila in filas:
    print(fila)
```

### Cerrar la conexión

```python
conexion.close()
```

---

## ORM — Object-Relational Mapping

Un **ORM** es una herramienta que permite trabajar con la base de datos usando **objetos Python** en lugar de SQL.

La librería más utilizada en Python es **SQLAlchemy**.

```
pip install sqlalchemy
```

---

## Definir un Model con SQLAlchemy

```python
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos"

    id     = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock  = Column(Integer, default=0)

    def __repr__(self):
        return f"Producto(nombre={self.nombre}, precio={self.precio})"
```

---

## Crear las tablas en la base de datos

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///tienda.db")
Base.metadata.create_all(engine)
```

---

## Sesión — Interactuar con la base de datos

```python
from sqlalchemy.orm import Session

with Session(engine) as session:

    # Insertar
    nuevo = Producto(nombre="Mouse", precio=25.00, stock=50)
    session.add(nuevo)
    session.commit()

    # Consultar todos
    productos = session.query(Producto).all()
    for p in productos:
        print(p)

    # Filtrar
    caro = session.query(Producto).filter(Producto.precio > 100).all()

    # Actualizar
    producto = session.query(Producto).filter_by(nombre="Mouse").first()
    producto.precio = 30.00
    session.commit()

    # Eliminar
    session.delete(producto)
    session.commit()
```

---

## Relaciones entre modelos

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = "clientes"

    id     = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    pedidos = relationship("Pedido", back_populates="cliente")


class Pedido(Base):
    __tablename__ = "pedidos"

    id          = Column(Integer, primary_key=True)
    producto    = Column(String, nullable=False)
    cliente_id  = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship("Cliente", back_populates="pedidos")
```

### Usar la relación

```python
with Session(engine) as session:
    cliente = session.query(Cliente).filter_by(nombre="Ana").first()

    for pedido in cliente.pedidos:
        print(pedido.producto)
```

---

## Resumen

| Concepto | Descripción |
|----------|-------------|
| **Base de datos** | Sistema para almacenar y gestionar información |
| **Tabla** | Estructura que organiza datos en filas y columnas |
| **SQL** | Lenguaje para interactuar con la base de datos |
| **Schema** | Define la estructura y restricciones de las tablas |
| **Model** | Clase Python que representa una tabla |
| **ORM** | Herramienta para usar la base de datos con objetos Python |
| **Primary Key** | Campo que identifica de forma única cada fila |
| **Foreign Key** | Campo que referencia otra tabla |
| **CRUD** | Crear, Leer, Actualizar y Eliminar datos |
