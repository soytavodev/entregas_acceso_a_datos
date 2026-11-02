-- PASO 2: usuario del programa, que solo puede ejecutar procedimientos.
-- Necesita administrador: sudo mysql < 02_usuario.sql
CREATE USER IF NOT EXISTS 'app_biblioteca'@'localhost' IDENTIFIED BY 'Biblio_2026';
GRANT EXECUTE ON biblioteca.* TO 'app_biblioteca'@'localhost';
