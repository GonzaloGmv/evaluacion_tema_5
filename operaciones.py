def suma(a, b):
    try:
        a + b
    except TypeError:
        return 'Error: Tipo de dato no válido'
    else:
        return a + b

def resta(a, b):
    try:
        a - b
    except TypeError:
        return 'Error: Tipo de dato no válido'
    else:
        return a - b
