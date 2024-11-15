while True:
    print("")
    print("Opciones:")
    print("1. Recetas Sin Gluten")
    print("2. Recetas Dulces")
    print("3. Recetas Saladas")
    print("4. Recetas Proteicas")
    print("5. Salir")

    opcion = input("Ingrese el número de opción que desea: ")

    if opcion == "1":
        print("Ha seleccionado Recetas Sin Gluten.")
    elif opcion == "2":
        print("Ha seleccionado Recetas Dulces.")
    elif opcion == "3":
        print("Ha seleccionado Recetas Saladas.")
    elif opcion == "4":
        print("Ha seleccionado Recetas Proteicas.")        
    elif opcion == "5":
        print("Saliendo del programa ... ")
        break