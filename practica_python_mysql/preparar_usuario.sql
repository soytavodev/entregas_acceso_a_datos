-- Usuario propio para la práctica (en lugar de root). Ejecutar una vez con:
-- sudo mysql < preparar_usuario.sql
CREATE USER IF NOT EXISTS 'tienda'@'localhost' IDENTIFIED BY 'tienda1234';
-- Permisos solo sobre la base tienda: así el programa puede crearla, pero no tocar nada más
GRANT ALL PRIVILEGES ON tienda.* TO 'tienda'@'localhost';
