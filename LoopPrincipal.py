import pygame
from config import *
pygame.mixer.music.play(loops=-1)
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 10
            if event.key == pygame.K_RIGHT:
                player.speedx += 10

            if event.key == pygame.K_a:
                player2.speedx -= 10
            if event.key == pygame.K_d:
                player2.speedx += 10

        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 10
            if event.key == pygame.K_RIGHT:
                player.speedx -= 10

            if event.key == pygame.K_a:
                player2.speedx += 10
            if event.key == pygame.K_d:
                player2.speedx -= 10

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()

    # Verifica se houve colisão entre nave e meteoro
    hits = pygame.sprite.spritecollide(player, all_livros, True)
    if len(hits) > 0:
        game = False

    hits2 = pygame.sprite.spritecollide(player2, all_livros, True)
    if len(hits2) > 0:
        game = False 
    
    #hits3 = pygame.sprite.spritecollide(player2, player, True)
    #if len(hits3) > 0:
        #game = False
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando livros
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador