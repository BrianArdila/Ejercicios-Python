
def maraton():    
    while True:
        print('*-'*10)
        print('1.Ejercicio 1')
        print('2.Ejercicio 2')
        print('3.Ejercicio 3')
        print('4.Ejercicio 4')
        print('5.Ejercicio 5')
        print('6.Ejercicio 6')
        print('7.Ejercicio 7')
        print('8.Ejercicio 8')
        print('9.Ejercicio 9')
        print('10.Ejercicio 10')
        print('11.Ejercicio 11')
        print('12.Ejercicio 12')
        print('13.Ejercicio 13')
        print('14.Salir')
        print('*-'*10)
        opcion=input('Digite su opción ')
        if opcion=='1':
            valor_compra = float(input("Ingrese el valor de la compra: "))
            if valor_compra > 200000:
                valor_pagar = valor_compra * 0.8
                print(f"El valor a pagar es de: {valor_pagar}")
            else:
                print(f"El valor a pagar es de: {valor_compra}")
        elif opcion=='2':
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
        elif opcion=='3':
            precioKilo = float(input("ingrese el precio del kilo: "))
            kilos = float(input("Cantidad de kilos comprados: "))
            if kilos >= 0.00:
                print(f"El valor a pagar es: {precioKilo} ")
            elif kilos >= 2.00:
                print(f"El valor a pagar es: {precioKilo*0.9} ")
            elif kilos >= 5.00:
                print(f"El valor a pagar es: {precioKilo*0.85} ")
            elif kilos >= 10.00:
                print(f"El valor a pagar es: {precioKilo*0.8} ")
        elif opcion=='4':
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
        elif opcion=='5':
            kmInicial = float(input("Ingrese la cantidad de kilometros que tiene el auto antes de alquilarlo: "))
            kmFinal = float(input("Ingrese la cantidad de kilometros que tiene el auto despues de alquilarlo: "))
            kmRecorrido = kmFinal - kmInicial 

            if kmRecorrido <= 3000:
                print(f"Sus kilometros recorridos fueron de {kmRecorrido} y el valor a pagar es de {300000}")
            elif kmRecorrido <= 10000:
                valorPagar = 300000 + (kmRecorrido - 3000) * 150
            else:
                valorPagar = 300000 + (kmRecorrido - 10000) * 200 + (10000-3000) * 150
            print(f"Sus kilometros recorridos fueron de {kmRecorrido} y el valor a pagar es de {valorPagar}")
        elif opcion=='6':
            valor_compra = float(input("Ingrese el valor de la compra: "))
            if valor_compra > 1000000:
                print(f"El valor a pagar es de: {valor_compra*0.8}")
            elif valor_compra < 0:
                print("ERROR: datos invalidos")
            else:
                print(f"El valor a pagar es de: {valor_compra}")
        elif opcion=='7':
            valor_temperatura = float(input("Ingrese el valor de la temperatura: "))
            if valor_temperatura >= -10 and valor_temperatura < 10:
                print("Mucho Frio")
            elif valor_temperatura < 15:
                print("Poco Frio")
            elif valor_temperatura < 25:
                print("Temperatura Normal")
            elif valor_temperatura < 30:
                print("Poco Calor")
            elif valor_temperatura < 45:
                print("Mucho Calor")
            else:
                print("Temperatura fuera de rango")
        elif opcion=='8':
            dia = int(input("Ingrese el numero que corresponde al dia de la semana: "))
            if dia == 1:
                print("Lunes")
            elif dia == 2:
                print("Martes")
            elif dia == 3:
                print("Miercoles")
            elif dia == 4:
                print("Jueves")
            elif dia == 5:
                print("Viernes")
            elif dia == 6:
                print("Sabado")
            elif dia == 7:
                print("Domingo")
            else:
                print("ERROR")
        elif opcion=='9':
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
        elif opcion=='10':
            valor_casa = float(input("Valor del casa: "))
            ingresos = float(input("Ingreso del comprador: "))
            if ingresos < 1500000:
                print(f"La cuota inicial será del 15% del valor de la vivienda: {valor_casa*0.15} y el restante se dividirá en cuotas (iguales) mensuales de {(valor_casa*0.85)/120} durante diez (10) años")
            else:
                print(f"La cuota inicial será del 30% del valor de la vivienda: {valor_casa*0.30} y el restante se dividirá en cuotas (iguales) mensuales de {(valor_casa*0.7)/84} durante diez (7) años")
        elif opcion=='11':
            cantidad_productos = int(input("Ingrese el numero de docenas del producto que va a comprar: "))
            valor_producto = float(input("Ingrese el valor de la docena del producto: "))
            valor_producto = valor_producto*cantidad_productos
            if cantidad_productos > 3:
                print(f"""el monto de la compra es de {valor_producto}
                Se ofrece un descuento del 15% equivalente a {valor_producto*0.15}
                se  obsequia  {(cantidad_productos-3)}  unidades  del  producto  por  cada  docena  en exceso  
                y el valor a pagar es de: {valor_producto*0.85}
                """)
            else:
                print(f"""el monto de la compra es de {valor_producto}
                Se ofrece un descuento del 10% equivalente a {valor_producto*0.1}
                no  obsequia  unidades  del  producto  por  cada  docena  en exceso  
                y el valor a pagar es de: {valor_producto*0.9}
                """)
        elif opcion=='12':
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

        elif opcion=='13':
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
        elif opcion=='14':
            break
        else:
            print('opcion no valida') 

def gallinas():
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

while True:
    print('*-'*10)
    print('1.Maraton de ejercicios')
    print('2.Ejercicio de las Gallinas')
    print('3.Ejercicio 3')
    print('4.Ejercicio 4')
    print('5.Ejercicio 5')
    print('6.Salir')
    print('*-'*10)
    opcion=input('Digite su opción ')
    if opcion=='1':
        maraton()
    elif opcion=='2':
        gallinas()
    elif opcion=='3':
        pass
    elif opcion=='4':
        pass
    elif opcion=='5':
        pass
    elif opcion=='6':
        break
    else:
        print('opcion no valida') 