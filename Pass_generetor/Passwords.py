import random
numbers = [0,1,2,3,4,5,6,7,8,9]
abecedary = ['A','B','C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

lowerAbc = [i.lower() for i in abecedary]
def getRandom (min, max):
    ans = random.randint(min, max)
    return ans
    
subPassword = []
def getPassword ():
    limit = int(input('Ingrese los caracteres maximos de nu nueva contraseña: '))
    space = ''
    for i in range(0, limit):
        letters = getRandom(0,len(abecedary))
        pass_Upper = abecedary[letters]
        subPassword.append(pass_Upper)
    password = space.join(subPassword)
    return print(password)
getPassword()



