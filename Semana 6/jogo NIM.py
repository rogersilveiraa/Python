def computador_escolhe_jogada (n, m):
    
    if n <= m:
        jogada_computador = n
    else:
        jogada_computador = (n % (m + 1))

        if jogada_computador == 0 and  n > m:
            jogada_computador = m

    peças_mesa = n - jogada_computador
    
    if jogada_computador == 1:
        print ("O computador tirou uma peça.")
        if peças_mesa == 1:
            print ("Agora resta apenas uma peça.")
        else:
            print ("Agora restam", peças_mesa, "peças")
    else:
        print ("O computador tirou", jogada_computador, "peças")
        if peças_mesa == 1:
            print ("Agora resta apenas uma peça.")
        else:
            print ("Agora restam", peças_mesa, "peças")

    return jogada_computador


def usuario_escolhe_jogada (n, m):

    jogada_usuario = int(input("Quantas peças você vai tirar?"))
            
    while (jogada_usuario > m or jogada_usuario <= 0) or (jogada_usuario <= m and jogada_usuario > n):
        print("Opss, jogada invalida, tente outro número.")
        jogada_usuario = int(input("Quantas peças você vai tirar?"))

    peças_mesa = n - jogada_usuario
    
    if jogada_usuario == 1:
        print ("Você tirou uma peças")
        if peças_mesa == 1:
            print ("Sobrou apenas uma peça")
        else:
            print ("sobraram", peças_mesa, "peças")
            
    else:
        print ("Você tirou", jogada_usuario, "peça")
        if peças_mesa == 1:
            print ("Sobrou apenas uma peça")
        else:
            print ("sobraram", peças_mesa, "peças")
            
    return jogada_usuario  

            
def partida ():

    n = int(input("Quantas peças?"))
    m = int(input("Qual o limite por jogada?"))
 
    if (n % (m + 1)) == 0:
        print ("Você começa!")

        while n != 0:
            jogada_usuario = usuario_escolhe_jogada (n, m)
            n -= jogada_usuario

            if n != 0:
                jogada_computador = computador_escolhe_jogada (n ,m)
                n -= jogada_computador

                if n == 0:
                    print ("Computador ganhou")
                    return "Computador ganhou"
                    
                        
            else:
                print ("Você ganhou")
                return "Você ganhou"
                
                
    else:
        print ("Computador começa")

        while n != 0:
            jogada_computador = computador_escolhe_jogada (n, m)
            n -= jogada_computador

            if n != 0:
                jogada_usuario = usuario_escolhe_jogada (n, m)
                n -= jogada_usuario

                if n == 0:
                    print ("Você ganhou")
                    return "Você ganhou"
                    
                    
            else:
                print ("Computador ganhou")
                return "Computador ganhou"


def campeonato ():

    placar_computador = 0
    placar_usuario = 0
    contador_partidas = 1
    while contador_partidas <= 3:
        
        print ("**** Rodada", contador_partidas, "****")
        contador_partidas += 1
        placar = (partida ())
        if placar == "Computador ganhou":
            placar_computador += 1
        else:
            placar_usuario += 1
       

    print ("**** Final do campeonato! ****")
    print ("Placar: Você", placar_usuario, "X", placar_computador, "Computador")




print ("bem vindo ao jogo NIM! Escolha:")
escolha = 0
while escolha != 1 and escolha != 2: 
    
    print ("1 - para jogar uma partida isolada")
    print ("2 - para jogar um campeonato")

    escolha = int(input())
    
    if escolha == 1:
        partida ()
    if escolha == 2:
        campeonato ()

