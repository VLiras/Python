from Square import toSquared # => Importando una funcion
from Square import root
 
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

def basic (req,x, y):
    if((req != 's') and (req != 'r') and (req != 'm') and (req != 'd')): print('Error!')
    if(req == 's'):
        do(x,y,'+')
    elif(req == 'r'):
        do(x,y,'-')
    elif(req == 'm'):
        do(x,y,'*')
    else: do(x,y,'/')

def numbers(first, second):
    a: int = input('Ingrese un numero a: ')
    b: int = input('Ingrese otro numero: ')
    quest = input('Que operacion desea hacer?: ').lower()
    if (quest == 's') or (quest == 'r') or (quest == 'm') or (quest == 'd'): 
        basic(quest, a, b)
    if(quest == 'n'): 
        toSquared(a)
    compare = input('Desea comparar si son iguales? ').lower()
    if(compare == 'y'):equal(first,second)
    else: print('Ok, finishing')
# numbers(a, b)
