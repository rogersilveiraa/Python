x = int(input("digite um número inteiro:"))

aux = 2
teste = True

while teste:
    
    if x % aux == 0 and x !=2:
        print ("não primo")
        teste = False
    if (x / aux) < 2:
        print ("primo")
        teste = False
    aux += 1
    
