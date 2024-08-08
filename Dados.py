import random

def lanzar_dado():
    return random.randint(1, 6)

def turno_jugador(nombre):
    puntaje_turno = 0
    while True:
        decision = input(f"{nombre}, ¿Quieres lanzar el dado? (s/n): ").lower()
        if decision == 's':
            dado = lanzar_dado()
            print(f"Lanzaste un {dado}")
            if dado == 1:
                print("¡Obtuviste un 1! Pierdes todos los puntos de este turno.")
                puntaje_turno = 0
                break
            else:
                puntaje_turno += dado
                print(f"Puntos actuales del turno: {puntaje_turno}")
        else:
            break
    return puntaje_turno

def main():
    puntaje_jugador1 = 0
    puntaje_jugador2 = 0
    meta = 100

    while puntaje_jugador1 < meta and puntaje_jugador2 < meta:
        print(f"\nTurno de Jugador 1 (Puntaje total: {puntaje_jugador1})")
        puntaje_jugador1 += turno_jugador("Jugador 1")
        print(f"Puntaje total de Jugador 1: {puntaje_jugador1}")
        if puntaje_jugador1 >= meta:
            print("¡Jugador 1 gana!")
            break

        print(f"\nTurno de Jugador 2 (Puntaje total: {puntaje_jugador2})")
        puntaje_jugador2 += turno_jugador("Jugador 2")
        print(f"Puntaje total de Jugador 2: {puntaje_jugador2}")
        if puntaje_jugador2 >= meta:
            print("¡Jugador 2 gana!")
            break

if __name__ == "__main__":
    main()
