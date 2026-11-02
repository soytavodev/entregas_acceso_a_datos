import mysql.connector

# PASO 2: conectar con MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="tienda",
    password="tienda1234"
)
cursor = conexion.cursor()
print("Conexión correcta con MySQL")

# PASO 3: crear la base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS tienda")
cursor.execute("SHOW DATABASES")
for base in cursor:
    print(base[0])
cursor.execute("USE tienda")

# PASO 4: crear la tabla de productos
cursor.execute("DROP TABLE IF EXISTS productos")
cursor.execute("""
    CREATE TABLE productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50),
        precio DECIMAL(6,2)
    )
""")
cursor.execute("SHOW TABLES")
for tabla in cursor:
    print("Tabla creada:", tabla[0])

# PASO 5: insertar productos
sql = "INSERT INTO productos (nombre, precio) VALUES (%s, %s)"
datos = [
    ("Teclado", 25),
    ("Raton", 12.5),
    ("Monitor", 140),
    ("Altavoces", 30)
]
cursor.executemany(sql, datos)
conexion.commit()
print(cursor.rowcount, "filas insertadas")

# PASO 6: consultar toda la tabla
print("--- Todos los productos ---")
cursor.execute("SELECT * FROM productos")
for fila in cursor.fetchall():
    print(fila[0], "|", fila[1], "|", fila[2])

# PASO 7: consultar con una condición
print("--- Productos de menos de 30 euros ---")
sql = "SELECT nombre, precio FROM productos WHERE precio < %s"
cursor.execute(sql, (30,))
for fila in cursor.fetchall():
    print(fila[0], "|", fila[1])

# PASO 8: modificar y borrar datos
sql = "UPDATE productos SET precio = %s WHERE nombre = %s"
cursor.execute(sql, (120, "Monitor"))
print("Filas modificadas:", cursor.rowcount)

sql = "DELETE FROM productos WHERE nombre = %s"
cursor.execute(sql, ("Raton",))
print("Filas borradas:", cursor.rowcount)

conexion.commit()

print("--- Productos después de los cambios ---")
cursor.execute("SELECT * FROM productos")
for fila in cursor.fetchall():
    print(fila[0], "|", fila[1], "|", fila[2])

# PASO 9: cerrar la conexión
cursor.close()
conexion.close()
print("Conexión cerrada")
