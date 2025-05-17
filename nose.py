def solicitar_dato(texto, es_numerico=False):
    while True:
        valor = input(texto).strip()
        if not valor:
            print("Este campo no puede estar vacío. Inténtalo de nuevo.")
            continue
        if es_numerico:
            try:
                return float(valor)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        else:
            return valor

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25.0 <= imc < 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc < 34.9:
        return "Obesidad grado I"
    elif 35.0 <= imc < 39.9:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III (mórbida)"

# Solicitar datos personales
nombre = solicitar_dato("Ingresa tu nombre: ")
apellido_paterno = solicitar_dato("Ingresa tu apellido paterno: ")
apellido_materno = solicitar_dato("Ingresa tu apellido materno: ")
edad = solicitar_dato("Ingresa tu edad: ", es_numerico=True)
peso = solicitar_dato("Ingresa tu peso en kg: ", es_numerico=True)
estatura = solicitar_dato("Ingresa tu estatura en metros: ", es_numerico=True)

# Calcular IMC
imc = peso / (estatura ** 2)
clasificacion = clasificar_imc(imc)

# Mostrar resultados
print("\n--- Datos del Usuario ---")
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {int(edad)} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC: {imc:.2f}")
print(f"Clasificación: {clasificacion}")
