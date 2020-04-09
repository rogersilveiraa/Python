largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))

larg = 1
alt = 1

while alt <= altura:
    
    while larg <= largura:
        print ("#",end = "")
        larg += 1

    print()
    alt +=1
    larg = 1
