NOMBRE_FICHERO = "peliculas_secuencial.txt"`

def escribir_varias_peliculas():
  peliculas = [
    "Matrix,148\n",
    "Titanic,195\n",
    "Avatar,162\n",
  ]
  fichero.open(NOMBRE_FICHERO, "w")
  fichero.writelines()
  fichero.close()
  
def anadir_una_pelicula():
  fichero.open(NOMBRE_FICHERO, "a")
  fichero.write()
  fichero.close()
  
def leer_todo_de_golpe():
  fichero.open(NOMBRE_FICHERO, "r")
  fichero.read()
  fichero.close()
  
def leer_linea_a_linea():
  fichero.open(NOMBRE_FICHERO, "r")
  while True:
    readline()

def main():
escribir_varias_peliculas()
anadir_una_pelicula()
leer_todo_de_golpe()
leer_linea_a_linea()

if __name__ == "__main__":
    main()
