# BUCLES FOR
## instrucción que ejecutara su bloque de código un número limitado de veces

# for x in range(1, 11):
#     print(x)

# imprime del 1 al 9, para imprimir del 1 al 10, pon del 1 al 11

# elem es la variable que toma el valor del elemento dentro del integrador
# sirve para inregrar listas, tuplas y diccionarios

# nos sirve para contar números

# for x in range (50, 101):
#     print(x)

# también puedes poner que vaya de dos en dos

# for x in range(50, 101, 2):
# print(x)

# EJEMPLO
# lista1= input("Ingresa tu nombre: ")
#  for x in lista1:
#     print(lista1)

# # FOR con listas

# numeros = [2, 3, 4, 5, 6, 7, 8, 9]
# for idx in numeros:  # Para [variable local] en [lista]
#     if idx % 2 == 0:
#         print(idx, ' es par')
#     else:
#         print(idx, ' es impar')

# # bueno otro ejemplo

# promedio = 0
# numeros= [2, 4, 6, 8,]
# for idx in numeros:
#     promedio += idx
#     print(str(idx))
# promedio /= len(numeros)
# print('el promedio es: ', promedio)

# # otro ejercicio:

# numeros = [0, 2, 4, 5, 6, 8]
# longitud = 0
# for _ in numeros:
#     longitud += 1
#     print('se está ejecutando el for')
# print('la longitud de la lista es: ', longitud)


# # ejemplo

# # numeros[2] = numeros[2]*2
# # numeros
#
# #Modificar ítems de la lista al vuelo
# #Para asignar un nuevo valor a los elementos de una lista
# # mientras la recorremos, podríamos intentar asignar al número
# # el nuevo valor:
#
# numeros = [0, 2, 4, 5, 6, 8]
# for numero in numeros:
#     numero += 10
#     print(numero)
#
# numeros
# # Sin embargo, ésto no funciona.
# # La forma correcta de hacerlo es haciendo referencia al índice
# # de la lista en lugar de la variable:
#
# # indice = 0
# # numeros = [1, 2, 3, 4, 5, 6, 8, 9 , 10]
# # for numero in numeros:
# #     numeros[indice] += 10
# #     indice += 1
#
# numeros
#
# # ejemplo
#
# # lista = ['azul', 'verde', 56, ['2da lista']]
# # for i in lista:
# #     print(i)
# #
# # lista = [4, 5, 6]
# # for i in lista:
# #     print(i)
# #
# # lista = [1, 2, 3, 4, 5, 6]
# # #lista[6]
# #
# # lista = [1, 2, 3, 4, 5, 6]
# # for i in lista:
# #     print(lista[i])
#
# indice = 0
# numeros = [1, 2, 3, 4, 5]
# for i in numeros:
#     numeros [i] *= 10
#     print('valor de i = {}, lista es: {}'.format(i, numeros))
# numeros



###
# enumerate(iterable, start=0)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
enumerate(seasons)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))

# FOR usando ENUMERATE

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for idx, numero in enumerate(numeros):
    numeros[idx] *= 10
numeros

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for idx, season in enumerate(seasons):
    print(idx, season)

# FOR con CADENAS

string = 'hola'
list(string)

cadena = 'Hola'
for caracter in cadena:
    print(caracter)

# recuerda que las cadenas son inmutables

# string = 'hola'
# string [1] = 'z'

# cadena = 'hola'
# for i, c in enumerate(cadena):
#     cadena[i] = "*"

cadena [2]*2

cadena = 'hola'
cadena2 = ""
for caracter in cadena:
    cadena2 += caracter * 2

print(cadena, cadena2)

# CADENA usando RANGE

list(range(10))

for i in range(10):
    print(i)

matrix = [[1, 2, 3, 4],
                [5, 6, 7, 8]]

for row in matrix:
    print(row)

matrix = [[1, 2, 3, 4],
               [5, 6, 7, 8]]
for row in matrix:
    print('val')
    for column in row:
        print(column)

    for idx_row, row in enumerate(matrix):
        for idx_col, column in enumerate(row):
            print(column)
