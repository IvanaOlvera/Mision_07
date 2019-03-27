#Autor: Ivana Olvera Mérida
#Escribe una función llamada dividir, que recibe como parámetros el dividendo
#y el divisor e IMPRIME el cociente y el residuo

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

main()


