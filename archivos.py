# leyendo un archivo

#c = open('archivo.txt','w') #variable c, funcion open (Nombre de archivo y permiso de archivo)

#c.write('\nagregamos una nueva linea a este archivo') #Escribimos esta linea en el archivo
#print(c.readline()) #Leemos linea por linea
#c.close() #Cerramos el archivo

#x = open ('archivo.txt')
#print(x.read())  #Se lee todo el archivo completo

#permisos de Manejo de Archivos
# Append 'a' = Solo agrega registros, no borra ni elimina
# Write  'w' = Elimina todo el archivo
# Read   'r' = Leemos el archivo

#Eliminando archivos y carpetas
import os  #importamos sistema operativo
if os.path.exists('archivo.txt'):
    os.remove('archivo.txt')
else:
    print('El archivo no existe')

#Para eliminar una carpeta
os.rmdir('micarpeta')