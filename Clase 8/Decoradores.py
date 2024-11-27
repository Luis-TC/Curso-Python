def manejador_errores(funcion):
    def wrapper(*args, **kwargs):
        try:
            resultado = funcion(*args, **kwargs) # Llamada a la funcion original
        except:
            resultado = "Hubo un error"
        return resultado
    return wrapper


## caso de errores
@manejador_errores
def division(a, b):
    return a / b

@manejador_errores
def sumar(a, b):
    return a + b

@manejador_errores
def restar(a, b):
    return a - b

@manejador_errores
def multiplicar(a, b, c):
    return a * b * c
E= [1,2,3]

resultado = multiplicar(2, 4, 2)
print(resultado)

resultado = multiplicar(2, None, None)
print(resultado)
