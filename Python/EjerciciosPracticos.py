# Multiplicar 2 numeros sin usar el signo *
from pydoc import doc

a = 8
b = 4
res = 0
for i in range (b):
    res += a
#print('El resultado es',res)

# Ingresar nombre y apellido e imprimelo al revez
nom = 'Pepon'
ape = 'Cede;o'

concade = nom + ' '+ ape
#print(concade [::-1])

# Funcion que encuentre el menor num de una lista

lista = [1, 3 , 54 ,-24 , 89, 0 ,-16]

menor = 'init'
for x in lista:
    if menor == 'init':
        menor = x 
    else:
        menor = x if x < menor else menor

#print ( 'menor' ,menor)

#Funcion que retorne el vol de una esfera por su radio
# 4/3 * pi * r**3
def calVol(r):
    return 4/3 *3.1415 * r**3
res = calVol(6)
#print(res)

#Funcion para verificar que user sea mayor de edad
def edad(usuario):
    return usuario.edad > 17
class Usuario:
    def __init__(self, edad):
        self.edad = edad
usuario = Usuario(15)
usuario2 = Usuario(21)

res1 = edad(usuario)
res2 = edad(usuario2)
#print(res1,res2)

#Funcion que indique si num es par o no
def esPar(num):
    return num % 2 == 0
par = esPar(13)
#print(par)

#Funcion que indique cuantas vocales tiene una palabra
palabra = 'chanchitofeliz'
vocales =0
for x in palabra:
    vocales+= 1 if x =='a' or x == 'e' or x =='i' or x == 'o' or x =='u' else 0
#print(vocales)

#Escribir una aplicacion que reciba una cant infinita
#de numeros hasta decir basta, luego que devuelva la suma de numeros ingresados

# lista =[]
# print('Ingrese numeros y para salir escriba basta')

# while True:
#     valor=input('Deme un valor ')
#     if(valor=='basta'):
#         break
#     else:
#         try:
#             valor = int(valor)
#             lista.append(valor)
#         except:
#             print('Valor Invalido')
#             exit
# total = 0
# for x in lista:
#     total+=x
# print(total)

#Escribir una funcion que reciba nombre y ape
#y vaya agregandolos a un archivo

def add(nombre,ape):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' '+ ape + '\n')
    c.close()
add('Tito','Canto')