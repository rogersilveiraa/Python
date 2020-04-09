x = int(input("Digite um número que para obter a soma de seus algarismos:"))

y = 10

soma = 0

while x//(y/10) > 0 :
    valor = x % y
    valor //= (y/10)
    soma += valor
    y *= 10
    
print ("soma", int(soma))
    
