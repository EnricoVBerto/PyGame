
import pygame
from os import path
from Imagens import *

from config import BLACK, FPS, GAME, DONE

def game_over(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    print('carreguei')
    # Carrega o fundo da tela inicial
    tela_final = pygame.image.load(path.join(IMG_DIR, 'assets.telafim.jpeg')).convert()
    background_rect = tela_final.get_rect()
    assets= load_assets()
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        print('QUIT')
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
        
        window.blit(assets[BG_QUIT], (0,0))
        # Depois de desenhar tudo, inverte o display.
        pygame.display.update()

    return state
