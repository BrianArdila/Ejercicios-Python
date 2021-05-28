"""
¿A una reunión, se presentan personas de diferentes edades y sexo biológico (no se permite el ingreso a personas menores de edad). 
Se desean generar las siguientes estadísticas:
- Cantidad de personas que asistieron a la reunión
- Cantidad discriminada por sexo biológico
- Promedio de edades por sexo biológico
- La edad de la persona más joven que asistió
"""
Npersonas = int(input("numero de personas: "))
hombres = 0
Mujeres = 0
edad_hombre = 0
edad_mujer = 0
edadMenor = 0
i = 0
for i in range(Npersonas):
    edad = int(input("Escriba la edad: "))
    if edad < 18:
        i = i - 1
    else:
        if edadMenor < edad:
            edadMenor = edad        
        sexo = input("Escriba H para Hombre y M para mujer: ").upper()
        if sexo == "H":
            hombres += 1
            edad_hombre += 1
        elif sexo == "M":
            Mujeres += 1
            edad_mujer += 1
print(f"""
- Cantidad de personas que asistieron a la reunión: {Npersonas}
- Cantidad discriminada por sexo biológico: {hombres} Hombres {Mujeres} Mujeres
- Promedio de edades por sexo biológico:  {edad_hombre//hombres} Hombres {edad_mujer//Mujeres} Mujeres
- La edad de la persona más joven que asistió: {edadMenor}
""")