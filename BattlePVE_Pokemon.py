from random import randint

#Pokemon CPU

POKEMON_CPU = \
    {
    "PIKACHU":
        {
        "vida": 80,
        "ataques": {
            "1": {"nombre": "Impactrueno", "daño": 10},
            "2": {"nombre": "Bola Voltio", "daño": 14},
            "3": {"nombre": "Onda Trueno", "daño": 9},
            "4": {"nombre": "Rayo", "daño": 20}
            }
        }
    }

#Pokemon Entrenador

POKEMON_J = {
    "SQUIRTLE": {
        "vida": 90,
        "ataques": {
            "1": {"nombre": "Placaje", "daño": 10},
            "2": {"nombre": "Pistola Agua", "daño": 12},
            "3": {"nombre": "Burbuja", "daño": 9},
            "4": {"nombre": "Hidrobomba", "daño": 18},
        }
    },
    "CHARMANDER": {
        "vida": 75,
        "ataques": {
            "1": {"nombre": "Arañazo", "daño": 11},
            "2": {"nombre": "Lanzallamas", "daño": 21},
            "3": {"nombre": "Ascuas", "daño": 8},
            "4": {"nombre": "Fuego Fatuo", "daño": 14},
        }
    },
    "UMBREON": {
        "vida": 95,
        "ataques": {
            "1": {"nombre": "Ataque Rápido", "daño": 10},
            "2": {"nombre": "Puño Sombra", "daño": 25},
            "3": {"nombre": "Mordisco", "daño": 20},
            "4": {"nombre": "Látigo Cepa", "daño": 15},
    }
}

}

TAMANIO_BARRA = 50

pokemon_jugador = None
pokemon_disponibles = list(POKEMON_J.keys())  # Obtener los nombres de los Pokémon disponibles

# Mostrar las opciones
print("Elige tu Pokémon:")
for idx, pokemon in enumerate(pokemon_disponibles, 1):
    print(f"{idx}. {pokemon}")

# Validar la elección del jugador
while pokemon_jugador not in pokemon_disponibles:
    eleccion = input(f"Escribe el número de tu Pokémon (1-{len(pokemon_disponibles)}): ").strip()
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(pokemon_disponibles):
        pokemon_jugador = pokemon_disponibles[int(eleccion) - 1]
    else:
        print("Por favor, elige una opción válida.")

pokemon_cpu = "PIKACHU"

# Vida inicial de ambos Pokémon
vida_jugador = POKEMON_J[pokemon_jugador]["vida"]
vida_cpu = POKEMON_CPU[pokemon_cpu]["vida"]

#Combate
while vida_jugador > 0 and vida_cpu > 0:

    #Turno del rival (CPU)

    print(f"Turno del rival ({pokemon_cpu})")
    ataque_cpu = randint (1, 4)
    ataque_info = list(POKEMON_CPU[pokemon_cpu]["ataques"].values())[ataque_cpu - 1]
    print(f"{pokemon_cpu} ataca con {ataque_info["nombre"]}")
    vida_jugador = max(0, vida_jugador - ataque_info["daño"])

    barra_de_vida_jugador = int(vida_jugador * TAMANIO_BARRA / POKEMON_J[pokemon_jugador]["vida"])
    print(f"{pokemon_jugador}: [{'∎' * barra_de_vida_jugador}{' ' * (TAMANIO_BARRA - barra_de_vida_jugador)}] ({vida_jugador}/{POKEMON_J[pokemon_jugador]['vida']})")
    barra_de_vida_cpu = int(vida_cpu * TAMANIO_BARRA / POKEMON_CPU[pokemon_cpu]["vida"])
    print(f"{pokemon_cpu}: [{'∎' * barra_de_vida_cpu}{' ' * (TAMANIO_BARRA - barra_de_vida_cpu)}] ({vida_cpu}/{POKEMON_CPU[pokemon_cpu]['vida']})")

    input("Enter para continuar\n\n")

    #Turno del jugador

    print(f"Turno de {pokemon_jugador}")
    ataque_jugador = None
    while ataque_jugador not in POKEMON_J[pokemon_jugador]["ataques"]:
        ataque_jugador = input(
            f"¿Qué ataque deseas realizar?\n {[key + ' (' + POKEMON_J[pokemon_jugador]['ataques'][key]['nombre'] + ')' for key in POKEMON_J[pokemon_jugador]['ataques']]}: ").upper()
    ataque_info = POKEMON_J[pokemon_jugador]["ataques"][ataque_jugador]
    print(f"{pokemon_jugador} ataca con {ataque_info['nombre']}")
    vida_cpu = max(0, vida_cpu - ataque_info["daño"])

    # Mostrar barras de vida
    barra_de_vida_jugador = int(vida_jugador * TAMANIO_BARRA / POKEMON_J[pokemon_jugador]["vida"])
    print(
        f"{pokemon_jugador}: [{'∎' * barra_de_vida_jugador}{' ' * (TAMANIO_BARRA - barra_de_vida_jugador)}] ({vida_jugador}/{POKEMON_J[pokemon_jugador]['vida']})")
    barra_de_vida_cpu = int(vida_cpu * TAMANIO_BARRA / POKEMON_CPU[pokemon_cpu]["vida"])
    print(
        f"{pokemon_cpu}: [{'∎' * barra_de_vida_cpu}{' ' * (TAMANIO_BARRA - barra_de_vida_cpu)}] ({vida_cpu}/{POKEMON_CPU[pokemon_cpu]['vida']})")

    input("Enter para continuar\n\n")

#Resultado del combate

if vida_jugador > 0:
    print(f"{pokemon_jugador} gana el combate!")
else:
    print(f"{pokemon_cpu} gana el combate!")
