#edad = input('Cuantos anios tienes: ')
#lista = ['hola','ernesto','lazlo','jean']

#if lista.count(edad) > 0: #Cuenta cuantas veces encuentra la variable EDAD en lista
#    print('El dato existe: ', edad)
#else:
#    print('El dato no existe: ', edad)  

uno = input('Ingrese el primer numero ')
try: 
    uno = int(uno)
except:
    uno = 'Malo'
if uno == 'Malo':
    print('Ingrese numeros solamente')
    exit()

dos = input('Ingrese el segundo numero ')

try: 
    dos = int(dos)
except:
    dos = 'Muy malo'

if dos == 'Muy malo':
    print('Ingresa numeros solamente')
    exit()

simbolo = input('Ingrese la operacion a realizar: ')
if simbolo =='+':
    print('La suma es:',uno + dos)
elif simbolo =='-':
    if uno > dos:
        print('La resta es:', uno - dos)
    else:
        print('La resta es: ', dos - uno)
elif simbolo =='/':
    if uno != 0 and dos != 0:
        print('La division es: ', uno / dos)
    else:
        print('Las divisiones no contienen ceros... ')
elif simbolo == '*':
    print('La multiplicacion es: ', uno * dos)
else: 
    print('El simbolo ingresado no es operacion')