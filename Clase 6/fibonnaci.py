numero=int(input("ingrese un numero: "))

anterior=0
nuevo=1
resultado=None

contador=0

while contador < numero:
    contador=contador+1
    resultado=anterior+nuevo
    print(f"{contador}.{anterior}+{nuevo}={resultado}")

    anterior=nuevo
    nuevo=resultado
