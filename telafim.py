
import pygame
from os import path
from Imagens import *

from config import *

def game_over(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    tela_final = pygame.image.load(path.join(IMG_DIR, 'images.jpeg')).convert()
    background_rectt = tela_final.get_rect()
    
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = None
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = None
                    running = False
                if event.key == pygame.K_SPACE:
                    state= INIT 
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        window.fill(BLACK)
        window.blit(tela_final, background_rectt)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.update()

    return state
