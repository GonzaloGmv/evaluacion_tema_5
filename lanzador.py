from ejercicio1.calculos import ejr1
from ejercicio2.contador import ejr2
from ejercicio3.main3 import ejr3

def main():
    ejr = input('Escriba el número del ejercicio que quiere ejecutar: ')
    print('\n')
    if ejr == '1':
        ejr1()
    elif ejr == '2':
        ejr2()
    elif ejr == '3':
        ejr3()