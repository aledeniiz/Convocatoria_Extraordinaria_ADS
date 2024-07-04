#Definimos una funcion que pida un Numero
def numero_entero(numero):
    try:
        num=int(numero)
        if num>1:
            return num
        
        else: 
            print("Ingrese otro numero diferente, que sea entero y mayor que uno.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número entero.")
        return None
#Definio una funcion que busque sus numeros primos
def factores_primos(n):
    factores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
    return factores
#Eejcutamos las funciones
def main():
    numero = input("Ingrese un número entero mayor que 1: ")
    num = numero_entero(numero)
    if num is not None:
        factores = factores_primos(num)
        print(f"Factores primos de {num}: {factores}")

if __name__ == "__main__":
    main()