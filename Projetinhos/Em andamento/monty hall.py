import random

def escondendo():
    portas = []
    premio = ["Carro", "Nada", "Pão"]
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
        elif i == "Nada":
            porta_nada = aux
        else:
            porta_pao = aux
        aux += 1
    if escolha == porta_nada:
        print("Na porta", porta_pao, "temos: Pão")
    elif escolha == porta_pao:
        print("Na porta", porta_nada, "temos: Nada")
    else:
        aux = random.choice([porta_esterco, porta_pao])
        if aux == porta_nada:
            aux1 = "Nada"
        else:
            aux1 = "Pão"
        print("Na porta", aux, "temos", aux1)
        

        
           
