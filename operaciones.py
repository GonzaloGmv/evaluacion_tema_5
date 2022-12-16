def suma(a, b):
    try:
        a == float(a) and b == float(b)
    except ValueError:
        return 'Error: Tipo de dato no válido'
    else:
        try:
            a + b
        except TypeError:
            return 'Error: Tipo de dato no válido'
        else:
            return a + b

def resta(a, b):
    try:
        a == float(a) and b == float(b)
    except ValueError:
        return 'Error: Tipo de dato no válido'
    else:
        try:
            a - b
        except TypeError:
            return 'Error: Tipo de dato no válido'
        else:
            return a - b

def producto(a, b):
    try:
        a == float(a) and b == float(b)
    except ValueError:
        return 'Error: Tipo de dato no válido'
    else:
        try:
            a * b
        except TypeError:
            return 'Error: Tipo de dato no válido'
        else:
            return a * b