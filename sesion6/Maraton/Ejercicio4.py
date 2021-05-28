"""
Ejercicio 4.
Durante una campaña de PyP, cierta EPS desea informar a sus afiliados sobre el riesgo de obesidad;
para lo cual utiliza la siguiente tabla suministrada por la OMS.
Dadas la estatura y el peso de una persona, determinar su nivel de riesgo.
Informar el nivel de riesgo a una persona

Nota : Todos los resultados se redondearán a un dígito decimal
 IMC = 14.356789 ==> 14.4
 IMC = 25.1389 ==> 25.1

Entrada
la estatura y el peso de una persona
Salida
nivel de riesgo
Proceso
IMC = peso / (estatura**2)
"""
try:
    estatura = float(input("Ingrese su estatura: "))
    peso = float(input("Ingrese su peso: "))

    imc = round((peso/(estatura**2)),1)

    if imc >= 18.5 and imc <= 24.9:
        print("Usted tiene una clasificacion Normal y un riesgo Promedio")
    elif imc <= 29.9:
        print("Usted tiene una clasificacion Sobrepeso y un riesgo Aumentado")
    elif imc <= 34.9:
        print("Usted tiene una clasificacion Obesidad grado I y un riesgo Moderado")
    elif imc <= 39.9:
        print("Usted tiene una clasificacion Obesidad grado II y un riesgo Severo")
    elif imc >= 40.0:
        print("Usted tiene una clasificacion Obesidad grado III y un riesgo Muy severo")
except Exception:
    print("Los datos ingresados no son validos")
