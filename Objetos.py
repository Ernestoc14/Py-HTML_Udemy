class Usuario: #clase padre
    def __init__(self, nombre, apellido) -> None:  #metodo uno
        self.nombre = nombre
        self.apellido = apellido
    def saludo(self):   #metodo dos
        print('Hola mi nombre es', self.nombre, self.apellido)

class Admin(Usuario):  #clase hijo pasamos la clase padre
    def superSaludo(self): #metodo uno hijo
        print('Hola me llamo ', self.nombre,'y soy Admin')

usuario = Usuario('Felpie','Felis')

usuario.saludo()
usuario.nombre = 'Chancho'
usuario.saludo()
admin = Admin('Super ', 'Fekuz')
admin.saludo()
admin.superSaludo()
#print(usuario.nombre, usuario.apellido)