import json
libros = [
{"titulos": "La vaca tuvo un bebe","autor": "Anonimo","anio": "XXXX","paginas":"99"},
{"titulos": "Hijo de la luna","autor": "Anonimo","anio": "XXXX","paginas":"199"},
{"titulos": "Fanhrenteit 365","autor": "Anonimo","anio": "XXXX","paginas":"299"}
]

print(libros)
print(type(libros))
cadena = json.dumps(libros) #volca y convierte en json
print(cadena) # lista en memoria
print(type(cadena)) #tipo de las variables

archivo = open("basededatos.dat",'w')
archivo.write(cadena)
archivo.close()

