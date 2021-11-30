from os import read


def ejemplo1():
    archivo=open("clase1.txt","w")           #creamos el archivo clase1.txt con el modo w que me permite crearlo cuando no existe
    asig1="prueba para el archivo clase1"    #preparamos una variable a la que se le asigno una cadena de texto
    archivo.write(asig1)                     #asignarle el contenido de la varible al archivo (escribir dentro del archivo)
    archivo.close()                          #cerramos el archivo
#ejemplo1()

def ejemplo2():
    archivo=open("clase1.txt","r")          #abrimos el archivo que ya existe en modo r
    asig2=archivo.read()                    #leemos el contenido del archivo en una variable
    archivo.close()                         #cerramos el archivo
    print(asig2)                            #imprimos la variable que tiene el contenido del archivo
#ejemplo2()

def ejemplo3():
    archivo=open("clase1.txt","r")          #abro el archivo de solo lectura        
    asig3=archivo.readlines()               #convierto el contenido en una lista
    for i in asig3:
        print(i)
    archivo.close()                         #cierro el archivo
    print(asig3)                            #imprimo la lista
#ejemplo3()

def ejemplo4():
    archivo=open("clase1.txt","a")          #abro el archivo de solo lectura        
    archivo.write(" esto esta sabroso!!!")   #al escribir esta frase en el archivo se agrega al final de la ultima letra que tenia el archivo
    archivo.close()                         #cierro el archivo
#ejemplo4()

def ejemplo5():
    archivo=open("clase1.txt","r")          #se abre el archivo para solo lectura
    print(archivo.read())                   #imprimo el contenido del archivo
    archivo.seek(0)                         #se regresa el puntero a la primera posicion del archivo
    print(archivo.read())                   #imprimo el contenido del archivo 
    archivo.close()                         #cierro el archivo
#ejemplo5()

def ejemplo6():
    archivo=open("clase1.txt","r")          #abro el archivo en modo lectura
    print(archivo.read(10))                 #imprimimos el archivo hasta la posicion 10
    print(archivo.read())                   #imprimimos el archivo desde el caracter 11 hasta el final
    archivo.close()                         #cierro el archivo
#ejemplo6()

def ejemplo7():
    archivo=open("clase1.txt","r")          #abro el archivo en modo lectur                #imprimimos el archivo desde el caracter 11 hasta el final
    archivo.seek(len(archivo.read())/2)     #nos ubicamos en la longitud dividido en dos (la mitad)
    print(archivo.read())                   #imprimimos desde la mitad en adelante
    archivo.close()                         #cierro el archivo
#ejemplo7()

def ejemplo8():
    archivo=open("clase1.txt","r")          #abro el archivo en modo lectur                #imprimimos el archivo desde el caracter 11 hasta el final

    print("primera linea")                  #imprimimos un titulo
    asig3=archivo.readline()                #leemos la primera linea y la asignamos a una variable
    print(asig3)                            #imprimimos la variable

    print("segunda linea")                  #imprimimos un titulo
    asig3=archivo.readline()                #leemos la segunda linea y la asignamos a una variable
    print(asig3)                            #imprimimos la variable

    print(archivo.read())                   #imprimimos el archivo en la ubicacion del cursor
    archivo.close()                         #cerramos el archivo
#ejemplo8()

def ejemplo9():
    archivo=open("clase1.txt","r+")         #leemos el archivo
    archivo.write("hola mundo\n")           #agregamos una linea que reemplaza lo que tenemos en la primera linea
    archivo.seek(0)                         #regresamos a la posicion cero o inicial del archivo
    print(archivo.read())                   #imprimimos el archivo desde el inicio
    archivo.close()                         #cerramos el archivo
#ejemplo9()
                                            #leer un archivo e imprimirlo con el metodo readline()
def ejemplo10():  
    archivo=open("clase1.txt","r")          #abrimos el archivo
    print(archivo.readlines())              #imprimimos las lineas
    archivo.close                           #cerrar el archivo
#ejemplo10()

                                            #manejador de contexto
                                            #es el with
def ejemplo11():
    with open("clase1.txt","r") as f:       #
        print(f.read())                     #
ejemplo11()

    



