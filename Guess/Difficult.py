def difficult ():
    level = input('Elegi un nivel de dificultad (facil, medio, dificil): ').lower()
    limit = 0
    if(level == 'facil'): 
        limit == 10
    elif(level == 'medio'):
        limit == 50    
    else: 
        limit == 100
    print(limit)
difficult()