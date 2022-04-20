# Una funcion con un num de entrada
# debera imprimir una piramide con el 
# n maximo de asteriscos en la piramide
# Eg n=5 Mostrara
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
'''
def recu(num):
    if num == 1:
        return num
    else:
        return num*recu(num-1)
        print(num*recu(num-1))

print(' Ingrese un numero: ')
num = int(input())
recu(num) 
print( 'factorial de ' ,num, 'es ', recu(num))
'''

#n que entra es el n de veces que ese numero se mostrara en pantalla
#list = [3, 1, 3, 4]
#Output  2213334444  
def rec( ):
    l= (2,2,3,4)
    for i in range(len(l)):
        if l[i] == 1:    #def creat(rows)
            print(l[i]) #for i in range (rows) #print "*"*(i+1)
            break
        else: 
            print(l[i] * (i+1))
            break
rec()

