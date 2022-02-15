# funciones en Python\

from ast import arg


def miFuncion():
    print('Mi primer funcion')

miFuncion()
def impDato(nombre, apellido):
    print('El nombre completo es:', nombre, apellido)

impDato('Pondo',15)

def recursion(i):
    if(i <= 1):
        return i
    print(i)
    recursion (i - 1)

recursion(6)