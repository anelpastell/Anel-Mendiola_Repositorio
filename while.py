# BUCLES WHILE
## ejecutará en bucle siempre que su condición siga siendo verdadera

# while 1 == 1:
#     print("AYUDAAAAA SE REPITE)

## siempre busca una forma de salir del bucle

nombre = ""

while not nombre or len(nombre) == 0:
    nombre = input(("Ingresa tu nombre: "))
print("Hola ", nombre)

