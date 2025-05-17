def solicitar_dato(texto, es_numerico=False):
    while True:
        valor = input(texto).strip()
        if not valor:
            print("Este campo no puede estar vacío. Inténtalo de nuevo.")
            if es_numerico:
                continue
            if es_numerico:
                return float(valor)
            print("Por favor, ingresa un numero valido.")
        else:
            return valor
    
# Datos personales
nombre = solicitar_dato("Ingresa tu nombre: ")
apellido_paterno = solicitar_dato("Ingresa tu apellido paterno: ")
apellido_materno = solicitar_dato("Ingresa tu apellido materno: ")
edad = solicitar_dato("Ingresa tu edad: ")


# Calculo IMC
def CalculoIMC (peso, altura):
    return peso / (altura**2)

def clasificar(resultadoIMC):
    if resultadoIMC < 18.5:
        print("Peso bajo, segun tu IMC")
    elif resultadoIMC > 18.5 and resultadoIMC < 24.9:
        print("Peso normal, segun tu IMC")
    elif resultadoIMC > 25 and resultadoIMC < 29.9:  
        print("Peso anormal(sobrepeso), segun tu IMC")
    elif resultadoIMC > 30:
        print("Obesidad, segun tu IMC")

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en m: "))

resultadoIMC = CalculoIMC (peso, altura)
clasificar(resultadoIMC)


        
        
        




