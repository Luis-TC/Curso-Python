#Cargar modulo de python
import random
#Definir funcion tablero
def generar_tablero(filas, columnas, caracter_fondo, caracter_especial):
    # Lista dentro de otra lista
    tablero = [[caracter_fondo for _ in range(columnas)] for _ in range(filas)]
    
    # DEterminar la coordenada del caracter especial
    fila_aleatoria = random.randint(0, filas - 1) # Obtiene un numero de fila aleatorio
    columna_aleatoria = random.randint(0, columnas - 1) # Obtiene un numero de columna aleatorio
    tablero[fila_aleatoria][columna_aleatoria] = caracter_especial # Reemplaza el valor de 0 por 8 en la coordenada anterior

    return tablero


#Funcion imprimir tablero
def imprimir_tablero(tablero):
    for fila in tablero: # Imprime cada lista en un renglon aparte
        print(fila)


cont="S"
while cont=="S":
    print()
    print("Generador de tablero aleatorio")
    print("Opciones:")
    print ()
    print("1. Deseas generar un tablero predeterminado")
    print("2. Deseas generar un tablero perzonalizado")
    print("3. Salir")
    print()

    # Solicitar al usuario que ingrese una opción
    opcion = input("Ingrese el número de opción que desea: ")

    # Procesar la opción seleccionada

    if opcion == "1": #Se genera un tablero de 5x5 con caracteres (0 y 8)
        print()
        print("Tablero Predeterminado.")
        tablero = generar_tablero(5, 5, 0, 8)
        imprimir_tablero(tablero)
        print()
        cont=input("Nuevo tablero? S/N:") # Solicita al usuario si desea continua generando un nuevo tablero
        cont=cont.upper()
        if cont!="S": # Si la decision es NO o se ingresa otra letra distina a S, se detiene el programa
            print("Saliendo del programa ... ")
            

    elif opcion == "2": # Se genera un tablero perzonalizado (dimensiones y caracteres)

        print()
        print("Tablero Perzonalizado")
        filas = int(input("Ingrese el número de filas: "))
        columnas = int(input("Ingrese el número de columnas: "))
        caracter_fondo = input("Ingrese el caracter de fondo: ")
        caracter_especial = input("Ingrese el caracter a buscar: ")
        print ()
        tablero = generar_tablero(filas, columnas, caracter_fondo, caracter_especial)
        imprimir_tablero(tablero)
        print()
        cont=input("Nuevo tablero? S/N:") # Solicita al usuario si desea continua generando un nuevo tablero
        cont=cont.upper()
        if cont!="S": # Si la decision es NO o se ingresa otra letra distina a S, se detiene el programa
            print("Saliendo del programa ... ")
           

    elif opcion == "3":
        print("Saliendo del programa ... ")
        cont="x"
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")
