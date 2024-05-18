import pygame

from ataque import *
from config import *
from livro import *

class Ship(pygame.sprite.Sprite):
    def __init__(self, ship_img, all_sprites, all_ataques, ataque_img, x):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = ship_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
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