# parametros de referencia y valor
# cuando trabajamos con funciones existen parámetros de referencia y de valor
## tipos de datos mutables -> referencia
## tipos de datos inmutables -> valor

def saluda(mensaje, usuarios):
    mensaje = mensaje.upper()
    usuarios[0] = usuarios [0].upper()
    resultado = ' '
    for usuario in usuarios:
        resultado += f'{mensaje} {usuario} \n'
    return resultado

nombres = ['Jorge', 'Juan']
mensaje= 'Hola'

texto1 = saluda(mensaje, nombres)
print(texto1)
print(mensaje)
print(nombres)
