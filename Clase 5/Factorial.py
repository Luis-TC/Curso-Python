# Factorial de un número
número = int(input("Ingresa un número: "))
números_lista=[]
for i in range(1,número+1):
     números_lista.append(i) 
print(números_lista)
producto= 1
for num in números_lista:
     producto= producto*num
print(f'El Factorial del numero',número, 'es',producto)
