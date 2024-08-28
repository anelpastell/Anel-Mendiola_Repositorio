#determinar si las demás modalidades son aplicables a rango
### crear un archivo.py para determinar si los tipos de dato range cumplen:
##### mutabilidad, suma, producto x un entero

## Creación de un objeto range
r = range(1,10)

# mutabilidad
r[0]=5
#marca error

# Suma de rangos
rango_suma = r + range(10,20)
## marca error

#Multuplicación por un entero
rango_multiplicación = r*2
## marca error

###Slicing
rango_slice= r[2:5]
print(rango_slice)
## si sale

### convertir a lista y a tupla
lista_r= list(r)
tupla_r = tuple(r_list)

print('tupla',tupla_r)
print('lista', lista_r)




