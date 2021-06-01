#una tienda registra las ventas realziadas 
#a sus clientes en el siguiente formato
# articulo;cantidad;valor
#se encuentra interesado en determinar
#a el articulo mas vendido
#b el articulo menos vendido
#c el articulo que mas ingresos Genera 



factura = []
ciclo = True
b = []
while ciclo:
    inpt = input("Registre la venta realziada articulo;cantidad;valor: ")
    c =inpt.split(";")
    factura.append([c[0],float(c[1]),float(c[2])])
    opcion = input("Ingrese 'Si' para registrar otra venta o 'No' para salir: ").lower()
    if opcion == "no":
        ciclo = False
print(factura)


# otra forma de se parar la información del input usando el split
sucursal, ayunas, glucosa=input().split()