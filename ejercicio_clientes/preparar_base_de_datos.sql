-- Deja la base de datos accesoadatos2526 como queda al terminar los scripts de clase.
-- Ejecutar una sola vez con: sudo mysql < preparar_base_de_datos.sql
SET NAMES utf8mb4;
CREATE DATABASE IF NOT EXISTS accesoadatos2526;
CREATE USER IF NOT EXISTS 'accesoadatos2526'@'localhost' IDENTIFIED BY 'Accesoadatos2526$';
GRANT ALL PRIVILEGES ON accesoadatos2526.* TO 'accesoadatos2526'@'localhost';
USE accesoadatos2526;

-- Tabla clientes, ya con la clave primaria autoincremental
CREATE TABLE IF NOT EXISTS clientes (
    Identificador INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL
) ENGINE = InnoDB;

-- Los dos clientes de prueba de clase (identificadores 1 y 2)
INSERT IGNORE INTO clientes VALUES (1, "Jose Vicente", "Carratala Sanchis", "info@jocarsa.com");
INSERT IGNORE INTO clientes VALUES (2, "Jose Vicente", "Carratala Sanchis", "info@jocarsa.com");

-- Juan se inserta (identificador 3) y se borra, como en 001, 002 y 003.
-- MySQL no reutiliza el 3, así que el siguiente cliente recibirá el 4.
INSERT INTO clientes VALUES (NULL, "Juan", "Garcia Lopez", "juan@garcialopez.com");
DELETE FROM clientes WHERE Identificador = 3;
