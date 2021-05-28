"""
Se requiere determinar, suministrado un mes (número de mes), cuantos días tiene ese mes.
Indicar la cantidad de días del mes especificado
EJEMPLOS
Entrada    Salida
mes = 1, Salida = 31
mes = 2, Salida = 28
mes = 15, Salida = Mes no valido
mes = enero, Salida = Mes no valido
Proceso
mes                 Dias
2                   28
1,3,5,7,8,10,12     31
4,6,8,11            30
"""
try:
    mes = int(input("Suministre un mes en número: "))

    if mes == 2:
        print("Tiene: 28 o 29 Dias")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        print("Tiene: 30 Dias")
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        print("Tiene: 31 Dias")
    else:
        print("Mes no valido")
except Exception:
    print("Mes no valido")