# Bucles anidados
fila = int(input("¿Cuantas filas quieres?"))
columna = int(input("¿Cuantas columnas quieres?"))
simbolo = input("Ingresa un simbolo: ")

for i in range(fila):
    for j in range(columna):
        print(simbolo, end= "")
    print()
# un bucle dentro de otro bucle para imprimir el símbolo