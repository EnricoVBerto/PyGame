import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, DONE
from init_screen import init_screen 
from main import game_screen
from telafim import game_over
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('O melhor jogo')

state = INIT
while True:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == DONE:
        state = game_over(window)
    else:
        break

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
