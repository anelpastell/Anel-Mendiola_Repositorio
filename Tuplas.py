# TUPLAS
## colecciones ordenadas e inmutables
## no se pueden modificar
## útiles para agrupar datos relacionados
## pueden ser más rápidas que las listas

# LISTA []
# TUPLA ()

# creando tupla de estudiantes
estudiantes = ('Anel', 21, 'F', 'Caro', 21, 'F', 'Fernando', 22, 'M')

# COUNT
# print(estudiantes.count(21))
# count nos dice cuantas veces aparece un valor en la tupla

# INDEX
print(estudiantes.index('M'))
# ayuda a encontrar el índice de un valor específico

# mostrar el contenido de una tupla usando for:

for x in estudiantes:
    print(x)

# comprobar si un valor específico existe en la tupla usando if
if 'Anel' in estudiantes:
    print("Si está!!")





