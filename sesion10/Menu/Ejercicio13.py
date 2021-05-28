"""
Como parte de las medidas preventivas para disminuir la tasa de contagio del COVID, se implementó unamedidaconocida como 
Pico y Cédula, en dicha medida se restringe la circulación de las personas de forma tal que pueden salir siempre y cuando la 
paridad del documento de identidad coincida con la paridad del día.
Proponga una solución informática que permita determinar si una persona puede o no salir en un día específico.

Entrada
cedula
fecha
Salida 
accion
Proceso

"""
cedula = int(input("Ingrese el numero del documento: "))
dia = int(input("Ingrese la fecha del dia: "))
if dia >= 1 and dia <= 31:
    if cedula % 2 == 0 and dia % 2 == 0:
        print("Puede salir.")
    elif cedula % 2 == 1 and dia % 2 == 1:
        print("Puede salir.")
    else:
        print("No puede salir")
else:
    print("ERROR: Datos no validos")

print("==========================================================")

# Una forma de hacerlo sin que consuma mas recursos 
if dia >= 1 and dia <= 31:
    if cedula[-1] % 2 == 0 and dia % 2 == 0:
        print("Puede salir")
    elif cedula[-1] % 2 == 1 and dia % 2 == 1:
        print("Puede salir")
    else:
        print("No puede salir")
else:
    print("ERROR: Datos no validos")

