# """Mostrar los numeros del 1 al 10"""
# num = 0
# while num != 10:
#     num += 1
#     print(num)

# """Dado un conjunto de números ingresados por teclado, determine cuantos fueron positivos y cuantos fueron negativos, hasta que se ingrese el número 0"""
# num = ""
# positivo = 0
# negativo = 0 
# while num != 0:
#     num = int(input("Digite un numero: "))
#     if num > 0:
#         positivo += 1
#     elif num < 0:
#         negativo += 1 
# print(f"Fueron {positivo} positivos y {negativo} negativos")

# """5 amigos desean hacer una vaca para una fiesta, hacer un algoritmo que pida la donación de cada uno de los participantes y diga total recaudado."""
# pedir = 1
# total = 0
# cantidad_amigos = int(input("Cuantos amigos van aportar dinero: "))
# while pedir <= cantidad_amigos:
#     money = float(input("Dame plata: "))
#     total += money
#     pedir += 1
# print(f"El total de la vaca es: {total}") 

# """
# Haga un programa que calcule el promedio de los estudiantes de un salon
# """

# try:
#     cantidad_estudiantes = int(input("Escriba la cantidad de estudiantes que hay en el salon: "))
#     promedio = 0
#     contador = 1
#     sumanotas = 0
#     while contador <= cantidad_estudiantes:
#         nota = float(input(f"Escriba la nota del estudiante {contador}: "))
#         if nota >= 1 and nota <= 5:
#             sumanotas += nota
#             promedio = sumanotas / cantidad_estudiantes
#             contador += 1
#         else: 
#             print("Dato invalido")
#     print(f"El promedio es de {promedio:.2f}") # de esta forma se puede formatear el codigo
# except Exception:
#     print("ERROR: Dato invalido")

"""
Escribe un programa usando el ciclo Mientras Que (while) que, dado un número por parte del usuario genere 
la tabla de multiplicar del 1 al 12 para ese número. 
"""

num = int(input("Escriba un numero: "))
multiplicador = 1
producto = 0
while multiplicador <= 12:
    producto = num * multiplicador
    print(f"{num}*{multiplicador}={producto}")
    multiplicador += 1