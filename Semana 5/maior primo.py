def maior_primo (x):
    
    aux = 2
    teste1 = True

    while x <= 1:

        x = int(input("Digite um valor inteiro maior que 1:"))

    while x != aux:

        if x % aux == 0:
            x -=1
            aux = 2
        else:
            aux += 1
        

        if (x / (aux - 1)) < 2:
            return x
