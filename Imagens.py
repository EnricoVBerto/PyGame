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

# ----- Inicia assets----
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('/Users/gianfrancobaglioni/Documents/mod sim /Corredores foto.npg.jpeg').convert()
livro_img=pygame.image.load('C:\Users\enric\Desktop\PyGame\PyGame\assets\img\l.png')
livro_WIDTH_img = pygame.image.load('/Users/gianfrancobaglioni/Desktop/l.png').convert_alpha()
livro_img= pygame.transform.scale(livro_img, (LIVRO_WIDTH, LIVRO_HEIGHT))
ship_img = pygame.image.load('C:\Users\enric\Desktop\PyGame\PyGame\assets\img\ooo.gif').convert_alpha()
ship_img = pygame.transform.scale(ship_img, (SHIP_WIDTH, SHIP_HEIGHT))
ataque_img = pygame.image.load('assets/img/laserRed16.png').convert_alpha()
fighter_img = pygame.image.load('C:\Users\enric\Desktop\PyGame\PyGame\assets\img\fot.png').convert_alpha()
fighter_img = pygame.transform.scale(fighter_img, (f_WIDTH, f_HEIGHT))