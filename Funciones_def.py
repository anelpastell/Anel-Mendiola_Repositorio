# FUNCIONES
# bloque de código que se ejecuta solamente cuando la llamas
# hay que evitar repetir código innecesario
# realiza una tarea específica cada vez que la llamamos

# definir una función

def saludo(primer_nombre, apellido, edad):
    print("Hola " + primer_nombre + " " + apellido) # las funciones no se limitan a una sola línea
    print("Tienes:  " + str(edad) + "  años")
    print("Ten un buen día :) ")

# aquí ya tenemos la función, ahora hay que llamarla

# llamar una función
# saludo() # si no escribirmos el nombre de la función, no se ejecuta nada
# saludo()
# saludo()

# podemos enviarle información a una función
# saludo('Anel !!')

# print(nombre)
# la variable nombre solamente existe de manera local DENTRO de la función
# por eso, si intentas llamarla, sale error

nombre =  input('Ingresa un nombre: ')
# aquí creamos una variable de nombre idéntica a la que está en la función
# la cosa es, que como está por fuera de la función, ya no es la misma y  sí la puedes llamar

saludo(nombre, "Mendiola", 20)
# también podemos enviar dos valores
# marca error porque solo tenemos una variable para recibir nuestro valor

# puedes mezclar los tipos de datos que se envían
## ahorita mandamos valores de cadena
