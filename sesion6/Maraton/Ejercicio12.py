"""
Modifique el programa del COVID (determina Pico y Cédula), para incluira)No se sale los domingosb)Si tiene permiso de salida 
(excepción) podrásalir cualquier día, incluso los domingosGenerar un mensaje indicando si la persona puede o no salir el día especificado

Entrada

Salida 

Proceso

"""

cedula = int(input("Ingrese el numero del documento: "))
dia = int(input("Ingrese la fecha del dia: "))
nombre_dia = input("Ingrese el nombre del dia: ").lower()
permiso = input("Si tiene permiso escriba si o de lo contrario escriba no: ").lower()

if dia >= 1 and dia <= 31:
    if permiso == "no":
        if nombre_dia != "domingo":
            if cedula % 2 == 0 and dia % 2 == 0:
                print("Puede salir")
            elif cedula % 2 == 1 and dia % 2 == 1:
                print("Puede salir")
            else:
                print("No puede salir")
        else:
            print("No se sale los domingos")
    else:
        print("Tiene permiso de salida (excepción) podrá salir cualquier día, incluso los domingos")
else:
    print("ERROR: Datos no validos")
