from main import *
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
player = Ship(ship_img, all_sprites, all_ataques, ataque_img)
all_sprites.add(player)
player2 = Ship(fighter_img, all_sprites, all_ataques, ataque_img)
all_sprites.add(player2)