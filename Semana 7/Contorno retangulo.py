largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))

alt = 1

while alt <= altura:
    larg = 1

    while larg <= largura:

        if alt == 1 or alt == altura or larg == 1 or larg == largura:
            print ("#", end = "")
        else:
            print(" ", end= "")

        larg += 1

    alt += 1
    print()
