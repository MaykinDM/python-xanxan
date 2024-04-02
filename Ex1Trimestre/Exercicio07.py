print("Programa de tabuada.")

numero = int(input("Entre com um número inteiro:"))
contador = 1

if(numero<= 10):
    while(contador <= 10):
        resultado = numero * contador
        print(numero, " X ", contador, "=", resultado)
        contador = contador + 1
else:
    print("Número inválido.")

    print("Fim de programa")