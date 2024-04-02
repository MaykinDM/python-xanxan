# importando o módulo ramdom
import random
print("Programa de dado")

""""
módulo ramdom tem a função de
gerar um valor aleatório
"""
numero_sorteado = random.randrange(1, 7)
print("O número sorteado é: ", numero_sorteado )


for teste in range(1, 4):
    numero_aleatorio = random.randrange(1, 101, 5)
    print(numero_aleatorio)

print("Teste do randint")
valor_qualquer = random.randint(1, 6)
print(valor_qualquer)