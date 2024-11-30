import time

def medir_tiempo(funcion):
    def wrapper(*args, ** kwargs):
        inicio = time.time() # Momento en que se inicia la ejecución de la función
        resultado = funcion(*args, ** kwargs) # Llamada a la funcion original
        fin = time.time() # Momento en que se finaliza la ejecución de la función
        tiempo_transcurrido = fin - inicio
        return resultado, tiempo_transcurrido
    return wrapper

@medir_tiempo
def contesta_pregunta(pregunta):
    respuesta = input(pregunta)
    return respuesta

preguntas = [
    "Cuánto es 7 + 5? ",
    "¿Cuánto es 9 * 3? ",
    "¿Cuál es el planeta más cercano al Sol? ",
    "¿Cuántos sentidos tiene el ser humano? ",
    "¿Cuál es el continente más grande? ",
]

respuestas = []
tiempos = []
print("Encuesta")
for idx, pregunta in enumerate(preguntas):
    respuesta = contesta_pregunta(f"{idx+1}. {pregunta}")
    respuestas.append(respuesta[0])
    tiempos.append(respuesta[1])

print('\n### RESPUESTAS ###')
# imprimiendo las preguntas con sus respuestas
for i in range(len(preguntas)):
    print(f"{i+1} {preguntas[i]}")    
    print(f"Tu respuesta fue: {respuestas[i]}")    
    print(f"El tiempo invertido en la respuesta fue: {tiempos[i]:.2f}")
    print("")