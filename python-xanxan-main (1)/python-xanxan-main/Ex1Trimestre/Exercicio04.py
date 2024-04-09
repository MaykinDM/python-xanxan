print("Programa que calcula o preço das maçãs")

preco_por_macas = 2.40

numero_de_macas = int(input("Digite o número de maçãs compradas: "))
custo_total = numero_de_macas * preco_por_macas if numero_de_macas >= 12 else numero_de_macas * preco_por_macas

print("O custo total da compra é de R$", custo_total)

print("Fim de programa")