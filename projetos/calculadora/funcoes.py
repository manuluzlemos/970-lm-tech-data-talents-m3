def soma(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError(f'As entradas "a" e "b" devem ser tipos numéricos. Recebeu-se a = {a} ({type(a)}) e b = {b} ({type(b)})')
    
    return a+b

def subtracao(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError(f'As entradas "a" e "b" devem ser tipos numéricos. Recebeu-se a = {a} ({type(a)}) e b = {b} ({type(b)})')

    return a-b

def divisao(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError(f'As entradas "a" e "b" devem ser tipos numéricos. Recebeu-se a = {a} ({type(a)}) e b = {b} ({type(b)})')
    
    if b == 0:
        print("Divisão inválida")
        return 0
    
    return a/b

def multiplicacao(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError(f'As entradas "a" e "b" devem ser tipos numéricos. Recebeu-se a = {a} ({type(a)}) e b = {b} ({type(b)})')
    return a*b