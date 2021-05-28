"""Ejercicio 1.
En un almacén se descuenta el 20% del valor a pagar, si el total de la compra excede $200.000.
Dado el valor que un cliente compró, determine el valor que debe pagar.
Calcular e imprimir el valor que un cliente debe pagar por su compra
EJEMPLOS
    Entradas           Salidas
valor_compra=200000, valor_pagar=200000
valor_compra=300000, valor_pagar=240000
valor_compra=50000, valor_pagar=50000
Proceso
valor_compra*0.8
"""
def ejercicio1():
    #Entradas 
    valor_compra = float(input("Ingrese el valor de la compra: "))
    #Proceso
    if valor_compra > 200000:
        valor_pagar = valor_compra * 0.8
        #Salida
        print(f"El valor a pagar es de: {valor_pagar}")
    else:
        #Salida
        print(f"El valor a pagar es de: {valor_compra}")


