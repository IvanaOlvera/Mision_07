#Autor: Ivana Olvera Mérida
#Encontrar e imprimir el mayor de un conjunto de valores enteros positivos que teclea el usuario

def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor)")
    int(input("Teclea un número [-1 para salir]: "))
    mayor = 0
    n = mayor

    while n!= -1:
        n= int(input("Teclea un número [-1 para salir]: "))

        if n >= mayor:
            mayor = n
            print(mayor)

        if n<0:
            print("ERROR")

        if mayor>0:
            print("El número mayor es", mayor)

        else:
            print("No existe un valor mayor")

def main():
    encontrarMayor()

main()