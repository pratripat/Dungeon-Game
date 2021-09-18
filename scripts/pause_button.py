import pygame
from .funcs import *
from .button import Button

class Pause_Button(Button):
    def __init__(self, game):
        super().__init__(game, self.pause_button_image, (game.screen.get_width()//2-self.pause_button_image.get_width()//2, 30), game.pause_menu.load)

    @property
    def pause_button_image(self):
        return load_image('data/graphics/images/pause_button.png', 3)
