# Nos ayudan a ahorrar código al escribir cadenas

# LEN para longitud de cadena
lista1 = "pera"
print(lista1)

#para saber la longitud de la cadena, le ponemos len
print(len(nombre))
# nos dice que la longitud de la cadena es de 4, tiene 4 caracteres

# METODO DE BÚSQUEDA

print(lista1.find("p"))
# el find nos ayuda a encontrar la posición de una letra
# nos da el valor en números, por ejemplo, de la P, su ubicación es 0
# La palabra inicia contando desde cero= P (0) E (1) R (2) A(3)

# METODO CAPITALIZE
print(lista1.capitalize())
# nos da la primera letra en mayuscula, si agregas más palabras
# ya no cambia la mayuscula

# METODO .UPPER y .LOWER
#convierte el texto a mayusculas y minusculas
print(lista1.upper()) # nos da PERA
print(lista1.lower()) # nos da pera

# METODO IS DIGITAL
# depende si la cadena de texto es un digito o no
print(lista1.isdigit())
# nos da False, porque si, es una cadena
# si pusieramos un número diría que es cierto:

lista2= "123456789"
print(lista2.isdigit()) # nos dice que es verdadero

# METODO IS ALPHA
#sirve para ver si hay espacios o caracteres especiales
# si lo corres así, te va a decir que es falso
# si pegas tu texto te dice que es verdadero

lista3= "Me gusta el pan"
# lista 3= "Me gusta el pan"
print(lista3.isalpha()) # sale falso

# ahora juntamos las letras:
# lista3= "Megustaelpan"
print(lista3.isalpha()) ## dice que es verdadero

# METODO COUNT
# cuenta los caracteres de cierto tipo de una cadena

print(lista3.count("e")) # hay 2 letras 3 en la lista3

# METODO REPLACE
print(lista3.replace("e", "o"))
# nos dice "Mo gusta ol pan ajjajaxd

# MOSTRAR UNA CADENA VARIAS VECES
print(lista2*4) # devuelve 4 veces la lista
