usuario=input("Ingrese nombre del usuario: ")
horas_mes=int(input("Ingrese cantidad de horas en el gimnasio al mes: "))

if horas_mes<=15:
    print( )
    print(usuario, "estuvo en el gimnasio", horas_mes,"horas en el mes")
    print("Su suscripcion es: BRONCE, el valor por hora es de: $5.000")
    print("El valor a pagar es: $",horas_mes*5000)

elif horas_mes<=30:
    print( )
    print(usuario, "estuvo en el gimnasio", horas_mes,"horas en el mes")
    print("Su suscripcion es: PLATA, el valor por hora es de: $3.500")
    print("El valor a pagar es: $",horas_mes*3500)

else:
    print( )
    print(usuario, "estuvo en el gimnasio", horas_mes,"horas en el mes")
    print("Su suscripcion es: ORO, el valor por hora es de: $2.000")
    print("El valor a pagar es: $",horas_mes*2000)