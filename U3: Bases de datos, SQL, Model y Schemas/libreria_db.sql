-- ============================================
--  BASE DE DATOS DE PRUEBA: Librería
--  Para enseñar SQL con pgAdmin
-- ============================================

-- 1. CREAR Y SELECCIONAR LA BASE DE DATOS
-- (Crear "libreria_db" desde pgAdmin, luego ejecutar el resto aquí)

-- 2. CREAR TABLAS

CREATE TABLE autores (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50),
    anio_nacimiento INT
);

CREATE TABLE generos (
    id      SERIAL PRIMARY KEY,
    nombre  VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE libros (
    id          SERIAL PRIMARY KEY,
    titulo      VARCHAR(200) NOT NULL,
    precio      NUMERIC(8, 2) NOT NULL,
    stock       INT DEFAULT 0,
    anio_publicacion INT,
    autor_id    INT REFERENCES autores(id),
    genero_id   INT REFERENCES generos(id)
);

CREATE TABLE clientes (
    id      SERIAL PRIMARY KEY,
    nombre  VARCHAR(100) NOT NULL,
    email   VARCHAR(150) UNIQUE,
    ciudad  VARCHAR(80)
);

CREATE TABLE ventas (
    id          SERIAL PRIMARY KEY,
    cliente_id  INT REFERENCES clientes(id),
    libro_id    INT REFERENCES libros(id),
    cantidad    INT NOT NULL DEFAULT 1,
    fecha       DATE NOT NULL DEFAULT CURRENT_DATE,
    total       NUMERIC(10, 2)
);

-- 3. INSERTAR DATOS DE EJEMPLO

INSERT INTO autores (nombre, nacionalidad, anio_nacimiento) VALUES
    ('Gabriel García Márquez', 'Colombiana',  1927),
    ('Jorge Luis Borges',      'Argentina',   1899),
    ('Isabel Allende',         'Chilena',     1942),
    ('Stephen King',           'Estadounidense', 1947),
    ('J.K. Rowling',           'Británica',   1965);

INSERT INTO generos (nombre) VALUES
    ('Realismo Mágico'),
    ('Fantasía'),
    ('Terror'),
    ('Ciencia Ficción'),
    ('Aventura');

INSERT INTO libros (titulo, precio, stock, anio_publicacion, autor_id, genero_id) VALUES
    ('Cien años de soledad',         1500.00, 10, 1967, 1, 1),
    ('El amor en los tiempos del cólera', 1200.00, 5, 1985, 1, 1),
    ('Ficciones',                    900.00, 8,  1944, 2, 2),
    ('El Aleph',                     850.00, 3,  1949, 2, 2),
    ('La casa de los espíritus',     1100.00, 7,  1982, 3, 1),
    ('It',                           1800.00, 4,  1986, 4, 3),
    ('El resplandor',                1600.00, 6,  1977, 4, 3),
    ('Harry Potter y la piedra filosofal', 1400.00, 15, 1997, 5, 2),
    ('Harry Potter y la cámara secreta',  1350.00, 12, 1998, 5, 2),
    ('Drácula',                      980.00,  2,  1897, NULL, 3);

INSERT INTO clientes (nombre, email, ciudad) VALUES
    ('Ana Pérez',    'ana@email.com',    'Buenos Aires'),
    ('Luis Gómez',   'luis@email.com',   'Córdoba'),
    ('Marta Díaz',   'marta@email.com',  'Rosario'),
    ('Carlos Ruiz',  'carlos@email.com', 'Buenos Aires'),
    ('Sofía Torres', 'sofia@email.com',  'Mendoza');

INSERT INTO ventas (cliente_id, libro_id, cantidad, fecha, total) VALUES
    (1, 1, 1, '2026-01-10', 1500.00),
    (1, 8, 2, '2026-01-10', 2800.00),
    (2, 3, 1, '2026-02-05', 900.00),
    (3, 6, 1, '2026-02-20', 1800.00),
    (4, 2, 1, '2026-03-01', 1200.00),
    (4, 5, 1, '2026-03-01', 1100.00),
    (5, 9, 3, '2026-03-15', 4050.00),
    (2, 7, 1, '2026-04-02', 1600.00),
    (1, 4, 2, '2026-04-10', 1700.00),
    (3, 8, 1, '2026-04-15', 1400.00);


-- ============================================
--  CONSULTAS DE EJEMPLO PARA CLASE
-- ============================================

-- SELECT básico
SELECT * FROM libros;
SELECT titulo, precio FROM libros;

-- WHERE (filtros)
SELECT titulo, precio FROM libros WHERE precio > 1000;
SELECT * FROM clientes WHERE ciudad = 'Buenos Aires';

-- ORDER BY
SELECT titulo, precio FROM libros ORDER BY precio DESC;

-- Funciones de agregación
SELECT COUNT(*) AS total_libros FROM libros;
SELECT AVG(precio) AS precio_promedio FROM libros;
SELECT MIN(precio), MAX(precio) FROM libros;

-- GROUP BY
SELECT ciudad, COUNT(*) AS cantidad_clientes
FROM clientes
GROUP BY ciudad;

-- JOIN básico (libros con su autor)
SELECT l.titulo, a.nombre AS autor, l.precio
FROM libros l
JOIN autores a ON l.autor_id = a.id;

-- JOIN múltiple (libros + autor + género)
SELECT l.titulo, a.nombre AS autor, g.nombre AS genero, l.precio
FROM libros l
JOIN autores a ON l.autor_id = a.id
JOIN generos g ON l.genero_id = g.id
ORDER BY a.nombre;

-- LEFT JOIN (libros sin autor asignado)
SELECT l.titulo, a.nombre AS autor
FROM libros l
LEFT JOIN autores a ON l.autor_id = a.id;

-- Subconsulta (libros más caros que el promedio)
SELECT titulo, precio
FROM libros
WHERE precio > (SELECT AVG(precio) FROM libros);

-- Ventas por cliente
SELECT c.nombre, COUNT(v.id) AS compras, SUM(v.total) AS total_gastado
FROM clientes c
JOIN ventas v ON c.id = v.cliente_id
GROUP BY c.nombre
ORDER BY total_gastado DESC;

-- HAVING (clientes que gastaron más de $3000)
SELECT c.nombre, SUM(v.total) AS total_gastado
FROM clientes c
JOIN ventas v ON c.id = v.cliente_id
GROUP BY c.nombre
HAVING SUM(v.total) > 3000;
