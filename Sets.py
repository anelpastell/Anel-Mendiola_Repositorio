# SETS
# estructura de datos usada para almacenar datos
# similar a las listas
# los elementos de un set son únicos -> no se pueden repetir
# no mantienen un orden
# sus elementos deben ser inmutables
# son más rápidos que las listas

utensilios = {"tenedor", "cuchara", "cuchillo"}
                        # aunque repitamos elementos, al imprimirlos, solo se imprimen una vez los que no están repetidos
platos = {"plato", "tazón", "tupper", "tenedor"}

#utensilios.add("cucharita")     # para agregar elementos
#utensilios.remove("cuchara") # elimina un elemento
#utensilios.pop() # elimina un elemento al azar
# utensilios.clear() # elimina los elementos del conjunto

#utensilios.update(platos) #agregó los elementos del set de platos
#print(utensilios.difference(platos)) # la diferencia del conjunto con el iterable con un conjunto nuevo
#print(utensilios.intersection(platos)) # nos da los elementos repetidos

for x in utensilios:
    print(x)
# al imprimir el set, nos lo da en orden diferente