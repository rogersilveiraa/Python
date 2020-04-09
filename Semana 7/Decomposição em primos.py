entrada_usuario = 1
fator = 2
while entrada_usuario < 2:
    entrada_usuario = int(input("Digite um número natural maior que 1 para saber sua fatoração: \n"))

while entrada_usuario != 1 :
    expoente = 0
    
    while (entrada_usuario % fator) == 0:
        entrada_usuario /= fator
        expoente += 1

    if expoente != 0 and entrada_usuario != 1:
        print (fator, "^" ,expoente, end = " * ")
    if entrada_usuario == 1:
        print (fator, "^", expoente)

    
    fator += 1

    
        
