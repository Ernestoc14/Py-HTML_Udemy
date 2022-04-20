# leyendo un archivo

c = open('archivo.txt','a')

c.write('agregamos una nueva linea a este archivo')
print(c.readline())
c.close()