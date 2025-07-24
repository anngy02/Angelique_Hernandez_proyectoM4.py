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
