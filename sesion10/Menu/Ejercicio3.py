"""
En una frutera, se ofrece un descuento por volumen a la compra del kilo de manzanas, de acuerdo
a la siguiente tabla.
Dado el precio por kilo y la cantidad de kilos comprados, determine cuánto pagará un cliente por su
compra.
Determinar el valor a pagar por un cliente en una compra.
Entrada 
el precio por kilo y la cantidad de kilos comprados
Salida
el valor a pagar
Proceso
precio * descuento
"""
try:
    precioKilo = float(input("ingrese el precio del kilo: "))
    kilos = float(input("Cantidad de kilos comprados: "))
    if kilos >= 0.00:
        print(f"El valor a pagar es: {precioKilo} ")
    elif kilos >= 2.00:
        print(f"El valor a pagar es: {precioKilo*0.9} ")
    elif kilos >= 5.00:
        print(f"El valor a pagar es: {precioKilo*0.85} ")
    elif kilos >= 10.00:
        print(f"El valor a pagar es: {precioKilo*0.8} ")
except Exception:
    print("Los datos ingresados no son validos")