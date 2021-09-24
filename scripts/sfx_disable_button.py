import pygame
from .funcs import *
from .button import Button

class SFX_Disable_Button(Button):
    def __init__(self, game):
        self.game = game
        super().__init__(self.game, self.sfx_disable_button, (self.game.screen.get_width()//2-20-self.sfx_disable_button.get_width(), 395), self.game.sfx_manager.disable)

    @property
    def sfx_disable_button(self):
        return load_image('data/graphics/images/sfx_button.png', 3)
