USE biblioteca;

-- PASO 3: procedimiento sin parámetros
DROP PROCEDURE IF EXISTS listar_libros;
DELIMITER //
CREATE PROCEDURE listar_libros()
BEGIN
    SELECT id, titulo, autor, ejemplares FROM libros ORDER BY id;
END //
DELIMITER ;

-- PASO 5: procedimiento con parámetro de entrada
DROP PROCEDURE IF EXISTS buscar_por_autor;
DELIMITER //
CREATE PROCEDURE buscar_por_autor(IN p_autor VARCHAR(100))
BEGIN
    SELECT titulo, ejemplares FROM libros WHERE autor = p_autor;
END //
DELIMITER ;

-- PASO 6: procedimiento con parámetro de salida
DROP PROCEDURE IF EXISTS contar_libros;
DELIMITER //
CREATE PROCEDURE contar_libros(OUT p_total INT)
BEGIN
    SELECT COUNT(*) INTO p_total FROM libros;
END //
DELIMITER ;

-- PASO 7: procedimiento que modifica datos y da error si no quedan ejemplares
DROP PROCEDURE IF EXISTS prestar_libro;
DELIMITER //
CREATE PROCEDURE prestar_libro(IN p_id INT)
BEGIN
    IF (SELECT ejemplares FROM libros WHERE id = p_id) = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No quedan ejemplares';
    END IF;
    UPDATE libros SET ejemplares = ejemplares - 1 WHERE id = p_id;
END //
DELIMITER ;
