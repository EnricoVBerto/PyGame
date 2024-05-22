import pygame
from os import path
from Imagens import *

from config import BLACK, FPS, GAME, QUIT


def vit1_screen(screen):
    print('aaaaaaaaaaaaaaaaaaaaaa')
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    tela_inicial = pygame.image.load(path.join(IMG_DIR, 'final.JPG')).convert()
    background_rect = tela_inicial.get_rect()

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = GAME
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)

        
        vertices = [(0, 0), (0, HEIGHT),(WIDTH, HEIGHT), (WIDTH, 0)] 
        pygame.draw.polygon(screen, BLACK, vertices)
                

        font = pygame.font.SysFont(None, 96)
        text = font.render(str('JOGADOR 2 VENCEU!!!'), True, (0, 0, 255))
        screen.blit(text, (WIDTH/4, HEIGHT/2)) 

        font = pygame.font.SysFont(None, 46)
        text = font.render(str('Aperte espaço para lutar denovo'), True, (0, 0, 255))
        screen.blit(text, (WIDTH/3, HEIGHT-HEIGHT/4))          

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

def vit2_screen(screen):
    print('aaaaaaaaaaaaaaaaaaaaaa')
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    tela_inicial = pygame.image.load(path.join(IMG_DIR, 'final.JPG')).convert()
    background_rect = tela_inicial.get_rect()

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = GAME
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        

        vertices = [(0, 0), (0, HEIGHT),(WIDTH, HEIGHT), (WIDTH, 0)] 
        pygame.draw.polygon(screen, BLACK, vertices)
                

        font = pygame.font.SysFont(None, 96)
        text = font.render(str('JOGADOR 1 VENCEU!!!'), True, (0, 0, 255))
        screen.blit(text, (WIDTH/4, HEIGHT/2)) 

        font = pygame.font.SysFont(None, 46)
        text = font.render(str('Aperte espaço para lutar denovo'), True, (0, 0, 255))
        screen.blit(text, (WIDTH/3, HEIGHT-HEIGHT/4)) 
        

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

