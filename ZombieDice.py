from os import system, name
from time import sleep
import pygame
import Game 
import Graphics
import random
import datetime
import re
import socket
import uuid


class user:
    logInfo = {}
    logData = []
    userData = []
    userInfo = {}
    

def clearScreen():
    # para windows
    if name == 'nt':
        _ = system('cls')
    # para mac e linux(aqui, os.name é 'posix')
    else:
        _ = system('clear')


class dados:
    dadoVerde = ("Cerebro", "Passo", "Cerebro", "Tiro", "Passo", "Cerebro")
    dadoAmarelo = ("Tiro", "Passo", "Cerebro", "Tiro", "Passo", "Cerebro")
    dadoVermelho = ("Tiro", "Passo", "Tiro", "Cerebro", "Passo", "Tiro")

class colors:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    blue = '\033[94m'
    reset = '\033[0m'


def ending():
    print(Graphics.gameGraphics.finaltext)


def regras():
        clearScreen()
        sleep(0.5)
        pygame.mixer.init()
        pygame.mixer.music.load('quick-mechanical-keyboard.wav')
        pygame.mixer.music.play()
        print(f"A primeira regra é: {colors.red}VOCÊ NÃO FALA DO CLUBE DA LUTA.", colors.reset)
        sleep(2)
        print("Ok não é essa")
        sleep(1.5)
        print("A primeira regra de fato é que são necessários dois jogadores ou mais")
        sleep(1)
        print("A cada rodada você joga a quantidade de dados correspondente ao numero da sua rodada")
        sleep(1)
        print("Por exemplo; se for a terceira rodada você joga 3 dados")
        sleep(1)
        print("E são 13 dados ao todo. Cada dado em uma cor, dados verdes tem as faces;")
        sleep(1)
        pygame.mixer.init()
        pygame.mixer.music.load('quick-mechanical-keyboard.wav')
        pygame.mixer.music.play()
        for cor in dados.dadoVerde:
            sleep(0.1)
            print(cor)
        sleep(1)
        print("Dados amarelos tem as faces;")
        sleep(1)
        for cor in dados.dadoAmarelo:
            sleep(0.1)
            print(cor)
        sleep(1)
        print("E dados vermelhos tem as faces;")
        sleep(1)
        for cor in dados.dadoVermelho:
            sleep(0.1)
            print(cor)
        sleep(1)
        print("Se cair 'Tiro', você levou um tiro e tendo 3 tiros você ta fora")
        sleep(1)
        print("Se cair 'Cerebro' você janta um cerebro e tendo 13 você ganha o jogo")
        pygame.mixer.init()
        pygame.mixer.music.load('quick-mechanical-keyboard.wav')
        pygame.mixer.music.play()
        sleep(1)
        print("E se cair em 'Passo', você deixou uma vítima fugir.")
        pygame.mixer.music.stop()
        sleep(5)
        clearScreen()
        pygame.mixer.init()
        pygame.mixer.music.load('quick-mechanical-keyboard.wav')
        pygame.mixer.music.play()
        print("AH É")
        sleep(1.5)
        clearScreen()
        print("E se por algum acaso você conseguiu jogar por mais de 12 turnos, você passa a vez e fica com os pontos.")
        sleep(1)
        print("Bom jogo!")
        sleep(1)
        pygame.mixer.init()
        pygame.mixer.music.load('Zombie-Throat.wav')
        pygame.mixer.music.play()
        print(f"{colors.red}{Graphics.gameGraphics.hand}", colors.reset)
        sleep(3)
        clearScreen()

def menu():
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    currentYear = int(date.strftime("%Y"))
    aux = 0
    while True:
        aux += 1
        login = str(input(f"Digite seu nome: {colors.red}"))  
        login = login.capitalize()
        user.logInfo["Endereço eletrônico"] = socket.gethostbyname(socket.gethostname())
        user.logInfo["Endereço MAC"] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        user.logInfo["Usuário"] = login
        user.logInfo["Hora"] = currentDateTime.strftime("%d/%m/%Y - %Hh:%Mm:%Ss")
        user.logInfo["OS"] = name
        for word in user.logInfo.items():
            infoInsert(f"{word} ")
        clearScreen()
        if login == "":
            print(colors.red, f"\n[VALOR INVALIDO - TENTATIVA: {aux + 1 - 1}]\n", colors.reset)
            if aux >= 5:
                Graphics.limit(0.1)
                sleep(2)
                clearScreen()
                pygame.mixer.init()
                pygame.mixer.music.load('Hmm.wav')
                pygame.mixer.music.play()
                sus()
                sleep(1)
                exit(f"\n\nFinalizando.")
        if login == "Olavo":
            print(colors.reset)
            Graphics.skull(7)
            break
        else:
            clearScreen()
            break
    print(currentDateTime.strftime(f"{colors.reset}%d/%m/%Y - %Hh:%Mm"))
    print(f"Bem vindo ao apocalipse {colors.red}{login}{colors.reset}, esse é o {colors.red}Zombie Dice{colors.reset} [¬º-°]¬")
    while True:
        pygame.mixer.init()
        pygame.mixer.music.load('Monster-In-The-Field.wav')
        pygame.mixer.music.play()
        request = str.capitalize(input(f"{Graphics.gameGraphics.menuStatic}\n► "))
        if request == 'Regras':
            regras()
            continue
        if request == 'Start':
            Game.jogo()
        if request == 'Exit':
            clearScreen()
            sleep(0.1)
            pygame.mixer.init()
            pygame.mixer.music.load('Zombie-Throat.wav')
            pygame.mixer.music.play()
            sleep(2)
            print(f"Finalizando o jogo.\nBYE\n")
            print(f"{colors.red}{Graphics.gameGraphics.severedHand}\n\n", colors.reset)
            ending()
            exit()
        elif request == "Dino":
            dino()
        elif request == "Creditos" or request == "Créditos":
            creditos()
        elif request == 'First':
            pygame.mixer.music.stop()
            randNames()
        else:
            clearScreen()
            print(colors.red, "[ENTRADA INVALIDA]", colors.reset)
            sleep(0.5)
            clearScreen()
            

def dino():
    clearScreen()
    print(Graphics.gameGraphics.dino)
    pygame.mixer.init()
    pygame.mixer.music.load('Dinosaur-Growl.wav')
    pygame.mixer.music.play()
    sleep(5)
    clearScreen()


def sus():
    print(Graphics.gameGraphics.sus)

def creditos():
    clearScreen()
    sleep(0.5)
    pygame.mixer.init()
    pygame.mixer.music.load('bensound-straight .wav')  # Royalty free from (https://www.bensound.com/royalty-free-music/4)
    pygame.mixer.music.play()
    dot = "☆" * 70
    space = " " * 10
    print(f"\n{dot}")
    sleep(1)
    print(space, "Desenvolvimento: Alexandre Magno Strukoski")
    sleep(1)
    print(space, "Animação: Alexandre Magno Strukoski")
    sleep(1)
    print(space, "Editor de Audio: Alexandre Magno Struksoki")
    sleep(1)
    print(space, "Arte: Alexandre Magno Strukoski")
    sleep(1)
    print(space, "Diretor Executivo: Alexandre Magno Strukoski")
    sleep(1)
    print(space, "Responsável por estragar minha vida: Alexandre Magno Struksoki")
    sleep(1)
    print(space, "Todos os direitos reservados")
    sleep(1)
    print(space, f"Baseado no jogo {colors.red}Zombie Dice ©{colors.reset} criado por Steve Jackson Games.")
    sleep(1)
    print(f"{dot}\n")
    sleep(4)
    clearScreen()
    

def randNames():
    clearScreen()
    while True:
        names = []
        cont = 0
        while True:
            cont += 1
            print(f"{colors.red}Digite 'Stop' para encerrar.", colors.reset)
            nameRequest = str.capitalize(input(f"Nome - {cont}: "))
            names.append(nameRequest)
            clearScreen()
            if nameRequest == "Stop":
                names.remove("Stop")
                break
            else:
                continue
        clearScreen()
        print(f"{colors.red}{int(1/7*100)}%\n▒▒▒▒▒▒▒▒▒▒")
        print("LOADING.")
        sleep(1)
        clearScreen()
        print(f"{colors.red}{int(2/7*100)}%\n█▒▒▒▒▒▒▒▒▒")
        print("LOADING..")
        sleep(1)
        clearScreen()
        print(f"{colors.red}{int(3/7*100)}%\n██▒▒▒▒▒▒▒▒")
        print("LOADING...")
        sleep(1)
        clearScreen()
        print(f"{colors.blue}{int(4/7*100)}%\n███▒▒▒▒▒▒▒")
        print("LOADING.")
        sleep(1)
        clearScreen()
        print(f"{colors.blue}{int(5/7*100)}%\n█████▒▒▒▒▒")
        print("LOADING..")
        sleep(1)
        clearScreen()
        print(f"{colors.green}{int(6/7*100)}%\n███████▒▒▒")
        print("LOADING...")
        sleep(1)
        clearScreen()
        print(f"{colors.green}{int(7/7*100)}%\n██████████")
        print("OK", colors.reset)
        sleep(2)
        clearScreen()
        luckyName = random.choice(names)
        print(f"Nome sorteado: {luckyName}")
        if str.upper(input("Deseja sortear novamente? [S/N] ")) == "N":
            clearScreen()
            print(f"Boa sorte {luckyName}")
            sleep(1.5)
            pygame.mixer.init()
            pygame.mixer.music.load('Laugh.wav')
            pygame.mixer.music.play()
            print(f"{colors.red}Vai precisar.", colors.reset)
            sleep(3)
            clearScreen()
            break
        else:
            clearScreen()
            names.clear()
            continue
    
# ainda sem utilidade.        
def rankingOpen(player):
    pass
    f = open("Ranking.txt", "r")
    linhas = f.readlines()
    for linha in linhas:
        linha = linha.replace("\n", "")
        nome, pontos, hora = linha.split(",")
        if player == nome:
            print(nome, pontos, hora)
    f.close()


def infoInsert(info):
    f = open("info.txt", "a")
    f.writelines(info)
    f.close()
    
    

    
