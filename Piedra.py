
import random  

print("Bienvenido al juego de Piedra, Papel o Tijera ")

nombre = input("Ingresa tu nombre: ")

puntaje_jugador = 0
puntaje_rival = 0

opciones = ["piedra", "papel", "tijera"]


while True:
    jugador = input("\nElige piedra, papel o tijera (o escribe 'salir' para terminar): ").lower()

    if jugador == "salir":
        break  

    if jugador not in opciones:
        print("Esto no es correcto, intentelo mas tarde")
        continue  

    Rival = random.choice(opciones)
    print(f"El rival eligio: {Rival}")

    if jugador == Rival:
        print("Empate")
    elif (jugador == "piedra" and Rival == "tijera") or \
         (jugador == "papel" and Rival== "piedra") or \
         (jugador == "tijera" and Rival == "papel"):
        print(f"Ganaste esta ronda bro, {nombre}")
        puntaje_jugador += 1
    else:
        print("El rival gana esta ronda.")
        puntaje_rival += 1

    print(f"\n Marcador: {nombre} {puntaje_jugador} - {puntaje_rival} Rival")


print("\n Juego terminado ")
print(f"Puntaje final: {nombre} {puntaje_jugador} - {puntaje_rival} Rival")

if puntaje_jugador > puntaje_rival:
    print(f"Felicidades {nombre}, ganaste el juego")
elif puntaje_jugador < puntaje_rival:
    print("El rival gano el juego")
else:
    print("El juego termino en empate")





