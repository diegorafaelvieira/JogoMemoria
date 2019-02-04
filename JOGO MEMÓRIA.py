
# INICIANDO O GAME
while True:
    iniciar = int(input("SE DESEJA INICIAR O JOGO DIGITE 1 | SE DESEJA SAIR DIGITE 0: "))
    print("")
    
    acerto = 0
    erro = 0
    rodada = 0

    if iniciar == 1:

# VARIÁVEIS CONTADORAS
        rodada = 0
        acerto = 0
        erro = 0
        valores = []
        posicoes = []



# TABELA ALEATÓRIA
        import random
        aleatoria = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
        random.shuffle(aleatoria)

        for x in range(0,16,4):
            print(aleatoria[x], aleatoria[x+1], aleatoria[x+2], aleatoria[x+3])
        print("")



# TABELA DE CARTAS FECHADAS
        fechada = [1]*16
        for x in range(0,16,4):
            print(fechada[x], fechada[x+1], fechada[x+2], fechada[x+3])



# INICIANDO O JOGO

        while acerto < 8:
            print("")
            print("ESCOLHA UMA DAS POSIÇÕES ABAIXO:")

            posicao = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            for y in range(0,16,4):
                print(posicao[y], posicao[y+1], posicao[y+2], posicao[y+3])
            print("")

# ESCOLHENDO UMA CARTA
            while True:
                q = int(input("ESCOLHA UMA CARTA: "))
                if q >= 0 and q <= 15:
                    print("Ok!")
                    break
                else:
                    print("ESCOLHA INVÁLIDA! ESCOLHA UMA DAS POISÇÕES ACIMA...")

# ESCOLHENDO OUTRA CARTA
            while True:
                q2 = int(input("ESCOLHA MAIS UMA CARTA: "))
                if q2 >= 0 and q2 <= 15:
                    print("Ok!")
                    break
                else:
                    print("ESCOLHA INVÁLIDA! ESCOLHA UMA DAS POISÇÕES ACIMA...")



            if q == q2:
                print("ERRO! VC ESCOLHEU A MESMA POSIÇÃO NAS DUAS PEDIDAS... TENTE NOVAMENTE!")
                print("")
                print("RODADAS:",rodada)
                print("")
                for y in range(0,16,4):
                    print(fechada[y], fechada[y+1], fechada[y+2], fechada[y+3])

            elif aleatoria[q] == aleatoria[q2]:


# ACERTOS-----------------

                if fechada[q] == 0 and fechada[q2] == 0:
                    print("ERRO! VC JÁ ESCOLHEU ESSES VALORES... TENTE NOVAMENTE!")
                    print("")
                    print("RODADAS:",rodada)
                    print("")
                    for y in range(0,16,4):
                        print(fechada[y], fechada[y+1], fechada[y+2], fechada[y+3])
                else:
                    print("")
                    print("VOCÊ ACERTOU!!!")
                    print("")

                    acerto += 1
                    rodada += 1

                    posicoes.append(q)
                    posicoes.append(q2)
                    valores.append(aleatoria[q])
                    
                    print("- Posições já escolhidas corretamente:",posicoes)
                    print("- Valores já escolhidos corretamente:",valores)
                    print("RODADAS:",rodada)
                    print("")

                    fechada[q] = 0
                    fechada[q2] = 0
                    for y in range(0,16,4):
                        print(fechada[y], fechada[y+1], fechada[y+2], fechada[y+3])

# ERROS ---------------------

            else:
                print("")
                print("VOCÊ ERROU!!!")
                print("")
                    
                erro += 1
                rodada += 1

                print("- Posições já escolhidas corretamente:",posicoes)
                print("- Valores já escolhidos corretamente:",valores)
                print("RODADAS:",rodada)
                print("")

                for y in range(0,16,4):
                    print(fechada[y], fechada[y+1], fechada[y+2], fechada[y+3])





# FIM DO JOGO -----------------
        print("")
        print("-------------- GAME OVER --------------")
        print("")
        print("SEUS ACERTOS:",acerto)
        print("SEUS ERROS:",erro)
        print("TENTATIVAS:",rodada)
        print("")
        print("SUA TABELA...")
        for x in range(0,16,4):
            print(aleatoria[x], aleatoria[x+1], aleatoria[x+2], aleatoria[x+3])
        print("")
        print("--- PARABÉNS, VOCE FINALIZOU O GAME ---")
        print("")






    elif iniciar == 0:
        print("Fechando o programa...")
        break
    else:
        print("Digito incorreto! Digite 1 para iniciar OU 0 para sair...")
