import pygame
from Imagens import *
BLACK=(0,0,0)
FPS=30


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    tela_inicial=pygame.image.load('assets/img/Corredores foto.npg.jpeg')
    tela_inicial_rect = tela_inicial.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(tela_inicial, tela_inicial_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
