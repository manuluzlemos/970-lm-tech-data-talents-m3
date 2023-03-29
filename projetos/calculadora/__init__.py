from funcoes import *

funcoes = {
    "soma": soma,
    "subtracao": subtracao,
    "divisao": divisao,
    "multiplicacao": multiplicacao
}

def calcule():
    a = float(input("Informe o primeiro número: "))
    b = float(input("Informe o segundo número: "))
    op = input("Informe a operação (soma, subtracao, divisao, multiplicacao): ")

    if op in funcoes.keys():
        print(f'Resultado da operação: {funcoes[op](a, b)}')
    else:
        print("Operaração inválida!")