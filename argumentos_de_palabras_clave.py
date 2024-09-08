# argumentos de palabra clave
## son argumentos que van precedidos por un identificador cuando los pasamos a una función

def saludo (nombre, apellido, lenguaje):
    print('Hola ' + nombre + ' ' + apellido + ', estás aprendiendo: ' + lenguaje)

saludo(lenguaje = 'Python', apellido = 'Mendiola',  nombre='Anel')
# sabe cual es el argumento !!!
# si pones el identificador, no importa el orden en que pongas las palabras
# estas se acomodan solas
