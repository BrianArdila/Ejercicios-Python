"""
Un coleccionista de películas mantiene su colección organizada por géneros;
 CIENCIA FICCIÓN,    ACCIÓN Y TERROR. Desea saber cuantas películas de cada genero tiene en su colección.
Ayude al coleccionista a resolver su problema.
"""

cf=0
accion=0
terror=0

while True:
    print("-"*30)
    print("1. CIENCIA FICCIÓN")
    print("2. ACCIÓN")
    print("3. TERROR")
    print("4. YA NO HAY MÁS PELICULAS")
    print("-"*30)
    opc=input("Seleccione el genero de la pelicula: ")
    if opc=="1":
        cf+=1        
    elif opc=="2":
        accion+=1
    elif opc=="3":
        terror+=1
    elif opc=="4":
        break
    else:
        print("Opción NO VALIDA")
print()
print("De CIENCIA FICCIÓN tiene: ",cf)
print("De ACCIÓN tiene: ",accion)
print("De TERROR tiene: ",terror)