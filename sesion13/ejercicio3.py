
def suma_matriz_rectangular (matriz):
    sumFilas = []
    sumColum = []
    for i in range(len(matriz)):   
        suma = 0    
        # suma2 = 0
        for b in range(len(matriz[i])):
            suma += matriz[i][b]
            # suma2 += matriz[b][i]
        sumFilas.append(suma)
        # sumColum.append(suma2)
    
    
    for i in range(len(matriz[0])):   
        suma2 = 0
        for b in range(len(matriz)):
            suma2 += matriz[b][i]
        sumColum.append(suma2)

    print(sumFilas)
    print(sumColum)


def suma_matriz_cuadrada (matriz):
    sumFilas = []
    sumColum = []
    if len(matriz) == len(matriz[0]):
        for i in range(len(matriz)):   
            suma = 0    
            suma2 = 0
            for b in range(len(matriz[i])):
                suma += matriz[i][b]
                suma2 += matriz[b][i]
            sumFilas.append(suma)
            sumColum.append(suma2)
    print(sumFilas)
    print(sumColum)


def actividad1():
    import random
    matriz = []
    for i in range(2):
        matriz.append([])
        for b in range(2):
            matriz[i].append(random.randint(1,10))
            print(f"|{matriz[i][b]}|", end=" ")
        print("|")
    print("\n") 
    suma_matriz_cuadrada(matriz) 
actividad1()
