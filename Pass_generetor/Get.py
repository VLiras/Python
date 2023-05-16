from Passwords import getRandom
from Passwords import lowerAbc
from Passwords import abecedary
from Passwords import numbers
prePass = []
def data_loop(limit, array, arrayLimit):
    for i in range(0, limit):
        var = getRandom(0, len(arrayLimit))
        varPass = array[var]
        prePass.append(varPass)
        # print(len(lowerAbc))
    return prePass

def getPasswords ():
    char=  int(input('Set min characters: '))
    space = ''
    # print(space.join(data_loop(char, lowerAbc, abecedary)))
    print(str(space.join(data_loop(char, numbers, numbers))))
    

getPasswords()
    
