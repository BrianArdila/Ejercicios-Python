"""
Una  empresa  de  bienes  raíces ofrece  programas  de  vivienda  de  interés  social,  bajo  las  siguientes condiciones: 
•Si los ingresos del compradorson inferiores a 1.5millones, la cuota inicial será del 15% del valor de la vivienda y el restante se 
dividirá en cuotas (iguales) mensuales durante diez (10) años. 
•Si los ingresosdel comprador son mayores o iguales a 1.5m, la cuota inicial será del 30% del valor de la vivienda y 
el resto se distribuirá en pagos mensuales (iguales) en 7 años.Determinar el plan de pagos del comprador.

Entrada
ingresos del comprador
valor de la casa
Salida 
la cuota inicial 
Proceso

"""
valor_casa = float(input("Valor del casa: "))
ingresos = float(input("Ingreso del comprador: "))

if ingresos < 1500000:
    print(f"La cuota inicial será del 15% del valor de la vivienda: {valor_casa*0.15} y el restante se dividirá en cuotas (iguales) mensuales de {(valor_casa*0.85)/120} durante diez (10) años")
else:
    print(f"La cuota inicial será del 30% del valor de la vivienda: {valor_casa*0.30} y el restante se dividirá en cuotas (iguales) mensuales de {(valor_casa*0.7)/84} durante diez (7) años")
