import pygame as pg
import random

class PacMan: 
    # definição de cores
    self.white = (255, 255, 255)
    self.black = (0, 0, 0)
    self.blue = (25, 25, 255)

    # Criação da janela com escala definida
    self.window = pg.display.set_mode((scale * 27.5, scale * 35))

    # Inicialização da fonte do jogo
    pg.font.init()
    self.font = pg.font.SysFont("Courier New", scale * 2, bold=True)

    # Relógio para controle de FPS
    self.clock = pg.time.Clock()

 # Variáveis gerais
    self.scale = scale
    self.sprite_frame = 0  # Frame atual da animação do Pac-Man
    self.sprite_speed = 2  # Velocidade da animação

    self.score = 0  # Pontuação do jogador
    self.lives = 5  # Número de vidas
    self.end_game = False  # Indica fim de jogo
    self.harmless_mode = False  # Modo onde fantasmas são inofensivos
    self.harmless_mode_timer = 0  # Timer do modo inofensivo