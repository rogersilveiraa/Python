x = int(input("digite um número inteiro:"))

testador = x
aux = 2
teste = True

while teste:
    
    if testador % aux == 0 and testador !=2:
        testador -=1

    if testador < 2:
            teste = False  

    if (testador / aux) < 2 and teste:
        print (testador)
        testador -= 1
        aux = 1
        
    aux += 1

   

    
