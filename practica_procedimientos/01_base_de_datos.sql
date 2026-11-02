-- PASO 1: base de datos y tabla.
-- La primera línea borra la biblioteca del ejercicio anterior, que tenía otra estructura.
DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE libros (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    titulo     VARCHAR(100),
    autor      VARCHAR(100),
    ejemplares INT
);

INSERT INTO libros (titulo, autor, ejemplares) VALUES
    ('Don Quijote de la Mancha', 'Miguel de Cervantes',   3),
    ('Novelas ejemplares',       'Miguel de Cervantes',   1),
    ('La casa de Bernarda Alba', 'Federico García Lorca', 2),
    ('Romancero gitano',         'Federico García Lorca', 0);

SELECT * FROM libros;
