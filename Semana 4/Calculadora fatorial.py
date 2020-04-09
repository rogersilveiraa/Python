n = int(input("Digite o valor de n, para obter n!: "))

if n < 0:
    print ("Não existe fatorial de números negativos")

else:
    fatorial = 1

    if n == 0:
        print("1")

    else:
        while n > 1:
            fatorial *= n
            n -=  1
    
        print(fatorial)
    

        
