"""
Una granja avicola, está interesada en determinar que tipo de gallinas resulta mas productivo, 
se cuenta con gallinas tipo A y gallinas tipo B; para ello, lleva un registro de las posturas de cada 
tipo gallina durante el mes, si sabemos que hay N gallinas tipo A y M gallinas tipo B, y que adicionalmente no hay 
diferencia significativa entre el precio de mercado de los huevos. proponga una solución para la empresa.
"""
numgallinaA = 0
numgallinaB = 0
gallinaA = 0
gallinaB = 0
numdias = 30
while numdias > 0:
    print("-"*30)
    print("1. Gallina A")
    print("2. Gallina B")
    print("3 Salir")
    print("-"*30)
    opc = int(input("Seleccione el tipo de gallina: "))
    numdias -= 1
    huevos = int(input("Ingrese la cantidad de huevos puestos en el mes: "))
    if opc == 1:
        numgallinaA +=1
        gallinaA += huevos
    elif opc == 2:
        numgallinaB +=1
        gallinaB += huevos
    elif opc == 3:
        break
    else:
        print("Opción NO VALIDA")
promedioA = gallinaA/numgallinaA
promedioB = gallinaB/numgallinaB
if promedioA > promedioB:
    print("Las gallinas tipo A son mas productivas")
elif promedioB > promedioA:
    print("Las gallinas tipo B son mas productivas")
elif promedioA == promedioB:
    print("Las gallinas tipo A y tipo B son igual de productivas")
print(f"Huevos puestos por las gallinas A {gallinaA} y Huevos puestos por las gallinas B {gallinaB}")
print(f"Numeros de gallinas es {numgallinaB+numgallinaA}")
