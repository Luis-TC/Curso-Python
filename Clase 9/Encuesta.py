"""crear un programa de preguntas abiertas, que el usuiario debe contestar
se debe definir una estructura (lista o diccionario) para visualizar las preguntas
y deben visualizar al finalizar el programa 

las preguntas son:
- que opina del alcalde de bucaramanga
- cual es la mejor gestion que considera que se ha desarrollado en el gov
- cual es la calle mas transitada en la ciudad 

al finalizar el programa debe mostrar las respuestas y el tiempo que el usario demoro el contestar"""



import time

# Decorador para medir el tiempo de ejecución de una función
def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()  # Momento en que se inicia la ejecución de la función
        resultado = funcion(*args, **kwargs)  # Llamada a la función original
        fin = time.time()  # Momento en que se finaliza la ejecución de la función
        tiempo_transcurrido = fin - inicio
        print(f"\nLa respuesta de la encuesta  {funcion.__name__} tardó {tiempo_transcurrido} segundos en ejecutarse.")
        return resultado
    return wrapper

preguntas = {
    1: "¿Qué opina de la alcaldía de Bucaramanga?",
    2: "¿Cuál es la mejor gestión que considera que se ha desarrollado en el gobierno?",
    3: "¿Cuál es la calle más transitada en la ciudad?",
    4: "¿Qué opina de la seguridad de la ciudad?"
}

respuestas = {}

@medir_tiempo
def encuesta():
    for num, pregunta in preguntas.items():
        respuesta = input(f"{pregunta}\n")
        respuestas[num] = respuesta

encuesta()

print("\nGracias por responder. Aquí están sus respuestas:\n")
for num, respuesta in respuestas.items():
    print(f"{preguntas[num]}: {respuesta}")