import math
a = int(input('Ingrese un numero a: '))
b = int(input('Ingrese otro numero: ')) 
# En el input() todo dato que ingrese lo toma como un string
def equal (x, y):
    if(x > y): print('a es mayor que b')
    elif(x == y) : print('Los numeros son iguales')
    else : print('b es mayor que a')
def do (x, y, o):
    select = {
        '+': x + y,
        '-' : x - y,
        '*' : x * y,
        '/': x / y
    }
    result = select.get(o, "Invalid operator")
    print(result)

def numbers(first, second):
    quest = input('Desea sumar, restar, multiplicar o dividir:').lower()
    if((quest != 's') and (quest != 'r') and (quest != 'm') and (quest != 'd')): print('Error!')
    if(quest == 's'):
        do(first,second,'+')
    elif(quest == 'r'):
        do(first,second,'-')
    elif(quest == 'm'):
        do(first,second,'*')
    else: do(first,second,'/')
    compare = input('Desea comparar si son iguales? ').lower()
    if(compare == 'y'):equal(first,second)
    else: print('Ok, finishing')
numbers(a, b)
