# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame, gif_pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 1500
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('player')

# ----- Inicia assets----
LIVRO_WIDTH = 60
LIVRO_HEIGHT = 45
SHIP_WIDTH = 200
SHIP_HEIGHT = 250
f_WIDTH = 200
f_HEIGHT = 250
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('/Users/gianfrancobaglioni/Documents/mod sim /Corredores foto.npg.jpeg').convert()
livro_img=pygame.image.load('/Users/gianfrancobaglioni/Desktop/l.png')
livro_WIDTH_img = pygame.image.load('/Users/gianfrancobaglioni/Desktop/l.png').convert_alpha()
livro_img= pygame.transform.scale(livro_img, (LIVRO_WIDTH, LIVRO_HEIGHT))
ship_img = pygame.image.load('/Users/gianfrancobaglioni/Desktop/ooo.gif').convert_alpha()
ship_img = pygame.transform.scale(ship_img, (SHIP_WIDTH, SHIP_HEIGHT))
ataque_img = pygame.image.load('assets/img/laserRed16.png').convert_alpha()
fighter_img = pygame.image.load('/Users/gianfrancobaglioni/Desktop/fot.png').convert_alpha()
fighter_img = pygame.transform.scale(fighter_img, (f_WIDTH, f_HEIGHT))

# Carrega os sons do jogo
pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.set_volume(0.4)
boom_sound = pygame.mixer.Sound('assets/snd/expl3.wav')
destroy_sound = pygame.mixer.Sound('assets/snd/expl6.wav')
pew_sound = pygame.mixer.Sound('assets/snd/pew.wav')

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Ship(pygame.sprite.Sprite):
    def __init__(self, ship_img, all_sprites, all_ataques, ataque_img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = ship_img
        self.rect = self.image.get_rect()
        self.rect.centerx = SHIP_WIDTH *3/ 2
        self.rect.bottom = HEIGHT -10
        self.speedx = 0
        self.all_sprites = all_sprites
        self.all_ataques = all_ataques
        self.ataque_img = ataque_img

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        new_ataque = Ataque(self.ataque_img, self.rect.top, self.rect.centerx)
        self.all_sprites.add(new_ataque)
        self.all_ataques.add(new_ataque)
    def __init__(self, fighter_img, all_sprites, all_ataques, ataque_img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = fighter_img
        self.rect = self.image.get_rect()
        self.rect.centerx = SHIP_WIDTH *3/ 2
        self.rect.bottom = HEIGHT -10
        self.speedx = 0
        self.all_sprites = all_sprites
        self.all_ataques = all_ataques
        self.ataque_img = ataque_img

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        new_ataque = Ataque(self.ataque_img, self.rect.top, self.rect.centerx)
        self.all_sprites.add(new_ataque)
        self.all_ataques.add(new_ataque)

class Livro(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-LIVRO_WIDTH)
        self.rect.y = random.randint(-100, -LIVRO_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-LIVRO_WIDTH)
            self.rect.y = random.randint(-100, -LIVRO_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

# Classe Ataque que representa os socos
class Ataque(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -10  # Velocidade fixa para cima

    def update(self):
        # O soco só vai pra frente
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de livros
all_sprites = pygame.sprite.Group()
all_livros = pygame.sprite.Group()
all_ataques = pygame.sprite.Group()
# Criando o jogador
player = Ship(ship_img, all_sprites, all_ataques, ataque_img)
all_sprites.add(player)
player2 = Ship(fighter_img, all_sprites, all_ataques, ataque_img)
all_sprites.add(player2)
# Criando os livros
for i in range(3):
    livro = Livro(livro_img)
    all_sprites.add(livro)
    all_livros.add(livro)

# ===== Loop principal =====
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
            if event.key == pygame.K_SPACE:
                player.shoot()

            if event.key == pygame.K_a:
                player2.speedx -= 10
            if event.key == pygame.K_d:
                player2.speedx += 10
            if event.key == pygame.K_s:
                player2.shoot()

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

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

