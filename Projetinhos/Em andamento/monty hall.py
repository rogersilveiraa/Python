import random

def escondendo():
    portas = []
    premio = ["Carro", "Esterco", "Titica de galinha"]
    while len(portas) < 3:
        aux = random.choice(premio)
        portas.append(aux)        
        if aux == premio[0]:
            del(premio[0])
        elif aux == premio [1]:
            del(premio[1])
        else:
            del(premio[2])
        
    return portas

def escolhas_pessoal(portas):
    escolha = 0
    aux = 1
    while (escolha < 1 or escolha > 3):
        escolha = int(input("Escolha uma porta, '1', '2' ou '3':\n"))
    for i in portas:
        if i == "Carro":
            porta_premio = aux
        elif i == "Esterco":
            porta_esterco = aux
        else:
            porta_titica = aux
        aux += 1
    if escolha == porta_esterco:
        print("Na porta", porta_titica, "temos: Titica de Galinha")
    elif escolha == porta_titica:
        print("Na porta", porta_esterco, "temos: Esterco")
    else:
        aux = random.choice([porta_esterco, porta_titica])
        if aux == porta_esterco:
            aux1 = "Esterco"
        else:
            aux1 = "Titica de galinha"
        print("Na porta", aux, "temos", aux1)
        

        
           
