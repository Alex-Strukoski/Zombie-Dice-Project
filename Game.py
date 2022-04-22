import Graphics
import ZombieDice
from time import sleep
import pygame
import random


def jogo():
    ZombieDice.clearScreen()
    dadoVerde = ZombieDice.dados.dadoVerde
    dadoAmarelo = ZombieDice.dados.dadoAmarelo
    dadoVermelho = ZombieDice.dados.dadoVermelho
    listaDados = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoVermelho, dadoVermelho, dadoVermelho]
    copo = listaDados.copy()
    jogadorAtual = 0
    dadosSorteados = []
    cont = 0
    tiros = 0
    cerebros = 0
    passos = 0
    numJogadores = 0
    contCerebro = {}
    contTiro = {}
    n = 0
    sleep(0.5)
    print(ZombieDice.colors.red, Graphics.gameGraphics.gameTitle, ZombieDice.colors.reset)
    pygame.mixer.init()
    pygame.mixer.music.load('Group-Of-Zombies-Growling.wav')
    pygame.mixer.music.play()
    sleep(0.5)
    while True:
        request = str.capitalize(input("Modo personalizado ou regular? "))
        ZombieDice.infoInsert(f"[Modo de jogo: {request}] ")
        if request == "Personalizado":
            ZombieDice.clearScreen()
            n = int(input("Limite de tiros: "))
            ZombieDice.infoInsert(f"[Limite de tiros: {n}] ")
            if n > 13:
                print(ZombieDice.colors.red, "\nERRO! Limite maximo atingido. [tente abaixo de 13]\n", ZombieDice.colors.reset)
                continue
            else:
                break
        if request == "Regular":
            ZombieDice.clearScreen()
            n = 3
            break
        else:
            print(ZombieDice.colors.red, "\nERRO\n", ZombieDice.colors.reset)
    while numJogadores < 2:
        try:
            numJogadores = int(input("Informe a quantidade de jogadores: "))
            ZombieDice.infoInsert(f"[Numero de jogadores: {numJogadores}] ")
            if numJogadores < 2:
                print("AVISO! O numero de jogadores deve ser maior do que 2.")
                continue
        except ValueError:
            cont += 1
            print(f"{ZombieDice.colors.red}\n[ERRO! VALOR INVALIDO] - TENTATIVA: {cont}\n", ZombieDice.colors.reset)
            if cont > 4:
                Graphics.limit(0.1)
                sleep(2)
                print(ZombieDice.colors.red)
                ZombieDice.clearScreen()
                Graphics.skull(60)
                exit()
            continue
        while True:
            ZombieDice.clearScreen()
            listaJogadores = []
            jogadores = {}
            for i in range(numJogadores):
                nameRequest = str.capitalize(input("Informe o nome do jogador - " + str(i + 1) + ": "))
                if nameRequest == "Nuno":
                    nameRequest = "Mestre Nuno"
                elif nameRequest == "Nara":
                    nameRequest = "Lady Anklan"
                listaJogadores.append(nameRequest)
                jogadores["Jogador"] = nameRequest
            ZombieDice.clearScreen()
            print(f"Os jogadores são", end=" ")
            for players in listaJogadores:
                print(players, end=" - ")
            request = str.upper(input("[S/N] "))
            if request.upper() != "N":
                break
            else:
                ZombieDice.clearScreen()
                continue
        ZombieDice.clearScreen()
        pygame.mixer.init()
        pygame.mixer.music.load('scary-horn.wav')
        pygame.mixer.music.play()
        for i in range(numJogadores):
            cont += 1
            loadingCounter =  ((cont/numJogadores) * 10) * 10
            print(f"\nINICIANDO O JOGO - {int(loadingCounter)}%\n")
            Graphics.loading(cont, 0.3)
            if cont > 10:
                break
        cont = 0
        corDadoSorteado = []
        while True:
            ZombieDice.clearScreen()
            try:
                control = listaJogadores[jogadorAtual]
                cont += 1
                print(f"{Graphics.gameGraphics.rolling}\n\n{Graphics.gameGraphics.rollingDices}\n\n{Graphics.gameGraphics.rolling}\n")
                sleep(0.3)
                print(f"{cont}º Turno do joador: {listaJogadores[jogadorAtual]}\nDados no copo: {len(copo)}")
                for i in range(0, cont, 1):
                    if cont > 12:
                        ZombieDice.clearScreen()
                        ZombieDice.infoInsert(f"{listaJogadores[jogadorAtual]} - cerebros: {cerebros} e tiros: {tiros} | ")
                        print(f"{cont} turnos\nPróximo jogador.")
                        dadosSorteados = []
                        tiros = 0
                        cerebros = 0
                        passos = 0
                        cont = 0
                        copo.clear()
                        copo = listaDados.copy()
                        ZombieDice.clearScreen()
                        continue
                    numSorteado = random.randint(0, int(len(copo)) - 1)
                    dadoSorteado = copo[numSorteado]
                    if dadoSorteado == ("Cerebro", "Passo", "Cerebro", "Tiro", "Passo", "Cerebro"):
                        corDado = "VERDE"
                        corDadoSorteado.append(corDado)
                        copo.remove(dadoSorteado)
                    elif dadoSorteado == ("Tiro", "Passo", "Cerebro", "Tiro", "Passo", "Cerebro"):
                        corDado = "AMARELO"
                        copo.remove(dadoSorteado)
                        corDadoSorteado.append(corDado)
                    else:
                        corDado = "VERMELHO"
                        corDadoSorteado.append(corDado)
                        copo.remove(dadoSorteado)
                dadosSorteados.append(dadoSorteado)
                for dado in corDadoSorteado:
                    print("Dado sorteado: ", dado)
                corDadoSorteado.clear()
                print("As faces foram: ")
                for dadoSorteado in dadosSorteados:
                    numface = random.randint(0, 5)
                    if dadoSorteado[numface] == "Cerebro":
                        print(ZombieDice.colors.green, "\nCÉREBRO: nham nham +1", ZombieDice.colors.reset)
                        pygame.mixer.init()
                        pygame.mixer.music.load('Zombie-Biting.wav')
                        pygame.mixer.music.play()
                        cerebros = cerebros + 1
                        contCerebro[listaJogadores[jogadorAtual]] = cerebros
                    elif dadoSorteado[numface] == "Tiro":
                        print(ZombieDice.colors.red, "\nTIRO: Você levou um tiro.", ZombieDice.colors.reset)
                        pygame.mixer.init()
                        pygame.mixer.music.load('Beefy-1911-.45-AC.wav')
                        pygame.mixer.music.play()
                        tiros = tiros + 1
                        contTiro[listaJogadores[jogadorAtual]] = tiros
                    else:
                        dadoSorteado[numface] == "Passo"
                        print(ZombieDice.colors.yellow, "\nPASSO: Uma vítima escapou.", ZombieDice.colors.reset)
                        pygame.mixer.init()
                        pygame.mixer.music.load('Running-footsteps-in-grass.wav')
                        pygame.mixer.music.play()
                        passos = passos + 1
                if cerebros >= 13:
                    ZombieDice.clearScreen()               
                    sleep(1)
                    pygame.mixer.init()
                    pygame.mixer.music.load('Funny-Scream.wav')
                    pygame.mixer.music.play()
                    sleep(3)
                    pygame.mixer.init()
                    pygame.mixer.music.load('Zombie-Saying-Brains.wav')
                    pygame.mixer.music.play()
                    print(f"\n{ZombieDice.colors.green}{Graphics.gameGraphics.winner}\n\n{listaJogadores[jogadorAtual]} ganhou.\n", ZombieDice.colors.reset)
                    request = input("Deseja continuar com os outros jogadores? [S/N] ")
                    if request.upper() != "N":
                        ZombieDice.clearScreen()
                        ZombieDice.infoInsert(f"{listaJogadores[jogadorAtual]} - cerebros: {cerebros} e tiros: {tiros} | ")
                        jogadorAtual = jogadorAtual + 1
                        dadosSorteados = []
                        tiros = 0
                        cerebros = 0
                        passos = 0
                        copo.clear()
                        copo = listaDados.copy()
                        sleep(1)
                        cont = 0
                        sleep(1)
                        continue
                    else:
                        request = str.upper(input("\nDeseja jogar mais uma rodada? [S/N] "))
                        if request != "N":
                            ZombieDice.infoInsert(f"{listaJogadores[jogadorAtual]} - cerebros: {cerebros} e tiros: {tiros} | ")
                            ZombieDice.clearScreen()
                            jogadorAtual = 0
                            dadosSorteados = []
                            tiros = 0
                            cerebros = 0
                            passos = 0
                            cont = 0
                            copo.clear()
                            copo = listaDados.copy()
                            continue
                        else:
                            ZombieDice.clearScreen()
                            pygame.mixer.init()
                            pygame.mixer.music.load('Zombie-Throat.wav')
                            pygame.mixer.music.play()
                            sleep(2)
                            for info in contCerebro.keys():
                                print(f"CEREBROS - {info}: {contCerebro[info]}")
                            for info in contTiro.keys():
                                print(f"TIROS - {info}: {contTiro[info]}")
                            print(f"\nFinalizando o jogo.\nBYE\n")
                            print(f"{ZombieDice.colors.red}{Graphics.gameGraphics.severedHand}\n\n", ZombieDice.colors.reset)
                            ZombieDice.ending()
                            ZombieDice.infoInsert(f"{listaJogadores[jogadorAtual]} - cerebros: {cerebros} e tiros: {tiros} | ")
                            exit()
                elif tiros >= n:
                    cerebros = 0 
                    ZombieDice.infoInsert(f"{listaJogadores[jogadorAtual]} - cerebros: {cerebros} e tiros: {tiros} | ")
                    contCerebro[listaJogadores[jogadorAtual]] = cerebros
                    sleep(1)
                    ZombieDice.clearScreen()
                    Graphics.skull(n)
                    pygame.mixer.init()
                    pygame.mixer.music.load('12-Gauge.wav')
                    pygame.mixer.music.play()
                    print(ZombieDice.colors.red, Graphics.gameGraphics.loser, f"\n\n{listaJogadores[jogadorAtual]} perdeu.\n", ZombieDice.colors.reset)
                    sleep(2)
                    ZombieDice.clearScreen()
                    jogadorAtual = jogadorAtual + 1
                    dadosSorteados = []
                    tiros = 0
                    cerebros = 0
                    passos = 0
                    copo.clear()
                    copo = listaDados.copy()
                    sleep(1)
                    cont = 0
                    continue
                
                print(f"\nScore atual - CEREBROS: {cerebros} - TIROS: {tiros} - PASSOS: {passos} - DADOS NO COPO: {len(copo)}")
                if len(copo) <= 3:
                    if str.upper(input(f"Dados: {len(copo)} - Recolocar Dados? [S/N] ")) == "N":
                        ZombieDice.clearScreen()
                        pygame.mixer.init()
                        pygame.mixer.music.load('Zombie-Throat.wav')
                        pygame.mixer.music.play()
                        sleep(2)
                        for info in contCerebro.keys():
                            print(f"CEREBROS - {info}: {contCerebro[info]}")
                        for info in contTiro.keys():
                            print(f"TIROS - {info}: {contTiro[info]}")
                        print(f"\nFinalizando o jogo.\nBYE\n")
                        print(f"{ZombieDice.colors.red}{Graphics.gameGraphics.severedHand}\n\n", ZombieDice.colors.reset)
                        ZombieDice.ending()
                        ZombieDice.infoInsert(f"{listaJogadores[jogadorAtual]} - cerebros: {cerebros} e tiros: {tiros} | ")
                        exit()
                    copo.clear()
                    copo = listaDados.copy()
                    Graphics.loadingDice()
                request = str.upper(input("AVISO: Você deseja continuar jogando dados? (Digite copo para ver o copo)  [S/N] "))
                if request == "COPO":
                    ZombieDice.clearScreen()
                    c = 0
                    for dados in copo:
                        sleep(0.5)
                        c += 1
                        if dados == ("Cerebro", "Passo", "Cerebro", "Tiro", "Passo", "Cerebro"):
                            print(f"{c} ➣ {ZombieDice.colors.green}⚃", ZombieDice.colors.reset)
                        elif dados == ("Tiro", "Passo", "Cerebro", "Tiro", "Passo", "Cerebro"):
                            print(f"{c} ➢ {ZombieDice.colors.yellow}⚄", ZombieDice.colors.reset)
                        else:
                            print(f"{c} ➣ {ZombieDice.colors.red}⚅", ZombieDice.colors.reset)
                    print("")
                    if str.upper(input("Você deseja continuar jogando dados? [S/N] ")) == "N":
                        ZombieDice.infoInsert(f"{listaJogadores[jogadorAtual]} - cerebros: {cerebros} e tiros: {tiros} | ")
                        jogadorAtual = jogadorAtual + 1
                        dadosSorteados = []
                        tiros = 0
                        cerebros = 0
                        passos = 0
                        cont = 0
                        copo.clear()
                        copo = listaDados.copy()
                        sleep(5)
                        ZombieDice.clearScreen()
                    else:
                        ZombieDice.clearScreen()
                        continue
                if request.upper() == "N":
                    ZombieDice.infoInsert(f"{listaJogadores[jogadorAtual]} - cerebros: {cerebros} e tiros: {tiros} | ")
                    ZombieDice.clearScreen()
                    jogadorAtual = jogadorAtual + 1
                    dadosSorteados = []
                    tiros = 0
                    cerebros = 0
                    passos = 0
                    cont = 0
                    copo.clear()
                    copo = listaDados.copy()
                else:
                    if jogadorAtual > numJogadores:
                        ZombieDice.clearScreen()
                        request = str.upper(input("Deseja jogar mais uma rodada? [S/N] "))
                        if request != "N":
                            ZombieDice.infoInsert(f"{listaJogadores[jogadorAtual]} - cerebros: {cerebros} e tiros: {tiros} | ")
                            dadosSorteados = []
                            tiros = 0
                            cerebros = 0
                            passos = 0
                            cont = 0
                            copo.clear()
                            copo = listaDados.copy()
                            continue
                        else:
                            ZombieDice.clearScreen()
                            pygame.mixer.init()
                            pygame.mixer.music.load('Zombie-Throat.wav')
                            pygame.mixer.music.play()
                            sleep(2)
                            for info in contCerebro.keys():
                                print(f"CEREBROS - {info}: {contCerebro[info]}")
                            for info in contTiro.keys():
                                print(f"TIROS - {info}: {contTiro[info]}")
                            print(f"\nFinalizando o jogo.\nBYE\n")
                            print(f"{ZombieDice.colors.red}{Graphics.gameGraphics.severedHand}\n\n", ZombieDice.colors.reset)
                            ZombieDice.ending()
                            ZombieDice.infoInsert(f"{listaJogadores[jogadorAtual]} - cerebros: {cerebros} e tiros: {tiros} | ")
                            exit()
                    else:
                        Graphics.newTurn()
                        dadoSorteado = []
            except ValueError:
                ZombieDice.clearScreen()
                if str.upper(input(f"Dados: {len(copo)} - Recolocar Dados? [S/N] ")) == "N":
                    ZombieDice.clearScreen()
                    pygame.mixer.init()
                    pygame.mixer.music.load('Zombie-Throat.wav')
                    pygame.mixer.music.play()
                    sleep(2)
                    for info in contCerebro.keys():
                        print(f"CEREBROS - {info}: {contCerebro[info]}")
                    for info in contTiro.keys():
                        print(f"TIROS - {info}: {contTiro[info]}")
                    print(f"\nFinalizando o jogo.\nBYE\n")
                    print(f"{ZombieDice.colors.red}{Graphics.gameGraphics.severedHand}\n\n", ZombieDice.colors.reset)
                    ZombieDice.ending()
                    ZombieDice.infoInsert(f"{listaJogadores[jogadorAtual]} - cerebros: {cerebros} e tiros: {tiros} | ")
                    exit()
                copo.clear()
                copo = listaDados.copy()
                Graphics.loadingDice()
                continue
            except IndexError:
                ZombieDice.clearScreen()
                pygame.mixer.init()
                pygame.mixer.music.load('Zombie-Throat.wav')
                pygame.mixer.music.play()
                sleep(2)
                for info in contCerebro.keys():
                    print(f"CEREBROS - {info}: {contCerebro[info]}")
                for info in contTiro.keys():
                    print(f"TIROS - {info}: {contTiro[info]}")
                if str.upper(input("\nDeseja jogar novamente? [S/N] ")) == "N":
                    print(f"\nFinalizando o jogo.\nBYE\n")
                    print(f"{ZombieDice.colors.red}{Graphics.gameGraphics.severedHand}\n\n", ZombieDice.colors.reset)
                    ZombieDice.ending()
                    exit()
                else:
                    ZombieDice.clearScreen() 
                    ZombieDice.menu()
    

