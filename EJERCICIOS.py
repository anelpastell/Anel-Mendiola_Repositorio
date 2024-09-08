# EJERCICIOS

# 1. Realiza un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar,
# debe repetise el proceso hasta que lo introduzca correctamente.

# numero = 0
# while numero %2 == 0:
#     numero= int(input("Introduce un número impar: "))

# 2. Realiza un programa que sume todos los numeros enteros pares
# desde el 0 hasta el 100:
# puedes usar sum () y range() para hacerlo más facil

# pares = sum(range(0, 101, 2))
# print(pares)

# 3. Realiza un programa que pida al usuario cuantos números
# quire introducir. Luego lee todos los números y realiza una media

# suma = 0
# cantidadnum = int(input(" ¿Cuántos números quieres introducir?: "))
# for x in range(cantidadnum):
#     suma += float(input("Introduce el numero: "))
#
# print("Tus números fueron: ", cantidadnum)
# print("La suma de tus números es: ", suma)
# print("La media es: ", suma/cantidadnum)


# Utilizando la función range() y la conversión a listas genera
# las siguientes listas dinámicamente:

### Todos los números del 0 al 10 [0, 1, 2, ..., 10]
### Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
### Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
### Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
### Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

# print( list( range( 0, 11)))
# print(list(range(-10, 1)))
# print(list(range(0,22,2))) # ponlo hasta el 22 para que llegue hasta 20
# print(list(range(-19, 1, 2))) # empieza en un impar y que vaya de 2 en 2
# print(list(range(0,55,5)))

# 5. Dado un número entero n realice las siguientes acciones condicionales:
# Si es impar, imprima 'Raro'
# Si es par y está en el rango inclusivo de 2 a 5 , imprima 'No es raro'
# Si es par y está en el rango inclusivo de 6 a 20, imprima 'Raro'
# Si es par y mayor que 20, imprima 'No es raro'

# def numero(n):
#     if n%2 != 0:
#         print("RAROOO")
#     elif n %2 == 0 and range(2,6):
#         print("NO ES RARO")
#     elif n%2 == 0 and range(6,21):
#         print("RAROOO")
#     elif n%2 ==0 and n>20:
#         print("NO ES RARO")

# 6. Escriba un numero que reciba un numero entero n
# y para todos los enteros i < n, imprime i^2


# 7. Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# En caso de no introducir una opción válida, el programa informará
# de que no es correcta.

# num1 = float(input("Introduce un número: "))
# num2 = float(input("Introduce otro numero: "))
# valor = 0
#
# print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
# valor = int(input("Introduce un numero: "))
#
# if valor ==1:
#     print("La suma de: ", num1, "+", num2, "es", num1+num2 )
# elif valor ==2:
#     print("La resta de", num1, "-", num2, "es", num1-num2)
# elif valor == 3:
#     print("El producto de", num1, "*", num2, "es", num1*num2)
# else:
#     print("opción inválida")


# 8. Realiza un programa que pida al usuario un número entero
# del 0 al 9, y que mientras el número no sea correcto
# se repita el proceso. Luego debe comprobar si el número
# se encuentra en la lista de números y notificarlo:

# valores = [1, 3, 6, 9]
#
# while True:
#     valor = int(input('Digite um valor del 0 al 9: '))
#     if valor >= 0 and valor <= 9:
#         break
# if valor in valores:
#     print("El número ", valor, "se encuentra en la lista", valores)
# else:
#     print("El número ", valor, "no se encuentra en la lista", valores)


#9.  Dadas dos listas, debes generar una tercera
# con todos los elementos que se repitan en ellas
# pero no debe repetise ningún elemento en la nueva lista:

# lista1 = ['n', 'a', 'r', 'a', 'n', 'j', 'a', ' ', 'y', ' ', 'p', 'a', 's', 't', 'e', 'l']
# lista2= ['p', 'e', 's', 'c', 'a', 'd', 'o', ' ', 'y ', 'c', 'a', 'm', 'a', 'r', 'o', 'n']
# lista3= []
#
# for letra in lista1:
#     if letra in lista2 and letra not in lista3:
#         lista3.append(letra)
# print(lista3)