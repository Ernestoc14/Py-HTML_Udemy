#Crea un programa que sume
#dos numeros ingresados por el User

def intro():
    num = input("Deme el numero para la operacion ")
    num = int(num)
    return num

def ope():
    num1 = intro()
    num2 = intro()
    print(num1+num2)
ope()
