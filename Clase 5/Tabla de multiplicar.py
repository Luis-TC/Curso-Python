# Tabla múltiplicar
número_multiplicar= int(input("ingrese número de cual desea ver la tabla de múltiplicar:"))
for número in range(0,11):
    resultado= número_multiplicar*número
    print(f'{número_multiplicar} * {número} = {resultado}')
