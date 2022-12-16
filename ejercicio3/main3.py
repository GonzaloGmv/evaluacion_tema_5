from ejercicio3.gestor import *

def ejr3():
    caballero = Personaje("Caballero", 4, 2, 4, 2)
    guerrero = Personaje("Guerrero", 2, 4, 2, 4)
    arquero = Personaje("Arquero", 2, 4, 1, 8)
    Gestor.añadir_personaje(caballero)
    Gestor.añadir_personaje(guerrero)
    Gestor.añadir_personaje(arquero)
    Gestor.mostrar_personajes()
    print('\n')
    print('Borramos al arquero:')
    print('\n')
    Gestor.borrar_personajes("Arquero")
    Gestor.mostrar_personajes()