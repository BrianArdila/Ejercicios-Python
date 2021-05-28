"""
Se dispone de un termómetro para medir con exactitud la temperatura en un determinado lugar.
Sin embargo, les basta con saber de manera aproximada si la temperatura se ajusta a los rangos
siguientes:

Lea el valor temperatura y devuelva la sensación térmica correspondiente

EJEMPLOS

Indicar la sensación térmica

Entrada
valor temperatura
Salida 
sensación térmica
""" 

valor_temperatura = float(input("Ingrese el valor de la temperatura: "))

if valor_temperatura >= -10 and valor_temperatura < 10:
    print("Mucho Frio")
elif valor_temperatura < 15:
    print("Poco Frio")
elif valor_temperatura < 25:
    print("Temperatura Normal")
elif valor_temperatura < 30:
    print("Poco Calor")
elif valor_temperatura < 45:
    print("Mucho Calor")
else:
    print("Temperatura fuera de rango")