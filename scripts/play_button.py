import pygame
from .funcs import *
from .button import Button

class Play_Button(Button):
    def __init__(self, game, main_menu):
        super().__init__(game, self.play_button_image, (game.screen.get_width()//2-self.play_button_image.get_width()//2, 400), main_menu.start_game)

    @property
    def play_button_image(self):
        return load_image('data/graphics/images/play_button.png', 3)
