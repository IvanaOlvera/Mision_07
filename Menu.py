#Autor: Ivana Olvera Mérida
#Escribe un menú para que el usuario pueda utilizar cualquiera de las funciones anteriores de manera repetida

def probarDivisiones(dividendo, divisor):
    contador = 0

    while dividendo >= divisor:
        dividendo = dividendo - divisor
        contador = contador + 1
        print(dividendo, "/", divisor, "=", contador, ", sobra ", dividendo)

def main():
    dividendo = int(input("Insertar dividendo: "))
    divisor = int(input("Insertar divisor: "))
    dividir = probarDivisiones(dividendo, divisor)

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


def insertarOpcion(opcion):
    print("Misión 07. Ciclos While")
    print("Autor: Ivana Olvera Mérida")
    print("Matrícula: A01746744")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    insertarOpcion(opcion)

    while opcion !=0:
        if opcion==1:
            print("Calculando divisiones")
            probarDivisiones()

        elif opcion==2:
            print("Teclea una serie de números para encontrar el mayor")
            encontrarMayor()

        elif opcion==3:
            print("Gracias por usar este programa, regresa pronto")

        if opcion > 3:
            print("ERROR, teclea 1,2 o 3")
            break

    print("Misión 07. Ciclos While")
    print("Autor: Ivana Olvera Mérida")
    print("Matrícula: A01746744")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    insertarOpcion(opcion)

main()