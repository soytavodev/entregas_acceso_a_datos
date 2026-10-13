NOMBRE_FICHERO_ALEATORIO = "peliculas_aleatorio.txt"
TAMANO_REGISTRO = 15

def escribir_Registros_tamano_fijo():

    peliculas = [
        "Matrix",
        "Titanic",
        "Interstellar",
        "Gladiator"
    ]
    flujo = open(NOMBRE_FICHERO_ALEATORIO,"w")
    for pelicula in peliculas:
        linea = pelicula.ljust(TAMANO_REGISTRO - 1) + "\n"
        flujo.write(linea)

    flujo.close()

    print("Se ha escrito",NOMBRE_FICHERO_ALEATORIO,"correctamente.")    

def leer_registro_directo(numero_registro):
    flujo = open(NOMBRE_FICHERO_ALEATORIO,"r")
    posicion = numero_registro * TAMANO_REGISTRO
    flujo.seek(posicion)
    linea = flujo.readline()
    flujo.close()

    print("Registro", numero_registro, ":", linea.strip())

def modificar_registro(numero_registro, titulo_nuevo):
    flujo = open(NOMBRE_FICHERO_ALEATORIO,"r")
    posicion = numero_registro * TAMANO_REGISTRO
    flujo.seek(posicion)
    linea_nueva = titulo_nuevo.ljust(TAMANO_REGISTRO - 1) + "\n"
    flujo.write(linea_nueva)
    flujo.close()
    print("Registro",NOMBRE_FICHERO_ALEATORIO, "modificado correctamente.")    