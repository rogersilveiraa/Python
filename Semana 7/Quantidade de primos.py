def n_primos (x):

    if x < 2:
        print(" Tente novamenta com um número maior que 2")
    else:
        contador_primo = 0

        while x >= 2:
            teste = teste_primo (x)

            if teste == True:
                contador_primo +=1

            x -= 1
            
        return contador_primo


def teste_primo (x):

    aux = 2
    teste = True

    while teste:
        if (x % aux) == 0 and x != 2:
            teste_primo = False
            teste = False
        if (x / aux) < 2:
            teste_primo = True
            teste = False
        aux += 1

    return teste_primo

        
    
