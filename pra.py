#
from ntpath import join


def doubleChar(str):
    lisp = list(str)
    out = []
    string = ''
    for i in range(len(lisp)):
        out.join(lisp[i])
        out.join(lisp[i])
    for i in range(len(out)):
        string = out.join(out[i])
    return string

str = input('string: ')
print('String Doble es: ' , doubleChar(str))