-- Pruebas de los pasos 3, 5, 6 y 7 (las que el enunciado hace en Workbench).
USE biblioteca;
CALL listar_libros();
CALL buscar_por_autor('Federico García Lorca');
CALL contar_libros(@total);
SELECT @total;
CALL prestar_libro(4);
