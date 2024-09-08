# Conversión de tipos de datos

x = 1
y = 2.8
z = "3"

print(x, y, z)
# Acuerdate que no se pueden hacer operaciones
# matemáticas entre cadenas
print(x)
print(y)
print(z)

# convertir a número entero
print(int(y))  # de flotante pasa a entero

# convertir a string
print(str(y))  # devuelve 2.8

# convertir a flotante
print(float(z))  # nos da 3.0, pasa a decimal

# OJOOOO
# la variable si la vuelves a imprimir, no te va a dar el valor cambiado:
print(z)  # nos da 3, que es la variable original
# comprueba usando type
print(type(z))  # nos dice que es un string

# aplicamos la conversion

y = str(y)
x = str(x)
# aquí ya hicimos string la variable x y
# cuando imprimes da "lo mismo" pero el tipo de variable cambia

print(x)  # da 1
print(y)  # da 2.8
# comprueba
print(type(x))  # es un string
print(type(y))  # es un string
# intenta multiplicarlo:
# print(x*y) # da error
# RECUERDA: las cadenas no se multiplican ni se suman

# como enteros
x = int(x)
print(type(x)) # nos dice que es un entero

#¿cuando usarlo?

edad = 24
# print("Edad:" + edad)
# no se pueden sumar cadenas con enteros
# puedes escribirlo con la coma ,
# o puedes escribirlo con str() y volverlo una cadena
print("Edad:", edad)
print("Edad:" + str(edad))
