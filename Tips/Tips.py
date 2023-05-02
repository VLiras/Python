# Calculadora de propinas con porcentaje a eleccion
billMount = int(input('Monto de factura: '))
percent = int(input('Porcentaje de propina: '))
def setTip (mount) :
    ans = mount * (percent / 100)
    return print('Propina: $'+str(ans))
setTip(billMount)    
