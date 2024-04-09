print("preço da maça")
quantidade = int(input("quantidade de maça"))
pedras = 2.40
if(quantidade < 12):
    pedras = 2.80

valor = quantidade * pedras
print("o valor é: {}" .format(valor))

