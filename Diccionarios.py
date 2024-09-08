# DICCIONARIOS
## Es una colección modificable y no ordenada de pares únicos clave-valor
## nos permiten acceder rapidamente a un valor
## se almacenan pares únicos clave-valor

# Diccionario países y capitales
## la clave serán los países y el valor las capitales
capitales = {
    'Estados unidos': 'Washington DC ',
    'Argentina' : 'Buenos Aires',
    'Chile' : 'Santiago de Chile',
    'Brasil' : 'Brasilia',
    'cursos' : ['python', 'c++'],
    'años' :  234
}

# para acceder a los valores, no usamos índices numéricos

print(capitales['Chile']) # nos arroja el valor que almacena la clave
# si ponemos una clave que no existe nos dice error
print(capitales.get('Alemania'))
# si ponemos .get, nos dirá 'none', de que no existe en la lista

print(capitales.get('Argentina'))
# con esta si nos da la capital porque si está Argentina en el diccionario

# imprimir solo las claves/valores
print(capitales.keys()) # nos da los países
print(capitales.values()) # nos da las capitales

#imprimir llaves y valores
print(capitales.items()) # nos da el diccionario completo

# Agregando un valor al diccionario
capitales.update({'Alemania': 'Berlín'})

# Eliminar valores de un diccionario
capitales.pop('Estados unidos')

#Limpiar diccionario
# capitales.clear()

# podemos usar un bucle for para traer el diccionario

for key, value in capitales.items():
    print(key, value)





