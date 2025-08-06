import requests
import json
import os

def obtener_datos_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        info_pokemon = {
            "peso": datos["weight"],
            "altura": datos["height"],
            "tipos": [tipo["type"]["name"] for tipo in datos["types"]],
            "habilidades": [habilidad["ability"]["name"] for habilidad in datos["abilities"]],
            "movimientos": [movimiento["move"]["name"] for movimiento in datos["moves"]],
            "imagen": datos["sprites"]["front_default"]
        }
        return info_pokemon
    else:
        return None


def mostrar_datos_pokemon(datos):
    print(f"Peso: {datos['peso']}")
    print(f"Altura: {datos['altura']}")
    print(f"Tipos: {', '.join(datos['tipos'])}")
    print(f"Habilidades: {', '.join(datos['habilidades'])}")
    print(f"Movimientos: {', '.join(datos['movimientos'][:5])}...") 
    print(f"Imagen: {datos['imagen']}")

def main():
    nombre_pokemon = input("Ingresa el nombre de un Pokémon: ")
    datos = obtener_datos_pokemon(nombre_pokemon)
    
    if datos:
        mostrar_datos_pokemon(datos)
        
    else:
        print("Pokémon no encontrado, verifique el nombre e intente de nuevo.")

if __name__ == "__main__":
    main()