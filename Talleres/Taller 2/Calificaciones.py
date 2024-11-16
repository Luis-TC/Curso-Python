estudiante=input("Ingrese el nombre del estudiante: ")
notas=[
float(input("Ingresa la calificación de la 1ra evaluación: ")),
float(input("Ingresa la calificación de la 2da evaluación: ")),
float(input("Ingresa la calificación de la 3ra evaluación: "))
]

prom=sum(notas)/len(notas)

if prom<=59:
    print()
    print("El Estudiante:",estudiante)
    print("Tiene un promedio de notas de:", round(prom,2))
    print("Su calificación Final es: INSUFICIENTE")

elif prom<=69:
    print()
    print("El Estudiante:",estudiante)
    print("Tiene un promedio de notas de:", round(prom,2))
    print("Su calificación Final es: BAJO")

elif prom<=79:
    print()
    print("El Estudiante:",estudiante)
    print("Tiene un promedio de notas de:", round(prom,2))
    print("Su calificación Final es: BÁSICO")

elif prom<=89:
    print()
    print("El Estudiante:",estudiante)
    print("Tiene un promedio de notas de:", round(prom,2))
    print("Su calificación Final es: ALTO")

else:
    print()
    print("El Estudiante:",estudiante)
    print("Tiene un promedio de notas de:", round(prom,2))
    print("Su calificación Final es: SUPERIOR")