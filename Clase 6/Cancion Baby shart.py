cancion = """
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!

Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!

Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!

Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!

Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!

Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt!

Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away!

Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last!

It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end! 

"""
cancion_sin_comas = cancion.replace(",", "") #suprimir las comas (,)
cancion_limpia = cancion_sin_comas.replace("!", "") #suprimir los signos de admiracion (!)
palabras = cancion_limpia.split() #Genera una lista de palabras
total_palabras=len(palabras) #Cuenta la cantidad de elemento de la lista

contar_shark=palabras.count("shark") #Cuenta las veces que se repite la palabra
contar_doo = palabras.count("doo")#Cuenta las veces que se repite la palabra

print("Analizando la letra de la canción Baby Shark")
print()
print("1.) La canción tiene",total_palabras,"palabras")
print("2.) La palabra shark se repite",contar_shark,"veces")
print("3.) La palabra doo se repite",contar_doo,"veces")