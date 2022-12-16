import pickle

class Personaje:
  def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

class Gestor:
    def añadir_personaje(personaje):
        f = open("ejercicio3/personajes.pckl", "ab")
        f.close()
        f = open("ejercicio3/personajes.pckl", "rb")
        while True:
            try:
                a = pickle.load(f)
                if a.nombre == personaje.nombre:
                    return
            except EOFError:
                break
        f.close()
        f = open("ejercicio3/personajes.pckl", "ab")
        pickle.dump(personaje, f)
        f.close()

    def mostrar_personajes():
        f = open("ejercicio3/personajes.pckl", "rb")
        while True:
            try:
                personaje = pickle.load(f)
                print(personaje.nombre, personaje.vida, personaje.ataque, personaje.defensa, personaje.alcance)
            except EOFError:
                break
        f.close()
    
    def borrar_personajes(nombre):
        f = open("ejercicio3/personajes.pckl", "rb")
        personajes = []
        while True:
            try:
                personaje = pickle.load(f)
                if personaje.nombre != nombre:
                    personajes.append(personaje)
            except EOFError:
                break
        f.close()
        f = open("ejercicio3/personajes.pckl", "wb")
        for personaje in personajes:
            pickle.dump(personaje, f)
        f.close()