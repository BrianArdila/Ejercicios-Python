'''lectura de datos desde un archivo
tenemos 3 formas de leer un archivo

forma 1
utilizando el metodo read: canal_de_comunicaciones.read([n])
que el transfiere a n-bytes(sino se especifica la n transfiere 
el archivo completo hasta una variable en memoria )

forma 2:
utilizar el metodo readline: canal_de_comunicaciones.readline([n])
que el transfiere a n-bytes(sino se especifica la n transfiere una linea
del archivo hasta una variable en memoria )

forma 3:
utilizando el metodo canal_de_comunicaciones.readlines([n])
que  transfiere a n-bytes(sino se especifica la n transfiere todo
el archivo desde el archivo hasta un arreglo y cada linea se almacena 
en una posicion del arreglo)

forma4:
utilizando el iterador de secuencias FOR: que transfiere el archivo 
hacia variables de memoria linea a linea

NOTA:
recordar que cualquiera de las opciones anteriores requiere que el 
archivo este abierto'''

#forma 1: utilizando el metodo read()

print("forma1 utilizando el metodo read()")
with open("clase1.txt","r", encoding= "utf8") as f:
    salida=f.read()
    print(salida)

print("forma2 utilizando el metodo readline()")
with open("clase1.txt","r", encoding= "utf8") as f:
    salida=f.readline()
    print(salida)

print("forma3 utilizando el metodo readlines()")
with open("clase1.txt","r", encoding= "utf8") as f:
    salida=f.readlines()
    print(salida)

print("forma4 utilizando el iterador de secuencia FOR")
with open("clase1.txt","r", encoding= "utf8") as f:
    print(f)
    for i in f:
        print(i)

print("forma5 utilizando el iterador de secuencia FOR AÑADIENDO EL NUMERO DE LA LINEA")
with open("clase1.txt","r", encoding= "utf8") as f:
    for k,i in enumerate(f):
        print(f"{k}::{i}")

        

