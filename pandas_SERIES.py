# clase series
## las series pueden tener etiquetas en los ejes

import numpy as np
import pandas as pd

# creación de series a partir de una lista, array o diciconario

## listas

etiquetas = ['A', 'B', 'C', 'D']
etiquetas

lista = [25, 50, 75, 100]
lista

# cast con otro tipo de datos
str(lista)

tuple(lista)

# serie básica
#pd.Series(lista)
pd.Series(lista)

# serie con etiquetas
pd.Series(data=lista, index=etiquetas)


# parámetros por posición
pd.Series(lista, etiquetas)

## arrays
array = np.random.randint(50, size=4)
array

# serie básica
pd.Series(array)

# serie con etiquetas
pd.Series(array, etiquetas)

## diccionarios

dicc= {'etiqueta1':25, 'etiqueta2':50, 'etiqueta2':75, 'etiqueta4':100}
dicc

# serie con etiquetas
pd.Series(dicc)

## indices

list= [100, 300, 200]
list

list[1]

ingresos = pd.Series([100,300,200], index = ['enero', 'febrero', 'marzo'])
ingresos


# acceso por nombre
ingresos['febrero']

# aceso por número
ingresos[1]

## metodos
gastos = pd.Series([100,150,250], index = ['enero', 'febrero', 'marzo'])
gastos
ingresos

total= ingresos.subtract(gastos)
total

ingresos-gastos

ingresos+gastos

## tipo de una serie

type(total)
type(3.5)


