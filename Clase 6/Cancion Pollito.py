cancion = """
En la radio, hay un pollito
En la radio, hay un pollito
El pollito pío, el pollito pío
El pollito pío, el pollito pío
El pollito pío, el pollito pío

En la radio, hay una gallina
En la radio, hay una gallina
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay también un gallo
En la radio, hay también un gallo
Y el gallo corococo, y la gallina coo
Y el pollito pío, el pollito pío
El pollito pío, el pollito pío

En la radio, hay un pavo
En la radio, hay un pavo
Y el pavo glugluglu, y el gallo corococo
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay una paloma
En la radio, hay una paloma
Y la paloma ruuu, el pavo glugluglu
El gallo corococo, y la gallina coo
El pollito pío, el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay también un gato
En la radio, hay también un gato
Y el gato miao, la paloma ruuu
El pavo glugluglu, el gallo corococo
Y la gallina coo, y el pollito pío
El pollito pío, y el pollito pío

En la radio, hay también un perro
En la radio, hay también un perro
Y el perro guau guau, el gato miao
La paloma ruu, el pavo glugluglu
El gallo cocoroco, y la gallina coo
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay una cabra
En la radio, hay una cabra
Y la cabra mee, el perro guau guau
El gato miao, y la paloma ruu
El pavo glugluglu, el gallo cocoroco
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay un cordero
En la radio, hay un cordero
Y el cordero bee, y la cabra mee
El perro guau guau, el gato miao
La paloma ruu, el pavo glugluglu
El gallo cocoroco, y la gallina coo
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay una vaca
En la radio, hay una vaca
Y la vaca moo, y el cordero bee
Y la cabra mee, el perro guau guau
El gato miao, y la paloma ruu
El pavo glugluglu, el gallo cocoroco
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay también un toro
En la radio, hay también un toro
Y el toro muu, y la vaca moo
Y el cordero bee, y la cabra mee
El perro guau guau, el gato miao
La paloma ruu, el pavo glugluglu
El gallo cocoroco, y la gallina coo
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay un tractor
En la radio, hay un tractor
Y el tractor brum, y el tractor brum
Y el tractor brum y el pollito oh-oh
"""
cancion_limpia=cancion.replace(",","") #suprimir las comas (,)
palabras = cancion_limpia.split() #Genera una lista con cada cadena de caracteres
total_palabras=len(palabras) #Cuenta la cantidad de elemento de la lista

contar_pio=palabras.count("pío") #Cuenta las veces que se repite la palabra
contar_pollito = palabras.count("pollito") #Cuenta las veces que se repite la palabra

print("Analizando la letra de la canción El pollito pio")
print()
print("1.) La canción tiene",total_palabras,"palabras")
print("2.) La palabra pío se repite",contar_pio,"veces")
print("3.) La palabra pollito se repite",contar_pollito,"veces")
