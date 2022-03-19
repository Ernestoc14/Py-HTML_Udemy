# Extender el comportamiento de la Clase padre a dos Clases hijas
class Animal: # Clase Padre
    def __init__(self, nombre, onoma): # Metodo Init
        self.nombre = nombre
        self.onoma = onoma

    def saludo(self): # Metodo Saludo
        print('El ',self.tipo,' se llama',self.nombre, 'y hace ',self.onoma)

class Gato(Animal): # Clase Hijo 1 extendiendo Clase Padre Manera #1
    tipo = 'gato'
    def __init__(self, nombre, onoma): 
        Animal.__init__(self, nombre, onoma)
        print('Hola Gato Extendido')

class Perro(Animal): # Clase Hijo 2 extendiendo Clase Padre Manera #2
    tipo = 'perro'
    def __init__(self, nombre, onoma):
        super().__init__(nombre, onoma)
        print('Instanciando un Doggo')

gato = Gato('Flofy', 'Mauya') # Llama a Clase Gato y se lleva vars de Nombre y Onoma
gato.saludo()  # Llama al metodo Saludo 
perro = Perro('Firulais', 'Ladra') # Llama a Clase Perro y se lleva vars de Nombre y Onoma
perro.saludo()  # Llama al metodo Saludo 