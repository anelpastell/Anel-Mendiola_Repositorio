# Manipular cadenas
# crear una subcadena extrayendo pedazos de cadenas

# CORTE DE CADENAS
## se usa SLICE como objeto de corte
## hay un índice de inicio, índice de finalización y un paso

# indice de iniciación

lista1 = "cafe con leche"
#cortamos la cadena

# bebida = lista1[0] # probamos cortando una letra
# se usan los corchetes [] para decir donde quieres partir la cadena
# recuerda que se cuenta desde cero

# print(bebida) # nos da c

# intenta cortar toda la palabra
bebida = lista1[0:4]
print(bebida) # nos da cafe

# se puede abreviar dejando en blanco [:4]
bebida = lista1[:4]
print(bebida) # nos da cafe

quemegusta = lista1[5:14]
print(quemegusta) # nos da con leche jajjaja

# como contar cada segundo caracter despues del primero
## cantidad en que incrementa el indice desde el inicio
## hasta el final

lista2 = lista1[0:14:1] # el 0:10 es hasta donde quieres cortar la lista
                                      # el step o los caracteres que cuenta son de 1

print(lista2)

# ahora prueba con espacio de 2
lista2= lista1[0:14:2]
print(lista2) # nos da cf o eh > salta los caracteres

# SUBCADENA
lista_invertida = lista1 [::-1]
print(lista_invertida) # nos da ehcel noc efac xdddd

# Función SLICE

sitioweb = "http://www.google.com"
# vamos a eliminar y crear una subcadena basada en el nombre del sitio web
# solo quiero el nombre del sitio web

nombresitioweb = sitioweb[11:17]
print(" así sería cortando la cadena:", nombresitioweb)

eslise = slice(11, -4)
# la función slice te pide un indice de inicio, uno de fin y uno de step
# para el valor de inicio cuentas de izquierda a derecha  : 0 , 1, 2, 3, 4 etc
# en este caso: 0: h, 1: t, 2:t, 3: p, 4: s y así
# para el valor de fin, cuentas de derecha a izquierda en negativos : -1, -2, -3, -4

print(sitioweb[eslise]) # nos dice que es google

