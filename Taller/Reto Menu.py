menu = [
    ['ID004', "entrada", "ensalada"],
    ['ID008', "entrada", "sopa de tomate"],
    ['ID005', "entrada", "sopa de cebolla"],
    ['ID011', "bebida", "Jugo de Fresa"],
    ['ID012', "bebida", "Limonada Natural"],
    ['ID102', "plato fuerte", "pasta"],
    ['ID106', "plato fuerte", "lassagna"],
]

# Filtrar elementos por tipo de plato
def filtrar_por_categoria(menu, categoria):
    return [item for item in menu if item[1] == categoria]

# Filtrar elementos por una subcadena
def filtrar_por_subcadena(menu, subcadena):
    return [item[2] for item in menu if subcadena.lower() in item[2].lower()]

# Diccionario agrupando por categoría
def agrupar_por_categoria(menu):
    categorias = {}
    for item in menu:
        tipo = item[1]
        nombre = item[2]
        if tipo not in categorias:
            categorias[tipo] = []
        categorias[tipo].append(nombre)
    return categorias

# Agregar un nuevo elemento al menú
def agregar_elemento(menu, id, categoria, nombre):
    menu.append([id, categoria, nombre])
    print(f"Elemento '{nombre}' agregado exitosamente al menú.")

# Imprimir el menú completo
def imprimir_menu(menu):
    print("\nMenú actual:")
    for item in menu:
        print(f"{item[0]} - {item[1].capitalize()} - {item[2]}")
    print()

# Menú interactivo
while True:

    print("""
    Ingrese la opción que desea realizar:
    1. Visualizar la información del menú
    2. Agregar nuevos elementos al menú
    3. Filtrar por una categoría
    4. Buscar por un nombre
    5. Visualizar nombres en categorías
    0. Salir
    """)
    opcion = input("Opción: ")
        
    if opcion == "1":
            imprimir_menu(menu)
    elif opcion == "2":
        id = input("Ingrese el ID del elemento: ")
        categoria = input("Ingrese la categoría (entrada, bebida, plato fuerte): ").lower()
        nombre = input("Ingrese el nombre del elemento: ")
        agregar_elemento(menu, id, categoria, nombre)
    elif opcion == "3":
        categoria = input("Ingrese la categoría a filtrar (entrada, bebida, plato fuerte): ").lower()
        filtrados = filtrar_por_categoria(menu, categoria)
        print(f"\nElementos en la categoría '{categoria}':")
        for item in filtrados:
            print(f"{item[0]} - {item[2]}")
    elif opcion == "4":
        subcadena = input("Ingrese la subcadena para buscar: ")
        resultados = filtrar_por_subcadena(menu, subcadena)
        print(f"\nResultados de la búsqueda por '{subcadena}': {resultados}")
    elif opcion == "5":
        categorias = agrupar_por_categoria(menu)
        print("\nMenú agrupado por categorías:")
        for categoria, nombres in categorias.items():
            print(f"{categoria.capitalize()}: {', '.join(nombres)}")
    elif opcion == "0":
        print("¡Gracias por usar el sistema de menú!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")