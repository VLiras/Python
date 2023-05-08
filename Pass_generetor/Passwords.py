import random
numbers = [0,1,2,3,4,5,6,7,8,9]
vocals = ['A','B','C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(len(vocals)):
    vocals[i] = vocals[i].lower()
# print(vocals)
def getRandom (min, max):
    ans = random.randint(min, max)
    return ans
    
password = []
limit = int(input('Ingrese los caracteres maximos de nu nueva contraseña: '))
def getPassword ():
    for i in range(0, limit):
        value = getRandom(0,len(vocals))
        pass_letters = vocals[value]
        password.append(pass_letters)
        # print(value)
getPassword()
print(password)


