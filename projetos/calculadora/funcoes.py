def soma(a, b):
    if not (type(a) in (int, float) and type(b) in (int, float)):
        raise TypeError()
    return a+b

def subtracao(a, b):
    if not (type(a) in (int, float) and type(b) in (int, float)):
        raise TypeError()
    return a-b

def divisao(a, b):
    if not (type(a) in (int, float) and type(b) in (int, float)):
        raise TypeError()
    
    if b == 0:
        print("Divisão inválida")
        return 0
    
    return a/b

def multiplicao(a, b):
    if not (type(a) in (int, float) and type(b) in (int, float)):
        raise TypeError()
    return a*b
