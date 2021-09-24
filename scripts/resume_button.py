import pygame
from .funcs import *
from .button import Button

class Resume_Button(Button):
    def __init__(self, game):
        self.game = game
        super().__init__(self.game, self.restart_button_image, (self.game.screen.get_width()//2-self.restart_button_image.get_width()//2, 330), self.game.pause_menu.refresh)

    @property
    def restart_button_image(self):
        return load_image('data/graphics/images/resume_button.png', 3)
