"""
Crea una aplicación para el siguiente juego. 
    a)  El programa de computador piensa un número
    b)  El concursante cuenta con un máximo de 5 intentos
    c)  Cada vez que el concursante indica un número, el programa le informa si: 
        i)  Gano
        ii) Es mayor que el que pensó
        iii)    Es menor que el que pensó
    d)  Si se agotan los turnos sin haber adivinado el número, el programa debe informar el número que había pensado

    a)  El programa piensa 81
    b)  En su primer turno el jugador indica 50, el programa informa MAYOR
        En su segundo turno el jugador indica 75, el programa informa MAYOR
        En su tercer turno el jugador indica 87, el programa informa MENOR
        En su cuarto turno el jugador indica 81, el programa informa GANO en 4 turnos
"""
import random
numeroPc = random.randint(1,100)
turnos = 0
print(numeroPc)
for i in range(5):
    turnos += 1
    numero = int(input("Indique el numero que piensa el computador: "))
    if numeroPc == numero:
        print(f"GANO en {turnos} turnos")
        break
    elif numeroPc < numero:
        print("MENOR")
    elif numeroPc > numero:
        print("MAYOR")
if i <= 4 and numeroPc != numero :
    print(f"Numero ganador: {numeroPc}")
