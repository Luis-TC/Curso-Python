while True:
    print("")
    print("Opciones:")
    print("1. Servicio Clinico de Mascotas")
    print("2. Guarderia de Mascotas")
    print("3. Adopciones de Mascotas")
    print("4. Baño y Peluqueria")
    print("5. Salir")

    opcion = input("Ingrese el número de opción que desea: ")

    if opcion == "1":
        print("Ha seleccionado Servicio Clinico de Mascotas.")
    elif opcion == "2":
        print("Ha seleccionado Guarderia de Mascotas.")
    elif opcion == "3":
        print("Ha seleccionado Adopciones de Mascotas.")
    elif opcion == "4":
        print("Ha seleccionado Baño y Peluqueria.")        
    elif opcion == "5":  
        print("Saliendo del programa ... ")
        break