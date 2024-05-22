import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, VIT1, VIT2
from init_screen import init_screen 
from vit_screen import vit1_screen, vit2_screen
from main import game_screen
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('O melhor jogo')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == VIT1:
        state = vit1_screen(window)
    elif state == VIT2:
        state = vit2_screen(window)
    elif state == GAME:
        state = game_screen(window)

    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
