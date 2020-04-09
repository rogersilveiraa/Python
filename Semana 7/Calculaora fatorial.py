def fatorial (x):

    if x < 0:
        print ("Não existe farorial de números negativos")
        return "Tente outra vez, para sair, digite 'sair'"

    if x == 0:
        x = 1

    aux = x - 1
        
    while aux >= 1:
        x *= aux
        aux -= 1
    return x

loop = True
print ("Quando quiser sair digite 'sair'")
while loop:
    entrada_usuario = input("Digite o valor que deseja para calcular seu fatorial: \n")
    
    if entrada_usuario == "sair":
        loop = False
    else:
        entrada = int(entrada_usuario)
        if entrada >= 0:
            print (entrada,"! =", fatorial (entrada), "\n")
        else:
            print (fatorial (entrada), "\n")
   
