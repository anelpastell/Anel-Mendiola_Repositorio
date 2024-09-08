# Crear un archivo llamado tarea04.py que resuelva los siguientes ejercicios:
# Considera las siguientes calificaciones:

# calif_1 = 10
# calif_2 = 7
# calif_3 = 4

# Calcula el promedio de las calificaciones considerando que:

# La primera nota vale un 15% del total
# La segunda nota vale un 35% del total
# La tercera nota vale un 50% del total

cali1 = 10
cali2 = 7
cali3 = 4

promedio = (cali1 * 0.15) + (cali2 *0.35) + (cali3*0.50)
print('El promedio de las calificaciones es: ', promedio)

#La siguiente matriz debe cumplir que el 4to valor de cada fila
# debe ser igual a la suma de los primeros 3 valores.
# Crea un código para hacer las correcciones necesarias

matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [ 3, 3, 3, 9],
    [ 4, 4, 4, 13]
]

for fila in matriz:
    suma = sum(fila[:3])
    fila [3] = suma

print('La matriz nos queda así: ', matriz)

