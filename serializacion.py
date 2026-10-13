import json
libros = [
{"titulos": "Leyendas de los Otori","autor": "Anonimo","anio": "XXXX","paginas":"99"},
{"titulos": "Harry Potter","autor": "Anonimo","anio": "XXXX","paginas":"199"},
{"titulos": "La Cupula","autor": "Anonimo","anio": "XXXX","paginas":"299"}
]

print(libros)
print(type(libros))
cadena = json.dumps(libros) #volca y convierte en json
print(cadena) # lista en memoria
print(type(cadena)) #tipo de las variables

archivo = open("basededatos.dat",'w')
archivo.write(cadena)
archivo.close()

