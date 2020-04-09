rg = int(input("Digite os oito primeiros digitos do seu RG:"))

z = rg
x = 9
soma = 0

while rg != 0:
    aux = rg % 10
    rg = rg // 10
    soma = soma + (x * aux)
    x -= 1
   

digito = 11 -(soma % 11)
if digito == 10:
    digito = x

if digito == 11:
    digito = 0
    
print ("Seu RG completo é:", z,"-",digito)
