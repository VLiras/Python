import datetime

# print(date.strftime('%A')) => Nombre del dia
# print(date.strftime('%B')) => Numero de dia del mes

def searchFriday_13(month, year):
    date = datetime.datetime(year, month, 13)
    if(date.strftime('%A') == 'Friday'):
        print('Si, este mes tendras un viernes 13')
    else: print('Este mes no tiene un viernes 13')

while True:
    year = input('Ingrese el año: ')
    if (year == 'q' or year == 'quit') : break
    month = input('Ingrese el mes: ')
    searchFriday_13(int(month), int(year))


   



    
    


        
