NOMBRE_FICHERO_TEMPERATURAS = "temperaturas.txt"
NOMBRE_FICHERO_CONTADOR = "contador.bin"

def escribir_temperaturas():
  print("1.escribir_temperaturas")
  flujo = open(NOMBRE_FICHERO_TEMPERATURAS, "w")
  flujo.write("Primera línea\nSegunda línea\nTercera línea\n")
  flujo.close()
 
 
def leer_temperaturas():
  print("2.leer_temperaturas")
  flujo = open(NOMBRE_FICHERO_TEMPERATURAS, "r")
  contenido = flujo.read()
  flujo.close()
  print(contenido)

def saltar_primera_temperatura():
    print("3.saltar_primera_temperatura")
    flujo = open(NOMBRE_FICHERO_TEMPERATURAS, "r")
    flujo.readline() 
    posicion = flujo.tell()
    flujo.seek(0)
    flujo.seek(posicion)    
    resto= flujo.read()
    flujo.close()
    print("Nos saltamos la primera línea y leemos el resto:")
    print(resto)

def comprobar_fichero_configuracion():
    try:
        flujo = open("fichero_que_no_existe.txt", "r")
        flujo.close()
    except FileNotFoundError:
        print("Error controlado: el fichero no existe, pero el programa no se cae.")



def guardar_numero_registros():
    datos = bytes([3])  # equivale a las letras A, B, C, D

    flujo_salida = open(NOMBRE_FICHERO_CONTADOR, "wb")  # wb = write binary
    flujo_salida.write(datos)
    flujo_salida.close()

    flujo_entrada = open(NOMBRE_FICHERO_CONTADOR, "rb")  # rb = read binary
    leido = flujo_entrada.read()
    flujo_entrada.close()

    print(f"Bytes escritos:  {list(datos)}")
    print(f"Bytes leídos:    {list(leido)}")
    print(f"Como texto:      {leido.decode('utf-8')}")

def main():
  escribir_temperaturas()
  leer_temperaturas()
  saltar_primera_temperatura()
  comprobar_fichero_configuracion()
  guardar_numero_registros()

if __name__ == "__main__":
    main()
