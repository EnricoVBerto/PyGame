import pygame
from ship import *
from Imagens import load_assets
from config import *

# ----- Inicia assets----
def game_creen(window):

    # Carrega os sons do jogo
    pygame.mixer.music.load('assets/snd/Survivor - Eye of the Tiger228574-6ff089da-f029-41c9-9ce8-81a81e9aedab.mp3')
    pygame.mixer.music.set_volume(0.4)
    boom_sound = pygame.mixer.Sound('assets/snd/expl3.wav')
    destroy_sound = pygame.mixer.Sound('assets/snd/expl6.wav')
    pew_sound = pygame.mixer.Sound('assets/snd/pew.wav')


    all_sprites = pygame.sprite.Group()
    all_livros = pygame.sprite.Group()
    all_ataques = pygame.sprite.Group()

    assets = load_assets()
    player = Ship(assets['ship_img'], all_sprites, all_ataques, assets['ataque_img'], 40)
    all_sprites.add(player)
    player2 = Ship(assets['fighter_img'], all_sprites, all_ataques, assets['ataque_img'], 400)
    all_sprites.add(player2)

    for i in range(3):
        livro = Livro(assets['livro_img'])
        all_sprites.add(livro)
        all_livros.add(livro)

    clock = pygame.time.Clock()
    FPS = 30
    pygame.mixer.music.play(loops=-1)


    game=True
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
    def soco(self):
        now = pygame.time.get_ticks()
        elapsed_ticks=now-self.last_ataque

        if elapsed_ticks>self.ataque_ticks:
            self.last_ataque=now
            new_soco=Ataque(self.assets, self.rect.right,self.rect.centerx)
            self.groups['all sprites']

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
        
        all_sprites.draw(window)
        #hits3 = pygame.sprite.spritecollide(player2, player, True)
        #if len(hits3) > 0:
            #game = False
        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['background'], (0, 0))
        # Desenhando livros
