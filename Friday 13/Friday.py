import datetime


# print(date.strftime('%A')) # %A => Nombre del dia
# print(date.strftime('%B')) => Numero de dia del mes

def searchFriday_13(month, year):
    date = datetime.datetime(year, month, 13)
    if(date.strftime('%A') == 'Friday'):
        print('Si, este mes tendras un viernes 13')
    else: print('Este mes no tiene un viernes 13')

def setMonth():
    year = int(input('Ingrese el año: '))
    month = int(input('Ingrese el mes: '))
    searchFriday_13(month, year)
setMonth()

   



    
    


        
