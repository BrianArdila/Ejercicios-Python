
from ..sesion6.sesion6 import Ej1 

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
            
        elif opcion=='2':
            
        elif opcion=='3':
            ejercicio3()
        elif opcion=='4':
            ejercicio4()
        elif opcion=='5':
            ejercicio5()
        elif opcion=='6':
            ejercicio2()
        elif opcion=='7':
            ejercicio3()
        elif opcion=='8':
            ejercicio4()
        elif opcion=='9':
            ejercicio5()
        elif opcion=='10':
            ejercicio2()
        elif opcion=='11':
            ejercicio3()
        elif opcion=='12':
            ejercicio4()
        elif opcion=='13':
            ejercicio5()
        elif opcion=='14':
            break
        else:
            print('opcion no valida') 



while True:
    print('*-'*10)
    print('1.Maraton de ejercicios')
    print('2.Ejercicio 2')
    print('3.Ejercicio 3')
    print('4.Ejercicio 4')
    print('5.Ejercicio 5')
    print('6.Salir')
    print('*-'*10)
    opcion=input('Digite su opción ')
    if opcion=='1':
        maraton()
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