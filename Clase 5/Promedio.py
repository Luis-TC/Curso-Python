# Promedio de números
cantidad_números= int(input("¿Cuántos números deseas ingresar? "))
números=[]
for _ in range(cantidad_números):
    número = int(input("Ingresa un número: "))
    números.append(número)

print("Números ingresados:", números)
suma_total= sum(números)
promedio = float(suma_total/ len(números))
print("la suma de los números ingresados es:", suma_total)
print('el promedio es:',suma_total,'/',len(números),'=',promedio)
