import random
numbers = [0,1,2,3,4,5,6,7,8,9]
abecedary = ['A','B','C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

lowerAbc = [i.lower() for i in abecedary]
def getRandom (min, max):
    ans = random.randint(min, max)
    return ans

def setArray (loop, array):
    for i in range(0, loop):
        data = getRandom(0, len(array))
        pass_data = array[data]


subPassword = []
def getPassword ():
    limit = int(input('Ingrese los caracteres maximos de nu nueva contraseña: '))
    space = ''
    for i in range(0, limit):
        upper = getRandom(0,len(abecedary))
        lower = getRandom(0,len(abecedary))
        naturals = getRandom(0,9) 
        pass_Upper = abecedary[upper]
        pass_Lower = lowerAbc[lower]
        pass_Natural = numbers[naturals]
        subPassword.append(pass_Upper+pass_Lower+str(pass_Natural))
    password = space.join(subPassword)
    return print(password)
# getPassword()



