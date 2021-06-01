
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
    while True:
        rest = input("Ingrese su compra {codigo,cantidad} {vacio para salir} ")

        if rest == " ":
            