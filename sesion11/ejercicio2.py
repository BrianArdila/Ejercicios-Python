"""
Dado un vector de n posiciones, llenar el vector con números y luego imprimir los
elementos que se encuentran en las posiciones pares.
"""
def lista():
    import random
    lista = []
    longitud = int(input("Digite la longitud del vector: "))
    for i in range(longitud):
        lista.append(i)   
    print(lista) 
    print("-"*30)
    return lista

def pares(x):
    for i in range(len(x)):
        if x[i]%2 == 0:
            print(f"{x[i]} Es un numero par que pertenece a la lista")

pares(lista())



# Ejercicios para practicar
# https://www.w3schools.com/python/python_lists.asp
# https://www.tutorialspoint.com/python3_programming_examples/
# 