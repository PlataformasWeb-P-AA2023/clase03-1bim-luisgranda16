# proceso 
#
# acceder al archivo
archivo = open('data/Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r")

# obtener las líneas del archivo
lineas = archivo.readlines()

# lineas es ina lista de cadenas
# se imprime las siguientes posiciones
print(lineas[0])
print(lineas[1])

# en línea tomo el valor de lineas[1]
linea = lineas[1]
# a línea que es una cadena, la separo mediante la función
# de Python split
# Recuerdo que el separador de la cadena es un "|"

linea = linea.split("|")

# imprimo la nueva línea; que ahora es una lista
print(linea)

for l in lineas: 
    l = l.split("|")
    nombre = l[1]
    canton = l[5]
    provincia = l[3]
    parroquia = l[7]

    cadena = """ nombre:%s\n provincia:%s \n canton:%s \n parroquia:%s """ %(nombre, provincia, canton, parroquia) 
    print (cadena)

archivo.close()

