import pygame
from .funcs import *
from .button import Button

class Music_Disable_Button(Button):
    def __init__(self, game):
        self.game = game
        super().__init__(self.game, self.music_disable_button, (self.game.screen.get_width()//2+20, 395), self.game.music_manager.disable)

    @property
    def music_disable_button(self):
        return load_image('data/graphics/images/music_button.png', 3)
