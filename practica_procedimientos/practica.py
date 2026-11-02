import warnings
import mysql.connector

# El conector 9.5 avisa de que stored_results() cambiará en el futuro; hoy funciona bien
warnings.filterwarnings("ignore", category=DeprecationWarning)

conexion = mysql.connector.connect(
    host="localhost",
    user="app_biblioteca",
    password="Biblio_2026",
    database="biblioteca"
)
cursor = conexion.cursor()

# PASO 4: procedimiento sin parámetros
print("=== Listado de libros ===")
cursor.callproc("listar_libros", ())
for resultado in cursor.stored_results():
    for id_libro, titulo, autor, ejemplares in resultado.fetchall():
        print(f"{id_libro} - {titulo} ({autor}) - {ejemplares} ejemplares")

# PASO 5: procedimiento con parámetro de entrada (IN)
print()
print("=== Libros de Federico García Lorca ===")
cursor.callproc("buscar_por_autor", ("Federico García Lorca",))
for resultado in cursor.stored_results():
    for titulo, ejemplares in resultado.fetchall():
        print(f"{titulo} - {ejemplares} ejemplares")

# PASO 6: procedimiento con parámetro de salida (OUT)
print()
print("=== Total de libros ===")
resultado = cursor.callproc("contar_libros", (0,))
print(f"Hay {resultado[0]} libros en la biblioteca")

# PASO 8: préstamo con commit si va bien y rollback si hay error
print()
print("=== Préstamo del libro 1 ===")
try:
    cursor.callproc("prestar_libro", (1,))
    conexion.commit()
    print("Préstamo registrado")
except mysql.connector.Error as e:
    conexion.rollback()
    print("Error:", e.msg)

print()
print("=== Préstamo del libro 4 ===")
try:
    cursor.callproc("prestar_libro", (4,))
    conexion.commit()
    print("Préstamo registrado")
except mysql.connector.Error as e:
    conexion.rollback()
    print("Error:", e.msg)

# PASO 9: el usuario solo puede usar los procedimientos, no la tabla
print()
print("=== Prueba de permisos ===")
try:
    cursor.execute("SELECT * FROM libros")
    print(cursor.fetchall())
except mysql.connector.Error as e:
    print("Acceso denegado:", e.msg)

cursor.close()
conexion.close()
