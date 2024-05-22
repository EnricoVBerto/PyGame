import pygame
class Ataque2(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, bottom, centerx,Xdoinimigo):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.inicialx = self.rect.x

        if self.rect.x > Xdoinimigo:
            self.speedx = -15  # Velocidade fixa para cima
        else:
            self.speedx = 15  # Velocidade fixa para cima


    def update(self):
        # O soco só vai pra frente
        self.rect.x += self.speedx
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
        if abs(self.inicialx-self.rect.x) > 100:
            self.kill()

