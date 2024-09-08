# FUNCIONES IF
# bloque de codigo que se ejecuta únicamente si su condición:
## ES VERDADERA

edad = int(input(" ¿cuantos años tienes? "))

if edad >= 18:
    print ("Eres mayor de edad !!!")

# pusimos que la condición para que if sea verdadero
# es que la persona tenga una edad mayor o igual a 18
# como puse que tengo 20, arroja el mensaje "Eres mayor de edad!!"

# si ponemos una edad menor a 18, no imprime nada

# podemos hacer que imprima otra cosa agregando ELSE

if edad >= 18:
    print(" Eres mayor de edad!!")
else:
    print(" Eres menor de edad :( ")

# se pueden agregar varias condiciones else e if

if edad >= 100:
    print(" Tienes un siglo de vida !!!")
elif edad >= 18:
    print(" Eres mayor de edad !!!")
else:
    print(" Eres menor de edad :( ")
