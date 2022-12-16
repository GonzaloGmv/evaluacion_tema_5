def ejr2():
    f = open('ejercicio2.py/contador.txt', "a+", encoding="utf-8")
    f.seek(0)
    if f.read() == '':
        f.write('0')
    f.seek(0)
    valor = f.read()
    try:
        valor == int(valor)
    except:
        print('Error: Fichero corrupto')
    else:
        argumento = input('Escriba "inc" o "dec" para incrementar o decrementar el contador: ')
        if argumento == 'inc':
            f.truncate(0)
            f.write(str(int(valor) + 1))
        elif argumento == 'dec':
            f.truncate(0)
            f.write(str(int(valor) - 1))
        else:
            print(valor)
        f.close

ejr2()