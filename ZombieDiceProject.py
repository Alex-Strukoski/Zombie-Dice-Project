# Alexandre Magno Strukoski
import ZombieDice
import Graphics
from time import sleep
import pygame


ZombieDice.clearScreen()
print("(Por favor maximizar a janela, o jogo funciona melhor em tela cheia.)\n")
if str.upper(input("Deseja iniciar o jogo? [S/N] ")) == "N":
    ZombieDice.clearScreen()
    pygame.mixer.init()
    pygame.mixer.music.load('Laugh.wav')
    pygame.mixer.music.play()
    sleep(3) 
    print(f"{ZombieDice.colors.red}OKIEDOKIE\nBYE.")
    sleep(1)
    exit(Graphics.gameGraphics.severedHand)
else:
    ZombieDice.clearScreen()
    # Caso não tenha instalado o pygame, recomendo instalar antes de jogar. [Exemplo linux: > pip install pygame]
    # Caso você tenha instalado e mesmo assim não rode, veja se tem duas versões de python instaladas.
    ZombieDice.menu()

