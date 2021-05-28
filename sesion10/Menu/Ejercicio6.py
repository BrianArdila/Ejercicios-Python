"""
Una tienda descuenta el 20%, si el valor total de la compra excede 1000000; proponga un programa
que indique el valor a pagar por un cliente, conocido el valor de la compra.
Calcular e indicar el valor a pagar
EJEMPLOS
 valor_compra = 500000, apagar = 500000
 valor_compra = 1000000, apagar = 1000000
 valor_compra = 1500000, apagar = 1200000
 valor_compra = -500, apagar = "ERROR: datos invalidos"

Entrada
valor de la compra

Salida
el valor a pagar

Proceso
valor de la compra * 0.8
"""
try:
    valor_compra = float(input("Ingrese el valor de la compra: "))

    if valor_compra > 1000000:
        print(f"El valor a pagar es de: {valor_compra*0.8}")
    elif valor_compra < 0:
        print("ERROR: datos invalidos")
    else:
        print(f"El valor a pagar es de: {valor_compra}")
except Exception:
    print("Los datos ingresados no son validos")