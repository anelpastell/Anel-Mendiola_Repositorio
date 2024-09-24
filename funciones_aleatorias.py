# continuación de funciones aleatorias

import numpy as np
# numero decimal entre 0 y 1
np.random.rand()

# array de 1D de decimales entre 0 y 1
np.random.randn(4)

#array2D de decimales entre 0 y 1
np.random.rand(4, 2)
import matplotlib.pyplot as plt
arreglo =  np.random.rand(100000)
plt.hist(arreglo)
plt.show()

# número entero entre 0 y N
np.random.randint(10)

# array de enteros entre 0 y N
np.random.randint(10, size=[3,2])

# array de enteros entre -N y M
np.random.randint(-10, 10, size=[2, 4])


# array uniforme con curva gaussiana
arreglo = np.random.normal(size=20000000)
plt.hist(arreglo, bins=100)
plt.show()

# permutaciones
arr = np.arange(9)

print(arr)

# desordenar un array
np.random.shuffle(arr)

print(arr)

arr.reshape(3, 3)

# generar secuencia permutada a partir de un número
np.random.permutation(arr.reshape(3, 3))

np.random.shuffle(np.arange(15))
np.random.permutation(15)
