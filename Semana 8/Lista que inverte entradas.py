entrada = int(input("Digite um número, para sair digite 0: \n"))
numeros = []

while entrada != 0:
    numeros.append(entrada)
    entrada = int(input("Digite um número, para sair digite 0: \n"))
    tam = len(numeros) - 1

while 0 <= tam:
    print (numeros[tam])
    tam -= 1
    
