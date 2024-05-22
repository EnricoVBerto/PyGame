# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from ataque import *
from ataque2 import *
from config import *
from livro import *
from ship import *
from Imagens import *

pygame.init()

# ----- Gera tela principal



# ----- Inicia assets----
def game_screen(window):
    pygame.display.set_caption('player')

    # Carrega os sons do jogo
    pygame.mixer.music.load('assets/snd/Survivor - Eye of the Tiger228574-6ff089da-f029-41c9-9ce8-81a81e9aedab.mp3')
    pygame.mixer.music.set_volume(0.4)
    assets = load_assets()
    all_sprites = pygame.sprite.Group()
    all_livros = pygame.sprite.Group()
    all_ataques = pygame.sprite.Group()
    all_ataques2 = pygame.sprite.Group()

    player = Ship(assets['ship_img'], all_sprites, all_ataques, assets['ataque_img'], 1350,HEIGHT-10)
    all_sprites.add(player)
    player2 = Ship(assets['fighter_img'], all_sprites, all_ataques2, assets['ataque_img'], 10,HEIGHT-10)
    all_sprites.add(player2)

    for i in range(3):
        livro = Livro(assets['livro_img'])
        all_sprites.add(livro)
        all_livros.add(livro)
    DONE = 0
    PLAYING = 1

   
    estado = PLAYING
    keys_down={}
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    FPS = 30

    vida_jogador_1=100
    vida_jogador_2=100

    pygame.mixer.music.play(loops=-1)
    while estado == PLAYING:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                estado = DONE
            if estado == PLAYING:
            # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key]= True
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 10
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 10
                    if event.key == pygame.K_UP:
                        if player.rect.bottom == HEIGHT-10:
                            print('S')
                            player.speedy -= 50              
                    if event.key == pygame.K_DOWN:
                        player.shoot(player2.rect.x,(player2))


                    
                    if event.key == pygame.K_a:
                        player2.speedx -= 10
                    if event.key == pygame.K_d:
                        player2.speedx += 10
                        
                    if event.key == pygame.K_w:
                        if player2.rect.bottom == HEIGHT-10:
                            print('S')
                            player2.speedy -= 50  
                        
                                
                    if event.key == pygame.K_s:
                        player2.shoot(player.rect.x,(player))

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
        player.Direção(player2,False)
        player2.Direção(player,True)
        
        # Verifica se houve colisão os jogadores e os livros
        hits = pygame.sprite.spritecollide(player, all_livros, True)

            
                    
        if len(hits) > 0:
            #game = False
            vida_jogador_1 -= 5
            livro = Livro(assets['livro_img'])
            all_sprites.add(livro)
            all_livros.add(livro)

            
        hits = pygame.sprite.spritecollide(player2, all_livros, True)
        if len(hits) > 0:
            #game = False 
            vida_jogador_2 -= 5
            livro = Livro(assets['livro_img'])
            all_sprites.add(livro)
            all_livros.add(livro)




        hits = pygame.sprite.spritecollide(player,all_ataques2,True)                
        if len(hits) > 0:
            #game = False 
            vida_jogador_1 -= 7.5



        hits = pygame.sprite.spritecollide(player2,all_ataques,True)                
        if len(hits) > 0:
            #game = False 
            vida_jogador_2 -= 7.5
  

        




        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['background'], (0, 0))
        # Desenhando livros
        all_sprites.draw(window)

        HP2Porcent = vida_jogador_2/100 #obtem a porcentagem de dano
        cor = (255, 0, 0) #Cor vermelha para HP perdido. 
        vertices = [(50, 50), (550, 50), (550, 75), (50, 75)] #barra de HP é um retângulo
        pygame.draw.polygon(window, cor, vertices)#desenha a barra de HP perdido

        cor = (0, 255, 0)#Escolhe a cor verde 
        vertices = [(50, 50), (50+HP2Porcent*500, 50), (50+HP2Porcent*500, 75), (50, 75)] #quanto menor a porcentagem de HP, menor sera a barra verde
        pygame.draw.polygon(window, cor, vertices) #desenha o HP que tem em cima do HP perdido.



        HP1Porcent = vida_jogador_1/100 #obtem a porcentagem de dano
        cor = (255, 0, 0) #Cor vermelha para HP perdido. 
        vertices = [(WIDTH-50, 50), (WIDTH-550, 50), (WIDTH-550, 75), (WIDTH-50, 75)] #barra de HP é um retângulo
        pygame.draw.polygon(window, cor, vertices)#desenha a barra de HP perdido

        cor = (0, 255, 0)#Escolhe a cor verde 
        vertices = [(WIDTH-50, 50), (WIDTH-50-HP1Porcent*500, 50),(WIDTH-50-HP1Porcent*500, 75), (WIDTH-50, 75)] #quanto menor a porcentagem de HP, menor sera a barra verde
        pygame.draw.polygon(window, cor, vertices) #desenha o HP que tem em cima do HP perdido.



        font = pygame.font.SysFont(None, 48)
        text = font.render(str(vida_jogador_2), True, (0, 0, 255))
        window.blit(text, (50, 50))

        font = pygame.font.SysFont(None, 48)
        text = font.render(str(vida_jogador_1), True, (0, 0, 255))
        window.blit(text, (WIDTH-100, 50))


        if vida_jogador_1 <= 0:
            estado = DONE
            return VIT2

        if vida_jogador_2 <= 0:
            estado = DONE
            return VIT1

        pygame.display.update()# Mostra o novo frame para o jogador

    return QUIT 
    # ===== Finalização =====
     # Função do PyGame que finaliza os recursos utilizados

