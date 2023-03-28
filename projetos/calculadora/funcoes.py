def soma(a, b):
    if not (type(a) in (int, float) and type(b) in (int, float)):
        raise TypeError()
    return a+b