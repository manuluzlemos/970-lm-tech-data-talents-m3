def soma(a, b):
    if not (type(a) in (int, float) and type(b) in (int, float)):
        raise TypeError(f'As entradas "a" e "b" devem ser tipos numéricos. Recebeu-se a = {a} ({type(a)}) e b = {b} ({type(b)})')
    
    return a+b

def subtracao(a, b):
    if not (type(a) in (int, float) and type(b) in (int, float)):
        raise TypeError(f'As entradas "a" e "b" devem ser tipos numéricos. Recebeu-se a = {a} ({type(a)}) e b = {b} ({type(b)})')

    return a-b

def divisao(a, b):
    if not (type(a) in (int, float) and type(b) in (int, float)):
        raise TypeError(f'As entradas "a" e "b" devem ser tipos numéricos. Recebeu-se a = {a} ({type(a)}) e b = {b} ({type(b)})')
    
    if b == 0:
        print("Divisão inválida")
        return 0
    
    return a/b

def multiplicacao(a, b):
    if not (type(a) in (int, float) and type(b) in (int, float)):
        raise TypeError(f'As entradas "a" e "b" devem ser tipos numéricos. Recebeu-se a = {a} ({type(a)}) e b = {b} ({type(b)})')
    return a*b