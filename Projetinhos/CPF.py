cpf = int(input("Digite os nove primeiros digitos do seu CPF:"))

multiplicador = 2
x = cpf
digito10 = 0
digito11 = 0

while x != 0:
    aux = x % 10
    x = x // 10
    digito10 = aux * multiplicador + digito10
    multiplicador += 1

digito10 = 11 - (digito10 % 11)
multiplicador = 2
x = (cpf*10) + digito10

while x != 0:
    aux = x % 10
    x = x // 10
    digito11 = aux * multiplicador + digito11
    multiplicador +=1

digito11 = 11 - (digito11 % 11)
if digito11 <=0:
    digito11 == 0

digito = digito10 * 10 + digito11

print ("Seu CPF é:",cpf,digito)
