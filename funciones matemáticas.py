import math
# con eso ya importamos la biblioteca que nos deja hacer operaciones

PI = 3.14
print(round(PI)) # redondea a 3

# Redondear un número hacia arriba
print(math.ceil(PI)) # redondea a 4

# Redondear un número hacia abajo
print(math.floor(PI)) # redondea a 3

# Función ABS: valor absoluto de un número
# si ponemos un número negativo, da uno positivo

print(abs(PI)) # su valor absoluto es 3.14

# ahora probamos con uno negativo
lista = -3.678
print(abs(lista)) # su valor absoluto es 3.678 POSITIVO

# Función POW
## eleva un número a una potencia

print(pow(PI, 2)) # da 9.8 , es la potencia 2

# Función SQRT
## da raíz cuadrada
print(math.sqrt(4652)) # su raíz es 68.20

# Función para MAX y MIN
x = 298
y = 567
z = 426
print(max(x,  y,  z)) # el valor máximo es y = 567
print(min(x, y , z)) # el valor mínimo es x = 298


