from funcoes import *

funcoes = (soma, subtracao, divisao, multiplicacao)
op_extenso = ("soma", "subtracao", "divisao", "multiplicacao")
op_simbolos = ("+", "-", "/", "*")

def calcule():
    a = float(input("Informe o primeiro número: "))
    b = float(input("Informe o segundo número: "))
    op = input("Informe a operação (soma, subtracao, divisao, multiplicacao, +, -, /, *): ")

    if op in op_extenso or op in op_simbolos:
        index = op_extenso.index(op) if op in op_extenso else op_simbolos.index(op)    
        print(f'Resultado da operação: {funcoes[index](a, b)}')
    else:
        print("Operação inválida!")