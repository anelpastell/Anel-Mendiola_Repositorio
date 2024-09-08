# TIPOS DE DATOS

#Tipo de dato STRINGS / CADENAS ' '
nombre = 'Anel'
print(nombre)
#cuando colocamos la variable dentro del print
# no se pone entre comillas dobles (" ")

print("hola", nombre)
# se puede combinar una cadena con texto

print(type(nombre))
# poner type() nos dice qué tipo de variable es nombre en este caso
# nos ayuda a comprobar el tipo de variable

# Combinar variables
apellido_segundo= "Mendiola"
nombre_completo = "Hola, " + nombre +  " " + apellido_segundo
print(nombre_completo)

# Tipo de dato: ENTERO
# Los números se ponen así como van, sin comillas porque
# si no, se entiende que son texto y no valores de número

edad = 20
# edad = edad + 1
print(edad)

edad += 1
print(edad)
# el += 1 es lo mismo que escribir edad +1
print(type(edad))
# nos indica que la variable edad tiene números enteros
# si lo escribieramos entre " " nos diría que es una cadena

print("Tu edad es: ", edad)
# no puedes sumar cadenas con enteros, mira:
# print("Tu edad es:" + edad)
#### sale error pues

print("Tu edad es:" + str(edad))
# escribir str hace la variable edad un string y se puede imprimir en suma
# pero hemos visto en clase que funciona mejor la coma


# Tipo de dato: FLOTANTE
altura = 180.5
# los decimales indican que el número es un flotante
print(altura)
print(type(altura))

# imprimir altura con cadena

print("Tu altura es:", altura)
# no se puede sumar cadena con flotante
# o sea, no puedes escribir:
# print("Tu altura es:" + altura)
### sale error

# Tipo de dato: BOOLEANOS
# Los boleanos son tipos de datos que solo pueden almacenar
# verdadero y falso

humano = False
print(humano)
# ¿ por qué usar boleaos en lugar de cadena de texto?
# Los boleanos son útiles cuando queremos comprobar si
# una declaración es verdadera o falsa

# comprobar tipo de dato
print(type(humano) # nos dice que es un bool

# concatenar con texto
# print("Eres un humano:" + humano)
### tampoco se pueden sumar los boleanos
