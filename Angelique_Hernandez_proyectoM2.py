# Longitud de una frase

palabra1= input ("ingrese una palabra: ")
longitud= len(palabra1)

if 4 <= longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:
    print(f"Sobran letras. Tiene {longitud} letras.")


palabra2= input ("ingrese una palabra: ")
longitud= len(palabra2)

if 4 <= longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:
    print(f"Sobran letras. Tiene {longitud} letras.")


palabra3= input ("ingrese una palabra: ")
longitud= len(palabra3)

if 4 <= longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:
    print(f"Sobran letras. Tiene {longitud} letras.")

# Encuentra el cuadrante

try:
    x = int(input("Ingrese el valor de X:"))
    y = int(input("Ingrese el valor de Y:"))

    if x == 0 or y == 0:
        print("Las coordenadas no deben ser cero")

    elif x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I")

    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II")

    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III")

    else:
        print("El punto se encuentra en el cuadrante IV")
        
except ValueError:
    print("Ingresar valores numéricos válidos") 