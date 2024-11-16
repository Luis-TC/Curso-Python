# Celsius a °F
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# Celsius a K
def celsius_a_kelvin(celsius):
    return celsius + 273.15

# Fahrenheit a °C
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
# Fahrenheit a K
def fahrenheit_a_kelvin(fahrenheit):
    return fahrenheit_a_celsius(fahrenheit) + 273.15

# Kelvin a °C
def kelvin_a_celsius(kelvin):
    return kelvin - 273.15
# Kelvin a °F
def kelvin_a_fahrenheit(kelvin):
    return celsius_a_fahrenheit(kelvin_a_celsius(kelvin))

# Opciones
def conversor_temperatura():
    print()
    print("Selecciona la conversión que desea realizar:")
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    print("3. Fahrenheit a Celsius")
    print("4. Fahrenheit a Kelvin")
    print("5. Kelvin a Celsius")
    print("6. Kelvin a Fahrenheit")
    print("7. Salir")
    print()

while True:
    conversor_temperatura()
    opcion = int(input("Ingrese la opción deseada: "))
    
    if opcion == 1:
        temperatura = float(input("Celsius a Fahrenheit\nIngrese la temperatura en °C: ")) 
        print(f"{temperatura} °C = {celsius_a_fahrenheit(temperatura):.2f} °F")
    elif opcion == 2:
        temperatura = float(input(f"Celsius a Kelvin\nIngrese la temperatura en °C: ")) 
        print(f"{temperatura} °C = {celsius_a_kelvin(temperatura):.2f} K")
    elif opcion == 3:
        temperatura = float(input("Fahrenheit a Celsius\nIngrese la temperatura en °F: ")) 
        print(f"{temperatura} °F = {fahrenheit_a_celsius(temperatura):.2f} °C")
    elif opcion == 4:
        temperatura = float(input("Fahrenheit a Kelvin\nIngrese la temperatura en °F: ")) 
        print(f"{temperatura} °F = {fahrenheit_a_kelvin(temperatura):.2f} K")
    elif opcion == 5:
        temperatura = float(input("Kelvin a Celsius\nIngrese la temperatura en K:")) 
        print(f"{temperatura} K = {kelvin_a_celsius(temperatura):.2f} °C")
    elif opcion == 6:
        temperatura = float(input("Kelvin a Fahrenheit\nIngrese la temperatura en K: ")) 
        print(f"{temperatura} K = {kelvin_a_fahrenheit(temperatura):.2f} °F")
    elif opcion == 7:
        print(f"Saliendo del programa ...")
        break
    else:
            print("Opción no válida. Por favor, ingrese un número válido.")
