# Juan y María están haciendo un programa para jugar a los dados con las siguientes reglas:


# Si sale 1, vuelven a lanzar.

# Si sale 6, quedan empatados.

# Si sale 2 o 3 gana Juan.

# Si sale 4 o 5 gana María.

# Escribe el programa en Python para escribir el mensaje según el resultado de lanzar el dado.

# import random


# numero = random.randint(1,6)

# if numero == 1:

#     print("vuelven a lanzar")

# elif numero == 6:

#     print("quedan empatados")

# elif numero == 2 or numero == 3:

#     print("gana Juan")

# elif numero == 4 or numero == 5:

#     print("gana María")

# print(f"---El numero aleatorio es: {numero}")


# #Escribe el código que imprima un comando dada la luz del semáforo

#     #Verde = Siga

#     #Amarillo = Precaución

#     #Rojo = Pare


# luz = input("De que color esta la luz del semaforo (verde, amarillo ó rojo): ").lower()


# if luz == "verde":

#     print("Siga")

# elif luz == "amarillo":

#     print(" Precaución")

# elif luz == "rojo":

#     print("Pare")
# else:

#     print("Error")


# #Escribe el código que basado en la actividad 1 y una variable que nos indica si hay peaton o no (hayPeaton), imprima:

#     #Verde -------- Si hay peaton - Pare, Sino - Siga

#     #Amarillo ----------- Si hay peaton - Pare, Sino - Precaución

#     #Rojo = Pare


# # luz = input("De que color esta la luz del semaforo (verde, amarillo ó rojo): ").lower()

# haypeaton = input("hay peaton (si o no): ").lower()


# if luz == "verde":

#     if haypeaton == "si":

#         print("Pare")
#     else:

#         print("Siga")

# elif luz == "amarillo":

#     if haypeaton == "si":

#         print("Pare")
#     else:

#         print("Precaución")

# elif luz == "rojo":

#     print("Pare")
# else:

#     print("Error")



# # Segunda forma de resolverlo


# # luz = input("De que color esta la luz del semaforo (verde, amarillo ó rojo): ").lower()

# haypeaton = input("hay peaton (si o no): ").lower()


# if haypeaton == "si" and (luz == "verde" or luz == "amarillo" or luz == "rojo"):

#     print("Pare")

# elif luz == "verde":

#     print("Siga")

# elif luz == "amarillo":

#     print("Precaución")

# elif luz == "rojo":

#     print("Pare")
# else:

#     print("Error")



#Escribe el código para dos numeros a y b, el usuario va a seleccionar una opcion: 

    #1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b) y 

    #retornar el resultado de la operación indicada.


# a = int(input("Ingrese un numero: "))

# b = int(input("Ingrese un numero: "))
# opcion = int(input("""seleccionar una opcion: 

# 1. para sumar, 

# 2. para multiplicar, 

# 3. para restar (a-b) y 

# 4. para dividir (a/b): """))


# if opcion == 1:

#     print(f"Resultado: {a+b}")

# elif opcion == 2:

#     print(f"Resultado: {a*b}")

# elif opcion == 3:

#     print(f"Resultado: {a-b}")

# elif opcion == 4 and b != 0:

#     print(f"Resultado: {a//b}")
# else:

#     print("No valido")



# Realice un programa que calcule el dinero total que una empresa debe pagar 

# por concepto de indemnización (pago que se realiza por un despido injustificado) 

# de sus empleados, teniendo en cuenta que la indemnización de un empleado se calcula de la siguiente manera en esa empresa:


#   Para empleados cuyo salario sea superior a tres salarios mínimos; recibirán, siempre y cuando hayan trabajado por lo menos un año en la empresa, 

# el 75% de su salario por cada uno de los primeros 5 años laborados en la empresa y el 100% de su salario por cada uno de los años restantes.


# •	Para empleados cuyo salario sea inferior o igual a 3 salarios mínimos; recibirán, siempre y cuando hayan trabajado 

# por lo menos un año en la empresa, el 100% de su salario por cada año laborado en la empresa.


salario = float(input("Salario del empleado: "))

tiempoTrabajado = float(input("Ingrese el tiempo laborado en la intitución en años: "))
SalarioMinimo = 1000000

if tiempoTrabajado >= 1:
    if salario>(SalarioMinimo*3) and tiempoTrabajado > 5:
        print(f"Indemnización es: {(salario*0.75*5)+(salario*1*(tiempoTrabajado-5))}")
    elif salario <= (SalarioMinimo*3):
        print(f"Indemnización es: {salario*1*tiempoTrabajado}")
else:
    print("No valido")

