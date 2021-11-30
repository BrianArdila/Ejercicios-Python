
productos = [
# nombre, unidades, precio 
    ['Leche', 5, 5000],
    ['Pan',   18, 1000],
    ['huevos', 82, 82000],
    ['huevos', 82, 82000],
    ['huevos', 82, 82000],
    ['huevos', 82, 82000],
]

def imprimir_menu():
    global productos
    for k, ele in enumerate(productos):
        print(f"{k}) {ele[0]:>10}    ${ele[2]:<6} ({ele[1]} u)")
imprimir_menu()

def atenter_menu():
    total_cliente = 0
    while True:
        rest = input("Ingrese su compra {codigo,cantidad} {vacio para salir} ")

        if rest == " ":
            break
        
        rest_list = rest.split(",")

        if len( rest_list ) != 2:
            print("Entrada invalida, vuelva a ingresar los valores")
            continue

        cod = int(rest_list[0])
        cant = int(rest_list[1])

        if productos[cod][1] > cant:
            total_cliente += cant * productos[cod][2]
            productos[cod][1]-=cant
        else:
            print(f"Solo te puedo vender {productos[cod][1]} unidades de {productos[cod][0]} y precio de {productos[cod][2]}")   
            total_cliente += productos[cod][1] * productos[cod][2]     
            productos[cod][1] = 0
    print(f"Gracias por su compra, su total es: {total_cliente}")

atenter_menu()