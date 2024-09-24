# DATA FRAME

# Un DataFrame es una agrupación de Series
# unidas bajo los mismos índices dando como resultado
# estructuras similares a tablas donde representar
# todo tipo de información.
# Cada serie del DataFrame se puede considerar una columna
# a la cuál podemos establecer un nombre:

import pandas as pd
import numpy as np

array = np.random.uniform(-10, 10, size=[4,4])
array

# Representación en jupyter
df = pd.DataFrame(array, index=['A','B','C','D'], columns=['W','X','Y','Z'])
df

# Representación por pantalla
print(df)

# Tipo de un df
type(df)

df

## trabajando con dataframes
df
df['X']
df.X

type(df['X'])
df[ ['W','Z'] ]
df

## añadir una columna
df
df['TOTAL'] = df['W'] + df['X'] + df['Y'] + df['Z']
df

df['add1'], df['add2'] = [1, 2, 3, 4], [5, 6, 7, 8]
df

aux_df = pd.DataFrame(data=[ [1, 2], [3, 4], [5, 6], [7, 8] ],
                      index=['A', 'B', 'C', 'D'], columns=['add1', 'add2'])
aux_df

df


df.drop(['add1'], axis=1, inplace=True)
df

df['extra'] = [1, 2, 3, 4]
df

## borrar una columna
new_df = df.drop('TOTAL', axis=1, inplace=False)
new_df

# No se modifica el df original
df

# A no ser que le indiquemos explícitamente
# df.drop('TOTAL', axis=1, inplace=True)
#
# df
#
# df.drop('TOTAL', axis=1)
# df

## borrar una fila
df.drop('C', axis=0)
df


df['add2']

## seleccionar filas
df
df.loc['C']

df
df.iloc[2]

## seleccionar subset
df
# Fila C y columna Z
df.loc['C','Z']
type(df.loc['C','Z'])
df.loc[ ['C'],['Z'] ]
type(df.loc[['C'],['Z']])

# Filas A,B y columnas W,Y
df.loc[ ['A','B'],['W','Y'] ]

## selección condicionada
df

df>0

# Valor de los registros >0
df[ df>0 ]

df
df['W']>0
# Valor de los registros cuando X>0
df[  df['W']>0  ]

df
# Valor de los registros en las columnas Y,Z si X>0
df[df['W']>0] [['Y', 'X']]

# Valor de los registros cuando X>0 o Z<0
df[(df['X']>0) | (df['Z'] < 0)]

# Valor de los registros en las columnas W e Y cuando X>0 o Z<0
df[(df['X']>0) | (df['Z'] < 0)] [['W','Y']]

## modificar indices
# Creamos de nuevo el dataframe
array = np.random.uniform(-10, 10, size=[4,4])
df = pd.DataFrame(array, index=['A','B','C','D'], columns=['W','X','Y','Z'])

df

# Añadimos una nueva Serie con el nombre de los índices
df['Códigos'] = ['AA','BB','CC','DD']

df

# Substituimos los índices de las filas
df.set_index('Códigos')
# No se guardan por defecto
df

# A no ser que lo especifiquemos explícitamente
df.set_index('Códigos', inplace=True)

df
print(df)

# consultamos una fila con el nuevo índice
df.loc['AA']

## indices por defecto
df

# Reiniciamos los índices y borramos los anteriores explícitamente
df.reset_index(drop=True, inplace=True)

df

