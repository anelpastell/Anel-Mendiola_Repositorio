# Operadores lógicos

temperatura = int(input(" ¿Cuál es la temperatura afuera? "))

if temperatura >= 0 and temperatura <= 30:
    print("La temperatura está bien hoy !!! ")
elif temperatura < 0 or temperatura >30:
    print("La temperatura no es tan buena hoy :(( ")
# con el operador OR podemos verificar otro tipo de rangos de datos

# OPERADOR NOT
## si la declaración es verdadera la podemos hacer falsa
## si la declaración es falsa, la podemos hacer verdadera

if not (temperatura >= 0 and temperatura <= 30):
    print("La temperatura no es tan buena hoy :(( ")
elif not (temperatura < 0 or temperatura >30):  # false -> con el not, se vuelve verdadero
    print("La temperatura está bien hoy!!")
