while True:
    print("Opciones:")
    print("1. Deportes de equipo")
    print("2. Deportes en solitario")
    print("3. Deportes extremos")
    print("4. Salir")

    # Solicitar al usuario que ingrese una opción
    opcion = input("Ingrese el número de opción que desea: ")

    # Procesar la opción seleccionada
    if opcion == "1":
        print("Ha seleccionado la Opción 1.")
    elif opcion == "2":
        print("Ha seleccionado la Opción 2.")
    elif opcion == "3":
        print("Ha seleccionado la Opción 3.")
    elif opcion == "4":
        print("Saliendo del programa ... ")
        break # Salir del ciclo while

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")