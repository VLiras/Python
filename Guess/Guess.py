import random
from Hint import hint
def guess_game ():
    guess = random.randint(1,10)
    for i in range(1,7):
        attempt = int(input('Ingrese un numero del 1 al 10: '))
        if(attempt != guess):
            print('Ups!, Numero equivocado')
            print('Intentalo otra vez')
        else:
            print('Correcto! Muy Bien!!')
            break
        if(i == 3):
            hint(guess)
        if(i == 6): 
            print('Game Over')
            print('El resultado era: '+str(guess))
                
start = input('Desea comenzar el juego: ').lower()
if((start == 'si') or (start == 'ok')): guess_game()

    
