import Assets
# Convertidor de unidades de distancia
x = int(input('Numero: '))
# Por default, las unidades seran en metros 
def getDist (value, med, operator, unit) : 
    choose = {
        '/': value / med,
        '*': value * med
    }
    result = choose.get(operator, 'Invalid')
    
    print(str(result)+' '+unit)
getDist(x, Assets.thou, '/', Assets.kM)




