# Diccionarios: Tarea 3

diccionario1 = {"nombre": "Carla", "edad": 22, "ciudad": "Querétaro"}

#1. pop()

edad = diccionario1.pop("edad")
print(f"pop:{edad}")
## el print es la edad que le puse a Carla, en este caso: 22

#2. get()
ciudad = diccionario1.get("ciudad")
print(f"get:{ciudad}")
## el print nos da la ciudad de Carla: Querétaro

#3. copy()
copia_diciconario = diccionario1.copy()
print(f"copy:{copia_diciconario}")
# el print nos da los siguientes datos del diciconario
# nombre: Carla y ciudad: Querétaro

#4. keys()
claves = diccionario1.keys()
print(f"keys:{claves}")
# el print nos dice que las keys son nombre y ciudad

#5. items ()
items = diccionario1.items()
print(f"items:{items}")
# el print nos dice que los prints son: nombre: carla, ciudad: querétaro

# 6. Clear()
diccionario1.clear()
print(f"clear:{diccionario1}")
# se limpió el diccionario

# Reiniciar el diccionario
diccionario1 = {"nombre": "Carla", "edad": 24, "ciudad": "Querétaro"}

# 7. fromkeys()

nuevas_claves = ["a", "b", "c"]

diccionario2 = dict.fromkeys(nuevas_claves, 0)
print(f"fromkeys: {diccionario2}")
# el print indica: a=0 , b=0, c=0

#8. popitem()
ultima_clave, ultimo_valor = diccionario1.popitem()
print(f"diciconario después del popitem: {diccionario1}")
# el print nos dice: nombre= Carla, edad = 24
## ups, me di cuenta que para el nuevo diccionario cambié la edad, de 22 a 24

#9. setdefault()
pais = diccionario1.setdefault("pais", "México")
print(f"setdefault: {pais}")
# el print es México
print(f"Diccionario después de setdefault:{diccionario1}")
# el print es: nombre= Carla, Edad= 24, país= México

#10. update()
diccionario1.update({"edad": 26, "ciudad": "Juriquilla"})
print(f"update:{diccionario1}")
# el print dice: nombre= Carla, edad= 26, país= México, ciudad= Juriquilla

#11. values()
valores=diccionario1.values()
print(f"values: {valores}")
# el print nos da los valores del diccionario: Carla, 26, México, Juriquilla

