#Comentario
#if 3 > 5:
  #  print('Esto no de va a imprimir')

x=5
y='Chanchito feliz'
#print(x, y)

inicio= 'Hola '
final='Chao'
#print(inicio + final)

lista=[0, 9, 3]
lista2=lista.copy()
#lista.clear()   #Borra toda la lista
lista.append(6) #Agrega el elemento 6 a la lista

#print(lista, lista2.count(3)) #cuenta cuantas veces se repite un elemento en array
#print(len(lista)) #longitud de lista
#lista.pop() #elimina el ultimo elemento de array
#lista.remove('lazlo') #elimina elemento especifico

lista.reverse()
lista.sort()

tupla=('hola','ern','somos','tupla')
listadetupla=list(tupla)
#listadetupla.append('carro')
#print(listadetupla)

rango = range(6)
#print(rango)

diccionario={
  "nombre": "Chancho",
  "raza": "Persa",
  "edad": "5"
}

#print(diccionario.get('raza'))
diccionario['nombre'] = 'Yops'
#print(diccionario)

diccionario['ronronea'] = 'Si'
#print(diccionario)

copia = diccionario.copy()
diccionario.pop('nombre')
#print(diccionario , copia)

