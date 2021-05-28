
#append(x) inserta un valor al final de la lista
#insert(pos, elem) inserta un elemento en un punto especifico
#extend([e1, e2, e3]) agrega varios elementos a la lista
#index(x) indica donde esta el indice de un elemento
#in comprueba si un elemento se encuentra o no en la lita
#remove(x) remover el primer valor de la lista
#pop([x]) remueve el valor en la posicion x
#len(x) permite determinar el tamaño de la lista

"""
Actividad 2:  Escribamos un programa que nos permita crear una lista de 6 números aleatorios entre 1 y 20 
en Python, y creemos dos funciones que reciban la lista como parámetro de la siguiente forma:
•	mayor(x) - Una función que imprima el número mayor valor de una lista x
•	primos(x) - Una función que imprima los números de la lista que son números primos
"""
def lista():
    import random
    lista = []
    for i in range(6):
        lista.append(random.randint(1,20))   
    print(lista) 
    print("-"*30)
    return lista

def mayor(x):
    num = x[0]
    for i in range(len(x)):
        if x[i] > num:
            num = x[i]
    print(f"El numero mayor de la lista es: {num}")

def primos(x):
    for i in range(len(x)):
        if x[i]%2 == 1:
            print(f"{x[i]} Es un numero primo que pertenece a la lista")

mayor(lista())
primos(lista())