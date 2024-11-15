## vocales
Texto =input("Ingrese el texto: ")
vocales = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U','á', 'é', 'í', 'ó', 'ú')
contador =0
for letra in Texto:
    if letra in vocales:
        contador = contador + 1
print('El texto tiene', contador, 'vocales')
