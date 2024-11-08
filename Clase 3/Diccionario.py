persona={
    "nombre": "Juan",
    "apellido": "Diaz",
    "edad": 28,
    "cuidad": "New York",
    "mascotas": ["Mimi", "Firulasi"]
}
mensaje="""
Hola mi nombre es {0} {1}
tengo {2} de edad,
vivo en la cuidad de {3}
tengo {4} mascotas,
sus mobre son: {5} y {6}
""".format("juan","diaz",25,"NY",2,"aa","bb")

print(mensaje)

#Con valores del diccionario

mensaje = """
Hola mi nombre es {0} {1}
tengo {2} de edad, 
vivo en la ciudad de {3}
tengo {4} mascotas, 
sus nombre son {5} y {6}
""".format(
    persona.get('nombre'),
    persona.get('apellido'),
    persona.get('edad'),
    persona.get('ciudad'),
    len(persona.get('mascotas')),
    persona.get('mascotas')[0],
    persona.get('mascotas')[1],
)

print(mensaje)