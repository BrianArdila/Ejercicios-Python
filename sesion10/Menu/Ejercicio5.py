"""Una compañía de alquiler de automóviles cobra un valor fijo de $300000, por los primeros 3000 Km
de recorrido; La siguiente tabla indica los cobros adicionales que lo compañía aplica a sus clientes.
Calcular el total a pagar

EJEMPLOS
 ki = 100, kf = 500 ==> kr = 400, apagar = $300.000
 ki = 100, kf = 4300 ==> kr = 4200, apagar = $300.000 + (4200-3000)*150 = 480000
 ki = 1000, kf = 12000 ==> kr = 11000, apagar = 300000+(11000-10000)*200+(10000-3000)*150

Entrada
kminicial
kmfinal

Salida
total a pagar

Proceso
kminicial - kmfinal = kmrecorrido
valor a pagar = 300000 + (kmrecorrido - 300000)*adicional
"""
try:
    kmInicial = float(input("Ingrese la cantidad de kilometros que tiene el auto antes de alquilarlo: "))
    kmFinal = float(input("Ingrese la cantidad de kilometros que tiene el auto despues de alquilarlo: "))
    kmRecorrido = kmFinal - kmInicial 

    if kmRecorrido <= 3000:
        print(f"Sus kilometros recorridos fueron de {kmRecorrido} y el valor a pagar es de {300000}")
    elif kmRecorrido <= 10000:
        valorPagar = 300000 + (kmRecorrido - 3000) * 150
    else:
        valorPagar = 300000 + (kmRecorrido - 10000) * 200 + (10000-3000) * 150
    print(f"Sus kilometros recorridos fueron de {kmRecorrido} y el valor a pagar es de {valorPagar}")
except Exception:
    print("Los datos ingresados no son validos")