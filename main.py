# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from ataque import *
from config import *
from criarLivros import *
from livro import *
from livrosCaindo import *
from LoopPrincipal import *
from ship import *
from CriarJogador import *
from TelaPrincipal import *
from Imagens import *
pygame.init()

# ----- Gera tela principal



# ----- Inicia assets----


# Carrega os sons do jogo
pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.set_volume(0.4)
boom_sound = pygame.mixer.Sound('assets/snd/expl3.wav')
destroy_sound = pygame.mixer.Sound('assets/snd/expl6.wav')
pew_sound = pygame.mixer.Sound('assets/snd/pew.wav')
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


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

