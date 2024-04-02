print('calculadora')
while True:
    try:
        v1 = float(input('entra com o primeiro valor'))
        v2 = float(input('entre com o segundo valor'))
        op = input('digite + para somar, - para subtrair, * para multiplicar, / para dividir ou S para sair.')

        if op == '+' :
            resultado = v1 + v2
        elif op   == '-':
            resultado = v1 - v2
        elif op == '*':
            resultado = v1 * v2
        elif op == '/':
            resultado = v1 / v2
        elif op == 'S':
            break
        else:
             print('Valor inválido')
             continue
    except:
        print('você digitou um valor inválido')
        continue

    print('A operação escolhida foi {} e o rsultado é {}' .format(op, resultado))

