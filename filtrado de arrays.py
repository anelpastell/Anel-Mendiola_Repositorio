# filtro unique
import numpy as np

# generamos un array con números aleatorios repetidos
arr = np.random.randint(0, 10, 40)
arr

# aplicamos el filtro unique
np.unique(arr) # se borran elementos duplicados

#Filtro in1d
#Devuelve un array de una dimensión indicando si los elementos
# de una lista se encuentran en otro array:

np.in1d([-1, 4, 8, 12], arr)

# Filtro where
# Sirve para generar un array filtrado a partir de una condición
# y un valor por defecto:

# generamos un array con números aleatorios
arr1 = np.random.uniform(-5, 5, size=[3,2])
arr1

# creamos un filtro que establece los negativos a 0
arr2 = np.where(arr1<0, 0, arr1)
arr2

# añadimos otro filtro que establece los positivos a 1
arr2 = np.where(arr2>0, True, arr2)
arr2

# filtros booleanos
# Permiten hacer comprobaciones lógicas en los arrays
# de booleanos:

arrbool = np.array([True, True, True, False])

# comprobar si todos los elementos del array son True
arrbool.all()

# comprobar si al menos un elementos del array es True
arrbool.any()

# definimos un array de booleanos 2d
arrbool2d = np.array(
    [
        [False, True],
        [False, True],
        [False, True]
    ]
)

arrbool2d

# comprobar si alguna de las columnas es todo True
arrbool2d.all(0)

# comprobar si alguna de las filas tiene algún True
arrbool2d.any(1)