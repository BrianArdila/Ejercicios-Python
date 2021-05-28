from operator import length_hint


def llenar(dato):
    nombres = []
    for i in range(dato):
        nombre = input("Ingrese un nombre: ")
        nombres.append(nombre)
    return nombres

def remover (lista):
    nombre = input("Ingrese el nombre a remover: ")
    lista.remove(nombre)
    return lista

def pop (lista):
    posicion = int(input("Ingrese la posoición a remover: "))
    lista.pop(posicion)
    return lista

def consultar (lista):
    valor = input("Ingrese el valor a consultar: ")
    if valor in lista:
        print(lista.index(valor))
    return lista

def insertar (lista):
    posicion = int(input("Ingrese la posición: "))
    nombre = input("Ingrese un nombre: ")
    if len(lista) >= posicion:
        lista.insert(posicion,nombre)
    else:
        return print("La posición se encuentra fuera del rango")
    return lista
