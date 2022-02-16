class Animal:
    def __init__(self, nombre, onoma):
        self.nombre = nombre
        self.onoma = onoma

    def saludo(self):
        print('El ',self.tipo,' se llama',self.nombre, 'y hace ',self.onoma)

class Gato(Animal):
    tipo = 'gato'

class Perro(Animal):
    tipo = 'perro'

gato = Gato('Flofy', 'Mauya')
gato.saludo()
perro = Perro('Firulai', 'Ladra')
perro.saludo()