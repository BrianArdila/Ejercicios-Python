def suma():
    num1 = 5
    num2 = 5
    print(f"La suma de los numeros es: {num1+num2}")

def suma1(a,b):
    print(f"La suma de los numeros es: {a+b}")
# suma1(1,21)

def suma2(mun1,mun2):
    resultado = mun1+mun2
    return resultado
rta = suma2(5,3)
print(rta)

def suma3(mun1,mun2):
    return mun1+mun2
def main():
    rta = suma2(5,3)
    print(rta)
main()