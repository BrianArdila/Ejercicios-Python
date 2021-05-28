# Actividad 1:  Ahora vamos a elaborar un algoritmo
#  que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número pero que termine el proceso si llega al 10.

from math import factorial


def ejercicio1():
    num = abs(int(input("Ingrese un numero: "))) # Atributo abs() Permite pasar apositivo los numeros
    for i in range(2,num+1,2):
        print(i)
        if i == 10:
            break
        
#  Vamos a realizar un algoritmo que nos calcule la serie de Fibonacci. La serie o secuencia de Fibonacci comienza con los 
# números 0 y 1 y 1, y a partir de allí es posible calcular el siguiente valor como la suma de los dos valores anteriores. 
# Por ejemplo, 1+1=2, 1+2=3, 2+3=5, etc. 
# Así, los primeros números de la secuencia son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#  Creemos un programa que a partir de un número N ingresado, imprima los primeros N números de la serie de Fibonacci.

def ejercicio2():
    num = abs(int(input("Ingrese un numero: ")))
    num1 = 0
    num2 = 1
    print(num1)
    print(num2)
    for i in range(num):
        rta = num1 + num2
        print(rta)
        num1 = num2
        num2 = rta

# Escribe el código usando break que reciba una palabra e imprima el número de letras que 
# tiene y las letras hasta que, o bien termine la palabra o encuentre la letra a.

def ejercicio3():
    contar = 0
    palabra = input("escriba una palabra: ").lower()
    for i in palabra:
        if i == "a":
            break
        contar += 1
    print(f"Se contaron {contar} letras")

# Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario, pero saltarse si el digito es 4

def ejercicio4():
    contador = 0
    numero = input("ingrese un numero: ")
    for i in numero:
        if i == "4":
            continue
        contador += 1
    print(f"El numero de digitos es:  {contador}")

# Usando tanto while como for, escribe el código que pida números al usuario hasta que este ingrese -1 y que retorne
#  el factorial de cada número ingresado usando un ciclo Para (For).

def ejercicio5():
    while True:
        num = abs(int(input("Ingrese un numero entero positivo: ")))
        factorial = 1
        if num == 4:
            break
        for i in range(num):
            factorial *= i+1
        print(f"El factorial del numero {num} es {factorial}")

while True:
    print('*-'*10)
    print('1.Ejercicio 1')
    print('2.Ejercicio 2')
    print('3.Ejercicio 3')
    print('4.Ejercicio 4')
    print('5.Ejercicio 5')
    print('6.Salir')
    print('*-'*10)
    opcion=input('Digite su opción ')
    if opcion=='1':
        ejercicio1()
    elif opcion=='2':
        ejercicio2()
    elif opcion=='3':
        ejercicio3()
    elif opcion=='4':
        ejercicio4()
    elif opcion=='5':
        ejercicio5()
    elif opcion=='6':
        break
    else:
        print('opcion no valida') 