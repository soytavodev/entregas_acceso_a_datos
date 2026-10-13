import csv
import json

contactos = []

# 1. Leer el CSV y convertir cada fila en un diccionario
with open('datos.csv', mode='r') as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        contactos.append(
            {
                'nombre': fila['nombre'],
                'apellidos': fila['apellidos'],
                'telefono': fila['telefono'],
            }
        )

# 2. Guardar los diccionarios en contactos.json
with open('contactos.json', mode='w') as archivo_json:
    json.dump(contactos, archivo_json, indent=4, ensure_ascii=False)

# 3. Escribir el archivo log.txt
with open('log.txt', mode='w') as archivo_log:
    for c in contactos:
        archivo_log.write(f"Contacto añadido: {c['nombre']} {c['apellidos']}\n")

# 4. Leer log.txt y mostrar el recuento total de contactos procesados
with open('log.txt', mode='r') as archivo_log:
    lineas = archivo_log.readlines()
    print(f'Total de contactos procesados: {len(lineas)}')
