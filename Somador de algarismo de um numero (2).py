x = input("Digite um número para obter a soma dos seus algarismos:")
i = int(x)
z = 0
y = 10
soma = 0

while z < len(x):
    valor = i % y
    valor = valor // ( y/10)
    soma = valor + soma
    y *= 10
    z += 1

  
print("soma", int(soma))
