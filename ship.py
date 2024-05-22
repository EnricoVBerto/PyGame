import pygame

from ataque import *
from config import *
from livro import *

class Ship(pygame.sprite.Sprite):
    def __init__(self, ship_img, all_sprites, all_ataques, ataque_img, x,y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = ship_img
        self.rect = self.image.get_rect()
        self.imagenormal = self.image
        self.imageespelho = pygame.transform.flip(self.image, True, False)
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0
        self.speedy = 0
        self.all_sprites = all_sprites
        self.all_ataques = all_ataques
        self.ataque_img = ataque_img

        self.last_shot = pygame.time.get_ticks()
        self.cooldown = 500

    def update(self):
        # Atualização da posição da nave
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        print(self.speedy)
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            print('N')
            self.rect.top = 0
        if self.rect.bottom > HEIGHT - 10:
            self.rect.bottom = HEIGHT -10
        elif self.rect.bottom < HEIGHT - 10:
            self.speedy = self.speedy + 4
            print('+10')
        elif self.rect.bottom == HEIGHT - 10:
            self.speedy = 0
            print('NN')

    def shoot(self,ddd,inimigo):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.cooldown:
            self.last_shot = now
            new_ataque = Ataque(self.ataque_img, self.rect.centery, self.rect.centerx,ddd,inimigo)
            self.all_sprites.add(new_ataque)
            self.all_ataques.add(new_ataque)



    def Direção(self, inimigo,lado):
        if lado == True:
            if self.rect.centerx < inimigo.rect.centerx:
                self.image = self.imagenormal
            else:
                self.image = self.imageespelho
        else:
            if self.rect.centerx < inimigo.rect.centerx:
                self.image = self.imageespelho
            else:
                self.image = self.imagenormal
