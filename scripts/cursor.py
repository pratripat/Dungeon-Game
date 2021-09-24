import pygame
from .funcs import *

class Cursor:
    def __init__(self, game):
        self.game = game
        self.image = load_image('data/graphics/images/cursor.png', 3)

    def render(self):
        self.game.screen.blit(self.image, pygame.mouse.get_pos())
