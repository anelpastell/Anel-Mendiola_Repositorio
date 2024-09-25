import numpy as np
import matplotlib.pyplot as plt
#
#Ejercicio 1.
freq= [1, 5, 7, 2]
freq = np.random.randint(1, 8, [4])
#
#Ejercicio 2.
amplitud= np.random.randint(1,8, [4])
amplitud= [4.5, 5.1, 3.4, 6]
#
#Ejercicio 3.
t= np.arange(0,1, 1/2000)
#
#Ejercicio 4.
idx= 0
y= amplitud[idx] * np.sin(2*np.pi * freq[idx] * t)
print(amplitud[idx], freq[idx])
plt.plot(t,y)
plt.show()
#
#Ejercicio 5.
for idx in range(2,4):
    y+= amplitud[idx]* np.sin(2*np.pi * freq[idx] * t)
print(amplitud[idx], freq[idx])
plt.plot(t,y)
plt.show()

# Numpy también permite aplicar operadores tales como la transormada de fourier a un arreglo de datos con
# el paquete np.fft, en particular la función np.fft.fft(x) aplica la transformada discreta de fourier al arreglo x

X = np.fft.fft(y)


# Ejercicio 6. Cree un arreglo, llamado frequence, de los enteros en el intervalo [0, 1999]
frequence = range(2000)

# Ejercicio 7. Calcular el valor absoluto a todos los elementos del arreglo X
abs_X= np.abs(X)

# Ejercicio 8. De los primeros 10 elementos del arreglo del ejercicio anterior, determine los 4 elementos máximos y en
# qué índices se localizan
print(abs_X[:10])

# Para mostrar la frecuencia y la amplitud en el dominio de Fourier use las siguientes líneas de código
plt.stem(frequence, abs_X)
plt.show()
