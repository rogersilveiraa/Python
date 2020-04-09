import random

def main ():
    print ("Bem-vindo ao jogo senha.\nPara jogar no facil digite: '1',\n"
           "Para jogar no dificil digite: '2'\nPara sair digite qualquer coisa:")
    entrada = int(input())
    if entrada == 1 or entrada == 2:
        rodada = 1
        acertos = 0
        jogando = True
        senha = config_partida()
        while jogando:
            jogada = jogadas(senha)
            lista_jogada = organizador_entrada(jogada)
            resultado = comparador(senha, lista_jogada)
            if senha == lista_jogada:
                jogando = False
                print ("Parabéns, você ganhou! Demorou", rodada, "rodadas. A senha é:")
                for i in resultado:
                    print(i, end="")
            else:
                print ("A senha ainda não foi descoberta, continue tentando:")
                rodada += 1
                if entrada == 1:
                    for i in resultado:
                        print(i, end="")
                else:
                    for i in resultado:
                        if i != "*":
                            acertos += 1
                    print ("Você acertou", acertos, "digitos")
                    acertos = 0
                print()
                
    else:
        print ("Volte mais tarde para jogar novamente")


def config_partida():
    tamanho_senha = int(input("Digite quantos algarismos tera a senha:\n"))
    senha = []
    while tamanho_senha > 0:
        senha.append(random.randint(0, 9))
        tamanho_senha -= 1
    if senha[0] == 0:
        senha[0] = random.randint(1, 9)

    return senha

def jogadas(senha):
    tamanho_senha = 0
    while tamanho_senha != len(senha):
        jogada = int(input("Digite uma senha:\n"))
        tamanho_senha = len(str(jogada))
        if tamanho_senha != len(senha):
            print ("jogada invalida, tente novamente")
    
    return jogada

def organizador_entrada(jogada):
    lista_jogada = []
    tamanho = len(str(jogada))
    for i in range(tamanho):
        lista_jogada.append(jogada // (10 ** (tamanho - 1)))
        jogada = jogada % (10 ** (tamanho - 1))
        tamanho -= 1

    return lista_jogada

def comparador(senha, jogada):
    resultado = []
    for i in range(len(senha)):
        if senha[i] == jogada[i]:
            resultado.append(senha[i])
        else:
            resultado.append("*")
    return resultado
