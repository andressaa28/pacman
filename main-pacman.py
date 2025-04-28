import pygame
import sys

# incializa o pygame
pygame.init()

# tamanho da tela

# cores
class colors:
        LIGHT_GREY = (79, 79, 79) # chão
        DARK_GREY = (56, 56, 56) # parede
        DARK_RED = (125, 45, 45) # vermelho escuro
        LIGHT_RED = (149, 56, 56) # vermelho claro
        BEIGE = (203, 194, 135) #bege claro
        DARK_GREEN = (17, 115, 35) # verde escuro
        GREEN = (28, 158, 52) # verde
        LIGHT_GREEN = (37, 173, 62) # verde claro
        LIGHTER_GREEN = (37, 173, 98) # verde mais claro bárbara sua chata
        AQUA_GREEN = (52, 203, 120) # verde água                                         
        DARK_YELLOW = (136, 158, 28) # amarelo escuro 
        LIGHT_YELLOW = (163, 188, 40) # ammarelo claro

# FPS

# mapa simples (1 = parede, 0 = caminho com ponto)
matrix = [
    "11111111111"
    "00000000000"
]

for row in matrix:
    for col in row:
        print(col)

levels = [
     level1_map, # matriz de parede para o n´vel 1
     level2_map # matriz diferente para o nível 2
     level3_map # e assim por diante
]

# importar arquivos em TXT
level1.txt

def load_level(level_num):
     with opem(f"levels/level{level_num}.txt") as f:
          map_data = f.readlines()
    

# level1
{
    "matrix": [
        "1111111111"
        "1110011111"
],
    "pacman_start":[],
    "ghost_den":[],
    "extra_voids":[],
    "num_rows": 31,
    "num_cols": 35,
    "cell_width": 20,
    "cell_height": 20,
}

TILE_SIZE = 32
ROWS = len(level)
COLS = len(level[0])

# posição incial do pac-man
pacman_x = TILE_SIZE
pacman_y = TILE_SIZE
direction = (0,0)

