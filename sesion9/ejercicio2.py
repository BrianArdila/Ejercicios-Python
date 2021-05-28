cantidadNumeros = int(input("Digite cantidad de numeros: "))
suma = 0
cuente = 0
for i in range(cantidadNumeros//2): # puedo operar con la variable que determina la longitud
    num = int(input("Digite el numero: "))
    if num < 25:
        cuente += 1
        suma += num
print(f"El promedio es {suma/cuente}")
