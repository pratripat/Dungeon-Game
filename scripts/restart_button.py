import pygame
from .funcs import *
from .button import Button

class Restart_Button(Button):
    def __init__(self, game):
        self.game = game
        super().__init__(self.game, self.restart_button_image, (self.game.screen.get_width()//2-self.restart_button_image.get_width()//2, 270), self.game.load_cutscene, ['game_over', self.game.load_level])

    @property
    def restart_button_image(self):
        return load_image('data/graphics/images/restart_button.png', 3)
