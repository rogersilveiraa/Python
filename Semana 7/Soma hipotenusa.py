def soma_hipotenusas (n):

    soma_hip = 0
    
    while n > 0:

        teste_hip = é_hipotenusa (n)

        if teste_hip == True:
            soma_hip += n
        n -= 1

    return soma_hip


def é_hipotenusa (x):

    cat1 = 1
    cat2 = 1
    hip2 = (cat1 ** 2) + (cat2 ** 2)
    hip = False
    
    while x**2 > hip2 and x > 0:
        
        while x**2 > hip2:
            cat2 += 1
            hip2 = (cat1 ** 2) + (cat2 ** 2)

        if (x**2) == hip2:
            hip = True

        else:
            cat2 = 1
            cat1 +=1
            hip2 = (cat1 ** 2) + (cat2 ** 2)
            
    return hip
    

        
         
        
    
        
