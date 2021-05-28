import Ejercicio1 as Ej1

def repaso ():
    lista = ['brian', 'Serafin', 'ardila', 'serafin', 'ardila', 'serafin', 'ardila']
    Ej1.remover(lista)
    print(lista)
    Ej1.pop(lista)
    print(lista)
    Ej1.consultar(lista)
    print(lista)
    Ej1.insertar(lista)
    print(lista)

"""
Hacer un programa que contenga 7  elementos y luego se ingrese en la posición 4 un elemento nuevo
"""
def ejercicio1 ():
    lista = ['brian', 'Serafin', 'ardila', 'serafin', 'ardila', 'serafin', 'ardila']
    Ej1.insertar(lista)
    print(lista)

"""
Implemente una rutina  que dado un vector y un elemento a buscar dentro del vector me indique si se encuentra
 o no y en caso de encontrarse informe en qué posición esta.
"""
def ejercicio2 ():
    lista = ['brian', 'Serafin', 'ardila', 'serafin', 'ardila', 'serafin', 'ardila']
    valor = input("Ingrese el valor a consultar: ")
    if valor in lista:
        print(f"La posicion es: {lista.index(valor)}")

"""
Dado un vector de 10 posiciones, cree una rutina que  ingrese los números pares; es decir en la posición 
0 aparezca el número 2, en la posición 1 aparezca el número 4, y así sucesivamente.
"""
def ejercicio3 ():
    vector = []
    numllenado = 0
    for i in range(10):
        numllenado += 2
        vector.append(numllenado)
    print(vector)

def ejercicio4 ():
    lista = ['1', '2', '3', '4', '5', '6', '7']
    print(lista)
    
    lista.reverse()
    print(lista)
ejercicio4()
