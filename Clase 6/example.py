def generar_tablero(filas=5, columnas=5, caracter_fondo='0', caracter_buscar='8'):

    # Crear un tablero lleno con el caracter de fondo
    tablero = [[caracter_fondo for _ in range(columnas)] for _ in range(filas)]

    print(tablero)

generar_tablero()


#def generar_tablero(filas=5, columnas=5, caracter_fondo='0', caracter_buscar='8'):
    # Crear un tablero lleno con el caracter de fondo
    #tablero = [[caracter_fondo for _ in range(columnas)] for _ in range(filas)]

    # Imprimir el tablero (como lista de listas)
    #print(tablero)

# Ejemplo de uso
#generar_tablero()
