def ejemplo2():
    a = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ") # end = " " imprime en una sola linea las cosas 
        print()
# ejemplo2()


#Actividad 1
#
#Vamos a escribir una funcion que llene una matriz de 5 filas y 10 columnas con números enteros entre 1 y 100
#aleatorios, imprima los valores máximo y mínimo y sus posiciones dentro de la matriz.

def actividad1():
    import random
    matriz = []
    for i in range(5):
        matriz.append([])
        for b in range(10):
            matriz[i].append(random.randint(1,100))
            print(f"|{matriz[i][b]}|", end=" ")
        print("|")
    print("\n")    
    print(max(max(matriz)))
    print(min(min(matriz)))
# actividad1()


def actividad3():
    import random
    matriz = []
    for i in range(5):
        fila = [0]*10
        matriz.append(fila)
    for i in range(5):
        for b in range(10):
            matriz[i][b] = random.randint(1,100)
            print(f"|{matriz[i][b]}|", end=" ")
        print("|")
# actividad3()



#Actividad 2
#
#El producto escalar de un número real, x , y una matriz A es la matriz xA. 
#Cada elemento de la matriz xA es x veces su elemento correspondiente en A.
#
#Diseñemos una funcion escalar(matriz, escalar) que dada matriz[n][m] y un escalar, 
#imprima el producto escalar de la matriz.

