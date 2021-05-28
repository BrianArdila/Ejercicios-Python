"""
Un supermercado ha colocado enoferta la venta al por mayor de cierto producto, ofreciendo 
un descuento del 15% por la compra de másde tres (3) docenas y 10% en caso contrario. Además por la  compra  
de másde  tres  (3)  docenas  se  obsequia  una  unidad  del  producto  por  cada  docena  en exceso 
(sobre las tres(3) inicialmente mencionadas). Diseñe un programa que determine el monto de la compra, el monto del descuento, 
las cortesías (unidades obsequiadas) y el valor a pagar por un cliente.Determina el monto 
de la compra, el monto del descuento, las cortesías (unidades obsequiadas) y el valor a pagar por un cliente.

Entrada
valor del producto
Numero de profuctos comprados
Salida 
monto de la compra, el monto del descuento, las cortesías (unidades obsequiadas) y el valor a pagar por un cliente.
Proceso

"""
cantidad_productos = int(input("Ingrese el numero de docenas del producto que va a comprar: "))
valor_producto = float(input("Ingrese el valor de la docena del producto: "))
valor_producto = valor_producto*cantidad_productos
if cantidad_productos > 3:
    print(f"""el monto de la compra es de {valor_producto}
    Se ofrece un descuento del 15% equivalente a {valor_producto*0.15}
    se  obsequia  {(cantidad_productos-3)}  unidades  del  producto  por  cada  docena  en exceso  
    y el valor a pagar es de: {valor_producto*0.85}
    """)
else:
    print(f"""el monto de la compra es de {valor_producto}
    Se ofrece un descuento del 10% equivalente a {valor_producto*0.1}
    no  obsequia  unidades  del  producto  por  cada  docena  en exceso  
    y el valor a pagar es de: {valor_producto*0.9}
    """)
