"""
Se desea diseñar un algoritmo que escriba los nombres de los días de la semana en función 
del valor de una variable DIA introducida por teclado. Los días de la semana son 7; 
por consiguiente, el rango de valores de DIA será 1..7.Indicar el nombre del día de la semana

Entrada
DIA
Salida 
nombre DIA
Proceso
"""

dia = int(input("Ingrese el numero que corresponde al dia de la semana: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("ERROR")

