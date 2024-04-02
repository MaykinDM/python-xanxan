print('programa para verificar maior e menor valor')
maior_Valor = 0
menor_valor = 0

while True:
    numero = int(input("digite o numero."))
    if(numero == 0):
        break
    if(maior_Valor == 0 and menor_valor == 0):
        maior_Valor = numero
        menor_valor = numero

    if(numero > maior_Valor):
        maior_Valor_valor = numero
    if(numero < menor_valor):
        menor_valor = numero
print("O maior valor é {}, e o menor valor {}" .format(maior_Valor, menor_valor))