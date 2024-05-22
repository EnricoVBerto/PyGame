import pygame
from config import *

def load_assets():
    
    livro_img = pygame.image.load('assets/img/l.png').convert_alpha()
    ship_img = pygame.image.load('assets/img/image .gif').convert_alpha()
    fighter_img = pygame.image.load('assets/img/fot.png').convert_alpha()
    tela_inicial = pygame.image.load('assets/img/final.JPG').convert_alpha()
    return {
        # ----- Inicia assets----
        'font': pygame.font.SysFont(None, 48),
        'background': pygame.image.load('assets/img/Corredores foto.npg.jpeg').convert(),
        'livro_img': pygame.transform.scale(livro_img, (LIVRO_WIDTH, LIVRO_HEIGHT)),
        'ship_img': pygame.transform.scale(ship_img, (SHIP_WIDTH, SHIP_HEIGHT)),
        'ataque_img': pygame.image.load('assets/img/ataquepygame.png').convert_alpha(),
        'fighter_img': pygame.transform.scale(fighter_img, (f_WIDTH, f_HEIGHT)),
        'tela_inicial': pygame.transform.scale(tela_inicial,(in_WIDTH, in_HEIGHT))
    }