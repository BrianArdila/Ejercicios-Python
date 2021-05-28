"""Calcular el promedio de edades de hombres, mujeres y de todo un grupo de estudiantes."""

# sumaEdad = 0

# numeroH = int(input("Cuantos hombres hay: "))
# for i in range(numeroH):
#     edad = int(input("edad: "))
#     sumaEdad += edad
# print(f"Promedio de edades de los Hombres es: {sumaEdad/numeroH}")
# numeroM = int(input("Cuantos Mujeres hay: "))
# for i in range(numeroM):
#     edad = int(input("edad: "))
#     sumaEdad += edad
# print(f"Promedio de edades de los Hombres es: {sumaEdad/numeroM}")

grupo = int(input("Cuantos estudiantes hay: "))
Sumah = 0
SumaM = 0
conteoH = 0
conteoM = 0
for i in range(grupo):
    tipoEstudiante = input("Escriba H para hombre o M para mujeres: ").upper()
    Edad = int(input("edad: "))
    if tipoEstudiante == "H":
        Sumah += Edad
        conteoH += 1
    elif tipoEstudiante == "M":
        SumaM += Edad
        conteoM += 1

print(f"Promedio de edades de los Hombres es: {Sumah/conteoH}")
print(f"Promedio de edades de los Mujeres es: {SumaM/conteoM}")