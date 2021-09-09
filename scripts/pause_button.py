import pygame
from .button import Button

class Pause_Button(Button):
    def __init__(self, game):
        super().__init__(game, self.pause_button_image, (game.screen.get_width()//2-self.pause_button_image.get_width()//2, 30), game.pause_menu.load)

    @property
    def pause_button_image(self):
        image = pygame.image.load('data/graphics/images/pause_button.png').convert()
        image = pygame.transform.scale(image, (image.get_width()*3, image.get_height()*3))
        image.set_colorkey((0, 0, 0))
        return image
