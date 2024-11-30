#crear una funcion para solicitarle al usuario que ingrese el nombre 
#crear una funcion para solicitarle al usuario que ingrese el apellido 
#crear una funcion para solicitarle al usuario que ingrese la ciudad 

#crear un decorador para "limpiar la data" - elimine los espacios, returne lo que ingrese el usuario en mayuscula


def limpar_data(funcion):
    def wrapper(*args, ** kwargs):
        resultado = funcion(*args, ** kwargs) # Llamada a la funcion original

        resultado = resultado.strip()
        resultado = resultado.upper()
        return resultado
    return wrapper

@limpar_data
def get_nombre():
    nombre = input("Ingresa el tu nombre: ")
    return nombre

@limpar_data
def get_apellido():
    nombre = input("Ingresa el tu apellido: ")
    return nombre
@limpar_data
def get_ciudad():
    nombre = input("Ingresa el tu ciudad: ")
    return nombre
@limpar_data
def get_ID():
    id= input("Ingresa tu numero de identificacion: ")
    return id
@limpar_data
def get_pais():
    pais= input("Ingresa tu pais de residencia: ")
    return pais



nombre = get_nombre()
apellido = get_apellido()
ciudad = get_ciudad()
id = get_ID()
pais = get_pais()


print(f"Yo {nombre} {apellido} mayor de edad, con documento de identidad {id} de la cuidad de {ciudad}, de {pais} autorizo el tratamiento de informacion")

