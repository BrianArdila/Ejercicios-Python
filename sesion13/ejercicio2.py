
def mayor(matriz):
    mayor = 0
    for i in range(5):
        for b in range(10):
            if matriz[i][b]>mayor:
                mayor = matriz[i][b]
    print(mayor)

def menor(matriz):
    menor = 999999999
    for i in range(5):
        for b in range(10):
            if matriz[i][b]<menor:
                menor = matriz[i][b]
    print(menor)

def actividad2():
    import random
    matriz = []
    for i in range(5):
        fila = [0]*10
        matriz.append(fila)
        for b in range(10):
            matriz[i][b] = random.randint(1,100)
            print(f"|{matriz[i][b]}|", end=" ")
        print("|")
    mayor(matriz)
    menor(matriz)
    print("|"*30)
    print(max(max(matriz))) # primero busca el vector mayor y dentro de ese vector saca el numero mayor 
                            # pero no corresponde al mayor de toda la matriz
    print(min(min(matriz))) # primero busca el vector menor y dentro de ese vector saca el numero menor 
                            # pero no corresponde al menor de toda la matriz
actividad2()