 # LISTAS
 # sirven para almacenar múltiples elementos

 comida = ['naranja', 'pastel', 'cafe', 'helado', 'pescado', 'camaron', 2345, 456.823, False]
 print(comida)
 # los elementos se cuentan del 0
 # si quieremos acceder al elemento 0:

 print(comida[0]) # imprime naranja
 print(comida[1]) # imprime pastel
 # print(comida[4]) # marca que estamos fuera de rango porque no hay elemento 4

 #los elementos de una lista siempre se pueden cambiar y actualizar

 comida[0] = 'quesadilla'
 print(comida[0]) # si cambió!!!

# FUNCIÓN APPEND
#  comida.append('camaron') # agrega elementos a la lista
#  comida.remove('helado') # quita elementos de la lista
#  comida.pop() # elimina el último elemento de la lista
 # comida.insert(4, 'camaron') # agrega un elemento
                         # primero pones la posición y después el elemento
# comida.sort() # acomoda en orden alafbético
# comida.clear() # vacia la lista

# las listas también pueden almacenar números enteros, flotantes y boleanos
#### se agregaron otros datos je
 for x in comida:
     print(x)
# el bucle for imprime todos los elementos de la lista comida

# LISTAS 2D/ MULTIDIMENSIONALES

lista1= ['agua', 'refresco', 'té']
lista2= ['huevo', 'chilaquiles', 'molletes']
lista3= ['pastel', 'dulces', 'hotcake']

# se pueden agregar todas las listas a una sola
# crea una nueva lista:

juntas = [lista1, lista2, lista3]
print(juntas[2][2]) # se agruparon las listas
# puedo establecer el número de índice
# si quiero un solo elemento, agrego otro par de corchetes
# [0][0] nos da el primer elemento de la primera lista


