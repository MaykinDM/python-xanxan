print("Programa que classifica triângulo.")
a = float(input("Digite o primeiro lado do triangulo"))
b = float(input("Digite o segundo lado do triangulo"))
c = float(input("Digite o terceiro lado do triangulo"))

if a > b+c or b > a+c or c > a+b:
    print("Não é um triangulo.")

else:
    print("É um triângulo.")

    if (a == b and b == c):
        print("triangulo equlilatero.")
    elif (a == b or b == c) or (a == c):
        print("triangulo isoceles.")
    else:
        print("triangulo escaleno.")