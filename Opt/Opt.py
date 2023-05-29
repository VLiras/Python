
quest = input('Datos: ')

def getString (array):
    return 'Hola'

def convert_data (value): 
    array = value.split()
    for i in array:
        print(i)
    return array
convert_data(quest)
# number = ['1', '2', '3']

def do (x, y, o):
    select = {
        '+': x + y,
        '-' : x - y,
        '*' : x * y,
        '/': x / y
    }
    result = select.get(o, "Invalid operator")
    print(result)

def data ():
#    return print(convert_data(quest))
    x = convert_data(quest)[0]
    y = convert_data(quest)[2]
    if ('+' in convert_data(quest)):
        do(x, y, '+')
    elif ('-' in convert_data(quest)): 
        do(x, y, '-')
    elif ('*' in convert_data(quest)):
        do(x, y, '*')
    else: 
        do(x, y, '/')
# data()


