# Calcular la suma de la diagonal principal de una matriz cuadrada


def actividad1(longitud:int)->list:
    import random
    matriz = []
    for i in range(longitud):
        matriz.append([])
        for b in range(longitud):
            matriz[i].append(random.randint(1,9))
            print(f"|{matriz[i][b]}|", end=" ")
        print()
    print("\n")
    return matriz    

def sumardiagonal(matriz:list)->int:
    acomulador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                acomulador += matriz[i][j]
    print(f"Suma de matriz diagonal : {acomulador}")
    return acomulador


def sumardiagonalinvertida(matriz:list)->int:
    matriz.reverse()
    acomulador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                acomulador += matriz[i][j]
    print(f"Suma de matriz diagonal invertida : {acomulador}")
    return acomulador

def sumardiagonalinvertida2(matriz:list):
    acomulador = 0
    for i in range(len(matriz)):
        c = len(matriz[0])-i-1
        acomulador += matriz[i][c-1]
    print(f"Suma de matriz diagonal invertida : {acomulador}")
    return acomulador

def suma_x(matriz:list):
    longitud = len(matriz)
    matriz1 = sumardiagonal(matriz)
    matriz2 = sumardiagonalinvertida(matriz)
    suma = matriz1+matriz2
    if longitud%2 == 1:
        suma = -int(matriz[int(longitud/2)][int(longitud/2)])
    print(f"Suma de matriz en x: {suma}")

matriz = actividad1(2)
suma_x(matriz)
# sumardiagonal(matriz)
# sumardiagonalinvertida(matriz)
# sumardiagonalinvertida2(matriz)
