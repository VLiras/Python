from Calculator import equal
from Calculator import do
quest = input('Datos: ')
def convert_data (value): 
    return value.split()

marcas = ['Peugeot','Maserati','Ferrari','Porsche']
# for x in marcas:
def search (value, array):
    if(value in array):print(f'{value} esta incluido')
    else: 
        print(f'{value} no existe')
        # array.append(value)
    print(array)

def look ():
    if('<' in convert_data(quest)): equal(convert_data(quest)[0], convert_data(quest)[2])
    if('+' in convert_data(quest)): 
        do(convert_data(quest)[0], convert_data(quest)[2], convert_data(quest)[1]) 
look()