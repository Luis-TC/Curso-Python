#Cargar modulo de python
import random

#Opciones validas
opciones = ["piedra","arma","luz","demonio","dragon","agua","aire","papel","esponja","lobo","arbol","humano","serpiente","tijera","fuego"]

#Reglas para ganar
reglas = {
    "piedra": ["fuego","tijera","serpiente","humano","arbol","lobo","esponja"],
    "papel": ["aire","agua","dragon","demonio","luz","arma","piedra"],
    "tijera": ["serpiente","humano","arbol","lobo","esponja","papel","aire"],
    "agua": ["dragon","demonio","luz","arma","piedra","fuego","tijera"],
    "aire": ["agua","dragon","demonio","luz","arma","piedra","fuego"],
    "esponja": ["papel","aire","agua","dragon","demonio","luz","arma"],
    "fuego": ["tijera","serpiente","humano","arbol","lobo","esponja","papel"],
    "arma": ["piedra","fuego", "tijera", "serpiente","humano","arbol", "lobo"],
    "luz": ["arma","piedra","fuego","tijera","serpiente","humano","arbol"],
    "demonio": ["luz","arma","piedra","fuego","tijera","serpiente","humano"],
    "dragon": ["demino","luz","arma","piedra","fuego","tijera","serpiente"],
    "lobo": ["esponja","papel","aire","agua","dragon","demonio","luz"],
    "arbol": ["lobo","esponja","papel","aire","agua","dragon","demonio"],
    "humano": ["arbol","lobo","esponja","papel","aire","agua","dragon"],
    "serpiente": ["hunamo","arbol","lobo","esponja","papel","aire","agua"]
    }

#Definir funcion Respuesta de la Computadora
def Rta_Computadora():
    rta_C = random.choice(opciones) # Eleccion aleatoria
    print("Computadora:",rta_C)
    return rta_C

#Definir funcion Respuesta del usuario
def Rta_Usuario():
    rta_U = input(f"Qué escoges? ({', '.join(opciones)}): ").strip().lower()
    #Valida la respuesta, solo recibe alguna de la anteriores opciones
    while rta_U not in opciones:
        rta_U = input(f"Digita una respuesta correcta ({', '.join(opciones)}): ").strip().lower()
    print("\nTu respuesta:",rta_U)
    return rta_U

#Definir funcion ganador
def ganador(rta_U, rta_C):
    if rta_C==rta_U:
        resultado="Empate"
        print("Resultado:", resultado)
    elif rta_C in reglas[rta_U]:
        resultado="Ganaste"
        print("Resultado:", resultado)
    else:
        resultado="Perdiste"
        print("Resultado:", resultado)
    
    return resultado
    

puntos_usuario = 0
puntos_computadora = 0

#Menu imprimible inicial
while True:

    print("\nJuego 7 Elementos")
    print("Opciones:")
    print("1. Jugar")
    print("2. Limpiar marcador")
    print("3. Salir")

    # Solicitar al usuario que ingrese una opción
    opcion = input("Selecciona una opción: ")

    # Procesar la opción seleccionada
    if opcion == "1": #Pregunta respuesta de usuario e imprime respuestas

        rta_U=Rta_Usuario()
        rta_C=Rta_Computadora()
        resultado=ganador(rta_U, rta_C)
        #contadores para el marcador
        if resultado == "Ganaste":
            puntos_usuario = puntos_usuario + 1
        elif resultado == "Perdiste":
            puntos_computadora= puntos_computadora + 1
        
        # Mostrar marcador
        print("\nMarcador:")
        print(f"Tú: {puntos_usuario}")
        print(f"Computadora: {puntos_computadora}")

    elif opcion == "2":
        print("\n --Marcador limpiado--")
        puntos_usuario = 0
        puntos_computadora = 0
                # Mostrar marcador
        print("Marcador:")
        print(f"Tú: {puntos_usuario}")
        print(f"Computadora: {puntos_computadora}")

    elif opcion == "3":
        print("Saliendo del programa ... ")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")