print('notas trimestrais')
tri1 = float(input('primeiro trimestre'))
tri2 = float(input('segundo trimestre'))
tri3 = float(input('terceiro trimestre'))
media = (tri1 + tri2 + tri3 )/3
if media < 40:
    print("aluno reprovado e sua média é: {}" .format(media))
elif media >= 40 and media < 60:
    print("aluno em recuperação e sua média é:".format(media))
else:
    print('aluno aprovado e sua média é:'.format(media))

    print('fim de programa')