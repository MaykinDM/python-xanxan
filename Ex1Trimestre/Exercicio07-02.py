print('programa para calcula')
salario = float(input('digite o valor do salario'))
if salario <= 1903.98:
    print("voce esta isento de imposto de renda.")
elif(slario > 1903.98 and salario < 2826.65):
    imposto = (salario * 7.5)/100
    print('voce deveria pagar R$ {} de imposto de renda'. formate (imposto))
elif(salario > 2826.66 and salario <= 3751.05):
    imposto = (salario * 15)/100
    print('voce devera pagar R$ {} de imposto de renda'. format(imposto))
elif(salario >= 3751.06 and salario <= 4664.68):
    imposto = (salario * 22.5)/100
    print("voce devera pagar R$ {} de imposto de renda".format(imposto))
else:
    imposto = (salario * 27.5)/100
    print('voce devera pagar R$ {} de imposto de renda'. format(imposto))