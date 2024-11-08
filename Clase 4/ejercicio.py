"""
Ejercicios:
1) Crea una lista con el nombre de 3 amigos, 
    - ordenala alfabeticamente
    - agrega un nombre adicional
    - imprime el nombre que esta en la ubicacion 2
    - ordena de fomra descendente

2) Define una tupla con los dias de la semana en minuscula empezando por el lunes
    - imprime el tercer dia en mayusculas
    - imprime el ultimo dia con la primera letra en mayuscula

3) Define una estructura para almacenar el himno nacional, que este por estrofas
    ejemplo:
    {
        "estrofa 1": '''Cesó la horrible noche 
                        La libertad sublime 
                        Derrama las auroras 
                        De su invencible luz. 
                        La humanidad entera, 
                        Que entre cadenas gime, 
                        Comprende las palabras 
                        Del que murió en la cruz ''',
        "estrofa 2": '''"Independencia" grita 
                        El mundo americano: 
                        Se baña en sangre de héroes 
                        La tierra de Colón. 
                        Pero este gran principio: "el rey no es soberano" 
                        Resuena, Y los que sufren 
                        Bendicen su pasión.  ''',

    }
    - imprimir la estrofa numero 10, 
    - imprimir el numero de estrofas,

    """
#1) Lista de nombres de 3 Amigos
amigos=["Andres","Pedro", "Julian"]
print("Amigos", amigos)

#Ordena Alfabeticamente
amigos.sort()
print("Orden alfabético", amigos)

#NOmbre adicional
amigos.append("Juan")
print("Amigo adicional", amigos)

#Nombre d ela ubicacion 2
print("El nombre de la ubicacion 2 es: ", amigos[2])

#Orden descendente
amigos.sort(reverse=True)
print("orden descendente",amigos)

#2. Tupla
dias_semana=("lunes","martes","miercoles","jueves","viernes","sabado","domingo")

#Tercer dia en mayusculas
print(f"Terce dia en mayusculas:", dias_semana[2].upper())

#El ultimo dia con la primera letra en mayuscula
print(f"El ultimo dia con la primera letra en mayuscula:", dias_semana[6].capitalize())

#3). Himno Nacional por estrofas

himno = {
        "Estrofa 1" : """Cesó la horrible noche 
        La libertad sublime 
        Derrama las auroras 
        De su invencible luz. 
        La humanidad entera, 
        Que entre cadenas gime, 
        Comprende las palabras 
        Del que murió en la cruz""",

        "Estrofa 2" : """"Independencia" grita 
        El mundo americano: 
        Se baña en sangre de héroes 
        La tierra de Colón. 
        Pero este gran principio: "el rey no es soberano" 
        Resuena, Y los que sufren 
        endicen su pasión.""",

        "Estrofa 3" : """"Del Orinoco el cauce 
        Se colma de despojos, 
        De sangre y llanto un río Se mira allí correr. 
        En Bárbula no saben 
        Las almas ni los ojos 
        Si admiración o espanto 
        Sentir o padecer.""",

        "Estrofa 4" : """"A orillas del Caribe 
        Hambriento un pueblo lucha Horrores prefiriendo 
        A pérfida salud. 
        Oh, sí de Cartagena 
        La abnegación es mucha, 
        Y escombros de la muerte 
        desprecian su virtud.""",

        "Estrofa 5" : """"De Boyacá en los campos 
        El genio de la gloria 
        Con cada espiga un héroe 
        invicto coronó. 
        Soldados sin coraza 
        Ganaron la victoria; 
        Su varonil aliento 
        De escudo les sirvió.""",

        "Estrofa 6" : """"Bolívar cruza el Ande 
        Que riega dos océanos 
        Espadas cual centellas 
        Fulguran en Junín. 
        Centauros indomables 
        Descienden a los llanos 
        Y empieza a presentirse 
        De la epopeya el fin.""", 

        "Estrofa 7" : """"La trompa victoriosa 
        Que en Ayacucho truena 
        En cada triunfo crece 
        Su formidable són. 
        En su expansivo empuje 
        La libertad se estrena, 
        Del cielo Americano 
        Formando un pabellón.""",

        "Estrofa 8" : """"La Virgen sus cabellos 
        Arranca en agonía 
        Y de su amor viuda 
        Los cuelga del ciprés. 
        Lamenta su esperanza 
        Que cubre losa fría; 
        Pero glorioso orgullo 
        circunda su alba tez.""",

        "Estrofa 9" : """"La Patria así se forma 
        Termópilas brotando; 
        Constelación de cíclopes Su noche iluminó; 
        La flor estremecida 
        Mortal el viento hallando 
        Debajo los laureles
        Seguridad buscó""",

        "Estrofa 10" : """"Mas no es completa gloria Vencer en la batalla, 
        Que al brazo que combate Lo anima la verdad. 
        La independencia sola 
        El gran clamor no acalla: 
        Si el sol alumbra a todos 
        Justicia es libertad.""",

        "Estrofa 11" : """"Del hombre los derechos 
        Nariño predicando, 
        El alma de la lucha 
        Profético enseñó. 
        Ricaurte en San Mateo 
        En átomos volando 
        "Deber antes que vida", 
        Con llamas escribió.""",

    }

#Estrofa numero 10
print("Estrofa #10", himno["Estrofa 10"])
#ó
print("Estrofa #10", himno.get("Estrofa 10"))

#Cantidad de estrofas
num_estrofas=len(himno)
print("Cantidad de estrofas:",num_estrofas)
#ó
print("Cantidad de estrofas:",len(himno.keys()))
