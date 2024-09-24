# métodos internos
## métodos estadísticos

import numpy as np

# array de 2*3 con números aleatorios

arr= np.arange(1,7)
arr

arr2d= arr.reshape(2, 3)
arr2d

#suma
arr.sum(), arr2d.sum()

# media
arr.mean()

# std
arr.std()

#varianza
arr.var()

# métodos de ordenación
import numpy as np

arr= np.random.randint(-10, 10, [3, 3])
arr

# Ordenar elementos horizontalmente
arr.sort()
arr

# Ordenar elementos verticalmente
arr.sort(0)
arr

arr


