"""
Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades, si la decisión setoma 
con base a la antigüedad en la empresa.Calcular el valor que un empleado recibe como reparto de utilidades.

Entrada
Tiempo
Valor
Salida 
Utilidad
Proceso

"""

tiempo = float(input("Ingrese la cantidad de años trabajados: "))
valor = float(input("Ingrese el valor con el cual se calculara las utilidades: "))

if tiempo < 1:
    print(f"la utilidad es del 5% {valor*0.05}")
elif tiempo < 2:
    print(f"la utilidad es del 7% {valor*0.07}")
elif tiempo < 5:
    print(f"la utilidad es del 10% {valor*0.1}")
elif tiempo <= 10:
    print(f"la utilidad es del 15% {valor*0.15}")
else:
    print(f"la utilidad es del 25% {valor*0.25}")