import random
import time
# number = random.randint(1,3)
# print(number)
def pair (value) :
    x = 1
    while x <= 1:
        time.sleep(2)
        print('Te doy una pista...')
        time.sleep(3)
        if(value % 2 == 0):
            print('El numero es par')
        else: print('El numero es impar')
        x += 1
def near_number (value , range):
    nearMinor = value - 2
    nearMajor = value + 2
    print(nearMinor)
    print(nearMajor)
def hint (number):
    return pair(number), near_number(number)

# while x <= 1:
#     time.sleep(2) # => 5 segundos
#     mi_funcion()
#     x += 1
