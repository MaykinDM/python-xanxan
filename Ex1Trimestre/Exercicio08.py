print("Programa que calcula a glicose no sangue")

glicose = int(input("Digite a quantidade de glicose no sangue em mg:"))

if glicose <= 100:
    print("Glicose Normal")
elif glicose > 100 and glicose <= 140:
    print("Glicose Alta")
if glicose > 140:
    print("Caso de Diabete")

print("Fim de programa")