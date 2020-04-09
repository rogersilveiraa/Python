n = int(input("Digite um número inteiro:"))

teste = True
QuantidadeDeAlgarismos = len(str(n))

while teste:
    aux1 = n % 10
    aux2 = ( n % 100) // 10
    if aux1 == aux2 and n != 0:
        print("sim")
        teste = False
    if QuantidadeDeAlgarismos == 1:
        print("não")
        teste = False
    else:
        n //= 10
        QuantidadeDeAlgarismos -= 1
